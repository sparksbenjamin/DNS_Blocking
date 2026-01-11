#!/usr/bin/env python3
"""
Merge multiple threat intelligence feeds into local services.json
- AdGuard: structured entries from Hostlists Registry
- Phishing Army: single grouped entry
- ThreatFox: malware-grouped entries (each malware family = service)
- URLhaus: malware distribution domains
- OpenPhish: verified phishing domains
- SSL Blacklist: malicious SSL certificate domains
- Phishtank: community-verified phishing URLs
- Emerging Threats: enterprise-grade threat intelligence (primarily IPs, some domains)
- Adult Content: 6 combined sources (Energized, StevenBlack, OISD, Clefspeare, ChadMayfield, UT1)
- Maintains a running set of unique domains (not persisted)
- Includes 100MB size check for GitHub compatibility
"""

import json
import re
from pathlib import Path
import requests
from collections import defaultdict
import csv
from io import StringIO, BytesIO
import tarfile
import tempfile

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

# Note: Phishtank may require API key for higher rate limits
# For API key usage, use: http://data.phishtank.com/data/{API_KEY}/online-valid.json

MAX_FILE_SIZE_MB = 100


# -----------------------------
# Size Check
# -----------------------------
def check_file_size(filepath, content, max_mb=MAX_FILE_SIZE_MB):
    """Check if content would exceed size limit"""
    size_mb = len(content.encode('utf-8')) / (1024 * 1024)
    if size_mb > max_mb:
        raise ValueError(
            f"ERROR: {filepath} would be {size_mb:.2f}MB, "
            f"exceeding {max_mb}MB GitHub limit"
        )
    return size_mb


# -----------------------------
# Fetchers
# -----------------------------
def fetch_adguard():
    """Return AdGuard services list."""
    print(f"Fetching AdGuard services from {ADGUARD_URL} ...")
    resp = requests.get(ADGUARD_URL, timeout=30)
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
    resp = requests.get(PHISHING_ARMY_URL, timeout=30)
    resp.raise_for_status()
    return resp.text


def fetch_threatfox_recent_domains():
    """Fetch recent ThreatFox domain IOCs as JSON."""
    print(f"Fetching ThreatFox recent domains from {THREATFOX_URL} ...")
    resp = requests.get(THREATFOX_URL, timeout=30)
    resp.raise_for_status()
    return resp.json()


def fetch_urlhaus_recent():
    """Fetch recent URLhaus malware URLs as CSV."""
    print(f"Fetching URLhaus recent domains from {URLHAUS_URL} ...")
    resp = requests.get(URLHAUS_URL, timeout=30)
    resp.raise_for_status()
    return resp.text


def fetch_openphish():
    """Fetch OpenPhish feed as plain text URLs."""
    print(f"Fetching OpenPhish feed from {OPENPHISH_URL} ...")
    try:
        resp = requests.get(OPENPHISH_URL, timeout=30)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"⚠️  OpenPhish fetch failed: {e}")
        return ""


def fetch_sslbl():
    """Fetch SSL Blacklist as CSV."""
    print(f"Fetching SSL Blacklist from {SSLBL_URL} ...")
    resp = requests.get(SSLBL_URL, timeout=30)
    resp.raise_for_status()
    return resp.text


def fetch_phishtank():
    """Fetch Phishtank verified phishing URLs as JSON."""
    print(f"Fetching Phishtank from {PHISHTANK_URL} ...")
    try:
        resp = requests.get(PHISHTANK_URL, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        print(f"⚠️  Phishtank fetch failed: {e}")
        print("    (May require API key for higher rate limits)")
        return []


def fetch_emerging_threats():
    """Fetch Emerging Threats block list as plain text."""
    print(f"Fetching Emerging Threats from {EMERGING_THREATS_URL} ...")
    try:
        resp = requests.get(EMERGING_THREATS_URL, timeout=30)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"⚠️  Emerging Threats fetch failed: {e}")
        return ""


def fetch_energized_porn():
    """Fetch Energized Porn blocklist."""
    print(f"Fetching Energized Porn from {ENERGIZED_PORN_URL} ...")
    try:
        resp = requests.get(ENERGIZED_PORN_URL, timeout=30)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"⚠️  Energized Porn fetch failed: {e}")
        return ""


def fetch_stevenblack_porn():
    """Fetch StevenBlack Porn hosts file."""
    print(f"Fetching StevenBlack Porn from {STEVENBLACK_PORN_URL} ...")
    try:
        resp = requests.get(STEVENBLACK_PORN_URL, timeout=30)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"⚠️  StevenBlack Porn fetch failed: {e}")
        return ""


def fetch_oisd():
    """Fetch OISD Big list (includes adult content)."""
    print(f"Fetching OISD Big list from {OISD_URL} ...")
    try:
        resp = requests.get(OISD_URL, timeout=60)  # Longer timeout for large file
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"⚠️  OISD fetch failed: {e}")
        return ""


def fetch_clefspeare_porn():
    """Fetch Clefspeare13 pornhosts."""
    print(f"Fetching Clefspeare Pornhosts from {CLEFSPEARE_PORN_URL} ...")
    try:
        resp = requests.get(CLEFSPEARE_PORN_URL, timeout=30)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"⚠️  Clefspeare Pornhosts fetch failed: {e}")
        return ""


def fetch_chadmayfield_porn():
    """Fetch Chad Mayfield Porn Top1M list."""
    print(f"Fetching Chad Mayfield Porn Top1M from {CHADMAYFIELD_PORN_URL} ...")
    try:
        resp = requests.get(CHADMAYFIELD_PORN_URL, timeout=30)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"⚠️  Chad Mayfield Porn Top1M fetch failed: {e}")
        return ""


def fetch_ut1_adult():
    """Fetch UT1 Adult category (tar.gz archive)."""
    print(f"Fetching UT1 Adult list from {UT1_ADULT_URL} ...")
    try:
        resp = requests.get(UT1_ADULT_URL, timeout=60)
        resp.raise_for_status()
        return resp.content  # Return bytes for tar.gz
    except requests.RequestException as e:
        print(f"⚠️  UT1 Adult fetch failed: {e}")
        return b""


# -----------------------------
# Domain Extractors
# -----------------------------
def extract_domain_from_url(url):
    """Extract domain from a full URL."""
    # Remove protocol
    url = re.sub(r'^https?://', '', url)
    # Remove path, query, fragment
    domain = url.split('/')[0].split('?')[0].split('#')[0]
    # Remove port
    domain = domain.split(':')[0]
    # Remove www prefix and lowercase
    domain = domain.lstrip('www.').lower()
    return domain


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


def extract_domains_from_urlhaus(csv_text):
    """Extract domains from URLhaus CSV format."""
    domains = set()
    domain_pattern = re.compile(r"^[a-z0-9.-]+\.[a-z]{2,63}$")
    
    reader = csv.DictReader(StringIO(csv_text), delimiter=',')
    for row in reader:
        # Skip comments
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
        
        # CSV format: Listingdate,SHA1,Listingreason
        # Common Name can contain domain
        parts = line.split(',')
        if len(parts) >= 3:
            # Try to extract domain from the listing reason or other fields
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
        
        # Extract URL and convert to domain
        url = entry.get('url', '').strip()
        if not url:
            continue
        
        # Only include verified entries
        if entry.get('verified') != 'yes':
            continue
        
        domain = extract_domain_from_url(url)
        if domain and domain_pattern.fullmatch(domain):
            domains.add(domain)
    
    return domains


def extract_domains_from_emerging_threats(text):
    """Extract domains from Emerging Threats IP block list.
    Note: This is primarily an IP list, but may contain some domains.
    We'll attempt to extract any domain-like entries."""
    domains = set()
    domain_pattern = re.compile(r"^[a-z0-9.-]+\.[a-z]{2,63}$")
    
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        # Skip IP addresses and CIDR notation
        if re.match(r'^\d+\.\d+\.\d+\.\d+', line):
            continue
        
        # Try to extract domain
        parts = line.split()
        for part in parts:
            part = part.lower().strip()
            if domain_pattern.fullmatch(part):
                domains.add(part)
    
    return domains


def extract_domains_from_hosts_file(text):
    """Extract domains from hosts file format (0.0.0.0 domain or 127.0.0.1 domain)."""
    domains = set()
    domain_pattern = re.compile(r"^[a-z0-9.-]+\.[a-z]{2,63}$")
    
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        # Hosts file format: IP_ADDRESS domain
        parts = line.split()
        if len(parts) >= 2:
            # First part is usually IP (0.0.0.0, 127.0.0.1, etc.)
            # Second part is the domain
            domain = parts[1].lower().strip()
            if domain_pattern.fullmatch(domain):
                domains.add(domain)
        elif len(parts) == 1:
            # Sometimes just domain on a line
            domain = parts[0].lower().strip()
            if domain_pattern.fullmatch(domain):
                domains.add(domain)
    
    return domains


def extract_domains_from_plain_list(text):
    """Extract domains from plain text list (one per line)."""
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


def extract_domains_from_adguard_style(text):
    """Extract domains from AdGuard-style rules (||domain^)."""
    domains = set()
    domain_pattern = re.compile(r"^[a-z0-9.-]+\.[a-z]{2,63}$")
    
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith(('!', '#', '[', '@')):
            continue
        
        # Strip AdGuard syntax
        domain = line.lstrip('|').rstrip('^').lstrip('*.').lower()
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
            # UT1 structure: adult/domains file contains the list
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


def fetch_and_merge_adult_content():
    """Fetch all adult content feeds and merge into deduplicated set."""
    all_adult_domains = set()
    stats = {}
    
    # 1. Energized Porn (plain text)
    energized_text = fetch_energized_porn()
    if energized_text:
        energized_domains = extract_domains_from_plain_list(energized_text)
        all_adult_domains.update(energized_domains)
        stats['Energized Porn'] = len(energized_domains)
        print(f"  ✓ Energized Porn: {len(energized_domains)} domains")
    
    # 2. StevenBlack Porn (hosts file)
    stevenblack_text = fetch_stevenblack_porn()
    if stevenblack_text:
        stevenblack_domains = extract_domains_from_hosts_file(stevenblack_text)
        all_adult_domains.update(stevenblack_domains)
        stats['StevenBlack Porn'] = len(stevenblack_domains)
        print(f"  ✓ StevenBlack Porn: {len(stevenblack_domains)} domains")
    
    # 3. OISD Big (AdGuard style - this is a large list, may include non-adult)
    # Note: OISD is a general blocklist, we're including it but marking it separately
    oisd_text = fetch_oisd()
    if oisd_text:
        oisd_domains = extract_domains_from_adguard_style(oisd_text)
        # OISD is huge and general-purpose, so we'll note this
        stats['OISD Big'] = len(oisd_domains)
        print(f"  ℹ️  OISD Big: {len(oisd_domains)} domains (general blocklist, includes adult)")
        # Only add OISD domains if they're not already covered
        # This prevents diluting the adult-specific list with general blocks
        # Comment out the next line if you want to include all OISD
        # all_adult_domains.update(oisd_domains)
    
    # 4. Clefspeare Pornhosts (hosts file)
    clefspeare_text = fetch_clefspeare_porn()
    if clefspeare_text:
        clefspeare_domains = extract_domains_from_hosts_file(clefspeare_text)
        all_adult_domains.update(clefspeare_domains)
        stats['Clefspeare Pornhosts'] = len(clefspeare_domains)
        print(f"  ✓ Clefspeare Pornhosts: {len(clefspeare_domains)} domains")
    
    # 5. Chad Mayfield Porn Top1M (plain text)
    chadmayfield_text = fetch_chadmayfield_porn()
    if chadmayfield_text:
        chadmayfield_domains = extract_domains_from_plain_list(chadmayfield_text)
        all_adult_domains.update(chadmayfield_domains)
        stats['Chad Mayfield Top1M'] = len(chadmayfield_domains)
        print(f"  ✓ Chad Mayfield Top1M: {len(chadmayfield_domains)} domains")
    
    # 6. UT1 Adult (tar.gz)
    ut1_content = fetch_ut1_adult()
    if ut1_content:
        ut1_domains = extract_domains_from_ut1_tarball(ut1_content)
        all_adult_domains.update(ut1_domains)
        stats['UT1 Adult'] = len(ut1_domains)
        print(f"  ✓ UT1 Adult: {len(ut1_domains)} domains")
    
    return all_adult_domains, stats


# -----------------------------
# Helpers
# -----------------------------
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
    """Save services.json with blocked_services list and size check."""
    data = {"blocked_services": services}
    content = json.dumps(data, indent=2, ensure_ascii=False)
    
    try:
        size_mb = check_file_size(path, content)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Wrote services.json ({size_mb:.2f}MB) with {len(services)} entries.")
    except ValueError as e:
        print(f"❌ {e}")
        print("⚠️  File NOT saved - would exceed GitHub limits")
        raise


def build_threatfox_services(data, domain_set, min_confidence=50):
    """
    Build ThreatFox services grouped by malware family.
    data: dict from ThreatFox API
    domain_set: set to update running unique domains
    min_confidence: only include IOCs with confidence >= threshold
    """
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

    # --- URLhaus ---
    urlhaus_csv = fetch_urlhaus_recent()
    urlhaus_domains = extract_domains_from_urlhaus(urlhaus_csv)
    domains.update(urlhaus_domains)
    urlhaus_service = {
        "id": "urlhaus_malware",
        "name": "URLhaus Malware Distribution",
        "rules": [f"||{d}^" for d in sorted(urlhaus_domains)],
        "group": "malware",
        "source": "urlhaus",
    }
    # Replace or add URLhaus entry
    for i, svc in enumerate(services):
        if svc.get("id", "").lower() == "urlhaus_malware":
            services[i] = urlhaus_service
            break
    else:
        services.append(urlhaus_service)

    # --- OpenPhish ---
    openphish_text = fetch_openphish()
    if openphish_text:
        openphish_domains = extract_domains_from_openphish(openphish_text)
        domains.update(openphish_domains)
        openphish_service = {
            "id": "openphish",
            "name": "OpenPhish Verified Phishing",
            "rules": [f"||{d}^" for d in sorted(openphish_domains)],
            "group": "phishing",
            "source": "openphish",
        }
        # Replace or add OpenPhish entry
        for i, svc in enumerate(services):
            if svc.get("id", "").lower() == "openphish":
                services[i] = openphish_service
                break
        else:
            services.append(openphish_service)
        print(f"  ✓ OpenPhish: {len(openphish_domains)} domains")
    else:
        print("  ⚠️  OpenPhish: skipped (fetch failed)")

    # --- SSL Blacklist ---
    sslbl_csv = fetch_sslbl()
    sslbl_domains = extract_domains_from_sslbl(sslbl_csv)
    domains.update(sslbl_domains)
    sslbl_service = {
        "id": "sslbl_malicious",
        "name": "SSL Blacklist - Malicious Certificates",
        "rules": [f"||{d}^" for d in sorted(sslbl_domains)],
        "group": "malware",
        "source": "sslbl",
    }
    # Replace or add SSL Blacklist entry
    for i, svc in enumerate(services):
        if svc.get("id", "").lower() == "sslbl_malicious":
            services[i] = sslbl_service
            break
    else:
        services.append(sslbl_service)

    # --- Phishtank ---
    phishtank_json = fetch_phishtank()
    if phishtank_json:
        phishtank_domains = extract_domains_from_phishtank(phishtank_json)
        domains.update(phishtank_domains)
        phishtank_service = {
            "id": "phishtank",
            "name": "Phishtank Verified Phishing",
            "rules": [f"||{d}^" for d in sorted(phishtank_domains)],
            "group": "phishing",
            "source": "phishtank",
        }
        # Replace or add Phishtank entry
        for i, svc in enumerate(services):
            if svc.get("id", "").lower() == "phishtank":
                services[i] = phishtank_service
                break
        else:
            services.append(phishtank_service)
        print(f"  ✓ Phishtank: {len(phishtank_domains)} verified phishing domains")
    else:
        print("  ⚠️  Phishtank: skipped (fetch failed or rate limited)")

    # --- Emerging Threats ---
    et_text = fetch_emerging_threats()
    if et_text:
        et_domains = extract_domains_from_emerging_threats(et_text)
        if et_domains:
            domains.update(et_domains)
            et_service = {
                "id": "emerging_threats",
                "name": "Emerging Threats Block List",
                "rules": [f"||{d}^" for d in sorted(et_domains)],
                "group": "malware",
                "source": "emerging_threats",
            }
            # Replace or add Emerging Threats entry
            for i, svc in enumerate(services):
                if svc.get("id", "").lower() == "emerging_threats":
                    services[i] = et_service
                    break
            else:
                services.append(et_service)
            print(f"  ✓ Emerging Threats: {len(et_domains)} domains")
        else:
            print("  ℹ️  Emerging Threats: no domains found (primarily IP-based list)")
    else:
        print("  ⚠️  Emerging Threats: skipped (fetch failed)")

    # --- Adult Content (All Feeds Combined) ---
    print("\n🔞 Fetching Adult Content Feeds...")
    adult_domains, adult_stats = fetch_and_merge_adult_content()
    
    if adult_domains:
        domains.update(adult_domains)
        adult_service = {
            "id": "adult_content",
            "name": "Adult Content Blocklist (Multi-Source)",
            "rules": [f"||{d}^" for d in sorted(adult_domains)],
            "group": "adult",
            "source": "multi_adult",
            "sources_included": list(adult_stats.keys())
        }
        # Replace or add Adult Content entry
        for i, svc in enumerate(services):
            if svc.get("id", "").lower() == "adult_content":
                services[i] = adult_service
                break
        else:
            services.append(adult_service)
        print(f"\n  ✅ Combined Adult Content: {len(adult_domains)} unique domains")
        print(f"     From {len(adult_stats)} sources (deduplicated)")
    else:
        print("  ⚠️  No adult content domains fetched")

    # --- Save and summary ---
    save_local_services(path, services)

    print("\n" + "="*60)
    print("✅ Update complete!")
    print("="*60)
    print(f"Total services: {len(services)}")
    print(f"Total unique domains across all feeds: {len(domains)}")
    print("\nBreakdown by feed:")
    print(f"  • AdGuard: {len(adguard_services)} services")
    print(f"  • Phishing Army: {len(phishing_domains)} domains")
    print(f"  • ThreatFox: {len(threatfox_services)} malware families")
    print(f"  • URLhaus: {len(urlhaus_domains)} domains")
    if openphish_text:
        print(f"  • OpenPhish: {len(openphish_domains)} domains")
    print(f"  • SSL Blacklist: {len(sslbl_domains)} domains")
    if phishtank_json:
        print(f"  • Phishtank: {len(phishtank_domains)} domains")
    if et_text and et_domains:
        print(f"  • Emerging Threats: {len(et_domains)} domains")
    if adult_domains:
        print(f"  • Adult Content (combined): {len(adult_domains)} domains")
        if adult_stats:
            print(f"    Sources: {', '.join(adult_stats.keys())}")
    print("="*60)


if __name__ == "__main__":
    main()
