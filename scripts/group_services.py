import os
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)

SERVICES_JSON = 'services.json'
LISTS_DIR = 'services/lists'
CATEGORIES_DIR = 'services/categories'

# Ensure the output directory exists
os.makedirs(CATEGORIES_DIR, exist_ok=True)

def load_services():
    with open(SERVICES_JSON, 'r') as f:
        data = json.load(f)
    return data.get("blocked_services", [])

def main():
    services = load_services()
    
    # Organize services by their group name
    groups = {}
    for service in services:
        group_name = service.get("group", "ungrouped").lower()
        if group_name not in groups:
            groups[group_name] = []
        groups[group_name].append(service)

    logging.info(f"Found {len(groups)} unique groups to process.")

    for group_name, service_list in groups.items():
        logging.info(f"Processing group: {group_name}")
        
        legit_domains = set()
        twisted_domains = set()

        for service in service_list:
            service_name = service.get("name")
            
            # 1. Collect Legit Domains (from the .txt files in lists/)
            legit_file = os.path.join(LISTS_DIR, f"{service_name}.txt")
            if os.path.exists(legit_file):
                with open(legit_file, 'r') as f:
                    legit_domains.update([line.strip() for line in f if line.strip()])
            
            # 2. Collect Twisted Domains (from the _twisted.txt files)
            twisted_file = os.path.join(LISTS_DIR, f"{service_name}_twisted.txt")
            if os.path.exists(twisted_file):
                with open(twisted_file, 'r') as f:
                    twisted_domains.update([line.strip() for line in f if line.strip()])

        # Define Output Paths
        # Example: adult.txt
        legit_out = os.path.join(CATEGORIES_DIR, f"{group_name}.txt")
        # Example: adult_twisted.txt
        twisted_out = os.path.join(CATEGORIES_DIR, f"{group_name}_twisted.txt")
        # Example: adult_full.txt
        full_out = os.path.join(CATEGORIES_DIR, f"{group_name}_full.txt")

        # Write Legit Only
        if legit_domains:
            with open(legit_out, 'w') as f:
                f.write('\n'.join(sorted(legit_domains)))
        
        # Write Twisted Only
        if twisted_domains:
            with open(twisted_out, 'w') as f:
                f.write('\n'.join(sorted(twisted_domains)))
        
        # Write Full (Legit + Twisted)
        full_combined = legit_domains.union(twisted_domains)
        if full_combined:
            with open(full_out, 'w') as f:
                f.write('\n'.join(sorted(full_combined)))

        logging.info(f"  [DONE] Created {group_name} (Legit: {len(legit_domains)}, Twisted: {len(twisted_domains)})")

if __name__ == "__main__":
    main()
