from collections import defaultdict
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import generator  # noqa: E402


def make_services():
    return defaultdict(generator.make_service_record)


def test_get_root_domain_handles_multi_label_cc_tld_without_psl(monkeypatch):
    monkeypatch.setattr(generator, "get_public_suffix_rules", lambda: None)
    assert generator.get_root_domain("store.example.co.uk") == "example.co.uk"


def test_load_custom_domains_merges_multiple_files(tmp_path, monkeypatch):
    first = tmp_path / "custom_a.json"
    second = tmp_path / "custom_b.json"
    first.write_text('{"alpha": ["example.com"]}\n', encoding="utf-8")
    second.write_text('{"beta": {"category": "dns", "domains": ["dns.example.com"]}}\n', encoding="utf-8")

    monkeypatch.setattr(generator, "CUSTOM_DOMAINS_FILES", [first, second])
    data = generator.load_custom_domains()

    assert data["alpha"] == ["example.com"]
    assert data["beta"]["domains"] == ["dns.example.com"]


def test_apply_custom_domains_preserves_dns_hosts():
    services = make_services()
    generator.apply_custom_domains(
        services,
        {
            "googleDNS": {
                "category": "DNS",
                "name": "Google DNS",
                "domains": ["dns.google.com"],
            }
        },
    )

    assert services["googleDNS"]["group"] == "dns"
    assert services["googleDNS"]["preserve_subdomains"] is True
    assert services["googleDNS"]["domains"] == {"dns.google.com"}


def test_extract_domains_from_urlhaus_skips_comment_banner():
    csv_text = """################################################################
# abuse.ch URLhaus Database Dump (CSV - recent URLs only)      #
# id,dateadded,url,url_status,last_online,threat,tags,urlhaus_link,reporter
"1","2026-04-24 15:10:10","https://innercoupon.foam-take.in.net/path","online","","malware_download","","","anonymous"
"2","2026-04-24 15:10:10","http://192.0.2.55:8080/payload","online","","malware_download","","","anonymous"
"""

    assert generator.extract_domains_from_urlhaus(csv_text) == {"innercoupon.foam-take.in.net"}


def test_apply_source_policies_filters_suffixes_and_sets_exact_mode():
    services = make_services()
    services["netflix"]["group"] = "streaming"
    services["netflix"]["name"] = "Netflix"
    services["netflix"]["domains"].update(
        {
            "netflix.com",
            "video-edge.edgesuite.net",
            "bucket.s3.amazonaws.com",
        }
    )
    services["googleDNS"]["group"] = "dns"
    services["googleDNS"]["name"] = "Google DNS"
    services["googleDNS"]["domains"].add("dns.google.com")

    policies = {
        "defaults": {"mode": "registrable"},
        "categories": {
            "streaming": {
                "exclude_suffix": ["edgesuite.net", "s3.amazonaws.com"],
            },
            "dns": {"mode": "exact"},
        },
        "services": {},
    }

    generator.apply_source_policies(services, policies)

    assert services["netflix"]["domains"] == {"netflix.com"}
    assert services["netflix"]["preserve_subdomains"] is False
    assert services["googleDNS"]["preserve_subdomains"] is True


def test_security_profile_preserves_exact_hosts_and_excludes_non_security_groups():
    services = make_services()
    services["openphish"]["group"] = "phishing"
    services["openphish"]["name"] = "OpenPhish"
    services["openphish"]["domains"].add("login.example.com")
    services["steam"]["group"] = "gaming"
    services["steam"]["name"] = "Steam"
    services["steam"]["domains"].add("store.steampowered.com")

    security_profile = generator.get_output_profile("security")

    assert generator.should_include_in_profile("openphish", services["openphish"], security_profile) is True
    assert generator.should_include_in_profile("steam", services["steam"], security_profile) is False
    assert generator.preserve_subdomains_for_profile("openphish", services["openphish"], security_profile) is True


def test_write_rpz_file_uses_exact_mode_without_wildcard(tmp_path):
    output = tmp_path / "security.rpz"

    count, _ = generator.write_rpz_file(
        output,
        {"login.microsoftonline.com"},
        header="; test",
        preserve_subdomains=True,
    )

    content = output.read_text(encoding="utf-8")
    assert count == 1
    assert "login.microsoftonline.com CNAME ." in content
    assert "*.login.microsoftonline.com CNAME ." not in content


def test_write_rpz_file_uses_wildcard_for_registrable_domains(tmp_path, monkeypatch):
    monkeypatch.setattr(generator, "get_public_suffix_rules", lambda: None)
    output = tmp_path / "services.rpz"

    count, _ = generator.write_rpz_file(
        output,
        {"store.example.co.uk"},
        header="; test",
        preserve_subdomains=False,
    )

    content = output.read_text(encoding="utf-8")
    assert count == 1
    assert "example.co.uk CNAME ." in content
    assert "*.example.co.uk CNAME ." in content
