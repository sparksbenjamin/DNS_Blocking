from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import generate_active_impersonation as active_impersonation  # noqa: E402


def test_limit_candidate_domains_prioritizes_most_similar_domains():
    domains = [
        "paypa1.com",
        "paypal-login.com",
        "completely-random-example.net",
    ]

    limited = active_impersonation.limit_candidate_domains(domains, ["paypal.com"], 2)

    assert "paypa1.com" in limited
    assert "paypal-login.com" in limited
    assert "completely-random-example.net" not in limited


def test_classify_domain_accepts_baseline_redirect_alias():
    baseline = active_impersonation.Fingerprint(
        domain="paypal.com",
        redirect_host="www.paypal.com",
        banner="nginx",
        issuer="DigiCert",
        scheme="https",
        title="PayPal",
        text_preview="Send payments worldwide",
        content_hash=active_impersonation.build_content_hash("Send payments worldwide"),
        reachable=True,
    )
    current = active_impersonation.Fingerprint(
        domain="paypa1-support.example",
        redirect_host="www.paypal.com",
        banner="nginx",
        issuer="DigiCert",
        scheme="https",
        title="PayPal",
        text_preview="Send payments worldwide",
        content_hash=active_impersonation.build_content_hash("Send payments worldwide"),
        http_status="200",
        reachable=True,
    )

    result = active_impersonation.classify_domain(current, baseline, "paypal", "PayPal")

    assert result.status == "HIGH_MATCH"
    assert result.score >= 8
    assert "redirects to baseline host www.paypal.com" in result.note


def test_choose_best_result_prefers_highest_scoring_baseline():
    current = active_impersonation.Fingerprint(
        domain="login-microsoftsecure.example",
        redirect_host="login.microsoftonline.com",
        banner="Microsoft-IIS/10.0",
        issuer="Microsoft Azure RSA TLS Issuing CA 07",
        scheme="https",
        title="Sign in to your account",
        text_preview="Enter your password to continue",
        content_hash=active_impersonation.build_content_hash("Enter your password to continue"),
        http_status="200",
        reachable=True,
    )
    weak = active_impersonation.Fingerprint(
        domain="office.com",
        redirect_host="www.office.com",
        banner="nginx",
        issuer="Other CA",
        scheme="https",
        title="Office",
        text_preview="Collaborate",
        content_hash=active_impersonation.build_content_hash("Collaborate"),
        reachable=True,
    )
    strong = active_impersonation.Fingerprint(
        domain="microsoftonline.com",
        redirect_host="login.microsoftonline.com",
        banner="Microsoft-IIS/10.0",
        issuer="Microsoft Azure RSA TLS Issuing CA 07",
        scheme="https",
        title="Sign in to your account",
        text_preview="Enter your password to continue",
        content_hash=active_impersonation.build_content_hash("Enter your password to continue"),
        reachable=True,
    )

    result = active_impersonation.choose_best_result(
        current,
        [weak, strong],
        "microsoft",
        "Microsoft",
    )

    assert result.matched_seed == "microsoftonline.com"
    assert result.status == "HIGH_MATCH"


def test_read_hosts_domains_extracts_unique_hosts(tmp_path):
    path = tmp_path / "domains.txt"
    path.write_text(
        "# sample\n"
        "0.0.0.0 foo.example.com\n"
        "0.0.0.0 foo.example.com\n"
        "0.0.0.0 bar.example.com\n",
        encoding="utf-8",
    )

    assert active_impersonation.read_hosts_domains(path) == [
        "foo.example.com",
        "bar.example.com",
    ]


def test_get_baseline_fingerprint_retries_timeouts(monkeypatch):
    calls = []

    def fake_get_fingerprint(domain, connect_timeout, read_timeout, max_response_bytes):
        calls.append((domain, connect_timeout, read_timeout, max_response_bytes))
        if len(calls) == 1:
            return active_impersonation.Fingerprint(
                domain=domain,
                reachable=False,
                error="https probe failed: Read timed out",
            )
        return active_impersonation.Fingerprint(
            domain=domain,
            reachable=True,
            scheme="https",
            title="Baseline",
            text_preview="Baseline content",
        )

    monkeypatch.setattr(active_impersonation, "get_fingerprint", fake_get_fingerprint)

    result = active_impersonation.get_baseline_fingerprint("adobe.com", 3.0, 5.0, 1024)

    assert result.reachable is True
    assert calls == [
        ("adobe.com", 3.0, 5.0, 1024),
        ("adobe.com", 6.0, 10.0, 1024),
    ]


def test_resolve_positive_float_prefers_env(monkeypatch):
    monkeypatch.setenv("ACTIVE_IMPERSONATION_READ_TIMEOUT", "9.5")

    assert active_impersonation.resolve_positive_float(
        None,
        "ACTIVE_IMPERSONATION_READ_TIMEOUT",
        active_impersonation.DEFAULT_READ_TIMEOUT,
    ) == 9.5


def test_audit_target_skips_when_no_baselines(monkeypatch):
    target = {
        "service_id": "servicenow",
        "name": "ServiceNow",
        "category": "brand_impersonation",
        "seed_domains": ["servicenow.com"],
    }

    monkeypatch.setattr(active_impersonation, "load_candidate_domains", lambda _: ["foo.example"])
    monkeypatch.setattr(
        active_impersonation,
        "build_baselines",
        lambda *args, **kwargs: ([], ["servicenow baseline failed"]),
    )

    target_summary, results, warnings_list = active_impersonation.audit_target(
        target,
        max_workers=4,
        connect_timeout=3.0,
        read_timeout=5.0,
        max_response_bytes=1024,
        max_domains_per_target=None,
    )

    assert results == []
    assert target_summary["audited_count"] == 0
    assert target_summary["status_counts"] == active_impersonation.empty_status_counts()
    assert "Skipped target because no reachable baselines were available." == target_summary["note"]
    assert any("no reachable baselines available" in warning for warning in warnings_list)
