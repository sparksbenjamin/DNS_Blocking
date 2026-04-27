#!/usr/bin/env python3
"""Validate generated blocklist outputs against repo quality policies."""

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import generator


HOST_PREFIX = "0.0.0.0 "


def parse_domains_from_hosts_text(text: str) -> Tuple[List[str], List[str]]:
    """Return domains plus any line-format errors from a generated hosts file."""
    domains: List[str] = []
    errors: List[str] = []

    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if not line.startswith(HOST_PREFIX):
            errors.append(f"line {lineno}: expected '{HOST_PREFIX}<domain>'")
            continue

        domain = line[len(HOST_PREFIX):].strip().lower().rstrip(".")
        if not domain:
            errors.append(f"line {lineno}: missing domain after '{HOST_PREFIX}'")
            continue

        domains.append(domain)

    return domains, errors


def parse_domains_from_rpz_text(text: str) -> Tuple[List[str], List[str]]:
    """Return RPZ rule names plus any line-format errors from a generated zone file."""
    domains: List[str] = []
    errors: List[str] = []

    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith(";"):
            continue
        if line.startswith("$TTL") or line.startswith("@"):
            continue

        parts = line.split()
        if len(parts) != 3 or parts[1].upper() != "CNAME" or parts[2] != ".":
            errors.append(f"line {lineno}: expected '<domain> CNAME .'")
            continue

        domain = parts[0].strip().lower().rstrip(".")
        if domain.startswith("*."):
            domain = domain[2:]
        if not domain:
            errors.append(f"line {lineno}: missing domain before 'CNAME .'")
            continue

        domains.append(domain)

    deduped_domains = list(dict.fromkeys(domains))
    return deduped_domains, errors


def parse_domains_for_profile(profile: Dict[str, object], text: str) -> Tuple[List[str], List[str]]:
    """Dispatch parsing based on output profile format."""
    if profile["format"] == "rpz":
        return parse_domains_from_rpz_text(text)
    return parse_domains_from_hosts_text(text)


def load_head_text(path: Path) -> Optional[str]:
    """Load the version of a file from HEAD for drift comparison."""
    absolute_path = path if path.is_absolute() else (generator.REPO_ROOT / path)
    relative_path = absolute_path.relative_to(generator.REPO_ROOT).as_posix()
    result = subprocess.run(
        ["git", "show", f"HEAD:{relative_path}"],
        cwd=generator.REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout


def get_file_context(path: Path, profile: Dict[str, object]) -> Dict[str, Optional[str]]:
    """Identify whether a file is a service or category output."""
    if path.is_relative_to(profile["lists_dir"]):
        return {
            "kind": "service",
            "group": path.parent.name,
            "service": path.stem,
        }
    return {
        "kind": "category",
        "group": path.stem,
        "service": None,
    }


def build_issue(
    message: str,
    profile_name: str,
    path: Optional[Path] = None,
    group: Optional[str] = None,
    service: Optional[str] = None,
) -> Dict[str, Optional[str]]:
    """Build a consistent issue payload for report and CLI output."""
    return {
        "message": message,
        "profile": profile_name,
        "path": str(path) if path else None,
        "group": group,
        "service": service,
    }


def expected_exact_mode(
    profile: Dict[str, object],
    effective_policy: Dict,
    group: str,
    service_id: Optional[str],
) -> bool:
    """Return whether an output file should preserve exact hostnames."""
    if effective_policy.get("mode") == "exact":
        return True
    if group in profile.get("force_exact_groups", set()):
        return True
    if service_id and service_id in profile.get("force_exact_services", set()):
        return True
    return False


def validate_file(path: Path, profile_name: str, profile: Dict[str, object], policies: Dict) -> Tuple[Dict, List[Dict]]:
    """Validate one generated file and return its summary plus any issues."""
    context = get_file_context(path, profile)
    group = context["group"] or ""
    service_id = context["service"] or group
    effective_policy = generator.get_effective_policy(policies, group, service_id)
    expect_exact = expected_exact_mode(profile, effective_policy, group, context["service"])

    text = path.read_text(encoding="utf-8")
    domains, line_errors = parse_domains_for_profile(profile, text)
    issues: List[Dict] = []

    for error in line_errors:
        issues.append(
            build_issue(error, profile_name, path=path, group=group, service=context["service"])
        )

    exclude_exact = set(effective_policy.get("exclude_exact", []))
    exclude_suffix = effective_policy.get("exclude_suffix", [])

    for domain in domains:
        if not generator.is_valid_domain(domain):
            issues.append(
                build_issue(
                    f"invalid domain '{domain}'",
                    profile_name,
                    path=path,
                    group=group,
                    service=context["service"],
                )
            )
            continue

        if effective_policy.get("forbid_public_suffix_entries", True):
            public_suffix = generator.get_public_suffix(domain)
            if public_suffix and domain == public_suffix:
                issues.append(
                    build_issue(
                        f"generic registry suffix '{domain}' should not appear in output",
                        profile_name,
                        path=path,
                        group=group,
                        service=context["service"],
                    )
                )

        if not expect_exact:
            root_domain = generator.get_root_domain(domain)
            if domain != root_domain:
                issues.append(
                    build_issue(
                        f"unexpected exact hostname '{domain}' in registrable-domain list",
                        profile_name,
                        path=path,
                        group=group,
                        service=context["service"],
                    )
                )

        if domain in exclude_exact:
            issues.append(
                build_issue(
                    f"excluded exact domain '{domain}' is still present",
                    profile_name,
                    path=path,
                    group=group,
                    service=context["service"],
                )
            )

        for suffix in exclude_suffix:
            if generator.domain_matches_suffix(domain, suffix):
                issues.append(
                    build_issue(
                        f"excluded suffix '{suffix}' matched '{domain}'",
                        profile_name,
                        path=path,
                        group=group,
                        service=context["service"],
                    )
                )
                break

    missing_required = [
        domain for domain in effective_policy.get("required_domains", []) if domain not in domains
    ]
    for domain in missing_required:
        issues.append(
            build_issue(
                f"required domain '{domain}' is missing",
                profile_name,
                path=path,
                group=group,
                service=context["service"],
            )
        )

    baseline_count = None
    delta_pct = None
    head_text = load_head_text(path)
    if head_text is not None:
        head_domains, _ = parse_domains_for_profile(profile, head_text)
        baseline_count = len(head_domains)
        min_baseline = effective_policy.get("min_baseline_count_for_delta", 5)
        max_delta_pct = effective_policy.get("max_delta_pct")

        if baseline_count >= min_baseline and max_delta_pct is not None:
            delta_pct = round(abs(len(domains) - baseline_count) * 100 / baseline_count, 2)
            if delta_pct > max_delta_pct:
                issues.append(
                    build_issue(
                        f"domain count drift {delta_pct}% exceeds limit {max_delta_pct}%",
                        profile_name,
                        path=path,
                        group=group,
                        service=context["service"],
                    )
                )

    summary = {
        "path": str(path),
        "profile": profile_name,
        "kind": context["kind"],
        "group": group,
        "service": context["service"],
        "domain_count": len(domains),
        "baseline_count": baseline_count,
        "delta_pct": delta_pct,
    }
    return summary, issues


def expected_service_paths(policies: Dict, profile: Dict[str, object]) -> List[Tuple[str, str, Path]]:
    """Return required generated service files for a given output profile."""
    include_groups = profile.get("include_groups")
    paths = []
    for service_id, policy in policies.get("services", {}).items():
        if not isinstance(policy, dict) or not policy.get("must_exist"):
            continue
        group = policy.get("group")
        if not group:
            continue
        if include_groups and group not in include_groups:
            continue
        paths.append(
            (
                group,
                service_id,
                profile["lists_dir"] / group / f"{service_id}{profile['file_extension']}",
            )
        )
    return paths


def write_report(path: Path, report: Dict) -> None:
    """Persist one validation report next to the generated output tree."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def validate_profile(profile_name: str, policies: Dict) -> Tuple[Dict, List[Dict]]:
    """Validate one output profile and return its report plus flattened issues."""
    profile = generator.get_output_profile(profile_name)
    issues: List[Dict] = []
    file_summaries: List[Dict] = []

    for group, service_id, expected_path in expected_service_paths(policies, profile):
        if not expected_path.exists():
            issues.append(
                build_issue(
                    "required generated file is missing",
                    profile_name,
                    path=expected_path,
                    group=group,
                    service=service_id,
                )
            )

    pattern = f"*{profile['file_extension']}"
    generated_files = sorted(profile["lists_dir"].rglob(pattern)) + sorted(
        profile["categories_dir"].glob(pattern)
    )
    for path in generated_files:
        summary, file_issues = validate_file(path, profile_name, profile, policies)
        file_summaries.append(summary)
        issues.extend(file_issues)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "profile": profile_name,
        "status": "passed" if not issues else "failed",
        "summary": {
            "files_checked": len(file_summaries),
            "issues": len(issues),
            "total_domains": sum(item["domain_count"] for item in file_summaries),
        },
        "files": file_summaries,
        "issues": issues,
    }
    write_report(profile["quality_report_path"], report)
    return report, issues


def main() -> int:
    policies = generator.load_source_policies()
    if not policies:
        print("No source policies loaded; refusing to validate without policy context.", file=sys.stderr)
        return 1

    all_reports = []
    all_issues: List[Dict] = []

    for profile_name in generator.OUTPUT_PROFILES:
        report, issues = validate_profile(profile_name, policies)
        all_reports.append(report)
        all_issues.extend(issues)
        print(
            f"{profile_name}: checked {report['summary']['files_checked']} files, "
            f"{report['summary']['issues']} issue(s)"
        )

    if all_issues:
        for issue in all_issues:
            location = issue["path"] or "<unknown>"
            print(f"[{issue['profile']}] {location}: {issue['message']}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
