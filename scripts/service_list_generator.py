#!/usr/bin/env python3
"""
Generate service blocklists from AdGuard Hostlists Registry
Compatible with Pi-hole and AdGuard Home

Notes:
- Blocklist files are written to services/lists/
- README links (File / Raw URL columns) point to services/links/ (per request)
  If you want the generated files to be written to services/links/ instead,
  change the `lists_dir` variable below or let me know.

Changes:
- Category files are now cleared and regenerated fresh each run (no more duplicates)
- Added 100MB size check for all output files to prevent GitHub errors
"""
import requests
import json
import os
from datetime import datetime
from pathlib import Path
import re

MAX_FILE_SIZE_MB = 100

def check_file_size(filepath, content, max_mb=MAX_FILE_SIZE_MB):
    """Check if content would exceed size limit"""
    size_mb = len(content.encode('utf-8')) / (1024 * 1024)
    if size_mb > max_mb:
        raise ValueError(
            f"ERROR: {filepath.name} would be {size_mb:.2f}MB, "
            f"exceeding {max_mb}MB GitHub limit. "
            f"Contains {content.count(chr(10))} lines."
        )
    return size_mb

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
    print(f"Loading Local Services")
    with open("services.json") as f:
        local_services = json.load(f)

    if isinstance(local_services, dict) and 'blocked_services' in local_services:
        local_services = local_services['blocked_services']
    elif not isinstance(local_services, list):
        raise ValueError(f"Unexpected JSON structure in local file. Keys: {local_services.keys() if isinstance(local_services, dict) else 'not a dict'}")

    # Avoid duplicates based on 'name'
    existing_names = {service.get("name") for service in services}
    for service in local_services:
        if service.get("name") not in existing_names:
            services.append(service)

    # If original structure was dict, keep that shape
    if isinstance(data, dict) and 'blocked_services' in data:
        data['blocked_services'] = services
    else:
        data = services
    print(f"Found {len(services)} services")

    # Directories (you can change lists_dir to 'links' if you want files written there)
    lists_dir = Path("services/lists")
    categories_dir = Path("services/categories")
    links_dir = Path("services/links")  # README will reference this path for links/raw

    lists_dir.mkdir(parents=True, exist_ok=True)
    categories_dir.mkdir(parents=True, exist_ok=True)
    links_dir.mkdir(parents=True, exist_ok=True)  # create so links exist if you want to copy files later

    # CLEAR CATEGORY FILES - regenerate fresh each run to avoid duplicates
    print("Clearing old category files...")
    for cat_file in categories_dir.glob("*.txt"):
        cat_file.unlink()
        print(f"  Removed {cat_file.name}")

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    # Dictionary to accumulate category domains (for size checking before writing)
    category_domains = {}

    # Process each service
    services_processed = 0
    for idx, service in enumerate(services):
        if not isinstance(service, dict):
            print(f"Warning: Skipping service at index {idx} - not a dictionary: {type(service)}")
            continue
        service_id = service.get('id', 'unknown')
        service_name = service.get('name', 'Unknown Service')
        rules = service.get('rules', [])
        group = service.get('group', 'unknown')
        if not rules:
            continue
        
        domains = []
        for rule in rules:
            domain = rule.strip()
            if domain:
                domains.append(domain)
        
        if not domains:
            continue
        
        filename = lists_dir / f"{service_id}.txt"

        # Build service file content
        service_content = f"# {service_name} Blocklist\n"
        service_content += f"# Service ID: {service_id}\n"
        service_content += f"# Generated: {timestamp}\n"
        service_content += f"# Total domains: {len(domains)}\n"
        service_content += f"# Compatible with Pi-hole and AdGuard Home\n\n"
        service['domains'] = domains
        for domain in sorted(domains):
            service_content += f"{domain}\n"

        # Check size before writing individual service file
        try:
            size_mb = check_file_size(filename, service_content)
            with filename.open('w', encoding='utf-8') as f:
                f.write(service_content)
            services_processed += 1
            print(f"Generated {filename.name} with {len(domains)} domains ({size_mb:.2f}MB)")
        except ValueError as e:
            print(f"⚠️  SKIPPED {filename.name}: {e}")
            continue

        # Accumulate domains for category file (deduplicated)
        if group not in category_domains:
            category_domains[group] = set()
        category_domains[group].update(domains)

    # Write category files with size checking
    print("\nGenerating category files...")
    for category_name, domain_set in category_domains.items():
        grouping = categories_dir / f"{category_name}.txt"
        category_content = "\n".join(sorted(domain_set)) + "\n"
        
        try:
            size_mb = check_file_size(grouping, category_content)
            with grouping.open('w', encoding='utf-8') as f:
                f.write(category_content)
            print(f"Generated {grouping.name} with {len(domain_set)} unique domains ({size_mb:.2f}MB)")
        except ValueError as e:
            print(f"⚠️  SKIPPED {grouping.name}: {e}")
            # Create a warning file instead
            warning_file = categories_dir / f"{category_name}_TOO_LARGE.txt"
            with warning_file.open('w', encoding='utf-8') as f:
                f.write(f"# WARNING: This category exceeds {MAX_FILE_SIZE_MB}MB GitHub limit\n")
                f.write(f"# Total domains: {len(domain_set)}\n")
                f.write(f"# Estimated size: {len(category_content.encode('utf-8')) / (1024 * 1024):.2f}MB\n")
                f.write(f"# Generated: {timestamp}\n")
            print(f"   Created warning file: {warning_file.name}")

    repo = os.environ.get('GITHUB_REPOSITORY', 'YOUR_USERNAME/YOUR_REPO')
    
    ### CATEGORY SECTION (will be placed before Services in README) ###
    category_files = sorted(categories_dir.glob("*.txt"))
    category_rows = []
    for cat_file in category_files:
        category_name = cat_file.stem
        # Skip warning files in the table
        if category_name.endswith("_TOO_LARGE"):
            continue
        # Count non-empty lines (domains)
        with cat_file.open('r', encoding='utf-8') as fh:
            count = sum(1 for line in fh if line.strip())
        # Markdown link points to services/categories/<file>
        md_link = f"categories/{cat_file.name}"
        raw_url = f"https://raw.githubusercontent.com/{repo}/main/services/categories/{cat_file.name}"
        category_rows.append(f"| {category_name} | {count} | [{cat_file.name}]({md_link}) | [Raw]({raw_url}) |")

    new_categories_section = f"""<!-- START:categories -->
Generated: {timestamp}

| Category | Domains | File | Raw URL |
|-----------|----------|------|----------|
{chr(10).join(category_rows)}
<!-- END:categories -->"""

    ### SERVICE TABLE SECTION ###
    table_rows = []
    for service in sorted(services, key=lambda x: x.get('name', '')):
        service_id = service.get('id', 'unknown')
        service_name = service.get('name', 'Unknown')
        domain_count = len(service.get('domains', []))
        
        if domain_count > 0:
            # README "File" column points to services/links/{service_id}.txt per your request
            md_link = f"links/{service_id}.txt"
            raw_url = f"https://raw.githubusercontent.com/{repo}/main/services/links/{service_id}.txt"
            table_rows.append(f"| {service_name} | {domain_count} | [{service_id}.txt]({md_link}) | [Raw]({raw_url}) |")
    
    new_services_section = f"""<!-- START:services -->
Generated: {timestamp}

| Service | Domains | File | Raw URL |
|---------|---------|------|----------|
{chr(10).join(table_rows)}
<!-- END:services -->"""

    ### UPDATE README: categories first, then services ###
    readme_path = Path("services/README.md")
    if not readme_path.exists():
        # If README doesn't exist yet, create a skeleton with both sections
        base = f"# Services\n\n{new_categories_section}\n\n{new_services_section}\n"
        readme_path.write_text(base, encoding='utf-8')
        print("Created new services/README.md with categories and services sections.")
    else:
        content = readme_path.read_text(encoding='utf-8')

        # Replace or insert categories section first
        if "<!-- START:categories -->" in content and "<!-- END:categories -->" in content:
            content = re.sub(
                r"<!-- START:categories -->.*?<!-- END:categories -->",
                new_categories_section,
                content,
                flags=re.DOTALL
            )
        else:
            # Prefer to place categories near top; if services section exists, place categories before it,
            # otherwise append at top.
            if "<!-- START:services -->" in content:
                content = re.sub(
                    r"<!-- START:services -->",
                    new_categories_section + "\n\n<!-- START:services -->",
                    content,
                    count=1
                )
            else:
                content = new_categories_section + "\n\n" + content

        # Replace or append services section (after categories)
        if "<!-- START:services -->" in content and "<!-- END:services -->" in content:
            content = re.sub(
                r"<!-- START:services -->.*?<!-- END:services -->",
                new_services_section,
                content,
                flags=re.DOTALL
            )
        else:
            # Append services section if missing
            content = content + "\n\n" + new_services_section

        readme_path.write_text(content, encoding='utf-8')
        print("Updated services/README.md with categories and services sections.")

    print(f"\n✅ Total services processed: {services_processed}")
    print(f"✅ Total categories generated: {len(category_domains)}")


if __name__ == "__main__":
    main()
