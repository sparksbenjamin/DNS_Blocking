#!/usr/bin/env python3
"""
Merge multiple threat intelligence feeds into split services files
- Splits large services across multiple JSON files (services_001.json, services_002.json, etc.)
- Each file stays under 100MB for GitHub compatibility
- Small services go in services_core.json
- Large services (like adult content) get their own files
"""

import json
import re
from pathlib import Path
import requests
from collections import defaultdict
import csv
from io import StringIO, BytesIO
import tarfile

# URLs
ADGUARD_URL = "https://adguardteam.github.io/HostlistsRegistry/assets/services.json"
PHISHING_ARMY_URL = (
    "https://raw.githubusercontent.com/Phishing-Database/Phishing.Database/"
    "refs/heads/master/phishing-domains-ACTIVE.adblock"
)
THREATFOX_URL = "https://threatfox.abuse.ch/export/json/domains/recent/"
URLHAUS_URL = "https://urlhaus.abuse.ch/downloads/csv_recent/"
OPENPHISH_URL = "https://openphish.com/feed.txt"
SSLBL_URL = "https://sslbl.abuse.ch/blacklist/sslblacklist.csv"
PHISHTANK_URL = "http://data.phishtank.com/data/online-valid.json"
EMERGING_THREATS_URL = "https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt"

# Adult Content Blocking Lists
ENERGIZED_PORN_URL = "https://block.energized.pro/porn/formats/domains.txt"
STEVENBLACK_PORN_URL = "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn/hosts"
OISD_URL = "https://big.oisd.nl/domainswild"
CLEFSPEARE_PORN_URL = "https://raw.githubusercontent.com/Clefspeare13/pornhosts/master/0.0.0.0/hosts"
CHADMAYFIELD_PORN_URL = "https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_top1m.list"
UT1_ADULT_URL = "https://dsi.ut-capitole.fr/blacklists/download/adult.tar.gz"

MAX_FILE_SIZE_MB = 90  # Leave buffer below 100MB
REQUEST_TIMEOUT = 45  # Increase timeout for large files


# -----------------------------
# Size Check
# -----------------------------
def get_json_size_mb(data):
    """Calculate size of JSON data in MB"""
    content = json.dumps(data, indent=2, ensure_ascii=False)
    return len(content.encode('utf-8')) / (1024 * 1024)


def estimate_service_size_mb(service):
    """Estimate size of a single service in MB"""
    return get_json_size_mb({"blocked_services": [service]})


# -----------------------------
# File Management
# -----------------------------
def load_existing_services():
    """Load all existing services_*.json files"""
    services = []
    for json_file in Path(".").glob("services_*.json"):
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict) and "blocked_services" in data:
                    services.extend(data["blocked_services"])
                elif isinstance(data, list):
                    services.extend(data)
        except Exception as e:
            print(f"⚠️  Failed to load {json_file}: {e}")
    return services


def save_services_split(services):
    """Save services split across multiple files to stay under size limit"""
    # Clean up old service files
    for old_file in Path(".").glob("services_*.json"):
        old_file.unlink()
        print(f"Removed old file: {old_file}")
    
    # Sort services by size (largest first)
    services_with_size = [(svc, estimate_service_size_mb(svc)) for svc in services]
    services_with_size.sort(key=lambda x: x[1], reverse=True)
    
    files_created = []
    current_file_idx = 1
    current_file_services = []
    current_file_size = 0
    
    for service, size_mb in services_with_size:
        # If adding this service would exceed limit, save current file and start new one
        if current_file_services and (current_file_size + size_mb > MAX_FILE_SIZE_MB):
            filename = f"services_{current_file_idx:03d}.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump({"blocked_services": current_file_services}, f, indent=2, ensure_ascii=False)
            actual_size = get_json_size_mb({"blocked_services": current_file_services})
            files_created.append((filename, len(current_file_services), actual_size))
            print(f"✅ Created {filename}: {len(current_file_services)} services ({actual_size:.2f}MB)")
            
            # Start new file
            current_file_idx += 1
            current_file_services = []
            current_file_size = 0
        
        current_file_services.append(service)
        current_file_size += size_mb
    
    # Save remaining services
    if current_file_services:
        filename = f"services_{current_file_idx:03d}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump({"blocked_services": current_file_services}, f, indent=2, ensure_ascii=False)
        actual_size = get_json_size_mb({"blocked_services": current_file_services})
        files_created.append((filename, len(current_file_services), actual_size))
        print(f"✅ Created {filename}: {len(current_file_services)} services ({actual_size:.2f}MB)")
    
    return files_created


# -----------------------------
# Fetchers (with increased timeout)
# -----------------------------
def fetch_adguard():
    """Return AdGuard services list."""
    print(f"Fetching AdGuard services...")
    resp = requests.get(ADGUARD_URL, timeout=REQUEST_TIMEOUT)
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
    print(f"Fetching Phishing Army...")
    resp = requests.get(PHISHING_ARMY_URL, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return resp.text


def fetch_threatfox_recent_domains():
    """Fetch recent ThreatFox domain IOCs as JSON."""
    print(f"Fetching ThreatFox...")
    resp = requests.get(THREATFOX_URL, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return resp.json()


def fetch_urlhaus_recent():
    """Fetch recent URLhaus malware URLs as CSV."""
    print(f"Fetching URLhaus...")
    resp = requests.get(URLHAUS_URL, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return resp.text


def fetch_openphish():
    """Fetch OpenPhish feed as plain text URLs."""
    print(f"Fetching OpenPhish...")
    try:
        resp = requests.get(OPENPHISH_URL, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"⚠️  OpenPhish failed: {e}")
        return ""


def fetch_sslbl():
    """Fetch SSL Blacklist as CSV."""
    print(f"Fetching SSL Blacklist...")
    resp = requests.get(SSLBL_URL, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return resp.text


def fetch_phishtank():
    """Fetch Phishtank verified phishing URLs as JSON."""
    print(f"Fetching Phishtank...")
    try:
        resp = requests.get(PHISHTANK_URL, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        print(f"⚠️  Phishtank failed: {e}")
        return []


def fetch_emerging_threats():
    """Fetch Emerging Threats block list as plain text."""
    print(f"Fetching Emerging Threats...")
    try:
        resp = requests.get(EMERGING_THREATS_URL, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"⚠️  Emerging Threats failed: {e}")
        return ""


# Adult content fetchers
def fetch_stevenblack_porn():
    """Fetch StevenBlack Porn hosts file."""
    print(f"Fetching StevenBlack Porn...")
    try:
        resp = requests.get(STEVENBLACK_PORN_URL, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"⚠️  StevenBlack Porn failed: {e}")
        return ""


def fetch_chadmayfield_porn():
    """Fetch Chad Mayfield Porn Top1M list."""
    print(f"Fetching Chad Mayfield Porn Top1M...")
    try:
        resp = requests.get(CHADMAYFIELD_PORN_URL, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"⚠️  Chad Mayfield Porn failed: {e}")
        return ""


def fetch_ut1_adult():
    """Fetch UT1 Adult category (tar.gz archive)."""
    print(f"Fetching UT1 Adult (this may take a while, it's a large file)...")
    try:
        resp = requests.get(UT1_ADULT_URL, timeout=120)  # Extra long timeout
        resp.raise_for_status()
        return resp.content
    except requests.RequestException as e:
        print(f"⚠️  UT1 Adult failed: {e}")
        return b""


# Domain extraction functions (simplified versions)
def extract_domain_from_url(url):
    """Extract domain from a full URL."""
    url = re.sub(r'^https?://', '', url)
    domain = url.split('/')[0].split('?')[0].split('#')[0]
    domain = domain.split(':')[0]
    domain = domain.lstrip('www.').lower()
    return domain


def extract_domains_from_adblock(text):
    """Extract domains from Adblock-style list."""
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


def extract_domains_from_urlhaus(csv_text):
    """Extract domains from URLhaus CSV format."""
    domains = set()
    domain_pattern = re.compile(r"^[a-z0-9.-]+\.[a-z]{2,63}$")
    
    reader = csv.DictReader(StringIO(csv_text), delimiter=',')
    for row in reader:
        if not row or any(str(v).startswith('#') for v in row.values()):
            continue
        url = row.get('url', '').strip()
        if not url or url.startswith('#'):
            continue
        domain = extract_domain_from_url(url)
        if domain and domain_pattern.fullmatch(domain):
            domains.add(domain)
    return domains


def extract_domains_from_openphish(text):
    """Extract domains from OpenPhish plain text URL list."""
    domains = set()
    domain_pattern = re.compile(r"^[a-z0-9.-]+\.[a-z]{2,63}$")
    
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        domain = extract_domain_from_url(line)
        if domain and domain_pattern.fullmatch(domain):
            domains.add(domain)
    return domains


def extract_domains_from_sslbl(csv_text):
    """Extract domains from SSL Blacklist CSV."""
    domains = set()
    domain_pattern = re.compile(r"^[a-z0-9.-]+\.[a-z]{2,63}$")
    
    for line in csv_text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split(',')
        if len(parts) >= 3:
            for part in parts:
                part = part.strip().lower()
                if domain_pattern.fullmatch(part):
                    domains.add(part)
    return domains


def extract_domains_from_phishtank(json_data):
    """Extract domains from Phishtank JSON format."""
    domains = set()
    domain_pattern = re.compile(r"^[a-z0-9.-]+\.[a-z]{2,63}$")
    
    if not json_data or not isinstance(json_data, list):
        return domains
    
    for entry in json_data:
        if not isinstance(entry, dict):
            continue
        url = entry.get('url', '').strip()
        if not url or entry.get('verified') != 'yes':
            continue
        domain = extract_domain_from_url(url)
        if domain and domain_pattern.fullmatch(domain):
            domains.add(domain)
    return domains


def extract_domains_from_hosts_file(text):
    """Extract domains from hosts file format."""
    domains = set()
    domain_pattern = re.compile(r"^[a-z0-9.-]+\.[a-z]{2,63}$")
    
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        if len(parts) >= 2:
            domain = parts[1].lower().strip()
            if domain_pattern.fullmatch(domain):
                domains.add(domain)
        elif len(parts) == 1:
            domain = parts[0].lower().strip()
            if domain_pattern.fullmatch(domain):
                domains.add(domain)
    return domains


def extract_domains_from_plain_list(text):
    """Extract domains from plain text list."""
    domains = set()
    domain_pattern = re.compile(r"^[a-z0-9.-]+\.[a-z]{2,63}$")
    
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        domain = line.lower().strip()
        if domain_pattern.fullmatch(domain):
            domains.add(domain)
    return domains


def extract_domains_from_ut1_tarball(tar_content):
    """Extract domains from UT1 tar.gz archive."""
    domains = set()
    domain_pattern = re.compile(r"^[a-z0-9.-]+\.[a-z]{2,63}$")
    
    if not tar_content:
        return domains
    
    try:
        with tarfile.open(fileobj=BytesIO(tar_content), mode='r:gz') as tar:
            for member in tar.getmembers():
                if member.isfile() and 'domains' in member.name:
                    f = tar.extractfile(member)
                    if f:
                        content = f.read().decode('utf-8', errors='ignore')
                        for line in content.splitlines():
                            line = line.strip()
                            if not line or line.startswith('#'):
                                continue
                            domain = line.lower()
                            if domain_pattern.fullmatch(domain):
                                domains.add(domain)
    except Exception as e:
        print(f"  ⚠️  Failed to extract UT1 tarball: {e}")
    
    return domains


def build_threatfox_services(data, domain_set, min_confidence=50):
    """Build ThreatFox services grouped by malware family."""
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
            "id": f"threatfox_{malware.lower().replace(' ', '_')}",
            "name": f"ThreatFox - {malware}",
            "rules": rules,
            "group": "malware",
            "source": "threatfox"
        })
    return services


def main():
    services = []
    existing_ids = set()
    domains = set()

    print("="*60)
    print("FETCHING THREAT INTELLIGENCE FEEDS")
    print("="*60)

    # --- AdGuard ---
    adguard_services = fetch_adguard()
    for svc in adguard_services:
        svc["source"] = "adguard"
        services.append(svc)
        existing_ids.add(svc["id"].lower())
        for rule in svc.get("rules", []):
            rule_domain = rule.strip("|^").lstrip("*.").lower()
            if re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", rule_domain):
                domains.add(rule_domain)

    # --- Phishing Army ---
    raw_text = fetch_phishing_army_active()
    phishing_domains = extract_domains_from_adblock(raw_text)
    domains.update(phishing_domains)
    services.append({
        "id": "phishing_army",
        "name": "Phishing Army Blocklist",
        "rules": [f"||{d}^" for d in sorted(phishing_domains)],
        "group": "phishing",
        "source": "phishing_army",
    })

    # --- ThreatFox ---
    threatfox_data = fetch_threatfox_recent_domains()
    threatfox_services = build_threatfox_services(threatfox_data, domains)
    services.extend(threatfox_services)

    # --- URLhaus ---
    urlhaus_csv = fetch_urlhaus_recent()
    urlhaus_domains = extract_domains_from_urlhaus(urlhaus_csv)
    domains.update(urlhaus_domains)
    services.append({
        "id": "urlhaus_malware",
        "name": "URLhaus Malware Distribution",
        "rules": [f"||{d}^" for d in sorted(urlhaus_domains)],
        "group": "malware",
        "source": "urlhaus",
    })

    # --- OpenPhish ---
    openphish_text = fetch_openphish()
    openphish_domains = set()
    if openphish_text:
        openphish_domains = extract_domains_from_openphish(openphish_text)
        domains.update(openphish_domains)
        services.append({
            "id": "openphish",
            "name": "OpenPhish Verified Phishing",
            "rules": [f"||{d}^" for d in sorted(openphish_domains)],
            "group": "phishing",
            "source": "openphish",
        })
        print(f"  ✓ OpenPhish: {len(openphish_domains)} domains")

    # --- SSL Blacklist ---
    sslbl_csv = fetch_sslbl()
    sslbl_domains = extract_domains_from_sslbl(sslbl_csv)
    domains.update(sslbl_domains)
    services.append({
        "id": "sslbl_malicious",
        "name": "SSL Blacklist - Malicious Certificates",
        "rules": [f"||{d}^" for d in sorted(sslbl_domains)],
        "group": "malware",
        "source": "sslbl",
    })

    # --- Phishtank ---
    phishtank_json = fetch_phishtank()
    phishtank_domains = set()
    if phishtank_json:
        phishtank_domains = extract_domains_from_phishtank(phishtank_json)
        domains.update(phishtank_domains)
        services.append({
            "id": "phishtank",
            "name": "Phishtank Verified Phishing",
            "rules": [f"||{d}^" for d in sorted(phishtank_domains)],
            "group": "phishing",
            "source": "phishtank",
        })
        print(f"  ✓ Phishtank: {len(phishtank_domains)} domains")

    # --- Adult Content (selective sources to avoid huge size) ---
    print("\n🔞 Fetching Adult Content Feeds (selective)...")
    adult_domains = set()
    
    # Only fetch smaller, more manageable lists
    stevenblack_text = fetch_stevenblack_porn()
    if stevenblack_text:
        sb_domains = extract_domains_from_hosts_file(stevenblack_text)
        adult_domains.update(sb_domains)
        print(f"  ✓ StevenBlack Porn: {len(sb_domains)} domains")
    
    chadmayfield_text = fetch_chadmayfield_porn()
    if chadmayfield_text:
        cm_domains = extract_domains_from_plain_list(chadmayfield_text)
        adult_domains.update(cm_domains)
        print(f"  ✓ Chad Mayfield Top1M: {len(cm_domains)} domains")
    
    # UT1 is HUGE (4.6M domains), so we'll make it optional
    # Uncomment if you want it despite the size:
    # ut1_content = fetch_ut1_adult()
    # if ut1_content:
    #     ut1_domains = extract_domains_from_ut1_tarball(ut1_content)
    #     adult_domains.update(ut1_domains)
    #     print(f"  ✓ UT1 Adult: {len(ut1_domains)} domains")
    
    if adult_domains:
        domains.update(adult_domains)
        services.append({
            "id": "adult_content",
            "name": "Adult Content Blocklist",
            "rules": [f"||{d}^" for d in sorted(adult_domains)],
            "group": "adult",
            "source": "multi_adult",
        })
        print(f"\n  ✅ Combined Adult Content: {len(adult_domains)} unique domains")

    # --- Save split files ---
    print("\n" + "="*60)
    print("SAVING SERVICES (SPLIT MODE)")
    print("="*60)
    
    files_created = save_services_split(services)
    
    print("\n" + "="*60)
    print("✅ UPDATE COMPLETE!")
    print("="*60)
    print(f"Total services: {len(services)}")
    print(f"Total unique domains: {len(domains)}")
    print(f"Files created: {len(files_created)}")
    for filename, count, size in files_created:
        print(f"  • {filename}: {count} services ({size:.2f}MB)")
    print("="*60)


if __name__ == "__main__":
    main()
