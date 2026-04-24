#!/usr/bin/env python3
"""Generate separate DNSTwist-based hardening lists for brand impersonation."""

from __future__ import annotations

import argparse
import json
import logging
import os
import shutil
import subprocess
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple
from urllib.parse import urlparse


REPO = "sparksbenjamin/DNS_Blocking"
BRANCH = "main"

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
CONFIG_PATH = SCRIPT_DIR / "hardening_targets.json"

HARDENING_DIR = REPO_ROOT / "hardening"
HARDENING_LISTS_DIR = HARDENING_DIR / "lists"
HARDENING_CATEGORIES_DIR = HARDENING_DIR / "categories"
HARDENING_README_PATH = HARDENING_DIR / "README.md"
HARDENING_REPORT_PATH = HARDENING_DIR / "report.json"

HOSTS_PREFIX = "0.0.0.0 "
DNS_KEYS = ("dns_a", "dns_aaaa", "dns_ns", "dns_mx")

DEFAULT_TIMEOUT_SECONDS = 300
DEFAULT_THREADS = 8
DEFAULT_JOBS = 2
DEFAULT_MAX_VARIANTS_PER_SEED = 300

DOMAIN_REGEX = r"^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def ensure_dir(path: Path) -> None:
    """Ensure a directory exists."""
    path.mkdir(parents=True, exist_ok=True)


def normalize_domain(value: str) -> str:
    """Normalize a domain or URL string into a bare lowercase hostname."""
    value = (value or "").strip().lower()
    if not value:
        return ""

    if "://" not in value and "/" not in value:
        domain = value
    else:
        candidate = value if "://" in value else f"https://{value}"
        parsed = urlparse(candidate)
        domain = parsed.hostname or ""

    return domain.rstrip(".")


def is_valid_domain(domain: str) -> bool:
    """Return True when a string looks like a valid fully qualified domain name."""
    import re

    if not domain or len(domain) > 253:
        return False
    return bool(re.match(DOMAIN_REGEX, domain))


def domain_matches_suffix(domain: str, suffix: str) -> bool:
    """Return True when a domain equals or is nested below a suffix."""
    domain = normalize_domain(domain)
    suffix = normalize_domain(suffix)
    return bool(domain and suffix and (domain == suffix or domain.endswith(f".{suffix}")))


def load_config(path: Path) -> Dict:
    """Load the curated hardening target configuration."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError("hardening config must be a JSON object")
    if not isinstance(data.get("targets"), list) or not data["targets"]:
        raise ValueError("hardening config must include a non-empty 'targets' list")

    return data


def merge_target_config(defaults: Dict, target: Dict) -> Dict:
    """Merge global defaults into a single target definition."""
    merged = dict(defaults)
    merged.update(target)

    merged["category"] = str(merged.get("category", "brand_impersonation")).lower()
    merged["service_id"] = str(merged.get("service_id", "")).strip().lower()
    merged["name"] = str(merged.get("name", merged["service_id"])).strip()
    merged["threads"] = int(merged.get("threads", DEFAULT_THREADS))
    merged["timeout_seconds"] = int(merged.get("timeout_seconds", DEFAULT_TIMEOUT_SECONDS))
    merged["max_variants_per_seed"] = int(
        merged.get("max_variants_per_seed", DEFAULT_MAX_VARIANTS_PER_SEED)
    )
    merged["require_dns_records"] = bool(merged.get("require_dns_records", True))
    merged["mxcheck"] = bool(merged.get("mxcheck", False))
    merged["enabled"] = bool(merged.get("enabled", True))
    merged["exclude_exact"] = [
        normalize_domain(value) for value in merged.get("exclude_exact", []) if normalize_domain(value)
    ]
    merged["exclude_suffix"] = [
        normalize_domain(value) for value in merged.get("exclude_suffix", []) if normalize_domain(value)
    ]
    merged["fuzzers"] = [str(value).strip() for value in merged.get("fuzzers", []) if str(value).strip()]

    seeds = []
    for value in merged.get("seed_domains", []):
        domain = normalize_domain(str(value))
        if domain and is_valid_domain(domain):
            seeds.append(domain)
        elif value:
            logger.warning("Skipping invalid seed '%s' for target %s", value, merged["service_id"])
    merged["seed_domains"] = list(dict.fromkeys(seeds))

    if not merged["service_id"]:
        raise ValueError("each hardening target needs a service_id")
    if not merged["seed_domains"]:
        raise ValueError(f"target '{merged['service_id']}' has no valid seed domains")

    return merged


def resolve_nameservers(cli_value: Optional[str]) -> Optional[str]:
    """Resolve the nameserver list from CLI or environment."""
    value = cli_value or os.environ.get("DNSTWIST_NAMESERVERS", "")
    return value.strip() or None


def resolve_threads(cli_value: Optional[int]) -> Optional[int]:
    """Resolve thread count from CLI or environment."""
    if cli_value is not None:
        return cli_value

    env_value = os.environ.get("DNSTWIST_THREADS", "").strip()
    if not env_value:
        return None

    try:
        return int(env_value)
    except ValueError:
        logger.warning("Ignoring invalid DNSTWIST_THREADS value: %s", env_value)
        return None


def resolve_jobs(cli_value: Optional[int]) -> int:
    """Resolve concurrent seed job count from CLI or environment."""
    if cli_value is not None:
        if cli_value < 1:
            raise ValueError("--jobs must be at least 1")
        return cli_value

    env_value = os.environ.get("DNSTWIST_JOBS", "").strip()
    if env_value:
        try:
            value = int(env_value)
            if value < 1:
                raise ValueError
            return value
        except ValueError:
            logger.warning("Ignoring invalid DNSTWIST_JOBS value: %s", env_value)

    return DEFAULT_JOBS


def build_dnstwist_command(
    seed_domain: str,
    target: Dict,
    nameservers: Optional[str],
    thread_override: Optional[int],
) -> List[str]:
    """Build the dnstwist subprocess command for a single seed domain."""
    cmd = [
        sys.executable,
        "-m",
        "dnstwist",
        "--registered",
        "--format",
        "json",
        "--threads",
        str(thread_override or target["threads"]),
    ]

    if target.get("mxcheck"):
        cmd.append("--mxcheck")
    if nameservers:
        cmd.extend(["--nameservers", nameservers])
    if target.get("fuzzers"):
        cmd.extend(["--fuzzers", ",".join(target["fuzzers"])])

    dictionary_file = target.get("dictionary")
    if dictionary_file:
        cmd.extend(["--dictionary", str((REPO_ROOT / dictionary_file).resolve())])

    tld_dictionary = target.get("tld_dictionary")
    if tld_dictionary:
        cmd.extend(["--tld", str((REPO_ROOT / tld_dictionary).resolve())])

    cmd.append(seed_domain)
    return cmd


def run_dnstwist(
    seed_domain: str,
    target: Dict,
    nameservers: Optional[str],
    thread_override: Optional[int],
) -> List[Dict]:
    """Execute dnstwist and return parsed JSON rows."""
    cmd = build_dnstwist_command(seed_domain, target, nameservers, thread_override)
    logger.info("    Twisting %s", seed_domain)
    result = subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=target["timeout_seconds"],
    )

    if result.stderr.strip():
        logger.info("    dnstwist stderr for %s: %s", seed_domain, result.stderr.strip())

    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "dnstwist failed")

    stdout = result.stdout.strip()
    if not stdout:
        return []

    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"invalid dnstwist JSON output: {exc}") from exc

    if not isinstance(payload, list):
        raise RuntimeError("dnstwist JSON output was not a list")

    return payload


def process_seed_domain(
    seed_domain: str,
    target: Dict,
    nameservers: Optional[str],
    thread_override: Optional[int],
) -> Dict:
    """Run dnstwist for one seed and return filtered results plus metadata."""
    try:
        results = run_dnstwist(seed_domain, target, nameservers, thread_override)
    except subprocess.TimeoutExpired:
        warning = f"{target['service_id']} timed out while twisting {seed_domain}"
        logger.warning(warning)
        return {"seed_domain": seed_domain, "count": 0, "skipped": False, "domains": set(), "warning": warning}
    except Exception as exc:
        warning = f"{target['service_id']} failed for {seed_domain}: {exc}"
        logger.warning(warning)
        return {"seed_domain": seed_domain, "count": 0, "skipped": False, "domains": set(), "warning": warning}

    filtered = filter_dnstwist_results(results, target)
    if len(filtered) > target["max_variants_per_seed"]:
        warning = (
            f"{target['service_id']} seed {seed_domain} produced {len(filtered)} live variants, "
            f"exceeding the limit of {target['max_variants_per_seed']}; skipping that seed"
        )
        logger.warning(warning)
        return {
            "seed_domain": seed_domain,
            "count": len(filtered),
            "skipped": True,
            "domains": set(),
            "warning": warning,
        }

    return {
        "seed_domain": seed_domain,
        "count": len(filtered),
        "skipped": False,
        "domains": filtered,
        "warning": None,
    }


def execute_seed_jobs(
    targets: Sequence[Dict],
    nameservers: Optional[str],
    thread_override: Optional[int],
    job_count: int,
) -> Tuple[Dict[Tuple[int, int], Dict], List[str]]:
    """Run seed domains concurrently and collect ordered results."""
    warnings: List[str] = []
    seed_outputs: Dict[Tuple[int, int], Dict] = {}
    work_items: List[Tuple[int, int, Dict, str]] = []

    for target_index, target in enumerate(targets):
        for seed_index, seed_domain in enumerate(target["seed_domains"]):
            work_items.append((target_index, seed_index, target, seed_domain))

    logger.info(
        "Running %d seed job(s) across %d target(s) with concurrency %d",
        len(work_items),
        len(targets),
        job_count,
    )

    with ThreadPoolExecutor(max_workers=job_count) as executor:
        future_map = {
            executor.submit(process_seed_domain, seed_domain, target, nameservers, thread_override): (
                target_index,
                seed_index,
            )
            for target_index, seed_index, target, seed_domain in work_items
        }
        for future in as_completed(future_map):
            job_key = future_map[future]
            seed_output = future.result()
            seed_outputs[job_key] = seed_output
            warning = seed_output.get("warning")
            if warning:
                warnings.append(warning)

    return seed_outputs, warnings


def filter_dnstwist_results(results: Sequence[Dict], target: Dict) -> Set[str]:
    """Filter dnstwist results into a set of exact lookalike hostnames."""
    exact_excludes = set(target.get("exclude_exact", []))
    suffix_excludes = target.get("exclude_suffix", [])
    seed_domains = set(target["seed_domains"])

    filtered: Set[str] = set()
    for entry in results:
        if not isinstance(entry, dict):
            continue

        domain = normalize_domain(str(entry.get("domain", "")))
        if not is_valid_domain(domain):
            continue
        if domain in seed_domains:
            continue
        if domain in exact_excludes:
            continue
        if any(domain_matches_suffix(domain, suffix) for suffix in suffix_excludes):
            continue
        if target["require_dns_records"] and not any(entry.get(key) for key in DNS_KEYS):
            continue

        filtered.add(domain)

    return filtered


def clear_previous_outputs() -> None:
    """Clear previously generated hardening outputs."""
    if HARDENING_LISTS_DIR.exists():
        shutil.rmtree(HARDENING_LISTS_DIR)
    if HARDENING_CATEGORIES_DIR.exists():
        shutil.rmtree(HARDENING_CATEGORIES_DIR)
    for path in (HARDENING_README_PATH, HARDENING_REPORT_PATH):
        if path.exists():
            path.unlink()


def write_hosts_file(path: Path, domains: Iterable[str], header: str) -> int:
    """Write a hosts-format list preserving exact hostnames."""
    ensure_dir(path.parent)
    unique_domains = sorted({normalize_domain(domain) for domain in domains if normalize_domain(domain)})

    content = header.rstrip() + "\n\n"
    for domain in unique_domains:
        content += f"{HOSTS_PREFIX}{domain}\n"

    path.write_text(content, encoding="utf-8")
    return len(unique_domains)


def render_category_name(category: str) -> str:
    """Convert a category id into a display label."""
    labels = {
        "brand_impersonation": "Brand Impersonation",
    }
    return labels.get(category, category.replace("_", " ").title())


def generate_readme(
    timestamp: str,
    stats: List[Dict],
    category_stats: List[Dict],
    nameservers: Optional[str],
    job_count: int,
) -> None:
    """Generate the hardening README."""
    lines: List[str] = []
    lines.append("# DNSTwist Hardening Lists\n")
    lines.append(f"**Generated:** {timestamp}\n")
    lines.append(
        "This section contains optional high-sensitivity blocklists generated from curated brand seeds "
        "with [dnstwist](https://github.com/elceef/dnstwist).\n"
    )
    lines.append(
        "These lists are designed for **hardening against brand impersonation and typo-squatting**, "
        "not for normal service blocking. They are intentionally kept separate from the standard `services/` lists.\n"
    )
    lines.append(
        "There is also a separate review layer at [active_impersonation/README.md](active_impersonation/README.md). "
        "That stage does **not** create another blocklist. Instead, it scores live lookalike domains against "
        "the real brand sites so you can review which ones look materially suspicious before promoting them "
        "anywhere.\n"
    )
    lines.append("## What DNSTwist Does\n")
    lines.append(
        "`dnstwist` generates lookalike permutations for a brand domain and checks which ones appear to be live. "
        "That makes it useful for catching typo-squatting, homoglyph tricks, and brand impersonation domains.\n"
    )
    lines.append("## Important Notes\n")
    lines.append("- **Aggressive by design** - these lists can block domains that are unrelated to your environment but happen to look like a protected brand")
    lines.append("- **Exact hostnames are preserved** - these are not collapsed to registrable roots")
    lines.append("- **Best used for high-risk brands** - identity providers, mail brands, payment brands, and collaboration tools")
    lines.append("- **Review before broad deployment** - especially if you use wildcard-heavy allow/block policies\n")
    lines.append("## Active Impersonation Review\n")
    lines.append(
        "If you want more than “this domain is a live DNSTwist permutation,” run "
        "`scripts/generate_active_impersonation.py` after the hardening lists are generated.\n"
    )
    lines.append("That report stage:")
    lines.append("- checks whether the real brand site is reachable")
    lines.append("- fingerprints live lookalikes with lightweight HTTP, TLS, and content signals")
    lines.append("- scores which domains most closely resemble the real site")
    lines.append("- writes review artifacts under `hardening/active_impersonation/`\n")
    lines.append(
        "This is useful when you want a tighter triage loop instead of auto-blocking every live permutation.\n"
    )
    lines.append("## Generation Settings\n")
    lines.append(f"- Source tool: [dnstwist](https://github.com/elceef/dnstwist)")
    lines.append("- Mode: registered lookalike domains only")
    lines.append("- Output format: hosts file (`0.0.0.0 hostname`)")
    lines.append(f"- Concurrent seed jobs: `{job_count}`")
    if nameservers:
        lines.append(f"- Nameservers: `{nameservers}`")
    else:
        lines.append("- Nameservers: system/default resolver")
    lines.append("")
    lines.append("## Running With Your Own Resolver\n")
    lines.append(
        "If you want DNSTwist to query a resolver you control, set `DNSTWIST_NAMESERVERS` or pass "
        "`--nameservers` when running the script. You can also raise `DNSTWIST_JOBS` to run multiple "
        "seed domains concurrently.\n"
    )
    lines.append("Example:\n")
    lines.append("```bash")
    lines.append("DNSTWIST_NAMESERVERS=192.168.100.5 DNSTWIST_JOBS=2 python3 scripts/generate_twisted.py")
    lines.append("```\n")
    lines.append(
        "If that resolver lives on a private address like `192.168.100.5`, the scheduled workflow should run on "
        "a **self-hosted runner inside your home network**. GitHub-hosted runners cannot reach private LAN IPs.\n"
    )
    lines.append("## Categories\n")
    lines.append("| Category | Exact Hosts | File | Raw URL |")
    lines.append("|----------|-------------|------|---------|")
    for category in sorted(category_stats, key=lambda item: item["category"]):
        rel_path = f"categories/{category['category']}.txt"
        raw_url = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/hardening/{rel_path}"
        lines.append(
            f"| {render_category_name(category['category'])} | {category['count']:,} | "
            f"[{category['category']}.txt]({rel_path}) | [Raw]({raw_url}) |"
        )
    lines.append("")
    lines.append("## Per-Target Lists\n")
    lines.append("| Target | Seeds | Exact Hosts | File | Raw URL |")
    lines.append("|--------|-------|-------------|------|---------|")
    for item in sorted(stats, key=lambda row: row["name"]):
        rel_path = f"lists/{item['category']}/{item['service_id']}.txt"
        raw_url = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/hardening/{rel_path}"
        lines.append(
            f"| {item['name']} | {len(item['seed_domains'])} | {item['count']:,} | "
            f"[{item['service_id']}.txt]({rel_path}) | [Raw]({raw_url}) |"
        )
    lines.append("")
    lines.append("## Recommended Use\n")
    lines.append("1. Start with one or two brands you care about most")
    lines.append("2. Watch DNS logs for a while before applying the aggregated category")
    lines.append("3. Prefer a resolver you control so DNSTwist lookups are consistent and fast")
    lines.append("4. Treat this as a security hardening layer, not a replacement for the main phishing lists\n")

    HARDENING_README_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_report(report: Dict) -> None:
    """Persist the generation report."""
    ensure_dir(HARDENING_DIR)
    HARDENING_REPORT_PATH.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Generate DNSTwist hardening lists")
    parser.add_argument("--config", default=str(CONFIG_PATH), help="Path to hardening target JSON config")
    parser.add_argument("--target", action="append", default=[], help="Limit generation to one or more service_ids")
    parser.add_argument("--nameservers", help="Comma-separated DNS or DoH servers passed through to dnstwist")
    parser.add_argument("--threads", type=int, help="Override dnstwist thread count for all targets")
    parser.add_argument("--jobs", type=int, help="Concurrent seed jobs to run across targets")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_config(Path(args.config).resolve())
    defaults = config.get("defaults", {})

    selected_targets = {value.strip().lower() for value in args.target if value.strip()}
    nameservers = resolve_nameservers(args.nameservers)
    thread_override = resolve_threads(args.threads)
    job_count = resolve_jobs(args.jobs)

    clear_previous_outputs()

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    target_stats: List[Dict] = []
    category_domains: Dict[str, Set[str]] = defaultdict(set)
    warnings: List[str] = []

    targets = [merge_target_config(defaults, target) for target in config["targets"]]
    if selected_targets:
        targets = [target for target in targets if target["service_id"] in selected_targets]

    if not targets:
        raise ValueError("no hardening targets selected")

    enabled_targets: List[Dict] = []
    for target in targets:
        if target["enabled"]:
            enabled_targets.append(target)
        else:
            logger.info("Skipping disabled target %s", target["service_id"])

    if not enabled_targets:
        raise ValueError("no enabled hardening targets selected")

    seed_outputs, warnings = execute_seed_jobs(enabled_targets, nameservers, thread_override, job_count)

    for target_index, target in enumerate(enabled_targets):
        logger.info("Processing %s", target["name"])
        collected: Set[str] = set()
        seed_results: List[Dict] = []
        skipped = False

        for seed_index, seed_domain in enumerate(target["seed_domains"]):
            seed_output = seed_outputs[(target_index, seed_index)]
            skipped = skipped or bool(seed_output["skipped"])
            collected.update(seed_output["domains"])
            seed_results.append(
                {
                    "seed_domain": seed_domain,
                    "count": seed_output["count"],
                    "skipped": seed_output["skipped"],
                }
            )

        out_path = HARDENING_LISTS_DIR / target["category"] / f"{target['service_id']}.txt"
        header = (
            f"# {target['name']} Brand Impersonation Hardening\n"
            f"# Category: {target['category']}\n"
            f"# Generated: {timestamp}\n"
            "# Format: Hosts file (0.0.0.0 hostname) - exact hostnames preserved\n"
            f"# Seed domains: {', '.join(target['seed_domains'])}\n"
            "# Purpose: Optional DNSTwist-based typo-squatting and impersonation hardening"
        )
        count = write_hosts_file(out_path, collected, header)
        logger.info("  Saved %d exact host(s) to %s", count, out_path)

        target_stats.append(
            {
                "category": target["category"],
                "service_id": target["service_id"],
                "name": target["name"],
                "seed_domains": target["seed_domains"],
                "count": count,
                "path": str(out_path.relative_to(REPO_ROOT)),
                "seed_results": seed_results,
                "had_skipped_seed": skipped,
            }
        )
        category_domains[target["category"]].update(collected)

    category_stats: List[Dict] = []
    for category, domains in sorted(category_domains.items()):
        out_path = HARDENING_CATEGORIES_DIR / f"{category}.txt"
        header = (
            f"# {render_category_name(category)} Hardening\n"
            f"# Generated: {timestamp}\n"
            "# Format: Hosts file (0.0.0.0 hostname) - exact hostnames preserved\n"
            "# Purpose: Aggregated DNSTwist-based impersonation hardening"
        )
        count = write_hosts_file(out_path, domains, header)
        category_stats.append(
            {
                "category": category,
                "count": count,
                "path": str(out_path.relative_to(REPO_ROOT)),
            }
        )
        logger.info("Saved %d exact host(s) to %s", count, out_path)

    generate_readme(timestamp, target_stats, category_stats, nameservers, job_count)
    write_report(
        {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "jobs": job_count,
            "nameservers": nameservers,
            "thread_override": thread_override,
            "targets": target_stats,
            "categories": category_stats,
            "warnings": warnings,
        }
    )

    logger.info("Hardening generation complete")
    logger.info("Targets: %d", len(target_stats))
    logger.info("Categories: %d", len(category_stats))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
