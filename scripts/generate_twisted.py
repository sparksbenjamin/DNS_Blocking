import os
import subprocess

LISTS_DIR = 'services/lists'

def run_dnstwist(domain):
    # --registered: only keeps active domains
    # --format list: returns just the domain names
    result = subprocess.run(
        ['dnstwist', '--registered', '--format', 'list', domain],
        capture_output=True, text=True
    )
    return result.stdout.splitlines()

for filename in os.listdir(LISTS_DIR):
    if filename.endswith('.txt') and not filename.endswith('_twisted.txt'):
        service_path = os.path.join(LISTS_DIR, filename)
        twisted_output = os.path.join(LISTS_DIR, filename.replace('.txt', '_twisted.txt'))
        
        all_twisted = set()
        with open(service_path, 'r') as f:
            for domain in f:
                domain = domain.strip()
                if domain:
                    print(f"Twisting: {domain}")
                    all_twisted.update(run_dnstwist(domain))
        
        with open(twisted_output, 'w') as f:
            f.write('\n'.join(sorted(all_twisted)))
