#!/usr/bin/env python3
"""
Generate service blocklists from AdGuard Hostlists Registry
Compatible with Pi-hole and AdGuard Home
"""

import requests
import json
import os
from datetime import datetime
from pathlib import Path
import re

def main():
    # Fetch the services.json file
    url = "https://adguardteam.github.io/HostlistsRegistry/assets/services.json"
    print(f"Fetching services from {url}...")
    
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    # The JSON structure uses "blocked_services" key
    if isinstance(data, dict) and 'blocked_services' in data:
        services = data['blocked_services']
    elif isinstance(data, list):
        services = data
    else:
        raise ValueError(f"Unexpected JSON structure. Keys: {data.keys() if isinstance(data, dict) else 'not a dict'}")
    
    print(f"Found {len(services)} services")

    # Create services directory
    os.makedirs("services", exist_ok=True)

    # Generate timestamp
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    # Process each service
    services_processed = 0
    for idx, service in enumerate(services):
        # Validate service is a dictionary
        if not isinstance(service, dict):
            print(f"Warning: Skipping service at index {idx} - not a dictionary: {type(service)}")
            continue
            
        service_id = service.get('id', 'unknown')
        service_name = service.get('name', 'Unknown Service')
        rules = service.get('rules', [])
        
        if not rules:
            continue
        
        # Convert AdGuard rules to domain format
        # Rules like "||example.com^" need to be converted to "example.com"
        domains = []
        for rule in rules:
            # Remove AdGuard syntax: ||domain^ -> domain
            domain = rule.strip()
            if domain.startswith('||'):
                domain = domain[2:]
            if domain.endswith('^'):
                domain = domain[:-1]
            if domain:  # Only add non-empty domains
                domains.append(domain)
        
        if not domains:
            continue
        
        # Create filename (sanitize service_id for filename)
        filename = f"services/{service_id}.txt"
        
        # Write blocklist file
        with open(filename, 'w', encoding='utf-8') as f:
            # Header compatible with both Pi-hole and AdGuard
            f.write(f"# {service_name} Blocklist\n")
            f.write(f"# Service ID: {service_id}\n")
            f.write(f"# Generated: {timestamp}\n")
            f.write(f"# Total domains: {len(domains)}\n")
            f.write(f"#\n")
            f.write(f"# Compatible with Pi-hole and AdGuard Home\n")
            f.write(f"#\n\n")


            service['domains'] = domains
            # Write domains (one per line, Pi-hole/AdGuard format)
            for domain in sorted(domains):
                f.write(f"{domain}\n")
        
        services_processed += 1
        print(f"Generated {filename} with {len(domains)} domains")

    # Get repository info from environment
    repo = os.environ.get('GITHUB_REPOSITORY', 'YOUR_USERNAME/YOUR_REPO')
    
    
    
    # Generate the services table
    table_rows = []
    for service in sorted(services, key=lambda x: x.get('name', '')):
        service_id = service.get('id', 'unknown')
        service_name = service.get('name', 'Unknown')
        domain_count = len(service.get('domains', []))
        
        if domain_count > 0:
            raw_url = f"https://raw.githubusercontent.com/{repo}/main/services/{service_id}.txt"
            table_rows.append(f"| {service_name} | {domain_count} | [{service_id}.txt]({service_id}.txt) | [Raw]({raw_url}) |")
    
    # Build the new section
    new_section = f"""<!-- START:services -->
    *(auto-generated section — do not edit manually)*
    
    Generated: {timestamp}
    
    | Service | Domains | File | Raw URL |
    |---------|---------|------|----------|
    {chr(10).join(table_rows)}
    <!-- END:services -->"""
    
    # Update the README
    readme_path = Path("README.md")
    content = readme_path.read_text(encoding='utf-8')
    
    section_start = "<!-- START:services -->"
    section_end = "<!-- END:services -->"
    
    # Replace only the services section
    updated = re.sub(
        f"{re.escape(section_start)}.*?{re.escape(section_end)}",
        new_section,
        content,
        flags=re.DOTALL
    )
    
    readme_path.write_text(updated, encoding='utf-8')

    print(f"\nTotal services processed: {services_processed}")


if __name__ == "__main__":

    main()

