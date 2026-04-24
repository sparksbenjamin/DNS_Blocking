#!/usr/bin/env python3
"""Generate active impersonation review reports from hardening lookalike lists."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import logging
import os
import re
import socket
import ssl
import sys
import warnings
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from difflib import SequenceMatcher
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import urlparse

import requests
import urllib3
from requests import Response
from requests.exceptions import RequestException
from urllib3.exceptions import InsecureRequestWarning

import generate_twisted


warnings.filterwarnings(
    "ignore",
    message="urllib3 v2 only supports OpenSSL 1.1.1+",
)

LOGGER = logging.getLogger("active_impersonation")

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)
DEFAULT_MAX_WORKERS = 10
DEFAULT_CONNECT_TIMEOUT = 3.0
DEFAULT_READ_TIMEOUT = 5.0
DEFAULT_MAX_RESPONSE_BYTES = 262144
BASELINE_RETRY_MULTIPLIER = 2.0

ACTIVE_REPORT_DIR = generate_twisted.HARDENING_DIR / "active_impersonation"
ACTIVE_REPORT_JSON = ACTIVE_REPORT_DIR / "report.json"
ACTIVE_REPORT_TSV = ACTIVE_REPORT_DIR / "results.tsv"
ACTIVE_REPORT_README = ACTIVE_REPORT_DIR / "README.md"
HOSTS_PREFIX = "0.0.0.0 "
MAX_NOTE_LENGTH = 400


@dataclass(frozen=True)
class Fingerprint:
    domain: str
    ip: str = "N/A"
    banner: str = "Hidden"
    issuer: str = "N/A"
    scheme: str = "N/A"
    final_url: str = ""
    redirect_host: str = "N/A"
    title: str = ""
    text_preview: str = ""
    content_hash: str = ""
    http_status: str = "N/A"
    reachable: bool = False
    error: str = ""


@dataclass(frozen=True)
class AuditResult:
    service_id: str
    target_name: str
    domain: str
    status: str
    score: int
    matched_seed: str
    matched_redirect_host: str
    ip: str
    issuer: str
    banner: str
    scheme: str
    http_status: str
    redirect_host: str
    title_similarity: str
    content_similarity: str
    note: str = ""


class VisibleTextParser(HTMLParser):
    """Extract visible text while skipping scripts and styles."""

    def __init__(self) -> None:
        super().__init__()
        self._skip_depth = 0
        self._chunks: List[str] = []

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self._skip_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self._skip_depth > 0:
            self._skip_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._skip_depth == 0:
            self._chunks.append(data)

    def get_text(self) -> str:
        return " ".join(self._chunks)


def configure_logging(verbose: bool) -> None:
    """Configure CLI logging."""
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )
    urllib3.disable_warnings(InsecureRequestWarning)


def normalize_domain(domain: str) -> str:
    """Normalize any bare hostname or URL-like input into a lowercase hostname."""
    return generate_twisted.normalize_domain(domain)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate active impersonation review reports from hardening lists."
    )
    parser.add_argument("--config", default=str(generate_twisted.CONFIG_PATH), help="Path to hardening target config")
    parser.add_argument("--target", action="append", default=[], help="Limit auditing to one or more service_ids")
    parser.add_argument("--output-dir", default=str(ACTIVE_REPORT_DIR), help="Directory to write the report artifacts")
    parser.add_argument(
        "--max-workers",
        type=int,
        default=None,
        help=f"Maximum concurrent probes (default: {DEFAULT_MAX_WORKERS})",
    )
    parser.add_argument(
        "--connect-timeout",
        type=float,
        default=None,
        help=f"Socket connect timeout in seconds (default: {DEFAULT_CONNECT_TIMEOUT})",
    )
    parser.add_argument(
        "--read-timeout",
        type=float,
        default=None,
        help=f"HTTP read timeout in seconds (default: {DEFAULT_READ_TIMEOUT})",
    )
    parser.add_argument(
        "--max-response-bytes",
        type=int,
        default=None,
        help=f"Maximum response body bytes to inspect per probe (default: {DEFAULT_MAX_RESPONSE_BYTES})",
    )
    parser.add_argument(
        "--max-domains-per-target",
        type=int,
        help="Optionally cap the number of candidate domains audited per target",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logging for baseline and probe failures",
    )
    return parser.parse_args()


def resolve_selected_targets(cli_targets: Sequence[str]) -> set[str]:
    """Resolve selected targets from CLI or environment."""
    values = list(cli_targets)
    if not values:
        env_value = os.environ.get("ACTIVE_IMPERSONATION_TARGETS", "")
        if env_value.strip():
            values = [item.strip() for item in env_value.split(",")]
    return {value.strip().lower() for value in values if value.strip()}


def resolve_max_domains_per_target(cli_value: Optional[int]) -> Optional[int]:
    """Resolve an optional per-target candidate cap from CLI or environment."""
    if cli_value is not None:
        if cli_value < 1:
            raise ValueError("--max-domains-per-target must be at least 1")
        return cli_value

    env_value = os.environ.get("ACTIVE_IMPERSONATION_MAX_CANDIDATES", "").strip()
    if not env_value:
        return None

    try:
        value = int(env_value)
        if value < 1:
            raise ValueError
        return value
    except ValueError as exc:
        raise ValueError("ACTIVE_IMPERSONATION_MAX_CANDIDATES must be a positive integer") from exc


def resolve_positive_int(
    cli_value: Optional[int],
    env_name: str,
    default: int,
) -> int:
    """Resolve a positive integer from CLI, env, or default."""
    if cli_value is not None:
        if cli_value < 1:
            raise ValueError(f"{env_name} must be at least 1")
        return cli_value

    env_value = os.environ.get(env_name, "").strip()
    if not env_value:
        return default

    try:
        value = int(env_value)
        if value < 1:
            raise ValueError
        return value
    except ValueError as exc:
        raise ValueError(f"{env_name} must be a positive integer") from exc


def resolve_positive_float(
    cli_value: Optional[float],
    env_name: str,
    default: float,
) -> float:
    """Resolve a positive float from CLI, env, or default."""
    if cli_value is not None:
        if cli_value <= 0:
            raise ValueError(f"{env_name} must be greater than 0")
        return cli_value

    env_value = os.environ.get(env_name, "").strip()
    if not env_value:
        return default

    try:
        value = float(env_value)
        if value <= 0:
            raise ValueError
        return value
    except ValueError as exc:
        raise ValueError(f"{env_name} must be a positive number") from exc


def normalize_whitespace(value: str) -> str:
    """Collapse repeated whitespace into single spaces."""
    return " ".join(value.split())


def shorten_note(value: str, limit: int = MAX_NOTE_LENGTH) -> str:
    """Keep report notes readable and bounded in size."""
    cleaned = normalize_whitespace(value)
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: limit - 3].rstrip() + "..."


def resolve_ip(domain: str) -> str:
    """Resolve a hostname to a comma-separated list of unique IP addresses."""
    try:
        addrinfo = socket.getaddrinfo(domain, None, type=socket.SOCK_STREAM)
    except socket.gaierror as exc:
        raise RuntimeError(f"DNS resolution failed: {exc}") from exc

    seen: List[str] = []
    for entry in addrinfo:
        ip_address = entry[4][0]
        if ip_address not in seen:
            seen.append(ip_address)

    if not seen:
        raise RuntimeError("DNS resolution returned no addresses")

    return ",".join(seen)


def request_url(
    domain: str,
    scheme: str,
    connect_timeout: float,
    read_timeout: float,
    max_response_bytes: int,
) -> Tuple[Response, str]:
    """Request one scheme for a host and return the response plus a capped text body."""
    headers = {"User-Agent": DEFAULT_USER_AGENT}
    response = requests.get(
        f"{scheme}://{domain}",
        headers=headers,
        timeout=(connect_timeout, read_timeout),
        verify=False if scheme == "https" else True,
        allow_redirects=True,
        stream=True,
    )

    try:
        chunks: List[bytes] = []
        total = 0
        for chunk in response.iter_content(chunk_size=8192):
            if not chunk:
                continue
            remaining = max_response_bytes - total
            if remaining <= 0:
                break
            if len(chunk) > remaining:
                chunks.append(chunk[:remaining])
                total += remaining
                break
            chunks.append(chunk)
            total += len(chunk)

        payload = b"".join(chunks)
        encoding = response.encoding or response.apparent_encoding or "utf-8"
        return response, payload.decode(encoding, errors="ignore")
    except Exception:
        response.close()
        raise


def extract_title(html: str) -> str:
    """Extract the HTML title element from a page."""
    match = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        return ""
    return normalize_whitespace(unescape(match.group(1)))


def extract_visible_text(html: str, limit: int = 4000) -> str:
    """Extract visible text from a page for content similarity checks."""
    stripped = re.sub(r"<!--.*?-->", " ", html, flags=re.DOTALL)
    parser = VisibleTextParser()
    parser.feed(stripped)
    parser.close()
    text = normalize_whitespace(unescape(parser.get_text()))
    return text[:limit]


def build_content_hash(text: str) -> str:
    """Return a short hash of visible text content."""
    if not text:
        return ""
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()[:16]


def similarity_ratio(left: str, right: str) -> float:
    """Compute a stable similarity ratio for two strings."""
    if not left or not right:
        return 0.0
    return SequenceMatcher(None, left, right).ratio()


def fetch_certificate_issuer(domain: str, connect_timeout: float) -> str:
    """Fetch the TLS issuer common name for a hostname, if available."""
    context = ssl._create_unverified_context()

    with socket.create_connection((domain, 443), timeout=connect_timeout) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as tls_sock:
            certificate = tls_sock.getpeercert()

    issuer_parts = []
    common_name = ""
    for rdn in certificate.get("issuer", ()):
        for key, value in rdn:
            issuer_parts.append(f"{key}={value}")
            if key == "commonName":
                common_name = value

    if common_name:
        return common_name
    if issuer_parts:
        return ", ".join(issuer_parts)
    return "Unknown"


def get_fingerprint(
    domain: str,
    connect_timeout: float,
    read_timeout: float,
    max_response_bytes: int,
) -> Fingerprint:
    """Collect a lightweight infrastructure/content fingerprint for one domain."""
    ip_address = "N/A"
    errors: List[str] = []

    try:
        ip_address = resolve_ip(domain)
    except RuntimeError as exc:
        return Fingerprint(domain=domain, error=str(exc))

    for scheme in ("https", "http"):
        response: Optional[Response] = None
        try:
            response, html = request_url(
                domain,
                scheme,
                connect_timeout,
                read_timeout,
                max_response_bytes,
            )
            banner = response.headers.get("Server", "Hidden")
            title = extract_title(html)
            text_preview = extract_visible_text(html)
            final_url = response.url
            redirect_host = normalize_domain(urlparse(final_url).hostname or domain) or domain
            issuer = "N/A"
            if scheme == "https":
                try:
                    issuer = fetch_certificate_issuer(domain, connect_timeout)
                except OSError as exc:
                    LOGGER.debug("Certificate lookup failed for %s: %s", domain, exc)
                    errors.append(f"certificate lookup failed: {exc}")

            return Fingerprint(
                domain=domain,
                ip=ip_address,
                banner=banner,
                issuer=issuer,
                scheme=scheme,
                final_url=final_url,
                redirect_host=redirect_host,
                title=title,
                text_preview=text_preview,
                content_hash=build_content_hash(text_preview),
                http_status=str(response.status_code),
                reachable=True,
                error=shorten_note("; ".join(errors)),
            )
        except RequestException as exc:
            LOGGER.debug("%s probe failed for %s: %s", scheme.upper(), domain, exc)
            errors.append(shorten_note(f"{scheme} probe failed: {exc}"))
        except Exception as exc:  # pragma: no cover - defensive safety net
            LOGGER.debug("%s probe crashed for %s: %s", scheme.upper(), domain, exc)
            errors.append(shorten_note(f"{scheme} probe crashed: {exc}"))
        finally:
            if response is not None:
                response.close()

    return Fingerprint(
        domain=domain,
        ip=ip_address,
        reachable=False,
        error=shorten_note("; ".join(errors)) if errors else "No successful probe",
    )


def get_baseline_fingerprint(
    domain: str,
    connect_timeout: float,
    read_timeout: float,
    max_response_bytes: int,
) -> Fingerprint:
    """Collect a baseline fingerprint, retrying once with softer timeouts if needed."""
    fingerprint = get_fingerprint(domain, connect_timeout, read_timeout, max_response_bytes)
    if fingerprint.reachable:
        return fingerprint

    error_text = fingerprint.error.lower()
    if "timed out" not in error_text and "timeout" not in error_text:
        return fingerprint

    retry_connect_timeout = max(connect_timeout, connect_timeout * BASELINE_RETRY_MULTIPLIER)
    retry_read_timeout = max(read_timeout, read_timeout * BASELINE_RETRY_MULTIPLIER)
    LOGGER.info(
        "Retrying slow baseline %s with connect timeout %.1fs and read timeout %.1fs",
        domain,
        retry_connect_timeout,
        retry_read_timeout,
    )
    return get_fingerprint(
        domain,
        retry_connect_timeout,
        retry_read_timeout,
        max_response_bytes,
    )


def classify_domain(
    current: Fingerprint,
    baseline: Fingerprint,
    service_id: str,
    target_name: str,
) -> AuditResult:
    """Classify one current fingerprint against one baseline fingerprint."""
    if not current.reachable:
        return AuditResult(
            service_id=service_id,
            target_name=target_name,
            domain=current.domain,
            status="OFFLINE",
            score=0,
            matched_seed=baseline.domain,
            matched_redirect_host=baseline.redirect_host,
            ip=current.ip,
            issuer="N/A",
            banner="N/A",
            scheme="N/A",
            http_status="N/A",
            redirect_host="N/A",
            title_similarity="0.00",
            content_similarity="0.00",
            note=current.error,
        )

    score = 0
    notes: List[str] = []
    title_ratio = similarity_ratio(current.title, baseline.title)
    content_ratio = similarity_ratio(current.text_preview, baseline.text_preview)
    baseline_hosts = {
        normalize_domain(baseline.domain),
        normalize_domain(baseline.redirect_host),
    }
    baseline_hosts.discard("")
    baseline_hosts.discard("n/a")

    if baseline.banner != "Hidden" and current.banner != "Hidden":
        if current.banner == baseline.banner:
            score += 1
    else:
        notes.append("server banner unavailable")

    if baseline.issuer != "N/A" and current.issuer != "N/A":
        if current.issuer == baseline.issuer:
            score += 1
    else:
        notes.append("certificate issuer unavailable")

    if normalize_domain(current.redirect_host) in baseline_hosts:
        score += 2
        notes.append(f"redirects to baseline host {current.redirect_host}")
    elif current.redirect_host != current.domain:
        notes.append(f"redirects to {current.redirect_host}")

    if title_ratio >= 0.9:
        score += 2
    elif title_ratio >= 0.75:
        score += 1

    if content_ratio >= 0.9:
        score += 3
    elif content_ratio >= 0.75:
        score += 2
    elif content_ratio >= 0.6:
        score += 1

    if current.content_hash and baseline.content_hash and current.content_hash == baseline.content_hash:
        score += 2
        notes.append("content hash matches baseline")

    if baseline.scheme != "N/A" and current.scheme != baseline.scheme:
        notes.append(f"served over {current.scheme} instead of {baseline.scheme}")

    if not current.title:
        notes.append("page title unavailable")
    if not current.text_preview:
        notes.append("visible text unavailable")

    if score >= 6:
        status = "HIGH_MATCH"
    elif score >= 3:
        status = "MEDIUM_MATCH"
    elif score >= 1:
        status = "LOW_MATCH"
    else:
        status = "INCONCLUSIVE"

    return AuditResult(
        service_id=service_id,
        target_name=target_name,
        domain=current.domain,
        status=status,
        score=score,
        matched_seed=baseline.domain,
        matched_redirect_host=baseline.redirect_host,
        ip=current.ip,
        issuer=current.issuer,
        banner=current.banner,
        scheme=current.scheme,
        http_status=current.http_status,
        redirect_host=current.redirect_host,
        title_similarity=f"{title_ratio:.2f}",
        content_similarity=f"{content_ratio:.2f}",
        note=shorten_note("; ".join(notes)),
    )


def choose_best_result(
    current: Fingerprint,
    baselines: Sequence[Fingerprint],
    service_id: str,
    target_name: str,
) -> AuditResult:
    """Classify a domain against all baselines and keep the best match."""
    classified = [classify_domain(current, baseline, service_id, target_name) for baseline in baselines]
    return max(
        classified,
        key=lambda item: (
            item.score,
            float(item.content_similarity),
            float(item.title_similarity),
            item.matched_seed,
        ),
    )


def audit_domain(
    domain: str,
    baselines: Sequence[Fingerprint],
    service_id: str,
    target_name: str,
    connect_timeout: float,
    read_timeout: float,
    max_response_bytes: int,
) -> AuditResult:
    """Audit one candidate domain safely so one failure does not stop the target."""
    try:
        current = get_fingerprint(domain, connect_timeout, read_timeout, max_response_bytes)
        return choose_best_result(current, baselines, service_id, target_name)
    except Exception as exc:  # pragma: no cover - defensive safety net
        LOGGER.exception("Unexpected audit failure for %s", domain)
        baseline = baselines[0]
        return AuditResult(
            service_id=service_id,
            target_name=target_name,
            domain=domain,
            status="ERROR",
            score=0,
            matched_seed=baseline.domain,
            matched_redirect_host=baseline.redirect_host,
            ip="N/A",
            issuer="N/A",
            banner="N/A",
            scheme="N/A",
            http_status="N/A",
            redirect_host="N/A",
            title_similarity="0.00",
            content_similarity="0.00",
            note=shorten_note(str(exc)),
        )


def read_hosts_domains(path: Path) -> List[str]:
    """Read exact hostnames from a generated hosts-format file."""
    domains: List[str] = []
    seen = set()

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if not line.startswith(HOSTS_PREFIX):
            continue

        domain = normalize_domain(line[len(HOSTS_PREFIX):].strip())
        if not domain or domain in seen:
            continue

        seen.add(domain)
        domains.append(domain)

    return domains


def candidate_similarity(domain: str, seed_domains: Sequence[str]) -> float:
    """Compute a cheap lexical similarity score for candidate prioritization."""
    return max((similarity_ratio(domain, seed) for seed in seed_domains), default=0.0)


def limit_candidate_domains(
    domains: Iterable[str],
    seed_domains: Sequence[str],
    max_domains: Optional[int],
) -> List[str]:
    """Optionally cap candidate domains while keeping the most similar ones first."""
    unique = sorted({normalize_domain(domain) for domain in domains if normalize_domain(domain)})
    if max_domains is None or len(unique) <= max_domains:
        return unique

    ranked = sorted(
        unique,
        key=lambda domain: (-candidate_similarity(domain, seed_domains), domain),
    )
    return ranked[:max_domains]


def count_statuses(results: Sequence[AuditResult]) -> Dict[str, int]:
    """Count statuses across a list of results."""
    counts: Dict[str, int] = {
        "HIGH_MATCH": 0,
        "MEDIUM_MATCH": 0,
        "LOW_MATCH": 0,
        "INCONCLUSIVE": 0,
        "OFFLINE": 0,
        "ERROR": 0,
    }
    for result in results:
        counts[result.status] = counts.get(result.status, 0) + 1
    return counts


def write_results_tsv(path: Path, results: Sequence[AuditResult]) -> None:
    """Write a flat TSV report for spreadsheet-friendly review."""
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            [
                "TARGET",
                "DOMAIN",
                "STATUS",
                "SCORE",
                "MATCHED_SEED",
                "MATCHED_REDIRECT_HOST",
                "IP",
                "SCHEME",
                "HTTP_STATUS",
                "REDIRECT_HOST",
                "TITLE_SIMILARITY",
                "CONTENT_SIMILARITY",
                "SSL_ISSUER",
                "SERVER_BANNER",
                "NOTE",
            ]
        )
        for result in results:
            writer.writerow(
                [
                    result.target_name,
                    result.domain,
                    result.status,
                    result.score,
                    result.matched_seed,
                    result.matched_redirect_host,
                    result.ip,
                    result.scheme,
                    result.http_status,
                    result.redirect_host,
                    result.title_similarity,
                    result.content_similarity,
                    result.issuer,
                    result.banner,
                    result.note,
                ]
            )


def write_json_report(path: Path, report: Dict) -> None:
    """Write a machine-readable JSON report."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_readme(path: Path, report: Dict, results: Sequence[AuditResult]) -> None:
    """Render a Markdown summary of the active impersonation review results."""
    path.parent.mkdir(parents=True, exist_ok=True)
    settings = report["settings"]
    targets = report["targets"]
    overall = report["summary"]["statuses"]
    lines: List[str] = []

    lines.append("# Active Impersonation Review\n")
    lines.append(f"**Generated:** {report['generated_at']}\n")
    lines.append(
        "This report scores live DNSTwist lookalike domains against the real brand sites using "
        "lightweight fingerprinting. It is a **review artifact**, not an auto-promoted blocklist.\n"
    )
    lines.append("Quick links:\n")
    lines.append("- [Back to Hardening](../README.md)")
    lines.append("- [Back to Repo Root](../../README.md)\n")
    lines.append("## What This Means\n")
    lines.append("- **HIGH_MATCH** - the candidate looks materially like the baseline and deserves immediate review")
    lines.append("- **MEDIUM_MATCH** - some signals line up, but it still needs analyst judgment")
    lines.append("- **LOW_MATCH / INCONCLUSIVE** - weak resemblance or not enough content to decide")
    lines.append("- **OFFLINE / ERROR** - the candidate did not respond cleanly during this run\n")

    lines.append("## Settings\n")
    lines.append(f"- Targets audited: `{report['summary']['targets_audited']}`")
    lines.append(f"- Candidate domains audited: `{report['summary']['domains_audited']}`")
    lines.append(f"- Max workers: `{settings['max_workers']}`")
    lines.append(f"- Connect timeout: `{settings['connect_timeout']}` seconds")
    lines.append(f"- Read timeout: `{settings['read_timeout']}` seconds")
    lines.append(f"- Max response bytes: `{settings['max_response_bytes']}`")
    if settings["max_domains_per_target"] is None:
        lines.append("- Max domains per target: `unlimited`")
    else:
        lines.append(f"- Max domains per target: `{settings['max_domains_per_target']}`")
    lines.append(f"- TSV report: [results.tsv](results.tsv)")
    lines.append(f"- JSON report: [report.json](report.json)\n")

    lines.append("## Overall Summary\n")
    lines.append("| HIGH | MEDIUM | LOW | INCONCLUSIVE | OFFLINE | ERROR |")
    lines.append("|------|--------|-----|--------------|---------|-------|")
    lines.append(
        f"| {overall['HIGH_MATCH']} | {overall['MEDIUM_MATCH']} | {overall['LOW_MATCH']} | "
        f"{overall['INCONCLUSIVE']} | {overall['OFFLINE']} | {overall['ERROR']} |"
    )
    lines.append("")

    lines.append("## Per-Target Summary\n")
    lines.append("| Target | Seeds | Audited | High | Medium | Low | Offline | Errors |")
    lines.append("|--------|-------|---------|------|--------|-----|---------|--------|")
    for target in sorted(targets, key=lambda item: item["name"]):
        counts = target["status_counts"]
        lines.append(
            f"| {target['name']} | {len(target['seed_domains'])} | {target['audited_count']} | "
            f"{counts['HIGH_MATCH']} | {counts['MEDIUM_MATCH']} | {counts['LOW_MATCH']} | "
            f"{counts['OFFLINE']} | {counts['ERROR']} |"
        )
    lines.append("")

    suspicious = [
        result
        for result in results
        if result.status in {"HIGH_MATCH", "MEDIUM_MATCH"}
    ]
    suspicious = sorted(
        suspicious,
        key=lambda item: (-item.score, -float(item.content_similarity), item.domain),
    )[:25]

    lines.append("## Top Suspicious Matches\n")
    if not suspicious:
        lines.append("No high-confidence or medium-confidence matches were found in this run.\n")
    else:
        lines.append("| Target | Domain | Status | Score | Baseline | Redirect | Title | Content |")
        lines.append("|--------|--------|--------|-------|----------|----------|-------|---------|")
        for result in suspicious:
            lines.append(
                f"| {result.target_name} | `{result.domain}` | {result.status} | {result.score} | "
                f"`{result.matched_seed}` | `{result.redirect_host}` | {result.title_similarity} | "
                f"{result.content_similarity} |"
            )
        lines.append("")

    lines.append("## Operational Notes\n")
    lines.append("1. Use this report to review and promote domains manually into a curated blocklist if needed")
    lines.append("2. A redirect to the real brand is suspicious, but not sufficient proof on its own")
    lines.append("3. Similar content and matching certificate/banner signals raise confidence")
    lines.append("4. Re-run the report when you regenerate hardening lists or change target coverage\n")

    path.write_text("\n".join(lines), encoding="utf-8")


def build_target_list(
    config_path: Path,
    selected_targets: set[str],
) -> List[Dict]:
    """Load and normalize configured hardening targets."""
    config = generate_twisted.load_config(config_path)
    defaults = config.get("defaults", {})

    targets = [
        generate_twisted.merge_target_config(defaults, target)
        for target in config["targets"]
    ]
    if selected_targets:
        targets = [target for target in targets if target["service_id"] in selected_targets]

    return [target for target in targets if target["enabled"]]


def load_candidate_domains(target: Dict) -> List[str]:
    """Load candidate domains for one target from the generated hardening list."""
    path = generate_twisted.HARDENING_LISTS_DIR / target["category"] / f"{target['service_id']}.txt"
    if not path.exists():
        raise FileNotFoundError(
            f"generated hardening list is missing for {target['service_id']}: {path}"
        )
    return read_hosts_domains(path)


def build_baselines(
    target: Dict,
    connect_timeout: float,
    read_timeout: float,
    max_response_bytes: int,
) -> Tuple[List[Fingerprint], List[str]]:
    """Build reachable baseline fingerprints from a target's seed domains."""
    baselines: List[Fingerprint] = []
    warnings_list: List[str] = []

    for seed_domain in target["seed_domains"]:
        fingerprint = get_baseline_fingerprint(
            seed_domain,
            connect_timeout,
            read_timeout,
            max_response_bytes,
        )
        if fingerprint.reachable:
            baselines.append(fingerprint)
        else:
            warning = f"{target['service_id']} baseline failed for {seed_domain}: {fingerprint.error}"
            warnings_list.append(warning)
            LOGGER.warning(warning)

    return baselines, warnings_list


def audit_target(
    target: Dict,
    max_workers: int,
    connect_timeout: float,
    read_timeout: float,
    max_response_bytes: int,
    max_domains_per_target: Optional[int],
) -> Tuple[Dict, List[AuditResult], List[str]]:
    """Audit all selected candidate domains for one target."""
    warnings_list: List[str] = []
    candidate_domains = load_candidate_domains(target)
    selected_domains = limit_candidate_domains(
        candidate_domains,
        target["seed_domains"],
        max_domains_per_target,
    )

    baselines, baseline_warnings = build_baselines(
        target,
        connect_timeout,
        read_timeout,
        max_response_bytes,
    )
    warnings_list.extend(baseline_warnings)

    if not baselines:
        raise RuntimeError(f"no reachable baselines available for target {target['service_id']}")

    results: List[AuditResult] = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_map = {
            executor.submit(
                audit_domain,
                domain,
                baselines,
                target["service_id"],
                target["name"],
                connect_timeout,
                read_timeout,
                max_response_bytes,
            ): domain
            for domain in selected_domains
        }

        for future in as_completed(future_map):
            try:
                results.append(future.result())
            except Exception as exc:  # pragma: no cover - defensive safety net
                domain = future_map[future]
                warning = f"{target['service_id']} probe crashed for {domain}: {exc}"
                LOGGER.warning(warning)
                warnings_list.append(warning)

    results.sort(
        key=lambda item: (-item.score, -float(item.content_similarity), item.domain)
    )
    status_counts = count_statuses(results)

    target_summary = {
        "service_id": target["service_id"],
        "name": target["name"],
        "category": target["category"],
        "seed_domains": target["seed_domains"],
        "candidate_count": len(candidate_domains),
        "audited_count": len(results),
        "status_counts": status_counts,
        "baselines": [asdict(item) for item in baselines],
        "results": [asdict(item) for item in results],
    }
    if max_domains_per_target is not None and len(candidate_domains) > max_domains_per_target:
        target_summary["note"] = (
            f"Audited the top {max_domains_per_target} domains by lexical similarity out of "
            f"{len(candidate_domains)} generated candidates."
        )

    return target_summary, results, warnings_list


def ensure_placeholder_readme(path: Path) -> None:
    """Ensure the output directory at least contains a README when no report exists yet."""
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "# Active Impersonation Review\n\n"
        "Run `python3 scripts/generate_active_impersonation.py` after generating hardening lists "
        "or trigger the `Update Active Impersonation Review` workflow to populate this directory "
        "with review reports.\n",
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    configure_logging(args.verbose)

    config_path = Path(args.config).resolve()
    output_dir = Path(args.output_dir).resolve()
    selected_targets = resolve_selected_targets(args.target)

    try:
        max_workers = resolve_positive_int(
            args.max_workers,
            "ACTIVE_IMPERSONATION_MAX_WORKERS",
            DEFAULT_MAX_WORKERS,
        )
        connect_timeout = resolve_positive_float(
            args.connect_timeout,
            "ACTIVE_IMPERSONATION_CONNECT_TIMEOUT",
            DEFAULT_CONNECT_TIMEOUT,
        )
        read_timeout = resolve_positive_float(
            args.read_timeout,
            "ACTIVE_IMPERSONATION_READ_TIMEOUT",
            DEFAULT_READ_TIMEOUT,
        )
        max_response_bytes = resolve_positive_int(
            args.max_response_bytes,
            "ACTIVE_IMPERSONATION_MAX_RESPONSE_BYTES",
            DEFAULT_MAX_RESPONSE_BYTES,
        )
        max_domains_per_target = resolve_max_domains_per_target(args.max_domains_per_target)

        targets = build_target_list(config_path, selected_targets)
        if not targets:
            raise RuntimeError("no active impersonation targets selected")

        all_results: List[AuditResult] = []
        target_reports: List[Dict] = []
        warnings_list: List[str] = []

        for target in targets:
            LOGGER.info("Auditing target %s", target["name"])
            target_report, results, target_warnings = audit_target(
                target,
                max_workers,
                connect_timeout,
                read_timeout,
                max_response_bytes,
                max_domains_per_target,
            )
            all_results.extend(results)
            target_reports.append(target_report)
            warnings_list.extend(target_warnings)

        all_results.sort(
            key=lambda item: (-item.score, -float(item.content_similarity), item.target_name, item.domain)
        )
        summary_counts = count_statuses(all_results)

        report = {
            "generated_at": generate_twisted.datetime.now(generate_twisted.timezone.utc).isoformat(),
            "settings": {
                "max_workers": max_workers,
                "connect_timeout": connect_timeout,
                "read_timeout": read_timeout,
                "max_response_bytes": max_response_bytes,
                "max_domains_per_target": max_domains_per_target,
                "selected_targets": sorted(selected_targets),
            },
            "summary": {
                "targets_audited": len(target_reports),
                "domains_audited": len(all_results),
                "statuses": summary_counts,
            },
            "targets": target_reports,
            "warnings": warnings_list,
        }

        output_dir.mkdir(parents=True, exist_ok=True)
        json_path = output_dir / ACTIVE_REPORT_JSON.name
        tsv_path = output_dir / ACTIVE_REPORT_TSV.name
        readme_path = output_dir / ACTIVE_REPORT_README.name

        write_json_report(json_path, report)
        write_results_tsv(tsv_path, all_results)
        write_readme(readme_path, report, all_results)

        LOGGER.info("Active impersonation review complete")
        LOGGER.info("Targets audited: %d", len(target_reports))
        LOGGER.info("Domains audited: %d", len(all_results))
        return 0
    except KeyboardInterrupt:
        LOGGER.error("Interrupted by user")
        return 130
    except RuntimeError as exc:
        LOGGER.error("%s", exc)
        ensure_placeholder_readme(output_dir / ACTIVE_REPORT_README.name)
        return 1
    except FileNotFoundError as exc:
        LOGGER.error("%s", exc)
        ensure_placeholder_readme(output_dir / ACTIVE_REPORT_README.name)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
