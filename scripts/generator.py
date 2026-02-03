#!/usr/bin/env python3
"""
Threat Intelligence Blocklist Generator

Generates two-tier blocklist structure:
1. Aggregated categories (recommended for most users)
   - services/categories/phishing.txt - All phishing sources combined
   - services/categories/malware.txt - All malware sources combined
   - services/categories/adult.txt - All adult content sources combined
   - services/categories/<group>.txt - Other categories

2. Individual sources (for advanced users)
   - services/lists/phishing/phishing_army.txt
   - services/lists/phishing/openphish.txt
   - services/lists/malware/threatfox.txt
   - services/lists/<group>/<source>.txt

3. Auto-generated README with stats and raw links
   - services/README.md

All lists use Pi-hole/AdGuard compatible format (root domains only, one per line).
"""

import requests
import re
import csv
import json
import tarfile
import logging
from io import StringIO, BytesIO
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from typing import Set, Dict, List, Optional
from urllib.parse import urlparse

# -----------------------------
# Configuration
# -----------------------------
REQUEST_TIMEOUT = 60
MAX_FILE_SIZE_MB = 90  # Safety buffer under GitHub 100MB limit
MAX_RETRIES = 3
RETRY_DELAY = 2

BASE_DIR = Path("services")
LISTS_DIR = BASE_DIR / "lists"
CATEGORIES_DIR = BASE_DIR / "categories"
README_PATH = BASE_DIR / "README.md"

REPO = "sparksbenjamin/DNS_Blocking"
BRANCH = "main"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# -----------------------------
# Feed URLs
# -----------------------------
ADGUARD_URL = "https://adguardteam.github.io/HostlistsRegistry/assets/services.json"
PHISHING_ARMY_URL = "https://raw.githubusercontent.com/Phishing-Database/Phishing.Database/refs/heads/master/phishing-domains-ACTIVE.adblock"
THREATFOX_URL = "https://threatfox.abuse.ch/export/json/domains/recent/"
URLHAUS_URL = "https://urlhaus.abuse.ch/downloads/csv_recent/"
OPENPHISH_URL = "https://openphish.com/feed.txt"
SSLBL_URL = "https://sslbl.abuse.ch/blacklist/sslblacklist.csv"
PHISHTANK_URL = "http://data.phishtank.com/data/online-valid.json"
EMERGING_THREATS_URL = "https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt"

# Adult lists (selective to avoid insane sizes)
STEVENBLACK_PORN_URL = "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn/hosts"
CHADMAYFIELD_PORN_URL = "https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_top1m.list"
UT1_ADULT_URL = "https://dsi.ut-capitole.fr/blacklists/download/adult.tar.gz"

# -----------------------------
# Utilities
# -----------------------------
# Enhanced domain regex to be more strict
DOMAIN_REGEX = re.compile(
    r"^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$",
    re.IGNORECASE
)


def is_valid_domain(domain: str) -> bool:
    """
    Validate domain name more thoroughly.
    
    Args:
        domain: Domain name to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not domain or len(domain) > 253:
        return False
    
    # Remove trailing dot if present
    domain = domain.rstrip('.')
    
    # Check overall pattern
    if not DOMAIN_REGEX.match(domain):
        return False
    
    # Additional checks
    parts = domain.split('.')
    if len(parts) < 2:
        return False
    
    # Check each label
    for part in parts:
        if not part or len(part) > 63:
            return False
        if part.startswith('-') or part.endswith('-'):
            return False
    
    return True


def extract_domain_from_url(url: str) -> str:
    """
    Extract domain from URL using proper parsing.
    
    Args:
        url: URL to parse
        
    Returns:
        Extracted domain or empty string
    """
    try:
        # Add scheme if missing for proper parsing
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        parsed = urlparse(url)
        domain = parsed.netloc or parsed.path.split('/')[0]
        
        # Remove port if present
        domain = domain.split(':')[0]
        
        # Remove www prefix
        domain = domain.lower()
        if domain.startswith('www.'):
            domain = domain[4:]
        
        return domain
    except Exception as e:
        logger.debug(f"Failed to parse URL '{url}': {e}")
        return ""


def extract_domains_from_adblock(text: str) -> Set[str]:
    """Extract domains from AdBlock format."""
    domains = set()
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith(("!", "#", "[", "@")):
            continue
        
        # Handle ||domain^ format
        if line.startswith("||"):
            domain = line[2:].split("^")[0].strip()
        else:
            domain = line.split("^")[0].strip()
        
        # Clean up
        domain = domain.lstrip("*.").lower()
        
        if is_valid_domain(domain):
            domains.add(domain)
    
    return domains


def extract_domains_from_plain_list(text: str) -> Set[str]:
    """Extract domains from plain text list."""
    domains = set()
    for line in text.splitlines():
        line = line.strip().lower()
        if not line or line.startswith("#"):
            continue
        
        if is_valid_domain(line):
            domains.add(line)
    
    return domains


def extract_domains_from_hosts_file(text: str) -> Set[str]:
    """Extract domains from hosts file format."""
    domains = set()
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        
        parts = line.split()
        if len(parts) >= 2:
            # Standard hosts format: IP domain
            domain = parts[1].lower()
        elif len(parts) == 1:
            # Just domain
            domain = parts[0].lower()
        else:
            continue
        
        if is_valid_domain(domain):
            domains.add(domain)
    
    return domains


def extract_domains_from_urlhaus(csv_text: str) -> Set[str]:
    """Extract domains from URLhaus CSV format."""
    domains = set()
    try:
        reader = csv.DictReader(StringIO(csv_text))
        for row in reader:
            url = row.get("url", "").strip()
            if not url:
                continue
            
            domain = extract_domain_from_url(url)
            if is_valid_domain(domain):
                domains.add(domain)
    except Exception as e:
        logger.error(f"Failed to parse URLhaus CSV: {e}")
    
    return domains


def extract_domains_from_openphish(text: str) -> Set[str]:
    """Extract domains from OpenPhish feed."""
    domains = set()
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        
        domain = extract_domain_from_url(line)
        if is_valid_domain(domain):
            domains.add(domain)
    
    return domains


def extract_domains_from_sslbl(csv_text: str) -> Set[str]:
    """Extract domains from SSL Blacklist CSV."""
    domains = set()
    for line in csv_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        
        # CSV format, check all fields for domains
        parts = line.split(",")
        for part in parts:
            part = part.strip().strip('"').lower()
            if is_valid_domain(part):
                domains.add(part)
    
    return domains


def extract_domains_from_phishtank(json_data: List[Dict]) -> Set[str]:
    """Extract domains from PhishTank JSON."""
    domains = set()
    if not isinstance(json_data, list):
        logger.warning("PhishTank data is not a list")
        return domains
    
    for entry in json_data:
        if not isinstance(entry, dict):
            continue
        
        # Only include verified entries
        if entry.get("verified") != "yes":
            continue
        
        url = entry.get("url", "").strip()
        if not url:
            continue
        
        domain = extract_domain_from_url(url)
        if is_valid_domain(domain):
            domains.add(domain)
    
    return domains


def extract_domains_from_ut1_tarball(tar_content: bytes) -> Set[str]:
    """Extract domains from UT1 tarball."""
    domains = set()
    try:
        with tarfile.open(fileobj=BytesIO(tar_content), mode="r:gz") as tar:
            for member in tar.getmembers():
                if member.isfile() and "domains" in member.name:
                    f = tar.extractfile(member)
                    if not f:
                        continue
                    
                    content = f.read().decode("utf-8", errors="ignore")
                    for line in content.splitlines():
                        line = line.strip().lower()
                        if not line or line.startswith("#"):
                            continue
                        
                        if is_valid_domain(line):
                            domains.add(line)
    except Exception as e:
        logger.error(f"Failed to extract UT1 tarball: {e}")
    
    return domains


def ensure_dir(path: Path) -> None:
    """Ensure directory exists."""
    path.mkdir(parents=True, exist_ok=True)


def get_root_domain(domain: str) -> str:
    """
    Extract root domain from a domain (remove subdomains).
    
    Args:
        domain: Full domain name
        
    Returns:
        Root domain (e.g., example.com from sub.example.com)
    """
    parts = domain.split('.')
    if len(parts) >= 2:
        # Return last two parts as root domain
        return '.'.join(parts[-2:])
    return domain


def write_domain_file(path: Path, domains: Set[str], header: Optional[str] = None) -> tuple:
    """
    Write domains to file with header in Pi-hole/AdGuard compatible format.
    
    Args:
        path: Output file path
        domains: Set of domains to write
        header: Optional header text
        
    Returns:
        Tuple of (domain_count, size_in_mb)
        
    Raises:
        ValueError: If file size exceeds limit
    """
    ensure_dir(path.parent)
    
    # Remove subdomains - only keep root domains
    root_domains = set()
    for domain in domains:
        root = get_root_domain(domain)
        root_domains.add(root)
    
    sorted_domains = sorted(root_domains)
    
    content = ""
    if header:
        content += header.rstrip() + "\n\n"
    
    # Pi-hole/AdGuard compatible format - one domain per line
    content += "\n".join(sorted_domains) + "\n"
    
    size_mb = len(content.encode("utf-8")) / (1024 * 1024)
    if size_mb > MAX_FILE_SIZE_MB:
        raise ValueError(f"{path} exceeds {MAX_FILE_SIZE_MB}MB ({size_mb:.2f}MB)")
    
    path.write_text(content, encoding="utf-8")
    return len(sorted_domains), size_mb


# -----------------------------
# Fetchers with retry logic
# -----------------------------
def fetch_with_retry(url: str, is_json: bool = False, timeout: int = REQUEST_TIMEOUT) -> Optional[any]:
    """
    Fetch URL with retry logic.
    
    Args:
        url: URL to fetch
        is_json: Whether to parse as JSON
        timeout: Request timeout in seconds
        
    Returns:
        Response text/JSON or None on failure
    """
    import time
    
    for attempt in range(MAX_RETRIES):
        try:
            logger.debug(f"Fetching {url} (attempt {attempt + 1}/{MAX_RETRIES})")
            resp = requests.get(url, timeout=timeout)
            resp.raise_for_status()
            
            if is_json:
                return resp.json()
            return resp.text
            
        except requests.exceptions.RequestException as e:
            logger.warning(f"Attempt {attempt + 1} failed for {url}: {e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY)
            else:
                logger.error(f"Failed to fetch {url} after {MAX_RETRIES} attempts")
                return None
    
    return None


def fetch_text(url: str) -> Optional[str]:
    """Fetch text content from URL."""
    return fetch_with_retry(url, is_json=False)


def fetch_json(url: str) -> Optional[any]:
    """Fetch JSON content from URL."""
    return fetch_with_retry(url, is_json=True)


def fetch_binary(url: str, timeout: int = 120) -> Optional[bytes]:
    """Fetch binary content from URL."""
    import time
    
    for attempt in range(MAX_RETRIES):
        try:
            logger.debug(f"Fetching binary {url} (attempt {attempt + 1}/{MAX_RETRIES})")
            resp = requests.get(url, timeout=timeout)
            resp.raise_for_status()
            return resp.content
            
        except requests.exceptions.RequestException as e:
            logger.warning(f"Attempt {attempt + 1} failed for {url}: {e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY)
            else:
                logger.error(f"Failed to fetch {url} after {MAX_RETRIES} attempts")
                return None
    
    return None


# -----------------------------
# Main Logic
# -----------------------------
def main():
    """Main execution function."""
    print("=" * 70)
    print("THREAT INTELLIGENCE BLOCKLIST GENERATOR")
    print("=" * 70)

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    ensure_dir(LISTS_DIR)
    ensure_dir(CATEGORIES_DIR)

    # Clear previous outputs
    logger.info("Clearing previous outputs...")
    for p in LISTS_DIR.rglob("*.txt"):
        p.unlink()
    for p in CATEGORIES_DIR.glob("*.txt"):
        p.unlink()

    # Dictionary to collect domains by target service/platform
    # Key: service name (e.g., "facebook", "tiktok", "emotet")
    # Value: {"group": category, "name": display_name, "domains": set()}
    services_by_target = defaultdict(lambda: {"group": "", "name": "", "domains": set()})
    
    # -----------------------------
    # ADGUARD SERVICES (social, gaming, streaming, etc.)
    # -----------------------------
    logger.info("Fetching AdGuard services...")
    adguard_data = fetch_json(ADGUARD_URL)
    
    if adguard_data is None:
        logger.error("Failed to fetch AdGuard data")
    else:
        if isinstance(adguard_data, dict) and "blocked_services" in adguard_data:
            adguard_services = adguard_data["blocked_services"]
        elif isinstance(adguard_data, list):
            adguard_services = adguard_data
        else:
            logger.error("Unexpected AdGuard JSON structure")
            adguard_services = []

        for svc in adguard_services:
            rules = svc.get("rules", [])
            if not rules:
                continue
            
            group = svc.get("group", "misc").lower()
            service_id = svc.get("id", "unknown").lower()
            service_name = svc.get("name", service_id)

            domains = set()
            for rule in rules:
                d = rule.strip().lstrip("|").rstrip("^").lstrip("*.").lower()
                if is_valid_domain(d):
                    domains.add(d)

            if not domains:
                continue

            # Store by target service name
            services_by_target[service_id]["group"] = group
            services_by_target[service_id]["name"] = service_name
            services_by_target[service_id]["domains"].update(domains)
        
        logger.info(f"Processed {len(services_by_target)} AdGuard services")

    # -----------------------------
    # PHISHING FEEDS (per-source + aggregated)
    # -----------------------------
    logger.info("Fetching phishing feeds...")
    
    # Track all phishing domains for category aggregation
    all_phishing_domains = set()

    # Phishing Army
    phishing_army_text = fetch_text(PHISHING_ARMY_URL)
    if phishing_army_text:
        pa_domains = extract_domains_from_adblock(phishing_army_text)
        all_phishing_domains.update(pa_domains)
        services_by_target["phishing_army"]["group"] = "phishing"
        services_by_target["phishing_army"]["name"] = "Phishing Army"
        services_by_target["phishing_army"]["domains"].update(pa_domains)
        logger.info(f"Phishing Army: {len(pa_domains)} domains")
    else:
        logger.error("Failed to fetch Phishing Army data")

    # OpenPhish
    openphish_text = fetch_text(OPENPHISH_URL)
    if openphish_text:
        op_domains = extract_domains_from_openphish(openphish_text)
        all_phishing_domains.update(op_domains)
        services_by_target["openphish"]["group"] = "phishing"
        services_by_target["openphish"]["name"] = "OpenPhish"
        services_by_target["openphish"]["domains"].update(op_domains)
        logger.info(f"OpenPhish: {len(op_domains)} domains")
    else:
        logger.error("Failed to fetch OpenPhish data")

    # PhishTank
    phishtank_json = fetch_json(PHISHTANK_URL)
    if phishtank_json:
        pt_domains = extract_domains_from_phishtank(phishtank_json)
        all_phishing_domains.update(pt_domains)
        services_by_target["phishtank"]["group"] = "phishing"
        services_by_target["phishtank"]["name"] = "PhishTank"
        services_by_target["phishtank"]["domains"].update(pt_domains)
        logger.info(f"PhishTank: {len(pt_domains)} domains")
    else:
        logger.error("Failed to fetch PhishTank data")

    # -----------------------------
    # MALWARE FEEDS (per-source + aggregated)
    # -----------------------------
    logger.info("Fetching malware feeds...")

    # ThreatFox - keep as single aggregated source
    threatfox_data = fetch_json(THREATFOX_URL)
    if threatfox_data:
        all_threatfox_domains = set()
        
        for entries in threatfox_data.values():
            if not isinstance(entries, list):
                continue
                
            for entry in entries:
                if not isinstance(entry, dict):
                    continue
                    
                if entry.get("ioc_type") != "domain":
                    continue
                
                if entry.get("confidence_level", 0) < 50:
                    continue
                
                d = entry.get("ioc_value", "").lower().strip()
                if not is_valid_domain(d):
                    continue
                
                all_threatfox_domains.add(d)
        
        services_by_target["threatfox"]["group"] = "malware"
        services_by_target["threatfox"]["name"] = "ThreatFox"
        services_by_target["threatfox"]["domains"].update(all_threatfox_domains)
        
        logger.info(f"ThreatFox: {len(all_threatfox_domains)} domains")
    else:
        logger.error("Failed to fetch ThreatFox data")

    # URLhaus - malware distribution
    urlhaus_csv = fetch_text(URLHAUS_URL)
    if urlhaus_csv:
        uh_domains = extract_domains_from_urlhaus(urlhaus_csv)
        services_by_target["urlhaus"]["group"] = "malware"
        services_by_target["urlhaus"]["name"] = "URLhaus"
        services_by_target["urlhaus"]["domains"].update(uh_domains)
        logger.info(f"URLhaus: {len(uh_domains)} domains")
    else:
        logger.error("Failed to fetch URLhaus data")

    # SSL Blacklist - malicious SSL certificates
    sslbl_csv = fetch_text(SSLBL_URL)
    if sslbl_csv:
        sb_domains = extract_domains_from_sslbl(sslbl_csv)
        services_by_target["sslbl"]["group"] = "malware"
        services_by_target["sslbl"]["name"] = "SSL Blacklist"
        services_by_target["sslbl"]["domains"].update(sb_domains)
        logger.info(f"SSLBL: {len(sb_domains)} domains")
    else:
        logger.error("Failed to fetch SSLBL data")

    # -----------------------------
    # ADULT CONTENT (per-source + aggregated)
    # -----------------------------
    logger.info("Fetching adult content feeds (selective)...")

    # StevenBlack
    sb_text = fetch_text(STEVENBLACK_PORN_URL)
    if sb_text:
        sb_adult = extract_domains_from_hosts_file(sb_text)
        services_by_target["stevenblack_porn"]["group"] = "adult"
        services_by_target["stevenblack_porn"]["name"] = "StevenBlack Porn"
        services_by_target["stevenblack_porn"]["domains"].update(sb_adult)
        logger.info(f"StevenBlack: {len(sb_adult)} domains")
    else:
        logger.error("Failed to fetch StevenBlack data")

    # Chad Mayfield
    cm_text = fetch_text(CHADMAYFIELD_PORN_URL)
    if cm_text:
        cm_adult = extract_domains_from_plain_list(cm_text)
        services_by_target["chadmayfield_porn"]["group"] = "adult"
        services_by_target["chadmayfield_porn"]["name"] = "Chad Mayfield Porn"
        services_by_target["chadmayfield_porn"]["domains"].update(cm_adult)
        logger.info(f"Chad Mayfield: {len(cm_adult)} domains")
    else:
        logger.error("Failed to fetch Chad Mayfield data")

    # UT1 optional (commented by default due to massive size)
    # logger.info("Fetching UT1 Adult tarball (this may take a while)...")
    # ut1_content = fetch_binary(UT1_ADULT_URL, timeout=120)
    # if ut1_content:
    #     ut1_domains = extract_domains_from_ut1_tarball(ut1_content)
    #     services_by_target["ut1_adult"]["group"] = "adult"
    #     services_by_target["ut1_adult"]["name"] = "UT1 Adult"
    #     services_by_target["ut1_adult"]["domains"].update(ut1_domains)
    #     logger.info(f"UT1: {len(ut1_domains)} domains")

    # -----------------------------
    # WRITE PER-SERVICE FILES
    # -----------------------------
    logger.info("Writing per-service/target files...")
    service_stats = []
    category_domains = defaultdict(set)

    for service_id, svc_data in services_by_target.items():
        if not svc_data["domains"]:
            continue
            
        group = svc_data["group"]
        name = svc_data["name"]
        domains = svc_data["domains"]

        out_path = LISTS_DIR / group / f"{service_id}.txt"
        header = (
            f"# {name}\n"
            f"# Category: {group}\n"
            f"# Generated: {timestamp}\n"
            f"# Format: Pi-hole/AdGuard compatible - one domain per line\n"
            f"# Original domains (before deduplication): {len(domains)}"
        )

        try:
            count, size_mb = write_domain_file(out_path, domains, header)
            logger.info(f"✓ {group}/{service_id}.txt — {count} root domains ({size_mb:.2f}MB)")
        except ValueError as e:
            logger.warning(f"Skipped {out_path}: {e}")
            continue
        except Exception as e:
            logger.error(f"Error writing {out_path}: {e}")
            continue

        service_stats.append({
            "group": group,
            "service": service_id,
            "name": name,
            "domains": count,
            "path": out_path,
        })

        category_domains[group].update(domains)

    # -----------------------------
    # WRITE PER-CATEGORY FILES
    # -----------------------------
    logger.info("Writing category files...")
    category_stats = []

    for group, domains in category_domains.items():
        out_path = CATEGORIES_DIR / f"{group}.txt"
        header = (
            f"# {group.capitalize()} Blocklist\n"
            f"# Generated: {timestamp}\n"
            f"# Format: Pi-hole/AdGuard compatible - one domain per line\n"
            f"# Original domains (before deduplication): {len(domains)}"
        )

        try:
            count, size_mb = write_domain_file(out_path, domains, header)
            logger.info(f"✓ {group}.txt — {count} root domains ({size_mb:.2f}MB)")
        except ValueError as e:
            logger.warning(f"Skipped {out_path}: {e}")
            continue
        except Exception as e:
            logger.error(f"Error writing {out_path}: {e}")
            continue

        category_stats.append({
            "group": group,
            "domains": count,
            "path": out_path,
        })

    # -----------------------------
    # GENERATE README
    # -----------------------------
    logger.info("Generating README...")
    lines = []
    lines.append("# Threat Intelligence & Content Blocklists\n")
    lines.append(f"**Generated:** {timestamp}\n")
    lines.append("This repository provides curated blocklists for home network protection.\n")
    lines.append("All lists are **Pi-hole and AdGuard Home compatible** - one root domain per line.\n")
    
    # Add quick start section
    lines.append("## 🚀 Quick Start (Recommended)\n")
    lines.append("**For most users**: Use the aggregated category lists below. Each combines multiple trusted sources.\n")
    
    # Category section with better descriptions
    lines.append("## 📋 Aggregated Categories\n")
    lines.append("One-click blocklists combining multiple sources for comprehensive protection.\n")
    lines.append("| Category | Root Domains | Sources | File | Raw URL |")
    lines.append("|----------|--------------|---------|------|---------|")

    # Count sources per category
    category_source_counts = defaultdict(int)
    for svc_data in services_by_target.values():
        if svc_data["group"]:
            category_source_counts[svc_data["group"]] += 1

    for cat in sorted(category_stats, key=lambda x: x["group"]):
        group = cat["group"]
        count = cat["domains"]
        source_count = category_source_counts[group]
        file_path = f"categories/{group}.txt"
        raw_url = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/services/{file_path}"
        
        # Add emoji and description per category
        if group == "phishing":
            emoji = "🎣"
            desc = "Phishing & Scam Sites"
        elif group == "malware":
            emoji = "🦠"
            desc = "Malware & Threats"
        elif group == "adult":
            emoji = "🔞"
            desc = "Adult Content"
        elif group == "social":
            emoji = "📱"
            desc = "Social Media"
        elif group == "gaming":
            emoji = "🎮"
            desc = "Gaming Platforms"
        else:
            emoji = "📁"
            desc = group.capitalize()
        
        lines.append(f"| {emoji} {desc} | {count:,} | {source_count} | [{group}.txt]({file_path}) | [Raw]({raw_url}) |")

    lines.append("")
    
    # Advanced section for individual sources
    lines.append("## 🔧 Individual Sources (Advanced)\n")
    lines.append("For granular control, each source is available separately. Use these if you:\n")
    lines.append("- Want to exclude a specific source with false positives")
    lines.append("- Need source attribution for security analysis")
    lines.append("- Prefer to test feeds individually before deployment\n")
    
    # Group services by category for better organization
    services_by_category = defaultdict(list)
    for svc in sorted(service_stats, key=lambda x: (x["group"], x["name"])):
        services_by_category[svc["group"]].append(svc)
    
    for group in sorted(services_by_category.keys()):
        lines.append(f"### {group.capitalize()}\n")
        lines.append("| Source | Root Domains | File | Raw URL |")
        lines.append("|--------|--------------|------|---------|")
        
        for svc in services_by_category[group]:
            service = svc["service"]
            name = svc["name"]
            count = svc["domains"]
            rel_path = f"lists/{group}/{service}.txt"
            raw_url = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/services/{rel_path}"
            lines.append(f"| {name} | {count:,} | [{service}.txt]({rel_path}) | [Raw]({raw_url}) |")
        
        lines.append("")

    # Add usage instructions
    lines.append("## 📖 Usage Guide\n")
    lines.append("### Pi-hole")
    lines.append("1. Navigate to **Settings** → **Blocklists**")
    lines.append("2. Paste the **Raw URL** of your desired list")
    lines.append("3. Click **Save and Update**")
    lines.append("4. Wait for gravity to update\n")
    
    lines.append("### AdGuard Home")
    lines.append("1. Go to **Filters** → **DNS blocklists**")
    lines.append("2. Click **Add blocklist** → **Add a custom list**")
    lines.append("3. Paste the **Raw URL** and provide a name")
    lines.append("4. Click **Save**\n")
    
    # Format details
    lines.append("## 📝 Format Details\n")
    lines.append("All lists follow these standards:\n")
    lines.append("- **Root domains only** - blocking `example.com` automatically blocks all `*.example.com`")
    lines.append("- **One domain per line** - clean, simple format")
    lines.append("- **No subdomains** - more efficient and smaller file sizes")
    lines.append("- **No IP addresses or wildcards** - pure domain lists")
    lines.append("- **Commented headers** - each file includes metadata and generation timestamp\n")
    
    # Add sources section
    lines.append("## 🔍 Data Sources\n")
    lines.append("This repository aggregates threat intelligence from trusted sources:\n")
    lines.append("### Security Feeds")
    lines.append("- **[Phishing Army](https://phishing.army/)** - Community-driven phishing database")
    lines.append("- **[OpenPhish](https://openphish.com/)** - Automated phishing detection")
    lines.append("- **[PhishTank](https://phishtank.org/)** - Verified phishing URLs")
    lines.append("- **[ThreatFox](https://threatfox.abuse.ch/)** - Malware IOCs from abuse.ch")
    lines.append("- **[URLhaus](https://urlhaus.abuse.ch/)** - Malware distribution sites")
    lines.append("- **[SSL Blacklist](https://sslbl.abuse.ch/)** - Malicious SSL certificates\n")
    
    lines.append("### Content Filters")
    lines.append("- **[AdGuard](https://adguard.com/)** - Service blocklists (social media, gaming, streaming)")
    lines.append("- **[StevenBlack](https://github.com/StevenBlack/hosts)** - Curated hosts files")
    lines.append("- **[Chad Mayfield](https://github.com/chadmayfield/my-pihole-blocklists)** - Pi-hole blocklists\n")
    
    lines.append("## ⚡ Updates\n")
    lines.append("Lists are automatically updated on a regular schedule to ensure fresh threat intelligence.\n")
    lines.append("Check the timestamp at the top of this README or in individual list files.\n")
    
    lines.append("## ⚠️ Important Notes\n")
    lines.append("- **Test before deploying** - Some lists may block legitimate services")
    lines.append("- **Start with categories** - Easier to manage and troubleshoot")
    lines.append("- **Whitelist as needed** - Add exceptions for false positives")
    lines.append("- **Monitor your logs** - Understand what's being blocked\n")
    
    lines.append("## 📜 License\n")
    lines.append("This repository is provided as-is for informational and protective purposes.\n")
    lines.append("Individual source feeds may have their own licenses and terms of use.\n")
    
    lines.append("## 🤝 Contributing\n")
    lines.append("Found a false positive? Have a suggestion for a new source?\n")
    lines.append("Please open an issue or submit a pull request!\n")

    README_PATH.write_text("\n".join(lines), encoding="utf-8")
    logger.info(f"README written to {README_PATH}")

    print("\n" + "=" * 70)
    print("✅ UPDATE COMPLETE!")
    print("=" * 70)
    print(f"Individual sources: {len(service_stats)}")
    print(f"Aggregated categories: {len(category_stats)}")
    total_domains = sum(cat["domains"] for cat in category_stats)
    print(f"Total unique root domains: {total_domains:,}")
    print("=" * 70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("\nOperation cancelled by user")
    except Exception as e:
        logger.exception(f"Fatal error: {e}")
        raise
