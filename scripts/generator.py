#!/usr/bin/env python3
"""
Threat Intelligence Blocklist Generator

Generates three output tiers from the same source data:
1. Standard service blocklists
   - services/categories/<group>.txt
   - services/lists/<group>/<source>.txt
   - services/README.md

2. Security exact-host blocklists
   - security/categories/<group>.txt
   - security/lists/<group>/<source>.txt
   - security/README.md

3. Unbound RPZ policies
   - rpz/categories/<group>.rpz
   - rpz/lists/<group>/<source>.rpz
   - rpz/README.md
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

SECURITY_OUTPUT_GROUPS = {
    "badware_hoster",
    "dynamic_dns",
    "malware",
    "phishing",
    "scam",
}

OUTPUT_CATEGORY_META = {
    "abuse": {"emoji": "🚨", "label": "Abuse & Malvertising"},
    "adult": {"emoji": "🔞", "label": "Adult Content"},
    "ai": {"emoji": "🤖", "label": "AI Assistants"},
    "crypto": {"emoji": "🪙", "label": "Crypto & Cryptojacking"},
    "badware_hoster": {"emoji": "🗄️", "label": "Badware Hosters"},
    "cdn": {"emoji": "☁️", "label": "CDNs & Edge"},
    "dating": {"emoji": "💕", "label": "Dating Services"},
    "dns": {"emoji": "🛜", "label": "DNS Providers"},
    "dns_bypass": {"emoji": "🛡️", "label": "DNS / VPN Bypass"},
    "drugs": {"emoji": "💊", "label": "Drugs"},
    "dynamic_dns": {"emoji": "🌐", "label": "Dynamic DNS"},
    "gambling": {"emoji": "🎰", "label": "Gambling & Betting"},
    "gaming": {"emoji": "🎮", "label": "Gaming Platforms"},
    "hosting": {"emoji": "🗃️", "label": "Hosting & File Platforms"},
    "malware": {"emoji": "🦠", "label": "Malware & Threats"},
    "messenger": {"emoji": "💬", "label": "Messaging Apps"},
    "phishing": {"emoji": "🎣", "label": "Phishing & Scam Sites"},
    "piracy": {"emoji": "🏴‍☠️", "label": "Piracy"},
    "privacy": {"emoji": "🕶️", "label": "Privacy Tools"},
    "redirect": {"emoji": "↪️", "label": "Redirectors"},
    "scam": {"emoji": "💸", "label": "Scam & Fraud"},
    "shopping": {"emoji": "🛍️", "label": "Shopping & Marketplaces"},
    "social_network": {"emoji": "📱", "label": "Social Networks"},
    "smart_tv": {"emoji": "📡", "label": "Smart TV Telemetry"},
    "software": {"emoji": "🧰", "label": "Software & Updates"},
    "streaming": {"emoji": "📺", "label": "Streaming Services"},
    "torrent": {"emoji": "🧲", "label": "Torrent"},
    "tracking": {"emoji": "🛰️", "label": "Tracking & Analytics"},
    "url_shortener": {"emoji": "🔗", "label": "URL Shorteners"},
    "vaping": {"emoji": "💨", "label": "Vaping"},
}

OUTPUT_PROFILES = {
    "services": {
        "base_dir": Path("services"),
        "lists_dir": Path("services/lists"),
        "categories_dir": Path("services/categories"),
        "recommended_dir": Path("services/recommended"),
        "readme_path": Path("services/README.md"),
        "quality_report_path": Path("services/quality_report.json"),
        "file_extension": ".txt",
        "format": "hosts",
        "title": "Threat Intelligence & Content Blocklists",
        "summary": (
            "Home-safe default layer for Pi-hole, AdGuard Home, and similar DNS blockers. "
            "Lists stay registrable-domain based by default so they are easier to reason about "
            "and less likely to overblock."
        ),
        "audience": "Home-safe / standard",
        "risk": "Moderate",
        "include_groups": None,
        "force_exact_groups": set(),
        "quick_start_title": "Quick Start (Recommended)",
        "quick_start_body": (
            "Use the aggregated category lists below if you want broad blocking with lower churn "
            "and easier troubleshooting."
        ),
        "category_intro": "One-click blocklists combining multiple sources for everyday blocking.",
        "advanced_intro": (
            "For granular control, each source is available separately if you want source-level "
            "attribution or need to disable one feed."
        ),
        "recommended_bundles": [
            {
                "bundle_id": "home_safe",
                "name": "Home Safe",
                "best_for": "Most home users",
                "description": "Balanced default with common security, abuse, and tracking coverage.",
                "groups": [
                    "abuse",
                    "badware_hoster",
                    "dynamic_dns",
                    "malware",
                    "phishing",
                    "redirect",
                    "scam",
                    "tracking",
                ],
                "preserve_subdomains": False,
            },
            {
                "bundle_id": "family",
                "name": "Family",
                "best_for": "Shared devices and kid-safe networks",
                "description": "Home Safe plus adult, dating, gambling, drugs, and vaping blocks.",
                "groups": [
                    "abuse",
                    "adult",
                    "badware_hoster",
                    "dating",
                    "drugs",
                    "dynamic_dns",
                    "gambling",
                    "malware",
                    "phishing",
                    "redirect",
                    "scam",
                    "tracking",
                    "vaping",
                ],
                "preserve_subdomains": False,
            },
            {
                "bundle_id": "aggressive",
                "name": "Aggressive",
                "best_for": "Lock-it-down blocking",
                "description": "Family profile plus crypto, piracy, and torrent-heavy domains.",
                "groups": [
                    "abuse",
                    "adult",
                    "badware_hoster",
                    "crypto",
                    "dating",
                    "drugs",
                    "dynamic_dns",
                    "gambling",
                    "malware",
                    "phishing",
                    "piracy",
                    "redirect",
                    "scam",
                    "torrent",
                    "tracking",
                    "vaping",
                ],
                "preserve_subdomains": False,
            },
        ],
        "usage": [
            "### Pi-hole",
            "1. Navigate to **Settings** → **Blocklists**",
            "2. Paste the **Raw URL** of your desired list",
            "3. Click **Save and Update**",
            "4. Wait for gravity to update",
            "",
            "### AdGuard Home",
            "1. Go to **Filters** → **DNS blocklists**",
            "2. Click **Add blocklist** → **Add a custom list**",
            "3. Paste the **Raw URL** and provide a name",
            "4. Click **Save**",
        ],
        "format_notes": [
            "**Hosts file format** - `0.0.0.0 hostname` for broad compatibility",
            "**Registrable domains by default** - avoids invalid suffixes like `co.uk`",
            "**Exact hostnames preserved where needed** - mainly DNS endpoint overrides",
            "**One entry per line** with commented headers and generation metadata",
        ],
    },
    "security": {
        "base_dir": Path("security"),
        "lists_dir": Path("security/lists"),
        "categories_dir": Path("security/categories"),
        "recommended_dir": Path("security/recommended"),
        "readme_path": Path("security/README.md"),
        "quality_report_path": Path("security/quality_report.json"),
        "file_extension": ".txt",
        "format": "hosts",
        "title": "Exact-Host Security Blocklists",
        "summary": (
            "Security-focused host blocking for phishing, malware, scam, dynamic DNS, and "
            "badware hoster feeds. These lists preserve exact hostnames so URL-derived feeds "
            "stay precise instead of collapsing to broad registrable roots."
        ),
        "audience": "Security-focused / higher churn",
        "risk": "Elevated",
        "include_groups": SECURITY_OUTPUT_GROUPS,
        "force_exact_groups": SECURITY_OUTPUT_GROUPS,
        "quick_start_title": "Quick Start",
        "quick_start_body": (
            "Use these lists when you want stronger protection against exact phishing or malware "
            "hosts and you are comfortable with faster list churn."
        ),
        "category_intro": (
            "Exact-host category bundles built from higher-sensitivity security feeds."
        ),
        "advanced_intro": (
            "Each source is also available separately if you want tighter source attribution or "
            "to tune false-positive handling."
        ),
        "recommended_bundles": [
            {
                "bundle_id": "security",
                "name": "Security",
                "best_for": "People who want stronger phishing and malware coverage",
                "description": "Exact-host security coverage across phishing, malware, scams, dynamic DNS, and badware hosters.",
                "groups": sorted(SECURITY_OUTPUT_GROUPS),
                "preserve_subdomains": True,
            },
        ],
        "usage": [
            "### Pi-hole / AdGuard Home",
            "1. Import the **Raw URL** of the exact-host list you want",
            "2. Start with the aggregated categories before stacking individual feeds",
            "3. Watch query logs closely after enabling them",
            "",
            "### When to use this layer",
            "1. You want stronger phishing and malware coverage",
            "2. You are comfortable whitelisting exact hosts when needed",
            "3. You prefer precision over broad domain collapsing",
        ],
        "format_notes": [
            "**Hosts file format** - `0.0.0.0 hostname`",
            "**Exact hostnames preserved** - designed for URL-derived security feeds",
            "**Higher churn** - entries can appear and disappear faster than the standard layer",
            "**Best paired with logging and allowlisting** when you run it broadly",
        ],
    },
    "rpz": {
        "base_dir": Path("rpz"),
        "lists_dir": Path("rpz/lists"),
        "categories_dir": Path("rpz/categories"),
        "recommended_dir": Path("rpz/recommended"),
        "readme_path": Path("rpz/README.md"),
        "quality_report_path": Path("rpz/quality_report.json"),
        "file_extension": ".rpz",
        "format": "rpz",
        "title": "RPZ Security Policies",
        "summary": (
            "Unbound-friendly RPZ zone files generated from the same exact-host security layer. "
            "This is the advanced output for users who want native response-policy feeds instead "
            "of hosts-style blocklists."
        ),
        "audience": "Advanced / Unbound RPZ",
        "risk": "Elevated",
        "include_groups": SECURITY_OUTPUT_GROUPS,
        "force_exact_groups": SECURITY_OUTPUT_GROUPS,
        "quick_start_title": "Quick Start",
        "quick_start_body": (
            "Use these files when you run Unbound or another resolver that supports RPZ and you "
            "want policy-zone blocking instead of hosts-style imports."
        ),
        "category_intro": "RPZ category bundles for exact-host security blocking.",
        "advanced_intro": (
            "Per-source RPZ files are available if you want to map individual feeds into separate "
            "policy zones."
        ),
        "recommended_bundles": [
            {
                "bundle_id": "security",
                "name": "Security RPZ",
                "best_for": "Unbound and RPZ-capable resolvers",
                "description": "Resolver-native exact-host policy zone covering phishing, malware, scams, dynamic DNS, and badware hosters.",
                "groups": sorted(SECURITY_OUTPUT_GROUPS),
                "preserve_subdomains": True,
            },
        ],
        "usage": [
            "### Unbound",
            "1. Place the `.rpz` file somewhere your resolver can read it",
            "2. Reference it from your RPZ configuration or local-zone include path",
            "3. Reload Unbound after updating the file",
            "",
            "### Why use RPZ here",
            "1. Keeps exact-host security feeds in a resolver-native format",
            "2. Makes feed separation easier than large monolithic includes",
            "3. Fits well with local automation and scheduled updates",
        ],
        "format_notes": [
            "**RPZ zone format** with `CNAME .` policy actions",
            "**Exact hostnames preserved** for URL-derived threat feeds",
            "**Advanced output** intended for Unbound or other RPZ-capable resolvers",
            "**Recommended after testing the matching `security/` hosts lists first**",
        ],
    },
}

# Backwards-compatible aliases for the default services output.
BASE_DIR = OUTPUT_PROFILES["services"]["base_dir"]
LISTS_DIR = OUTPUT_PROFILES["services"]["lists_dir"]
CATEGORIES_DIR = OUTPUT_PROFILES["services"]["categories_dir"]
README_PATH = OUTPUT_PROFILES["services"]["readme_path"]

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
BLOCKLISTPROJECT_ABUSE_URL = "https://raw.githubusercontent.com/blocklistproject/Lists/master/abuse.txt"
BLOCKLISTPROJECT_CRYPTO_URL = "https://raw.githubusercontent.com/blocklistproject/Lists/master/crypto.txt"
BLOCKLISTPROJECT_DRUGS_URL = "https://raw.githubusercontent.com/blocklistproject/Lists/master/drugs.txt"
BLOCKLISTPROJECT_PIRACY_URL = "https://raw.githubusercontent.com/blocklistproject/Lists/master/piracy.txt"
BLOCKLISTPROJECT_REDIRECT_URL = "https://raw.githubusercontent.com/blocklistproject/Lists/master/redirect.txt"
BLOCKLISTPROJECT_SMART_TV_URL = "https://raw.githubusercontent.com/blocklistproject/Lists/master/smart-tv.txt"
BLOCKLISTPROJECT_TORRENT_URL = "https://raw.githubusercontent.com/blocklistproject/Lists/master/torrent.txt"
BLOCKLISTPROJECT_VAPING_URL = "https://raw.githubusercontent.com/blocklistproject/Lists/master/vaping.txt"
HAGEZI_DYNDNS_URL = "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/dyndns-onlydomains.txt"
HAGEZI_HOSTER_URL = "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/hoster-onlydomains.txt"
HAGEZI_FAKE_URL = "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/fake-onlydomains.txt"
HAGEZI_DOH_VPN_PROXY_BYPASS_URL = "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/doh-vpn-proxy-bypass-onlydomains.txt"
HAGEZI_URLSHORTENER_URL = "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/wildcard/urlshortener-onlydomains.txt"
SHADOWWHISPERER_DATING_URL = "https://raw.githubusercontent.com/ShadowWhisperer/BlockLists/master/RAW/Dating"

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
SHADOWWHISPERER_DATING_OVERRIDES = {
    "badoo": {"service_id": "badoo", "name": "Badoo"},
    "badoocdn": {"service_id": "badoo", "name": "Badoo"},
    "boo": {"service_id": "boo", "name": "Boo"},
    "bumble": {"service_id": "bumble", "name": "Bumble"},
    "bumbcdn": {"service_id": "bumble", "name": "Bumble"},
    "bumblexternalstatic": {"service_id": "bumble", "name": "Bumble"},
    "coffeemeetsbagel": {"service_id": "coffee_meets_bagel", "name": "Coffee Meets Bagel"},
    "eharmony": {"service_id": "eharmony", "name": "eHarmony"},
    "happn": {"service_id": "happn", "name": "happn"},
    "her": {"service_id": "her", "name": "HER"},
    "hily": {"service_id": "hily", "name": "Hily"},
    "hinge": {"service_id": "hinge", "name": "Hinge"},
    "jaumo": {"service_id": "jaumo", "name": "Jaumo"},
    "match": {"service_id": "match", "name": "Match"},
    "okccdn": {"service_id": "okcupid", "name": "OkCupid"},
    "okcupid": {"service_id": "okcupid", "name": "OkCupid"},
    "pof": {"service_id": "plenty_of_fish", "name": "Plenty of Fish"},
    "skout": {"service_id": "skout", "name": "Skout"},
    "tantanapp": {"service_id": "tantan", "name": "TanTan"},
    "tancdn": {"service_id": "tantan", "name": "TanTan"},
    "tinder": {"service_id": "tinder", "name": "Tinder"},
    "weareher": {"service_id": "her", "name": "HER"},
    "zoosk": {"service_id": "zoosk", "name": "Zoosk"},
}
SHADOWWHISPERER_DATING_PATTERN_OVERRIDES = (
    (re.compile(r"^rdv\d+$"), {"service_id": "rdv", "name": "RDV"}),
)
SHADOWWHISPERER_DATING_NUMERIC_FAMILY_REGEX = re.compile(r"^(?P<base>[a-z][a-z-]{2,})(?P<number>\d{2,3})$")
SHADOWWHISPERER_DATING_NUMERIC_FAMILY_MIN_SIBLINGS = 3

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


def make_service_record() -> Dict[str, object]:
    """Return the default mutable record used for a service target."""
    return {"group": "", "name": "", "domains": set(), "preserve_subdomains": False}


def get_output_profile(profile_name: str) -> Dict[str, object]:
    """Return one output profile definition."""
    return OUTPUT_PROFILES[profile_name]


def should_include_in_profile(service_id: str, svc_data: Dict, profile: Dict) -> bool:
    """Return True when a service should be emitted for the given output profile."""
    if not svc_data.get("domains") or not svc_data.get("group"):
        return False

    include_groups = profile.get("include_groups")
    if not include_groups:
        return True

    return svc_data["group"] in include_groups


def preserve_subdomains_for_profile(service_id: str, svc_data: Dict, profile: Dict) -> bool:
    """Resolve whether this service should keep exact hostnames in an output profile."""
    if svc_data.get("preserve_subdomains", False):
        return True

    if svc_data.get("group") in profile.get("force_exact_groups", set()):
        return True

    return service_id in profile.get("force_exact_services", set())


def format_output_label(format_name: str, preserve_subdomains: bool) -> str:
    """Return a human-readable note describing how one output is encoded."""
    if format_name == "rpz":
        if preserve_subdomains:
            return "; Format: RPZ (exact hostnames preserved)"
        return "; Format: RPZ (registrable domains plus wildcard subdomains)"

    if preserve_subdomains:
        return "# Format: Hosts file (0.0.0.0 hostname) - exact hostnames preserved"
    return "# Format: Hosts file (0.0.0.0 domain.com) - blocks all subdomains"


def humanize_service_name(service_id: str) -> str:
    """Convert a service id into a readable display name."""
    return service_id.replace("_", " ").replace("-", " ").title()


def get_category_anchor(group: str) -> str:
    """Return the markdown anchor used for a category section heading."""
    return "#" + group.replace("_", "-")


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


def get_brand_key_from_root_domain(root_domain: str) -> str:
    """Return the left-hand brand label for a registrable domain."""
    labels = [label for label in root_domain.lower().strip(".").split(".") if label]
    if not labels:
        return ""

    public_suffix = get_public_suffix(root_domain)
    suffix_labels = public_suffix.split(".") if public_suffix else [labels[-1]]
    if len(labels) <= len(suffix_labels):
        return labels[0]

    return ".".join(labels[: len(labels) - len(suffix_labels)])


def get_shadowwhisperer_dating_override(brand_key: str) -> Optional[Dict[str, str]]:
    """Return an explicit dating service mapping for imported discovery domains."""
    override = SHADOWWHISPERER_DATING_OVERRIDES.get(brand_key)
    if override:
        return override

    for pattern, pattern_override in SHADOWWHISPERER_DATING_PATTERN_OVERRIDES:
        if pattern.match(brand_key):
            return pattern_override

    return None


def build_shadowwhisperer_numeric_family_overrides(domains: Set[str]) -> Dict[str, Dict[str, str]]:
    """
    Build source-scoped overrides for numbered dating-domain families.

    This lets imported discovery feeds collapse obvious shard families like
    `dial01.fr` through `dial95.fr` into one local service record without
    applying broad regex merging across unrelated categories.
    """
    family_members: Dict[str, Set[str]] = defaultdict(set)

    for domain in domains:
        root_domain = get_root_domain(domain)
        brand_key = get_brand_key_from_root_domain(root_domain)
        if not brand_key:
            continue

        if SHADOWWHISPERER_DATING_OVERRIDES.get(brand_key):
            continue
        if any(pattern.match(brand_key) for pattern, _ in SHADOWWHISPERER_DATING_PATTERN_OVERRIDES):
            continue

        match = SHADOWWHISPERER_DATING_NUMERIC_FAMILY_REGEX.match(brand_key)
        if not match:
            continue

        family_members[match.group("base")].add(brand_key)

    overrides: Dict[str, Dict[str, str]] = {}
    for base_key, members in family_members.items():
        if len(members) < SHADOWWHISPERER_DATING_NUMERIC_FAMILY_MIN_SIBLINGS:
            continue

        service_id = re.sub(r"[^a-z0-9]+", "_", base_key.lower()).strip("_")
        if not service_id:
            continue

        override = {"service_id": service_id, "name": humanize_service_name(service_id)}
        for member in members:
            overrides[member] = override

    return overrides


def get_unique_service_id(
    services_by_target: Dict,
    service_id: str,
    group: str,
) -> str:
    """Return a service id that will not collide with another category."""
    existing_group = services_by_target[service_id]["group"]
    if not existing_group or existing_group == group:
        return service_id

    candidate = f"{group}_{service_id}"
    if not services_by_target[candidate]["group"] or services_by_target[candidate]["group"] == group:
        return candidate

    counter = 2
    while True:
        candidate = f"{group}_{service_id}_{counter}"
        if not services_by_target[candidate]["group"] or services_by_target[candidate]["group"] == group:
            return candidate
        counter += 1


def add_shadowwhisperer_dating_domains(
    services_by_target: Dict,
    domains: Set[str],
) -> int:
    """
    Expand imported dating domains into per-service records.

    The dating feed is used as discovery input, but the repo should expose
    dating services uniformly as individual service files instead of a single
    upstream-branded source file.
    """
    added_roots = 0
    numeric_family_overrides = build_shadowwhisperer_numeric_family_overrides(domains)

    for domain in domains:
        root_domain = get_root_domain(domain)
        brand_key = get_brand_key_from_root_domain(root_domain)
        if not brand_key:
            continue

        override = get_shadowwhisperer_dating_override(brand_key)
        if not override:
            override = numeric_family_overrides.get(brand_key)
        if override:
            service_id = override["service_id"]
            display_name = override["name"]
        else:
            service_id = re.sub(r"[^a-z0-9]+", "_", brand_key.lower()).strip("_")
            if not service_id:
                continue
            display_name = humanize_service_name(service_id)

        service_id = get_unique_service_id(services_by_target, service_id, "dating")
        services_by_target[service_id]["group"] = "dating"
        if not services_by_target[service_id]["name"]:
            services_by_target[service_id]["name"] = display_name
        services_by_target[service_id]["domains"].add(root_domain)
        added_roots += 1

    return added_roots


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

        forbid_public_suffix_entries = effective_policy.get("forbid_public_suffix_entries", True)
        exclude_exact = set(effective_policy.get("exclude_exact", []))
        exclude_suffix = effective_policy.get("exclude_suffix", [])
        if not forbid_public_suffix_entries and not exclude_exact and not exclude_suffix:
            continue

        filtered_domains = set()
        removed_domains = []

        for domain in domains:
            candidate = domain.lower().strip(".")
            if forbid_public_suffix_entries:
                public_suffix = get_public_suffix(candidate)
                if public_suffix and candidate == public_suffix:
                    removed_domains.append(candidate)
                    continue
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
    sorted_domains = normalize_domains(domains, preserve_subdomains)
    
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


def normalize_domains(domains: Set[str], preserve_subdomains: bool = False) -> List[str]:
    """Normalize domains for an output profile and return a sorted unique list."""
    normalized_domains = set()
    for domain in domains:
        candidate = domain.lower().strip(".")
        if not candidate:
            continue
        if preserve_subdomains:
            normalized_domains.add(candidate)
        else:
            normalized_domains.add(get_root_domain(candidate))

    return sorted(normalized_domains)


def write_rpz_file(
    path: Path,
    domains: Set[str],
    header: Optional[str] = None,
    preserve_subdomains: bool = False,
) -> tuple:
    """
    Write domains to a compact RPZ zone file.

    Exact-host profiles emit one `CNAME .` rule per hostname. Registrable-domain
    profiles also emit a wildcard rule so subdomains are covered in RPZ-aware
    resolvers.
    """
    ensure_dir(path.parent)
    sorted_domains = normalize_domains(domains, preserve_subdomains)
    serial = datetime.utcnow().strftime("%Y%m%d%H")

    lines = []
    if header:
        for raw_line in header.rstrip().splitlines():
            stripped = raw_line.lstrip("#; ").rstrip()
            lines.append(f"; {stripped}" if stripped else ";")
        lines.append("")

    lines.extend(
        [
            "$TTL 300",
            f"@ 300 IN SOA localhost. root.localhost. {serial} 3600 900 1209600 300",
            "@ 300 IN NS localhost.",
            "",
        ]
    )

    for domain in sorted_domains:
        lines.append(f"{domain} CNAME .")
        if not preserve_subdomains:
            lines.append(f"*.{domain} CNAME .")

    content = "\n".join(lines) + "\n"
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
def clear_profile_outputs(profile_name: str) -> None:
    """Remove previously generated files for one output profile."""
    profile = get_output_profile(profile_name)
    ensure_dir(profile["lists_dir"])
    ensure_dir(profile["categories_dir"])
    ensure_dir(profile["recommended_dir"])

    pattern = f"*{profile['file_extension']}"
    for path in profile["lists_dir"].rglob(pattern):
        path.unlink()
    for path in profile["categories_dir"].glob(pattern):
        path.unlink()
    for path in profile["recommended_dir"].glob(pattern):
        path.unlink()


def write_output_file(
    profile: Dict[str, object],
    path: Path,
    domains: Set[str],
    header: Optional[str],
    preserve_subdomains: bool,
) -> tuple:
    """Dispatch to the correct writer for one output profile."""
    if profile["format"] == "rpz":
        return write_rpz_file(path, domains, header, preserve_subdomains=preserve_subdomains)

    return write_domain_file(path, domains, header, preserve_subdomains=preserve_subdomains)


def get_raw_url(path: Path) -> str:
    """Return the raw GitHub URL for a repo-relative file path."""
    rel_path = path.as_posix()
    return f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{rel_path}"


def get_quality_report_link(profile: Dict[str, object]) -> str:
    """Return the README-local link to the profile quality report."""
    return profile["quality_report_path"].relative_to(profile["base_dir"]).as_posix()


def get_bundle_group_labels(groups: List[str]) -> str:
    """Return a readable comma-separated category label list for a bundle."""
    labels = []
    for group in groups:
        meta = OUTPUT_CATEGORY_META.get(group, {"label": group.replace("_", " ").title()})
        labels.append(meta["label"])
    return ", ".join(labels)


def generate_recommended_bundles(
    profile_name: str,
    timestamp: str,
    category_domains: Dict[str, Set[str]],
    category_preserve_subdomains: Dict[str, bool],
) -> List[Dict[str, object]]:
    """Generate recommended starter bundles for one output profile."""
    profile = get_output_profile(profile_name)
    bundle_stats: List[Dict[str, object]] = []
    bundles = profile.get("recommended_bundles", [])
    if not bundles:
        return bundle_stats

    extension = profile["file_extension"]
    comment_prefix = ";" if profile["format"] == "rpz" else "#"

    for bundle in bundles:
        selected_groups = [group for group in bundle["groups"] if group in category_domains]
        if not selected_groups:
            continue

        bundle_domains: Set[str] = set()
        for group in selected_groups:
            bundle_domains.update(category_domains[group])

        preserve_subdomains = bundle.get(
            "preserve_subdomains",
            any(category_preserve_subdomains.get(group, False) for group in selected_groups),
        )
        out_path = profile["recommended_dir"] / f"{bundle['bundle_id']}{extension}"
        format_line = format_output_label(profile["format"], preserve_subdomains)
        header = (
            f"{comment_prefix} {bundle['name']}\n"
            f"{comment_prefix} Generated: {timestamp}\n"
            f"{format_line}\n"
            f"{comment_prefix} Included categories: {', '.join(selected_groups)}\n"
            f"{comment_prefix} Original domains (before deduplication): {len(bundle_domains)}"
        )

        try:
            count, size_mb = write_output_file(
                profile,
                out_path,
                bundle_domains,
                header,
                preserve_subdomains=preserve_subdomains,
            )
            logger.info("✓ %s — %d entries (%.2fMB)", out_path, count, size_mb)
        except ValueError as e:
            logger.warning("Skipped %s: %s", out_path, e)
            continue
        except Exception as e:
            logger.error("Error writing %s: %s", out_path, e)
            continue

        bundle_stats.append(
            {
                "bundle_id": bundle["bundle_id"],
                "name": bundle["name"],
                "best_for": bundle["best_for"],
                "description": bundle["description"],
                "groups": selected_groups,
                "domains": count,
                "path": out_path,
            }
        )

    return bundle_stats


def build_profile_readme(
    profile_name: str,
    timestamp: str,
    service_stats: List[Dict],
    category_stats: List[Dict],
    bundle_stats: List[Dict[str, object]],
) -> None:
    """Write the README for one generated output profile."""
    profile = get_output_profile(profile_name)
    base_dir = profile["base_dir"]
    readme_path = profile["readme_path"]
    count_label = "Root Domains" if profile_name == "services" else "Entries"
    lines = []

    lines.append(f"# {profile['title']}\n")
    lines.append(f"**Generated:** {timestamp}\n")
    lines.append(f"**Audience:** {profile['audience']}\n")
    lines.append(f"**False-Positive Risk:** {profile['risk']}\n")
    lines.append(profile["summary"] + "\n")

    lines.append("## Output Tiers\n")
    lines.append("- **[services](../services/README.md)** - home-safe, registrable-domain blocklists")
    lines.append("- **[security](../security/README.md)** - exact-host security blocklists")
    lines.append("- **[rpz](../rpz/README.md)** - Unbound-friendly RPZ policies")
    lines.append("- **[hardening](../hardening/README.md)** - DNSTwist-derived brand impersonation blocklists")
    lines.append("- **[active impersonation review](../hardening/active_impersonation/README.md)** - scored live-lookalike review reports\n")

    lines.append(f"## {profile['quick_start_title']}\n")
    lines.append(profile["quick_start_body"] + "\n")

    if bundle_stats:
        lines.append("## Recommended Entry Points\n")
        lines.append("Use these starter bundles if you want a fast, opinionated default instead of picking categories one by one.\n")
        lines.append(f"| Bundle | Best For | {count_label} | Includes | File | Raw URL |")
        lines.append("|--------|----------|---------|----------|------|---------|")
        for bundle in bundle_stats:
            rel_path = bundle["path"].relative_to(base_dir)
            raw_url = get_raw_url(bundle["path"])
            lines.append(
                f"| **{bundle['name']}** | {bundle['best_for']} | {bundle['domains']:,} | "
                f"{get_bundle_group_labels(bundle['groups'])} | "
                f"[{rel_path.name}]({rel_path.as_posix()}) | [Raw]({raw_url}) |"
            )
        lines.append("")

    lines.append("## Why Trust This Layer\n")
    lines.append("- Public Suffix List-aware domain normalization prevents bad roots like `co.uk` from leaking into generated outputs")
    lines.append("- Repo-local source policies remove noisy shared infrastructure and known false-positive patterns before lists are written")
    lines.append(f"- Validation reports are published at [{profile['quality_report_path'].name}]({get_quality_report_link(profile)}) and check syntax, exclusions, and count drift")
    lines.append("- Standard, exact-host, and RPZ outputs are generated from the same source graph so the repo stays internally consistent\n")

    lines.append("## Aggregated Categories\n")
    lines.append(profile["category_intro"] + "\n")
    lines.append(f"| Category | {count_label} | Sources | File | Raw URL |")
    lines.append("|----------|---------|---------|------|---------|")

    category_source_counts = defaultdict(int)
    for svc in service_stats:
        category_source_counts[svc["group"]] += 1

    for category in sorted(category_stats, key=lambda item: item["group"]):
        group = category["group"]
        meta = OUTPUT_CATEGORY_META.get(group, {"emoji": "📁", "label": group.replace("_", " ").title()})
        rel_path = category["path"].relative_to(base_dir)
        raw_url = get_raw_url(category["path"])
        lines.append(
            f"| [{meta['emoji']} {meta['label']}]({get_category_anchor(group)}) | {category['domains']:,} | "
            f"{category_source_counts[group]} | [{rel_path.name}]({rel_path.as_posix()}) | [Raw]({raw_url}) |"
        )

    lines.append("")
    lines.append("## Individual Sources\n")
    lines.append(profile["advanced_intro"] + "\n")

    services_by_category = defaultdict(list)
    for svc in sorted(service_stats, key=lambda item: (item["group"], item["name"])):
        services_by_category[svc["group"]].append(svc)

    for group in sorted(services_by_category.keys()):
        meta = OUTPUT_CATEGORY_META.get(group, {"label": group.replace("_", " ").title()})
        lines.append(f"### {meta['label']}\n")
        lines.append(f"| Source | {count_label} | File | Raw URL |")
        lines.append("|--------|---------|------|---------|")
        for svc in services_by_category[group]:
            rel_path = svc["path"].relative_to(base_dir)
            raw_url = get_raw_url(svc["path"])
            lines.append(
                f"| {svc['name']} | {svc['domains']:,} | "
                f"[{rel_path.name}]({rel_path.as_posix()}) | [Raw]({raw_url}) |"
            )
        lines.append("")

    lines.append("## Usage\n")
    lines.extend(profile["usage"])
    lines.append("")

    lines.append("## Format Details\n")
    for note in profile["format_notes"]:
        lines.append(f"- {note}")
    lines.append("")

    lines.append("## Data Sources\n")
    lines.append("- **[AdGuard](https://adguard.com/)** - service blocklists for social media, gaming, streaming, and more")
    lines.append("- **[Phishing Army](https://phishing.army/)** - active phishing domains")
    lines.append("- **[OpenPhish](https://openphish.com/)** - phishing URLs converted to exact hosts")
    lines.append("- **[PhishTank](https://phishtank.org/)** - verified phishing URLs converted to exact hosts")
    lines.append("- **[ThreatFox](https://threatfox.abuse.ch/)** - malware indicators from abuse.ch")
    lines.append("- **[URLhaus](https://urlhaus.abuse.ch/)** - malware distribution URLs converted to exact hosts")
    lines.append("- **[The Block List Project](https://github.com/blocklistproject/Lists)** - curated category feeds for abuse, crypto, drugs, piracy, redirects, smart TV, torrent, tracking, vaping, and more")
    lines.append("- **[HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists)** - dynamic DNS, badware hoster, fake-domain, DNS-bypass, and URL-shortener feeds")
    lines.append("- **[UKLANS cache-domains](https://github.com/uklans/cache-domains)** - gaming CDN/cache hostnames")
    lines.append("- **[StevenBlack](https://github.com/StevenBlack/hosts)** and **[Chad Mayfield](https://github.com/chadmayfield/my-pihole-blocklists)** - adult-content feeds\n")

    lines.append("## Notes\n")
    lines.append("- Start with the recommended bundles if you want the fewest decisions")
    lines.append("- Move to aggregated categories when you want control without going fully source-by-source")
    lines.append("- Whitelist when needed and watch your resolver logs after major changes")
    lines.append("- Exact-host security and RPZ layers are more aggressive than the standard services layer")
    lines.append("- Source feeds change over time, so entry counts will drift\n")

    readme_path.write_text("\n".join(lines), encoding="utf-8")
    logger.info("README written to %s", readme_path)


def generate_profile_outputs(
    profile_name: str,
    services_by_target: Dict[str, Dict],
    timestamp: str,
) -> Dict[str, object]:
    """Generate files and README for one output profile."""
    profile = get_output_profile(profile_name)
    clear_profile_outputs(profile_name)

    logger.info("Writing %s outputs...", profile_name)
    service_stats = []
    category_domains = defaultdict(set)
    category_preserve_subdomains = defaultdict(bool)

    for service_id, svc_data in services_by_target.items():
        if not should_include_in_profile(service_id, svc_data, profile):
            continue

        group = svc_data["group"]
        name = svc_data["name"]
        domains = svc_data["domains"]
        preserve_subdomains = preserve_subdomains_for_profile(service_id, svc_data, profile)
        extension = profile["file_extension"]
        format_line = format_output_label(profile["format"], preserve_subdomains)
        comment_prefix = ";" if profile["format"] == "rpz" else "#"
        out_path = profile["lists_dir"] / group / f"{service_id}{extension}"
        header = (
            f"{comment_prefix} {name}\n"
            f"{comment_prefix} Category: {group}\n"
            f"{comment_prefix} Generated: {timestamp}\n"
            f"{format_line}\n"
            f"{comment_prefix} Original domains (before deduplication): {len(domains)}"
        )

        try:
            count, size_mb = write_output_file(
                profile,
                out_path,
                domains,
                header,
                preserve_subdomains=preserve_subdomains,
            )
            logger.info("✓ %s — %d entries (%.2fMB)", out_path, count, size_mb)
        except ValueError as e:
            logger.warning("Skipped %s: %s", out_path, e)
            continue
        except Exception as e:
            logger.error("Error writing %s: %s", out_path, e)
            continue

        service_stats.append(
            {
                "group": group,
                "service": service_id,
                "name": name,
                "domains": count,
                "path": out_path,
            }
        )
        category_domains[group].update(domains)
        category_preserve_subdomains[group] = (
            category_preserve_subdomains[group] or preserve_subdomains
        )

    logger.info("Writing %s category files...", profile_name)
    category_stats = []
    extension = profile["file_extension"]
    comment_prefix = ";" if profile["format"] == "rpz" else "#"

    for group, domains in sorted(category_domains.items()):
        preserve_subdomains = category_preserve_subdomains[group]
        out_path = profile["categories_dir"] / f"{group}{extension}"
        format_line = format_output_label(profile["format"], preserve_subdomains)
        header = (
            f"{comment_prefix} {group.replace('_', ' ').title()} Blocklist\n"
            f"{comment_prefix} Generated: {timestamp}\n"
            f"{format_line}\n"
            f"{comment_prefix} Original domains (before deduplication): {len(domains)}"
        )

        try:
            count, size_mb = write_output_file(
                profile,
                out_path,
                domains,
                header,
                preserve_subdomains=preserve_subdomains,
            )
            logger.info("✓ %s — %d entries (%.2fMB)", out_path, count, size_mb)
        except ValueError as e:
            logger.warning("Skipped %s: %s", out_path, e)
            continue
        except Exception as e:
            logger.error("Error writing %s: %s", out_path, e)
            continue

        category_stats.append({"group": group, "domains": count, "path": out_path})

    bundle_stats = generate_recommended_bundles(
        profile_name,
        timestamp,
        category_domains,
        category_preserve_subdomains,
    )
    build_profile_readme(profile_name, timestamp, service_stats, category_stats, bundle_stats)
    return {
        "service_stats": service_stats,
        "category_stats": category_stats,
        "bundle_stats": bundle_stats,
        "total_entries": sum(item["domains"] for item in category_stats),
    }


# -----------------------------
# Main Logic
# -----------------------------
def main():
    """Main execution function."""
    print("=" * 70)
    print("THREAT INTELLIGENCE BLOCKLIST GENERATOR")
    print("=" * 70)

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    # Dictionary to collect domains by target service/platform
    # Key: service name (e.g., "facebook", "tiktok", "emotet")
    # Value: {"group": category, "name": display_name, "domains": set()}
    services_by_target = defaultdict(make_service_record)
    
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
    
    # Phishing Army
    phishing_army_text = fetch_text(PHISHING_ARMY_URL)
    if phishing_army_text:
        pa_domains = extract_domains_from_adblock(phishing_army_text)
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
            "service_id": "shadowwhisperer_dating",
            "group": "dating",
            "name": "ShadowWhisperer Dating",
            "url": SHADOWWHISPERER_DATING_URL,
            "extractor": extract_domains_from_plain_list,
            "split_into_services": True,
        },
        {
            "service_id": "blp_abuse",
            "group": "abuse",
            "name": "Block List Project Abuse",
            "url": BLOCKLISTPROJECT_ABUSE_URL,
            "extractor": extract_domains_from_hosts_file,
        },
        {
            "service_id": "blp_crypto",
            "group": "crypto",
            "name": "Block List Project Crypto",
            "url": BLOCKLISTPROJECT_CRYPTO_URL,
            "extractor": extract_domains_from_hosts_file,
        },
        {
            "service_id": "blp_drugs",
            "group": "drugs",
            "name": "Block List Project Drugs",
            "url": BLOCKLISTPROJECT_DRUGS_URL,
            "extractor": extract_domains_from_hosts_file,
        },
        {
            "service_id": "blp_piracy",
            "group": "piracy",
            "name": "Block List Project Piracy",
            "url": BLOCKLISTPROJECT_PIRACY_URL,
            "extractor": extract_domains_from_hosts_file,
        },
        {
            "service_id": "blp_redirect",
            "group": "redirect",
            "name": "Block List Project Redirect",
            "url": BLOCKLISTPROJECT_REDIRECT_URL,
            "extractor": extract_domains_from_hosts_file,
        },
        {
            "service_id": "blp_scam",
            "group": "scam",
            "name": "Block List Project Scam",
            "url": BLOCKLISTPROJECT_SCAM_URL,
            "extractor": extract_domains_from_hosts_file,
        },
        {
            "service_id": "blp_smart_tv",
            "group": "smart_tv",
            "name": "Block List Project Smart TV",
            "url": BLOCKLISTPROJECT_SMART_TV_URL,
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
            "service_id": "blp_torrent",
            "group": "torrent",
            "name": "Block List Project Torrent",
            "url": BLOCKLISTPROJECT_TORRENT_URL,
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
            "service_id": "blp_vaping",
            "group": "vaping",
            "name": "Block List Project Vaping",
            "url": BLOCKLISTPROJECT_VAPING_URL,
            "extractor": extract_domains_from_hosts_file,
        },
        {
            "service_id": "hagezi_doh_vpn_proxy_bypass",
            "group": "dns_bypass",
            "name": "HaGeZi DoH VPN Proxy Bypass",
            "url": HAGEZI_DOH_VPN_PROXY_BYPASS_URL,
            "extractor": extract_domains_from_plain_list,
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
        {
            "service_id": "hagezi_urlshortener",
            "group": "url_shortener",
            "name": "HaGeZi URL Shortener",
            "url": HAGEZI_URLSHORTENER_URL,
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

        if feed.get("split_into_services"):
            added_domains = add_shadowwhisperer_dating_domains(services_by_target, feed_domains)
            logger.info(
                "%s: expanded %d raw domains into dating service files",
                feed["name"],
                added_domains,
            )
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
    # GENERATE ALL OUTPUT TIERS
    # -----------------------------
    profile_summaries = {}
    for profile_name in OUTPUT_PROFILES:
        profile_summaries[profile_name] = generate_profile_outputs(
            profile_name,
            services_by_target,
            timestamp,
        )

    print("\n" + "=" * 70)
    print("✅ UPDATE COMPLETE!")
    print("=" * 70)
    for profile_name, summary in profile_summaries.items():
        print(
            f"{profile_name}: {len(summary['service_stats'])} sources, "
            f"{len(summary['category_stats'])} categories, "
            f"{summary['total_entries']:,} entries"
        )
    print("=" * 70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("\nOperation cancelled by user")
    except Exception as e:
        logger.exception(f"Fatal error: {e}")
        raise
