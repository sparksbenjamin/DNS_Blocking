import os
import json

SERVICES_JSON = 'services/services.json'
LISTS_DIR = 'services/lists'
CATEGORIES_DIR = 'services/categories'

with open(SERVICES_JSON, 'r') as f:
    config = json.load(f)

for category, list_files in config.items():
    combined_content = set()
    for list_name in list_files:
        # Load the base service list
        base_file = os.path.join(LISTS_DIR, f"{list_name}.txt")
        twisted_file = os.path.join(LISTS_DIR, f"{list_name}_twisted.txt")
        
        for fpath in [base_file, twisted_file]:
            if os.path.exists(fpath):
                with open(fpath, 'r') as f:
                    combined_content.update(f.read().splitlines())

    output_path = os.path.join(CATEGORIES_DIR, f"{category}.txt")
    with open(output_path, 'w') as f:
        f.write('\n'.join(sorted(filter(None, combined_content))))
