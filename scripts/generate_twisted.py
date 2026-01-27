import json
import os
import subprocess
import logging
import re

# Configure logging for clear GitHub Action feedback
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)

SERVICES_JSON = 'services.json'
LISTS_DIR = 'services/lists'

# Groups to ignore (Malware/Phishing/etc.)
EXCLUDED_GROUPS = ['malware', 'phishing', 'scam', 'security']

def clean_domain(rule):
    """Converts AdGuard style ||domain.com^ to domain.com"""
    return re.sub(r'[|\\^]', '', rule)

def run_dnstwist(domain):
    """Runs dnstwist with registered and MX checks."""
    logging.info(f"    --> Twisting: {domain}")
    try:
        # --mxcheck: filters for domains that can actually receive/send mail
        # --registered: filters for domains that actually resolve
        result = subprocess.run(
            ['dnstwist', '--registered', '--mxcheck', '--format', 'list', domain],
            capture_output=True, text=True, timeout=240
        )
        
        variations = result.stdout.splitlines()

        # 1. Brand Isolation: Remove the original domain so it doesn't end up in the 'twisted' list
        if domain in variations:
            variations.remove(domain)

        # 2. Wildcard Protection: If a domain returns an insane number of results, it's a false positive
        if len(variations) > 400:
            logging.warning(f"    [!] Wildcard DNS detected for {domain} ({len(variations)} vars). Skipping.")
            return []

        logging.info(f"    --> Found {len(variations)} active variations.")
        return variations

    except subprocess.TimeoutExpired:
        logging.error(f"    [!] Timeout on {domain}. Skipping.")
        return []
    except Exception as e:
        logging.error(f"    [!] Error on {domain}: {str(e)}")
        return []

# --- Main Logic ---

if not os.path.exists(SERVICES_JSON):
    logging.error(f"File not found: {SERVICES_JSON}")
    exit(1)

with open(SERVICES_JSON, 'r') as f:
    data = json.load(f)

# Use the 'blocked_services' key from your JSON snippet
services = data.get("blocked_services", [])
logging.info(f"Starting twist generation for {len(services)} services...")

for service in services:
    name = service.get("name")
    group = service.get("group")
    rules = service.get("rules", [])

    # Skip Malware/Phishing/etc.
    if group in EXCLUDED_GROUPS:
        logging.info(f"[-] Skipping {name}: Group '{group}' is in excluded list.")
        continue

    logging.info(f"[+] Processing {name} (Group: {group})")
    
    service_twisted_domains = set()
    for rule in rules:
        domain = clean_domain(rule)
        if domain:
            found_vars = run_dnstwist(domain)
            service_twisted_domains.update(found_vars)

    # Save to a dedicated _twisted.txt file
    if service_twisted_domains:
        output_file = os.path.join(LISTS_DIR, f"{name}_twisted.txt")
        with open(output_file, 'w') as f:
            f.write('\n'.join(sorted(service_twisted_domains)))
        logging.info(f"    [SUCCESS] Saved {len(service_twisted_domains)} domains to {output_file}")
    else:
        logging.info(f"    [INFO] No active twisted domains found for {name}.")

logging.info("Twisted domain generation complete.")
