#!/usr/bin/env python3
"""
Generate per-provider tunneling lists:
  - VPN providers
  - Proxy providers
  - Aggregated all.txt
Sources:
  - az0 vpn_ip public hostname.txt
  - az0 proxy.txt
  - Cisco Umbrella top domains
"""

import requests
from pathlib import Path
import re
import csv
from io import StringIO, BytesIO
import zipfile
import os
from datetime import datetime
# === Configuration ===
TUNNELING_DIR = Path("tunneling")
TUNNELING_DIR.mkdir(exist_ok=True)

# === Sources ===
AZ0_VPN = "https://az0-vpnip-public.oooninja.com/hostname.txt"
AZ0_PROXY = "https://raw.githubusercontent.com/az0/vpn_ip/main/data/input/hostname_only/proxy.txt"
UMBRELLA_TOP_DOMAINS = "http://s3-us-west-1.amazonaws.com/umbrella-static/top-1m.csv.zip"

# === Filters ===
EXCLUDE_KEYWORDS = ["aws-proxy", "gcp-proxy", "internal-proxy"]
PROXY_KEYWORDS = ["proxy", "prox", "tunnel", "socks"]
VPN_KEYWORDS = ["vpn", "wireguard", "expressvpn", "nordvpn", "privatevpn", "surfshark", "hide", "securevpn"]

# === Helpers ===
def get_provider(domain: str) -> str:
    """Extract provider name from domain"""
    parts = domain.split(".")
    provider_candidate = parts[-2] if len(parts) >= 2 else parts[0]
    return re.sub(r"[^a-z0-9]", "", provider_candidate.lower())

def domain_matches_keywords(domain: str, keywords: list[str]) -> bool:
    """Check if a domain contains at least one of the given keywords and no excluded ones"""
    domain_lower = domain.lower()
    if not any(k in domain_lower for k in keywords):
        return False
    if any(exclude in domain_lower for exclude in EXCLUDE_KEYWORDS):
        return False
    return True

def fetch_list(url: str) -> list[str]:
    """Download a simple text list"""
    print(f"Fetching: {url}")
    resp = requests.get(url)
    resp.raise_for_status()
    return [line.strip() for line in resp.text.splitlines() if line.strip()]

# === Fetch Sources ===

# 1. VPN list
vpn_domains = set(fetch_list(AZ0_VPN))
print(f"Fetched {len(vpn_domains)} VPN domains from az0.")

# 2. Proxy list
proxy_domains = set(fetch_list(AZ0_PROXY))
print(f"Fetched {len(proxy_domains)} proxy domains from az0.")

# 3. Umbrella filtering for proxies
print("Fetching Umbrella top domains...")
resp = requests.get(UMBRELLA_TOP_DOMAINS)
resp.raise_for_status()

with zipfile.ZipFile(BytesIO(resp.content)) as z:
    csv_files = z.namelist()
    if not csv_files:
        raise ValueError("No CSV found in Umbrella zip")
    with z.open(csv_files[0]) as f:
        csv_text = f.read().decode()
        reader = csv.reader(StringIO(csv_text))
        umbrella_proxies = set()
        umbrella_vpns = set()

        for row in reader:
            if len(row) > 1:
                domain = row[1].strip().lower()
                # Check separately
                if domain_matches_keywords(domain, PROXY_KEYWORDS):
                    umbrella_proxies.add(domain)
                elif domain_matches_keywords(domain, VPN_KEYWORDS):
                    umbrella_vpns.add(domain)

print(f"Umbrella matched {len(umbrella_proxies)} proxy-like domains.")
print(f"Umbrella matched {len(umbrella_vpns)} vpn-like domains.")
# === Combine sources ===
all_proxies = proxy_domains | set(umbrella_proxies)
all_vpns = vpn_domains | set(umbrella_vpns)
print(f"Total {len(all_proxies)} proxy domains, {len(all_vpns)} VPN domains.")

# === Write output ===
def write_per_provider(domains: set[str], prefix: str):
    providers = {}
    for domain in domains:
        provider = get_provider(domain)
        providers.setdefault(provider, set()).add(domain)

    for provider, items in providers.items():
        filename = TUNNELING_DIR / prefix / f"{prefix}_{provider}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for d in sorted(items):
                f.write(f"{d}\n")
        print(f"Wrote {len(items):>4} domains to {filename.name}")

# Per-provider lists
write_per_provider(all_proxies, "proxy")
write_per_provider(all_vpns, "vpn")

# === Aggregated lists ===
all_proxy_file = TUNNELING_DIR / "proxies.txt"
all_vpn_file = TUNNELING_DIR / "vpns.txt"   # <-- renamed from vpns.txt

with open(all_proxy_file, "w", encoding="utf-8") as f:
    for d in sorted(all_proxies):
        f.write(f"{d}\n")

with open(all_vpn_file, "w", encoding="utf-8") as f:
    for d in sorted(all_vpns):
        f.write(f"{d}\n")

print(f"Aggregated {len(all_proxies)} proxies → {all_proxy_file}")
print(f"Aggregated {len(all_vpns)} VPNs → {all_vpn_file}")

print("✅ Completed tunneling list generation.")

# Get repository info from environment
repo = os.environ.get('GITHUB_REPOSITORY', 'YOUR_USERNAME/YOUR_REPO')
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

# Build table rows for tunneling files
table_rows = []
for f in sorted(TUNNELING_DIR.glob("*.txt")):
    name = f.stem
    entry_count = sum(1 for _ in open(f, encoding="utf-8"))
    raw_url = f"https://raw.githubusercontent.com/{repo}/main/{TUNNELING_DIR}/{f.name}"
    table_rows.append(
        f"| {name} | {entry_count} | [{f.name}]({TUNNELING_DIR}/{f.name}) | [Raw]({raw_url}) |"
    )
# Build the new README section
new_section = f"""<!-- START:tunneling -->
*(auto-generated section — do not edit manually)*

Generated: {timestamp}

| List | Entries | File | Raw URL |
|------|----------|------|---------|
{chr(10).join(table_rows)}
<!-- END:tunneling -->"""

# Update README.md
readme_path = Path("tunneling/README.md")
if readme_path.exists():
    content = readme_path.read_text(encoding="utf-8")
    section_start = "<!-- START:tunneling -->"
    section_end = "<!-- END:tunneling -->"

    updated = re.sub(
        f"{re.escape(section_start)}.*?{re.escape(section_end)}",
        new_section,
        content,
        flags=re.DOTALL
    )
    readme_path.write_text(updated, encoding="utf-8")
    print("✅ Updated tunneling section in README.md")
else:
    print("⚠️ No README.md found — skipping update.")
