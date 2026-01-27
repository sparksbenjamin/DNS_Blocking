import os
import subprocess
import logging
import time

# Configure logging for GitHub Actions
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)

LISTS_DIR = 'services/lists'

def run_dnstwist(domain):
    logging.info(f"  --> Starting dnstwist for: {domain}")
    start_time = time.time()
    try:
        # Using a timeout to prevent infinite hangs
        result = subprocess.run(
            ['dnstwist', '--registered', '--format', 'list', domain],
            capture_output=True, text=True, timeout=300 
        )
        domains = result.stdout.splitlines()
        duration = time.time() - start_time
        logging.info(f"  --> Found {len(domains)} registered variations in {duration:.2f}s")
        return domains
    except subprocess.TimeoutExpired:
        logging.warning(f"  [!] Timeout reached for {domain}. Skipping.")
        return []
    except Exception as e:
        logging.error(f"  [!] Error processing {domain}: {str(e)}")
        return []

files_to_process = [f for f in os.listdir(LISTS_DIR) if f.endswith('.txt') and not f.endswith('_twisted.txt')]
logging.info(f"Found {len(files_to_process)} service files to process.")

for index, filename in enumerate(files_to_process, 1):
    service_path = os.path.join(LISTS_DIR, filename)
    twisted_output = os.path.join(LISTS_DIR, filename.replace('.txt', '_twisted.txt'))
    
    logging.info(f"[{index}/{len(files_to_process)}] Processing file: {filename}")
    
    all_twisted = set()
    with open(service_path, 'r') as f:
        core_domains = [line.strip() for line in f if line.strip()]
        
    for d_idx, domain in enumerate(core_domains, 1):
        logging.info(f"    ({d_idx}/{len(core_domains)}) Checking: {domain}")
        all_twisted.update(run_dnstwist(domain))
    
    if all_twisted:
        with open(twisted_output, 'w') as f:
            f.write('\n'.join(sorted(all_twisted)))
        logging.info(f"Successfully saved {len(all_twisted)} domains to {twisted_output}")
    else:
        logging.warning(f"No twisted domains found for {filename}")

logging.info("Twisted generation complete.")
