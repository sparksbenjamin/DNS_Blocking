from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import generate_twisted  # noqa: E402


def test_normalize_domain_handles_urls():
    assert generate_twisted.normalize_domain("https://login.microsoftonline.com/path") == "login.microsoftonline.com"
    assert generate_twisted.normalize_domain("paypal.com.") == "paypal.com"


def test_merge_target_config_normalizes_domains_and_defaults():
    merged = generate_twisted.merge_target_config(
        {
            "category": "brand_impersonation",
            "threads": 4,
            "require_dns_records": True,
        },
        {
            "service_id": "paypal",
            "name": "PayPal",
            "seed_domains": ["paypal.com", "https://www.paypal.com"],
        },
    )

    assert merged["service_id"] == "paypal"
    assert merged["threads"] == 4
    assert merged["category"] == "brand_impersonation"
    assert merged["seed_domains"] == ["paypal.com", "www.paypal.com"]


def test_filter_dnstwist_results_excludes_seeds_and_suffixes():
    target = {
        "seed_domains": ["microsoft.com", "office.com"],
        "require_dns_records": True,
        "exclude_exact": ["paypa1.com"],
        "exclude_suffix": ["example.net"],
    }

    results = [
        {"domain": "microsoft.com", "dns_a": ["1.1.1.1"]},
        {"domain": "micr0soft.com", "dns_a": ["1.1.1.1"]},
        {"domain": "paypa1.com", "dns_a": ["1.1.1.1"]},
        {"domain": "portal.example.net", "dns_ns": ["ns1.example.net"]},
        {"domain": "office-login.com"},
    ]

    assert generate_twisted.filter_dnstwist_results(results, target) == {"micr0soft.com"}


def test_filter_dnstwist_results_keeps_exact_hosts():
    target = {
        "seed_domains": ["dropbox.com"],
        "require_dns_records": True,
        "exclude_exact": [],
        "exclude_suffix": [],
    }

    results = [
        {"domain": "login-dropbox.com", "dns_a": ["1.1.1.1"]},
        {"domain": "secure.dropbox-login.com", "dns_ns": ["ns1.example.com"]},
    ]

    assert generate_twisted.filter_dnstwist_results(results, target) == {
        "login-dropbox.com",
        "secure.dropbox-login.com",
    }
