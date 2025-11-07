#!/usr/bin/env python3
"""
Merge AdGuard, Phishing Army, and ThreatFox services into local services.json
- AdGuard: structured entries from Hostlists Registry
- Phishing Army: single grouped entry
- ThreatFox: malware-grouped entries (each malware family = service)
- Maintains a running set of unique domains (not persisted)
"""

import json
import re
from pathlib import Path
import requests
from collections import defaultdict

ADGUARD_URL = "https://adguardteam.github.io/HostlistsRegistry/assets/services.json"
PHISHING_ARMY_URL = (
    "https://raw.githubusercontent.com/Phishing-Database/Phishing.Database/"
    "refs/heads/master/phishing-domains-ACTIVE.adblock"
)
THREATFOX_URL = "https://threatfox.abuse.ch/export/json/domains/recent/"


# -----------------------------
# Fetchers
# -----------------------------
def fetch_adguard():
    """Return AdGuard services list."""
    print(f"Fetching AdGuard services from {ADGUARD_URL} ...")
    resp = requests.get(ADGUARD_URL)
    resp.raise_for_status()
    data = resp.json()
    if isinstance(data, dict) and "blocked_services" in data:
        return data["blocked_services"]
    elif isinstance(data, list):
        return data
    else:
        raise ValueError("Unexpected AdGuard JSON structure")


def fetch_phishing_army_active():
    """Return raw adblock text from Phishing Army."""
    print(f"Fetching Phishing Army list from {PHISHING_ARMY_URL} ...")
    resp = requests.get(PHISHING_ARMY_URL)
    resp.raise_for_status()
    return resp.text


def fetch_threatfox_recent_domains():
    """Fetch recent ThreatFox domain IOCs as JSON."""
    print(f"Fetching ThreatFox recent domains from {THREATFOX_URL} ...")
    resp = requests.get(THREATFOX_URL, timeout=30)
    resp.raise_for_status()
    return resp.json()


# -----------------------------
# Helpers
# -----------------------------
def extract_domains_from_adblock(text):
    """Extract domains from Adblock-style list using || and ^ markers."""
    domains = set()
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith(("!", "#", "[", "@")):
            continue
        if line.startswith("||"):
            domain = line[2:].split("^")[0].strip()
        else:
            domain = line.split("^")[0].strip()
        domain = domain.lstrip("*.").lower()
        if re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", domain):
            domains.add(domain)
    return domains


def load_local_services(path: Path):
    """Load local services.json and return blocked_services list."""
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict) and "blocked_services" in data:
        return data["blocked_services"]
    return data


def save_local_services(path: Path, services):
    """Save services.json with blocked_services list."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"blocked_services": services}, f, indent=2, ensure_ascii=False)
    print(f"Wrote updated services.json with {len(services)} entries.")


def build_threatfox_services(data, domain_set, min_confidence=50):
    """
    Build ThreatFox services grouped by malware family.
    data: dict from ThreatFox API
    domain_set: set to update running unique domains
    min_confidence: only include IOCs with confidence >= threshold
    """
    from collections import defaultdict
    services_by_malware = defaultdict(set)
    domain_pattern = re.compile(r"^[a-z0-9.-]+\.[a-z]{2,63}$")

    for ioc_id, entries in data.items():
        for entry in entries:
            if entry.get("ioc_type") != "domain":
                continue
            if entry.get("confidence_level", 0) < min_confidence:
                continue
            domain = entry.get("ioc_value", "").lower().strip()
            if not domain_pattern.fullmatch(domain):
                continue
            malware = entry.get("malware_printable") or entry.get("malware") or "unknown"
            services_by_malware[malware].add(domain)
            domain_set.add(domain)

    services = []
    for malware, domains in services_by_malware.items():
        rules = [f"||{d}^" for d in sorted(domains)]
        services.append({
            "id": malware.lower().replace(" ", "_"),
            "name": malware,
            "rules": rules,
            "group": "malware",
            "source": "threatfox"
        })
    return services



# -----------------------------
# Main Flow
# -----------------------------
def main():
    path = Path("services.json")
    services = load_local_services(path)
    existing_ids = {svc.get("id", "").lower() for svc in services}
    domains = set()

    # --- AdGuard ---
    adguard_services = fetch_adguard()
    for svc in adguard_services:
        if svc["id"].lower() not in existing_ids:
            svc["source"] = "adguard"
            services.append(svc)
            existing_ids.add(svc["id"].lower())
        # Collect domains from AdGuard entries
        for rule in svc.get("rules", []):
            rule_domain = rule.strip("|^").lstrip("*.").lower()
            if re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", rule_domain):
                domains.add(rule_domain)

    # --- Phishing Army ---
    raw_text = fetch_phishing_army_active()
    phishing_domains = extract_domains_from_adblock(raw_text)
    domains.update(phishing_domains)
    phishing_service = {
        "id": "phishing_army",
        "name": "Phishing Army Blocklist",
        "rules": [f"||{d}^" for d in sorted(phishing_domains)],
        "group": "phishing",
        "source": "phishing_army",
    }
    # Replace or add Phishing Army entry
    for i, svc in enumerate(services):
        if svc.get("id", "").lower() == "phishing_army":
            services[i] = phishing_service
            break
    else:
        services.append(phishing_service)

    # --- ThreatFox ---
    threatfox_data = fetch_threatfox_recent_domains()
    threatfox_services = build_threatfox_services(threatfox_data, domains)
    # Remove any existing threatfox entries before adding new
    services = [s for s in services if s.get("source") != "threatfox"]
    services.extend(threatfox_services)

    # --- Save and summary ---
    save_local_services(path, services)

    print("✅ Update complete.")
    print(f"Total services: {len(services)}")
    print(f"Total unique domains: {len(domains)}")
    print(f"Phishing Army: {len(phishing_domains)} | ThreatFox families: {len(threatfox_services)}")


if __name__ == "__main__":
    main()
