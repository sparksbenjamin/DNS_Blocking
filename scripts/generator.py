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
import gzip
import json
import subprocess
import tarfile
import logging
from functools import lru_cache
from io import StringIO, BytesIO
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from typing import Set, Dict, List, Optional
from urllib.parse import quote, urlparse

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
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
CUSTOM_DOMAINS_FILES = [
    SCRIPT_DIR / "custom_domains.json",
    REPO_ROOT / "custom_domains.json",
]
SOURCE_POLICIES_FILE = SCRIPT_DIR / "source_policies.json"

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
PHISHTANK_URL = "https://data.phishtank.com/data/online-valid.json"
PHISHTANK_GZ_URL = "https://data.phishtank.com/data/online-valid.json.gz"
PHISHTANK_USER_AGENT = "phishtank/sparksbenjamin-dns-blocking"
EMERGING_THREATS_URL = "https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt"
UKLANS_CACHE_DOMAINS_URL = "https://raw.githubusercontent.com/uklans/cache-domains/master/cache_domains.json"
UKLANS_RAW_BASE_URL = "https://raw.githubusercontent.com/uklans/cache-domains/master/"
PUBLIC_SUFFIX_LIST_URL = "https://publicsuffix.org/list/public_suffix_list.dat"
BLOCKLISTPROJECT_SCAM_URL = "https://raw.githubusercontent.com/blocklistproject/Lists/master/scam.txt"
BLOCKLISTPROJECT_FRAUD_URL = "https://raw.githubusercontent.com/blocklistproject/Lists/master/fraud.txt"
BLOCKLISTPROJECT_RANSOMWARE_URL = "https://raw.githubusercontent.com/blocklistproject/Lists/master/ransomware.txt"
BLOCKLISTPROJECT_TRACKING_URL = "https://raw.githubusercontent.com/blocklistproject/Lists/master/tracking.txt"
HAGEZI_DYNDNS_URL = "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/dyndns-onlydomains.txt"
HAGEZI_HOSTER_URL = "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/hoster-onlydomains.txt"
HAGEZI_FAKE_URL = "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/fake-onlydomains.txt"

# Adult lists (selective to avoid insane sizes)
STEVENBLACK_PORN_URL = "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn/hosts"
CHADMAYFIELD_PORN_URL = "https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_top1m.list"
UT1_ADULT_URL = "https://dsi.ut-capitole.fr/blacklists/download/adult.tar.gz"

UKLANS_SKIP_SERVICES = {"test", "wsus"}
COMMON_SECOND_LEVEL_REGISTRIES = {
    "ac",
    "co",
    "com",
    "edu",
    "gen",
    "go",
    "gov",
    "id",
    "lg",
    "mil",
    "ne",
    "net",
    "nom",
    "or",
    "org",
    "sch",
}
UKLANS_SERVICE_OVERRIDES = {
    "arenanet": {"service_id": "arenanet", "name": "ArenaNet", "group": "gaming"},
    "blizzard": {"service_id": "blizzard_entertainment", "name": "Blizzard Entertainment", "group": "gaming"},
    "bsg": {"service_id": "battlestate_games", "name": "Battlestate Games", "group": "gaming"},
    "cityofheroes": {"service_id": "city_of_heroes", "name": "City of Heroes", "group": "gaming"},
    "cod": {"service_id": "activision_blizzard", "name": "Activision Blizzard", "group": "gaming"},
    "daybreak": {"service_id": "daybreak_games", "name": "Daybreak Games", "group": "gaming"},
    "epicgames": {"service_id": "epic_games", "name": "Epic Games", "group": "gaming"},
    "frontier": {"service_id": "frontier_games", "name": "Frontier Games", "group": "gaming"},
    "neverwinter": {"service_id": "neverwinter", "name": "Neverwinter", "group": "gaming"},
    "nexusmods": {"service_id": "nexusmods", "name": "Nexus Mods", "group": "gaming"},
    "nintendo": {"service_id": "nintendo", "name": "Nintendo", "group": "gaming"},
    "origin": {"service_id": "origin", "name": "Origin", "group": "gaming"},
    "pathofexile": {"service_id": "path_of_exile", "name": "Path of Exile", "group": "gaming"},
    "renegadex": {"service_id": "renegade_x", "name": "Renegade X", "group": "gaming"},
    "riot": {"service_id": "riot_games", "name": "Riot Games", "group": "gaming"},
    "rockstar": {"service_id": "rockstar_games", "name": "Rockstar Games", "group": "gaming"},
    "sony": {"service_id": "playstation", "name": "PlayStation", "group": "gaming"},
    "square": {"service_id": "square_enix", "name": "Square Enix", "group": "gaming"},
    "steam": {"service_id": "steam", "name": "Steam", "group": "gaming"},
    "teso": {"service_id": "the_elder_scrolls_online", "name": "The Elder Scrolls Online", "group": "gaming"},
    "uplay": {"service_id": "ubisoft", "name": "Ubisoft", "group": "gaming"},
    "warframe": {"service_id": "warframe", "name": "Warframe", "group": "gaming"},
    "wargaming": {"service_id": "wargaming", "name": "Wargaming", "group": "gaming"},
    "xboxlive": {"service_id": "xboxlive", "name": "Xbox Live", "group": "gaming"},
}

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


def extract_domains_from_uklans_file(text: str) -> Set[str]:
    """
    Extract domains from UKLANS cache-domains files.

    The upstream format allows comments and leading wildcard entries like
    `*.example.com`. We normalize those into plain domains so the existing
    blocklist writer can deduplicate and emit them in hosts-file format.
    """
    domains = set()
    for line in text.splitlines():
        line = line.strip().lower()
        if not line or line.startswith("#"):
            continue

        domain = line.split()[0]
        if domain.startswith("*."):
            domain = domain[2:]

        if is_valid_domain(domain):
            domains.add(domain)

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
        csv_lines = []
        for raw_line in csv_text.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            if line.startswith("#"):
                candidate = line.lstrip("#").strip()
                if candidate.lower().startswith("id,dateadded,url,"):
                    csv_lines.append(candidate)
                continue
            csv_lines.append(line)

        if not csv_lines:
            logger.warning("URLhaus feed did not contain a parseable CSV payload")
            return domains

        reader = csv.DictReader(StringIO("\n".join(csv_lines)))
        if not reader.fieldnames or "url" not in reader.fieldnames:
            logger.warning("URLhaus CSV header did not expose a 'url' column")
            return domains

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


def humanize_service_name(service_id: str) -> str:
    """Convert a service id into a readable display name."""
    return service_id.replace("_", " ").replace("-", " ").title()


def get_uklans_target(service_name: str, description: str = "") -> Dict[str, str]:
    """
    Map a UKLANS source into the local service model.

    Known services are merged into existing gaming targets where possible so
    the generated README stays tidy and overlapping domains enrich the same
    per-service blocklist.
    """
    if service_name in UKLANS_SERVICE_OVERRIDES:
        return UKLANS_SERVICE_OVERRIDES[service_name]

    display_name = description.replace("CDN for ", "").strip() or humanize_service_name(service_name)
    service_id = re.sub(r"[^a-z0-9]+", "_", service_name.lower()).strip("_")
    return {"service_id": service_id, "name": display_name, "group": "gaming"}


def load_custom_domains() -> Dict[str, List[str]]:
    """
    Load custom domain additions from JSON file(s).
    
    Returns:
        Dictionary mapping service_id to list of domains
    """
    existing_files = [path for path in CUSTOM_DOMAINS_FILES if path.exists()]
    if not existing_files:
        searched = ", ".join(str(path) for path in CUSTOM_DOMAINS_FILES)
        logger.info(f"No custom domains file found. Checked: {searched}")
        return {}
    
    try:
        custom_domains = {}
        for path in existing_files:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if not isinstance(data, dict):
                logger.warning(f"Skipping custom domains file with invalid structure: {path}")
                continue
            custom_domains.update(data)

        logger.info(
            "Loaded custom domains from %s",
            ", ".join(str(path) for path in existing_files),
        )
        return custom_domains
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in custom domains file: {e}")
        return {}
    except Exception as e:
        logger.error(f"Failed to load custom domains: {e}")
        return {}


def load_source_policies() -> Dict:
    """
    Load source validation/filter policies from JSON.

    Returns:
        Policy dictionary or empty configuration on failure.
    """
    if not SOURCE_POLICIES_FILE.exists():
        logger.info(f"No source policies file found at {SOURCE_POLICIES_FILE}")
        return {}

    try:
        with open(SOURCE_POLICIES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            logger.warning("Source policies must be a JSON object")
            return {}
        logger.info("Loaded source policies from %s", SOURCE_POLICIES_FILE)
        return data
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in source policies file: {e}")
        return {}
    except Exception as e:
        logger.error(f"Failed to load source policies: {e}")
        return {}


def _merge_unique(items: List[str]) -> List[str]:
    """Preserve list order while removing duplicates."""
    seen = set()
    merged = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        merged.append(item)
    return merged


def domain_matches_suffix(domain: str, suffix: str) -> bool:
    """Return True when the domain is the suffix or sits below it."""
    domain = domain.lower().strip(".")
    suffix = suffix.lower().strip(".")
    return domain == suffix or domain.endswith(f".{suffix}")


def merge_policy_layers(*layers: Optional[Dict]) -> Dict:
    """Merge default/category/service policy layers into one effective policy."""
    merged = {
        "mode": "registrable",
        "forbid_public_suffix_entries": True,
        "allow_shared_hosts": False,
        "must_exist": False,
        "max_delta_pct": None,
        "min_baseline_count_for_delta": 5,
        "exclude_exact": [],
        "exclude_suffix": [],
        "required_domains": [],
        "group": None,
    }

    list_keys = ("exclude_exact", "exclude_suffix", "required_domains")
    scalar_keys = (
        "mode",
        "forbid_public_suffix_entries",
        "allow_shared_hosts",
        "must_exist",
        "max_delta_pct",
        "min_baseline_count_for_delta",
        "group",
    )

    for layer in layers:
        if not isinstance(layer, dict):
            continue
        for key in scalar_keys:
            if key in layer:
                merged[key] = layer[key]
        for key in list_keys:
            values = layer.get(key, [])
            if isinstance(values, list):
                merged[key].extend(str(value).lower().strip(".") for value in values if value)

    for key in list_keys:
        merged[key] = _merge_unique(merged[key])

    return merged


def get_effective_policy(policies: Dict, group: str, service_id: str) -> Dict:
    """Resolve the effective policy for a service/category pair."""
    return merge_policy_layers(
        policies.get("defaults"),
        policies.get("categories", {}).get(group, {}),
        policies.get("services", {}).get(service_id, {}),
    )


def apply_custom_domains(services_by_target: Dict, custom_domains: Dict) -> None:
    """
    Apply custom domain additions from custom_domains.json.
    
    Supports two formats:
    1. Simple: "service_id": ["domain1.com", "domain2.com"]
    2. Detailed: "service_id": {"category": "adult", "name": "Display Name", "domains": ["domain.com"]}
    
    Args:
        services_by_target: Dictionary of services to update
        custom_domains: Dictionary from JSON file
    """
    for service_id, config in custom_domains.items():
        # Skip comment keys
        if service_id.startswith("_"):
            continue
        
        # Determine format and extract data
        if isinstance(config, list):
            # Simple format: ["domain1.com", "domain2.com"]
            domain_list = config
            category = None  # Will auto-categorize
            display_name = None  # Will auto-generate
            preserve_subdomains = False
        elif isinstance(config, dict):
            # Detailed format: {"category": "adult", "name": "Grindr", "domains": [...]}
            domain_list = config.get("domains", [])
            category = config.get("category")
            display_name = config.get("name")
            preserve_subdomains = bool(config.get("preserve_subdomains", False))
        else:
            logger.warning(f"Invalid format for service '{service_id}' - must be list or dict")
            continue
        
        if not domain_list:
            logger.warning(f"No domains specified for service '{service_id}'")
            continue
        
        # Validate and add domains
        valid_domains = set()
        for domain in domain_list:
            domain = str(domain).lower().strip()
            if is_valid_domain(domain):
                valid_domains.add(domain)
            else:
                logger.warning(f"Invalid custom domain '{domain}' for service '{service_id}'")
        
        if not valid_domains:
            continue
        
        # If service doesn't exist, create it
        if service_id not in services_by_target or not services_by_target[service_id]["group"]:
            # Determine category
            if category:
                # Use explicitly provided category
                group = category.lower()
            else:
                # Auto-categorize based on service name
                if any(keyword in service_id.lower() for keyword in ["dating", "tinder", "bumble", "grindr", "hinge", "onlyfans", "match", "pof"]):
                    group = "adult"
                else:
                    group = "misc"
            
            # Determine display name
            if display_name:
                name = display_name
            else:
                name = service_id.replace("_", " ").title()
            
            services_by_target[service_id]["group"] = group
            services_by_target[service_id]["name"] = name
            services_by_target[service_id]["domains"] = set()
            services_by_target[service_id]["preserve_subdomains"] = False
            logger.info(f"Created new service '{service_id}' in category '{group}' as '{name}'")

        if category and category.lower() == "dns" and not preserve_subdomains:
            preserve_subdomains = True

        if preserve_subdomains:
            services_by_target[service_id]["preserve_subdomains"] = True
        
        # Add custom domains
        services_by_target[service_id]["domains"].update(valid_domains)
        logger.info(f"Added {len(valid_domains)} custom domain(s) to '{service_id}'")


def apply_source_policies(services_by_target: Dict, policies: Dict) -> None:
    """
    Apply repo-local source policies before writing generated files.

    The first pass focuses on explicit exclusions and mode overrides so noisy
    shared infrastructure entries can be trimmed without hard-coding those
    decisions in Python.
    """
    if not policies:
        return

    for service_id, svc_data in services_by_target.items():
        domains = svc_data.get("domains")
        group = svc_data.get("group", "")
        if not domains or not group:
            continue

        effective_policy = get_effective_policy(policies, group, service_id)
        if effective_policy.get("mode") == "exact":
            svc_data["preserve_subdomains"] = True

        exclude_exact = set(effective_policy.get("exclude_exact", []))
        exclude_suffix = effective_policy.get("exclude_suffix", [])
        if not exclude_exact and not exclude_suffix:
            continue

        filtered_domains = set()
        removed_domains = []

        for domain in domains:
            candidate = domain.lower().strip(".")
            if candidate in exclude_exact:
                removed_domains.append(candidate)
                continue
            if any(domain_matches_suffix(candidate, suffix) for suffix in exclude_suffix):
                removed_domains.append(candidate)
                continue
            filtered_domains.add(candidate)

        if removed_domains:
            preview = ", ".join(sorted(removed_domains)[:5])
            if len(removed_domains) > 5:
                preview += ", ..."
            logger.info(
                "Policy filtered %d domain(s) from %s/%s: %s",
                len(removed_domains),
                group,
                service_id,
                preview,
            )

        svc_data["domains"] = filtered_domains


def build_existing_domains_index(services_by_target: Dict) -> Dict[str, str]:
    """
    Build an index of all existing domains and which service they belong to.
    Used for deduplication.
    
    Args:
        services_by_target: Dictionary of all services
        
    Returns:
        Dictionary mapping domain -> service_id
    """
    domain_index = {}
    
    for service_id, svc_data in services_by_target.items():
        if not svc_data.get("domains"):
            continue
        
        for domain in svc_data["domains"]:
            root = get_root_domain(domain)
            # Only index non-adult services (we want adult lists checked against these)
            if svc_data["group"] != "adult":
                domain_index[root] = service_id
    
    return domain_index


def clean_adult_content(adult_domains: Set[str], existing_domains: Dict[str, str]) -> Set[str]:
    """
    Remove domains that already exist in other (non-adult) services.
    This prevents legitimate services like Netflix/Discord from appearing in adult lists.
    
    Args:
        adult_domains: Set of domains from adult content feeds
        existing_domains: Index of existing domains -> service_id
        
    Returns:
        Cleaned set with duplicates removed
    """
    original_count = len(adult_domains)
    cleaned = set()
    removed = []
    
    for domain in adult_domains:
        root = get_root_domain(domain)
        
        # Check if this domain exists in a non-adult service
        if root in existing_domains:
            removed.append(f"{root} (in {existing_domains[root]})")
        else:
            cleaned.add(domain)
    
    removed_count = original_count - len(cleaned)
    if removed_count > 0:
        logger.info(f"Removed {removed_count} domains already in other services from adult feeds")
        if removed_count <= 20:  # Only show details if not too many
            logger.debug(f"Removed: {', '.join(removed[:20])}")
    
    return cleaned


def get_root_domain(domain: str) -> str:
    """
    Extract the registrable domain from a hostname.

    Uses the Public Suffix List when available so domains like
    `store.example.co.uk` are reduced to `example.co.uk` instead of `co.uk`.
    If the PSL cannot be fetched, falls back to a heuristic for common
    multi-label country-code suffixes.
    
    Args:
        domain: Full domain name
        
    Returns:
        Registrable domain (e.g., example.com from sub.example.com)
    """
    labels = [label for label in domain.lower().strip('.').split('.') if label]
    if len(labels) < 2:
        return domain.lower().strip('.')

    public_suffix = get_public_suffix(domain)
    suffix_labels = public_suffix.split('.') if public_suffix else [labels[-1]]

    if len(labels) <= len(suffix_labels):
        return '.'.join(labels)

    return '.'.join(labels[-(len(suffix_labels) + 1):])


def get_public_suffix(domain: str) -> str:
    """Return the public suffix for a domain using PSL rules when possible."""
    labels = [label for label in domain.lower().strip('.').split('.') if label]
    if not labels:
        return ""

    rules = get_public_suffix_rules()
    if rules is None:
        return get_fallback_public_suffix(labels)

    exact_rules, wildcard_rules, exception_rules = rules
    matches = [labels[-1]]

    for idx in range(len(labels)):
        candidate = ".".join(labels[idx:])
        if candidate in exception_rules:
            return ".".join(labels[idx + 1:])
        if candidate in exact_rules:
            matches.append(candidate)
        if idx + 1 < len(labels) and ".".join(labels[idx + 1:]) in wildcard_rules:
            matches.append(candidate)

    return max(matches, key=lambda item: item.count("."))


def get_fallback_public_suffix(labels: List[str]) -> str:
    """Heuristic fallback for common multi-label public suffixes."""
    if (
        len(labels) >= 2
        and len(labels[-1]) == 2
        and labels[-2] in COMMON_SECOND_LEVEL_REGISTRIES
    ):
        return ".".join(labels[-2:])

    return labels[-1]


@lru_cache(maxsize=1)
def get_public_suffix_rules() -> Optional[tuple]:
    """
    Fetch and parse the Public Suffix List.

    Returns a tuple of exact, wildcard, and exception rule sets. Falls back to
    a heuristic if the list cannot be fetched.
    """
    text = fetch_text(PUBLIC_SUFFIX_LIST_URL)
    if not text:
        logger.warning("Falling back to heuristic public suffix parsing")
        return None

    exact_rules = set()
    wildcard_rules = set()
    exception_rules = set()

    for line in text.splitlines():
        line = line.strip().lower()
        if not line or line.startswith("//"):
            continue
        if line.startswith("!"):
            exception_rules.add(line[1:])
        elif line.startswith("*."):
            wildcard_rules.add(line[2:])
        else:
            exact_rules.add(line)

    logger.info(
        "Loaded %d public suffix rules",
        len(exact_rules) + len(wildcard_rules) + len(exception_rules),
    )
    return exact_rules, wildcard_rules, exception_rules


def write_domain_file(
    path: Path,
    domains: Set[str],
    header: Optional[str] = None,
    preserve_subdomains: bool = False,
) -> tuple:
    """
    Write domains to file with header in Pi-hole/AdGuard compatible format.
    Uses wildcard format to ensure ALL subdomains are blocked.
    
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
    
    normalized_domains = set()
    for domain in domains:
        if preserve_subdomains:
            normalized_domains.add(domain.lower().strip('.'))
        else:
            normalized_domains.add(get_root_domain(domain))

    sorted_domains = sorted(normalized_domains)
    
    content = ""
    if header:
        content += header.rstrip() + "\n\n"
    
    # Pi-hole format: Use wildcard to block all subdomains
    # Format: 0.0.0.0 domain.com
    # This ensures *.domain.com is blocked
    for domain in sorted_domains:
        content += f"0.0.0.0 {domain}\n"
    
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


def fetch_json_with_curl(
    url: str,
    user_agent: Optional[str] = None,
    gzipped: bool = False,
) -> Optional[any]:
    """
    Fetch JSON via curl.

    This is used as a fallback for endpoints such as PhishTank where Python
    requests can fail on the final signed CDN redirect while curl succeeds.
    """
    cmd = ["curl", "-fsSL"]
    if user_agent:
        cmd.extend(["-A", user_agent])
    cmd.append(url)

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            check=True,
        )
        payload = result.stdout
        if gzipped:
            payload = gzip.decompress(payload)
        return json.loads(payload.decode("utf-8"))
    except subprocess.CalledProcessError as e:
        stderr = e.stderr.strip() if e.stderr else str(e)
        logger.error(f"curl failed for {url}: {stderr}")
    except gzip.BadGzipFile as e:
        logger.error(f"Invalid gzip returned by curl for {url}: {e}")
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON returned by curl for {url}: {e}")

    return None


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
    services_by_target = defaultdict(
        lambda: {"group": "", "name": "", "domains": set(), "preserve_subdomains": False}
    )
    
    # Load custom domains from JSON file
    custom_domains = load_custom_domains()
    source_policies = load_source_policies()
    
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
    logger.info("Fetching UKLANS cache-domains gaming feeds...")
    uklans_data = fetch_json(UKLANS_CACHE_DOMAINS_URL)

    if not uklans_data or not isinstance(uklans_data, dict):
        logger.error("Failed to fetch UKLANS cache-domains metadata")
    else:
        cache_domains = uklans_data.get("cache_domains", [])
        imported_sources = 0
        imported_domains = 0

        for entry in cache_domains:
            if not isinstance(entry, dict):
                continue

            source_name = str(entry.get("name", "")).strip().lower()
            if not source_name or source_name in UKLANS_SKIP_SERVICES:
                continue

            domain_files = entry.get("domain_files", [])
            if not isinstance(domain_files, list) or not domain_files:
                continue

            source_domains = set()
            for domain_file in domain_files:
                domain_file = str(domain_file).strip()
                if not domain_file:
                    continue

                file_url = f"{UKLANS_RAW_BASE_URL}{quote(domain_file)}"
                file_text = fetch_text(file_url)
                if not file_text:
                    logger.warning(f"Failed to fetch UKLANS file: {domain_file}")
                    continue

                source_domains.update(extract_domains_from_uklans_file(file_text))

            if not source_domains:
                logger.warning(f"No valid domains found for UKLANS source '{source_name}'")
                continue

            target = get_uklans_target(source_name, str(entry.get("description", "")).strip())
            service_id = target["service_id"]

            services_by_target[service_id]["group"] = target["group"]
            if not services_by_target[service_id]["name"]:
                services_by_target[service_id]["name"] = target["name"]
            services_by_target[service_id]["domains"].update(source_domains)

            imported_sources += 1
            imported_domains += len(source_domains)
            logger.info(
                f"UKLANS {source_name}: added {len(source_domains)} domains into {service_id}"
            )

        logger.info(
            f"Processed {imported_sources} UKLANS gaming sources ({imported_domains} raw domains)"
        )

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
    if phishtank_json is None:
        logger.info("Retrying PhishTank with curl gzip fallback...")
        phishtank_json = fetch_json_with_curl(
            PHISHTANK_GZ_URL,
            user_agent=PHISHTANK_USER_AGENT,
            gzipped=True,
        )
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
        if uh_domains:
            services_by_target["urlhaus"]["group"] = "malware"
            services_by_target["urlhaus"]["name"] = "URLhaus"
            services_by_target["urlhaus"]["domains"].update(uh_domains)
            logger.info(f"URLhaus: {len(uh_domains)} domains")
        else:
            logger.warning("URLhaus returned no valid domains after parsing")
    else:
        logger.error("Failed to fetch URLhaus data")

    # SSL Blacklist - certificate/IP intelligence rather than hostname domains
    logger.info(
        "Skipping SSLBL for services output: upstream export is certificate/IP-oriented, not a DNS domain hosts feed"
    )

    # Curated category feeds
    logger.info("Fetching curated category feeds...")
    curated_feeds = (
        {
            "service_id": "blp_scam",
            "group": "scam",
            "name": "Block List Project Scam",
            "url": BLOCKLISTPROJECT_SCAM_URL,
            "extractor": extract_domains_from_hosts_file,
        },
        {
            "service_id": "blp_fraud",
            "group": "scam",
            "name": "Block List Project Fraud",
            "url": BLOCKLISTPROJECT_FRAUD_URL,
            "extractor": extract_domains_from_hosts_file,
        },
        {
            "service_id": "blp_ransomware",
            "group": "malware",
            "name": "Block List Project Ransomware",
            "url": BLOCKLISTPROJECT_RANSOMWARE_URL,
            "extractor": extract_domains_from_hosts_file,
        },
        {
            "service_id": "blp_tracking",
            "group": "tracking",
            "name": "Block List Project Tracking",
            "url": BLOCKLISTPROJECT_TRACKING_URL,
            "extractor": extract_domains_from_hosts_file,
        },
        {
            "service_id": "hagezi_dyndns",
            "group": "dynamic_dns",
            "name": "HaGeZi Dynamic DNS",
            "url": HAGEZI_DYNDNS_URL,
            "extractor": extract_domains_from_plain_list,
        },
        {
            "service_id": "hagezi_hoster",
            "group": "badware_hoster",
            "name": "HaGeZi Badware Hoster",
            "url": HAGEZI_HOSTER_URL,
            "extractor": extract_domains_from_plain_list,
        },
        {
            "service_id": "hagezi_fake",
            "group": "scam",
            "name": "HaGeZi Fake",
            "url": HAGEZI_FAKE_URL,
            "extractor": extract_domains_from_plain_list,
        },
    )

    for feed in curated_feeds:
        feed_text = fetch_text(feed["url"])
        if not feed_text:
            logger.error(f"Failed to fetch {feed['name']} data")
            continue

        feed_domains = feed["extractor"](feed_text)
        if not feed_domains:
            logger.warning(f"{feed['name']}: no valid domains extracted")
            continue

        service_id = feed["service_id"]
        services_by_target[service_id]["group"] = feed["group"]
        services_by_target[service_id]["name"] = feed["name"]
        services_by_target[service_id]["domains"].update(feed_domains)
        logger.info(f"{feed['name']}: {len(feed_domains)} domains")

    # -----------------------------
    # BUILD DOMAIN INDEX FOR DEDUPLICATION
    # -----------------------------
    logger.info("Building domain index for deduplication...")
    existing_domains = build_existing_domains_index(services_by_target)
    logger.info(f"Indexed {len(existing_domains)} domains from non-adult services")
    
    # -----------------------------
    # ADULT CONTENT (per-source + aggregated)
    # -----------------------------
    logger.info("Fetching adult content feeds (selective)...")

    # StevenBlack
    sb_text = fetch_text(STEVENBLACK_PORN_URL)
    if sb_text:
        sb_adult = extract_domains_from_hosts_file(sb_text)
        # Clean out domains already in other services
        sb_adult = clean_adult_content(sb_adult, existing_domains)
        services_by_target["stevenblack_porn"]["group"] = "adult"
        services_by_target["stevenblack_porn"]["name"] = "StevenBlack Porn"
        services_by_target["stevenblack_porn"]["domains"].update(sb_adult)
        logger.info(f"StevenBlack: {len(sb_adult)} domains (after deduplication)")
    else:
        logger.error("Failed to fetch StevenBlack data")

    # Chad Mayfield
    cm_text = fetch_text(CHADMAYFIELD_PORN_URL)
    if cm_text:
        cm_adult = extract_domains_from_plain_list(cm_text)
        # Clean out domains already in other services
        cm_adult = clean_adult_content(cm_adult, existing_domains)
        services_by_target["chadmayfield_porn"]["group"] = "adult"
        services_by_target["chadmayfield_porn"]["name"] = "Chad Mayfield Porn"
        services_by_target["chadmayfield_porn"]["domains"].update(cm_adult)
        logger.info(f"Chad Mayfield: {len(cm_adult)} domains (after deduplication)")
    else:
        logger.error("Failed to fetch Chad Mayfield data")

    # UT1 optional (commented by default due to massive size)
    # logger.info("Fetching UT1 Adult tarball (this may take a while)...")
    # ut1_content = fetch_binary(UT1_ADULT_URL, timeout=120)
    # if ut1_content:
    #     ut1_domains = extract_domains_from_ut1_tarball(ut1_content)
    #     ut1_domains = clean_adult_content(ut1_domains, existing_domains)
    #     services_by_target["ut1_adult"]["group"] = "adult"
    #     services_by_target["ut1_adult"]["name"] = "UT1 Adult"
    #     services_by_target["ut1_adult"]["domains"].update(ut1_domains)
    #     logger.info(f"UT1: {len(ut1_domains)} domains (after deduplication)")

    # -----------------------------
    # APPLY CUSTOM DOMAINS
    # -----------------------------
    logger.info("Applying custom domain additions...")
    apply_custom_domains(services_by_target, custom_domains)

    # -----------------------------
    # APPLY SOURCE POLICIES
    # -----------------------------
    logger.info("Applying source policies...")
    apply_source_policies(services_by_target, source_policies)

    # -----------------------------
    # WRITE PER-SERVICE FILES
    # -----------------------------
    logger.info("Writing per-service/target files...")
    service_stats = []
    category_domains = defaultdict(set)
    category_preserve_subdomains = defaultdict(bool)

    for service_id, svc_data in services_by_target.items():
        if not svc_data["domains"]:
            continue
            
        group = svc_data["group"]
        name = svc_data["name"]
        domains = svc_data["domains"]
        preserve_subdomains = svc_data.get("preserve_subdomains", False)
        format_line = (
            "# Format: Hosts file (0.0.0.0 hostname) - exact hostnames preserved"
            if preserve_subdomains
            else "# Format: Hosts file (0.0.0.0 domain.com) - blocks all subdomains"
        )

        out_path = LISTS_DIR / group / f"{service_id}.txt"
        header = (
            f"# {name}\n"
            f"# Category: {group}\n"
            f"# Generated: {timestamp}\n"
            f"{format_line}\n"
            f"# Original domains (before deduplication): {len(domains)}"
        )

        try:
            count, size_mb = write_domain_file(
                out_path,
                domains,
                header,
                preserve_subdomains=preserve_subdomains,
            )
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
        category_preserve_subdomains[group] = (
            category_preserve_subdomains[group] or preserve_subdomains
        )

    # -----------------------------
    # WRITE PER-CATEGORY FILES
    # -----------------------------
    logger.info("Writing category files...")
    category_stats = []

    for group, domains in category_domains.items():
        out_path = CATEGORIES_DIR / f"{group}.txt"
        preserve_subdomains = category_preserve_subdomains[group]
        format_line = (
            "# Format: Hosts file (0.0.0.0 hostname) - exact hostnames preserved"
            if preserve_subdomains
            else "# Format: Hosts file (0.0.0.0 domain.com) - blocks all subdomains"
        )
        header = (
            f"# {group.capitalize()} Blocklist\n"
            f"# Generated: {timestamp}\n"
            f"{format_line}\n"
            f"# Original domains (before deduplication): {len(domains)}"
        )

        try:
            count, size_mb = write_domain_file(
                out_path,
                domains,
                header,
                preserve_subdomains=preserve_subdomains,
            )
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
    lines.append(
        "All lists are **Pi-hole and AdGuard Home compatible** - registrable domains by default, "
        "with exact hostnames preserved where needed.\n"
    )
    
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
        category_meta = {
            "adult": ("🔞", "Adult Content"),
            "badware_hoster": ("🗄️", "Badware Hosters"),
            "dynamic_dns": ("🌐", "Dynamic DNS"),
            "gaming": ("🎮", "Gaming Platforms"),
            "malware": ("🦠", "Malware & Threats"),
            "phishing": ("🎣", "Phishing & Scam Sites"),
            "scam": ("💸", "Scam & Fraud"),
            "social_network": ("📱", "Social Networks"),
            "tracking": ("🛰️", "Tracking & Analytics"),
        }
        emoji, desc = category_meta.get(group, ("📁", group.replace("_", " ").title()))
        
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
        lines.append(f"### {group.replace('_', ' ').title()}\n")
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
    lines.append("- **Hosts file format** - `0.0.0.0 hostname` for maximum compatibility")
    lines.append("- **Registrable domains by default** - avoids invalid suffixes like `co.uk` and keeps lists smaller")
    lines.append("- **Exact hostnames preserved when needed** - useful for DNS endpoints and similar targeted overrides")
    lines.append("- **One entry per line** - clean, simple format")
    lines.append("- **Commented headers** - each file includes metadata and generation timestamp")
    lines.append("- **Works with Pi-hole, AdGuard Home, hosts file, and most DNS blockers**\n")
    
    # Add sources section
    lines.append("## 🔍 Data Sources\n")
    lines.append("This repository aggregates threat intelligence from trusted sources:\n")
    lines.append("### Security Feeds")
    lines.append("- **[Phishing Army](https://phishing.army/)** - Community-driven phishing database")
    lines.append("- **[OpenPhish](https://openphish.com/)** - Automated phishing detection")
    lines.append("- **[PhishTank](https://phishtank.org/)** - Verified phishing URLs")
    lines.append("- **[ThreatFox](https://threatfox.abuse.ch/)** - Malware IOCs from abuse.ch")
    lines.append("- **[URLhaus](https://urlhaus.abuse.ch/)** - Malware distribution sites\n")
    
    lines.append("### Content Filters")
    lines.append("- **[AdGuard](https://adguard.com/)** - Service blocklists (social media, gaming, streaming)")
    lines.append("- **[The Block List Project](https://github.com/blocklistproject/Lists)** - Curated scam, tracking, and ransomware blocklists")
    lines.append("- **[HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists)** - Curated fake, dynamic DNS, and badware hoster categories")
    lines.append("- **[UKLANS cache-domains](https://github.com/uklans/cache-domains)** - Gaming CDN and cache hostnames")
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
