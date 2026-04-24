#!/usr/bin/env python3
"""Validate generated service/category lists against repo quality policies."""

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import generator


HOST_PREFIX = "0.0.0.0 "
REPORT_PATH = generator.BASE_DIR / "quality_report.json"


def parse_domains_from_text(text: str) -> Tuple[List[str], List[str]]:
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


def get_file_context(path: Path) -> Dict[str, Optional[str]]:
    """Identify whether a file is a service or category output."""
    if path.is_relative_to(generator.LISTS_DIR):
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
    path: Optional[Path] = None,
    group: Optional[str] = None,
    service: Optional[str] = None,
) -> Dict[str, Optional[str]]:
    """Build a consistent issue payload for report and CLI output."""
    return {
        "message": message,
        "path": str(path) if path else None,
        "group": group,
        "service": service,
    }


def validate_file(path: Path, policies: Dict) -> Tuple[Dict, List[Dict]]:
    """Validate one generated file and return its summary plus any issues."""
    context = get_file_context(path)
    group = context["group"] or ""
    service = context["service"] or group
    effective_policy = generator.get_effective_policy(policies, group, service)

    text = path.read_text(encoding="utf-8")
    domains, line_errors = parse_domains_from_text(text)
    issues: List[Dict] = []

    for error in line_errors:
        issues.append(build_issue(error, path=path, group=group, service=context["service"]))

    exclude_exact = set(effective_policy.get("exclude_exact", []))
    exclude_suffix = effective_policy.get("exclude_suffix", [])

    for domain in domains:
        if not generator.is_valid_domain(domain):
            issues.append(
                build_issue(
                    f"invalid domain '{domain}'",
                    path=path,
                    group=group,
                    service=context["service"],
                )
            )
            continue

        if effective_policy.get("forbid_public_suffix_entries", True):
            public_suffix = generator.get_public_suffix(domain)
            labels = [label for label in domain.split(".") if label]
            fallback_suffix = generator.get_fallback_public_suffix(labels) if labels else ""
            if public_suffix and domain == public_suffix and fallback_suffix == domain:
                issues.append(
                    build_issue(
                        f"generic registry suffix '{domain}' should not appear in output",
                        path=path,
                        group=group,
                        service=context["service"],
                    )
                )

        if effective_policy.get("mode") != "exact":
            root_domain = generator.get_root_domain(domain)
            if domain != root_domain:
                issues.append(
                    build_issue(
                        f"unexpected exact hostname '{domain}' in registrable-domain list",
                        path=path,
                        group=group,
                        service=context["service"],
                    )
                )

        if domain in exclude_exact:
            issues.append(
                build_issue(
                    f"excluded exact domain '{domain}' is still present",
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
                path=path,
                group=group,
                service=context["service"],
            )
        )

    baseline_count = None
    delta_pct = None
    head_text = load_head_text(path)
    if head_text is not None:
        head_domains, _ = parse_domains_from_text(head_text)
        baseline_count = len(head_domains)
        min_baseline = effective_policy.get("min_baseline_count_for_delta", 5)
        max_delta_pct = effective_policy.get("max_delta_pct")

        if baseline_count >= min_baseline and max_delta_pct is not None:
            delta_pct = round(abs(len(domains) - baseline_count) * 100 / baseline_count, 2)
            if delta_pct > max_delta_pct:
                issues.append(
                    build_issue(
                        f"domain count drift {delta_pct}% exceeds limit {max_delta_pct}%",
                        path=path,
                        group=group,
                        service=context["service"],
                    )
                )

    summary = {
        "path": str(path),
        "kind": context["kind"],
        "group": group,
        "service": context["service"],
        "domain_count": len(domains),
        "baseline_count": baseline_count,
        "delta_pct": delta_pct,
    }
    return summary, issues


def expected_service_paths(policies: Dict) -> List[Tuple[str, str, Path]]:
    """Return service files the policy marks as required."""
    paths = []
    for service_id, policy in policies.get("services", {}).items():
        if not isinstance(policy, dict) or not policy.get("must_exist"):
            continue
        group = policy.get("group")
        if not group:
            continue
        paths.append((group, service_id, generator.LISTS_DIR / group / f"{service_id}.txt"))
    return paths


def write_report(report: Dict) -> None:
    """Persist the validation report next to the generated services."""
    REPORT_PATH.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    policies = generator.load_source_policies()
    if not policies:
        print("No source policies loaded; refusing to validate without policy context.", file=sys.stderr)
        return 1

    issues: List[Dict] = []
    file_summaries: List[Dict] = []

    for group, service_id, expected_path in expected_service_paths(policies):
        if not expected_path.exists():
            issues.append(
                build_issue(
                    "required generated file is missing",
                    path=expected_path,
                    group=group,
                    service=service_id,
                )
            )

    generated_files = sorted(generator.LISTS_DIR.rglob("*.txt")) + sorted(generator.CATEGORIES_DIR.glob("*.txt"))
    for path in generated_files:
        summary, file_issues = validate_file(path, policies)
        file_summaries.append(summary)
        issues.extend(file_issues)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if not issues else "failed",
        "summary": {
            "files_checked": len(file_summaries),
            "issues": len(issues),
            "total_domains": sum(item["domain_count"] for item in file_summaries),
        },
        "files": file_summaries,
        "issues": issues,
    }
    write_report(report)

    if issues:
        print("Validation failed:")
        for issue in issues[:50]:
            path_text = issue["path"] or "<no path>"
            print(f"- {path_text}: {issue['message']}")
        if len(issues) > 50:
            print(f"- ... and {len(issues) - 50} more issue(s)")
        print(f"Full report written to {REPORT_PATH}")
        return 1

    print(f"Validation passed. Report written to {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
