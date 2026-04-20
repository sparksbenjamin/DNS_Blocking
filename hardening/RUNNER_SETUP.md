# Hardening Runner Setup

This workflow is designed to run best on a **self-hosted GitHub Actions runner**
that lives on the same network as your DNS resolver.

If you want DNSTwist to use a private resolver such as `192.168.100.5`, a
GitHub-hosted runner will not work because it cannot reach your LAN.

## Recommended Topology

- Host the runner inside an `LXC` container on your home network
- Keep the container on the same VLAN/subnet that can reach your Unbound server
- Give the runner a custom label such as `dns-hardening`

## Repo Configuration

Set these GitHub repository variables:

- `HARDENING_RUNNER_LABELS`
  Example:
  `["self-hosted","linux","dns-hardening"]`
- `DNSTWIST_NAMESERVERS`
  Example:
  `192.168.100.5`
- `DNSTWIST_THREADS`
  Example:
  `8`

The workflow at `.github/workflows/update_twisted.yml` reads those values and
uses them automatically.

## Minimum Runner Checklist

Inside the container:

1. Install Python 3.11+
2. Install the GitHub Actions runner
3. Register it with this repo
4. Add the custom label `dns-hardening`
5. Confirm it can resolve through `192.168.100.5`

## Quick Validation

From the runner host, this should work:

```bash
python3 -m pip install dnstwist dnspython
DNSTWIST_NAMESERVERS=192.168.100.5 python3 scripts/generate_twisted.py --target paypal
```

If that succeeds, the scheduled workflow should work too.
