# Hardening Runner Setup

This workflow now defaults to a **self-hosted Linux GitHub Actions runner** so
it can reach a private resolver on your home network without extra repo setup.

If you want DNSTwist to use a private resolver such as `192.168.100.5`, a
GitHub-hosted runner will not work because it cannot reach your LAN.

## Recommended Topology

- Host the runner inside an `LXC` container on your home network
- Keep the container on the same VLAN/subnet that can reach your Unbound server
- Let it keep the default GitHub labels such as `self-hosted` and `linux`

## Repo Configuration

Set these GitHub repository variables:

- `HARDENING_RUNNER_LABELS`
  Optional override if you want a stricter runner match than the default
  `["self-hosted","linux"]`
  Example:
  `["self-hosted","linux","x64"]`
- `DNSTWIST_NAMESERVERS`
  Example:
  `192.168.100.5`
- `DNSTWIST_THREADS`
  Example:
  `8`

If you leave `HARDENING_RUNNER_LABELS` unset, the workflow at
`.github/workflows/update_twisted.yml` will target any runner with the default
`self-hosted` and `linux` labels.

## Minimum Runner Checklist

Inside the container:

1. Install Python 3.11+
2. Install the GitHub Actions runner
3. Register it with this repo
4. Confirm the runner shows the default `self-hosted` and `linux` labels
5. Confirm it can resolve through `192.168.100.5`

## Quick Validation

From the runner host, this should work:

```bash
python3 -m pip install dnstwist dnspython
DNSTWIST_NAMESERVERS=192.168.100.5 python3 scripts/generate_twisted.py --target paypal
```

If that succeeds, the scheduled workflow should work too.
