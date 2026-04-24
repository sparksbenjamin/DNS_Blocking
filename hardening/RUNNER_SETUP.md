# Hardening Runner Setup

This workflow now defaults to a **self-hosted Linux GitHub Actions runner** so
it can reach a private resolver on your home network without extra repo setup.
It uses the runner's installed `python3` instead of `actions/setup-python`,
which avoids platform-compatibility issues on self-hosted systems. On Debian 13
and similar systems, the workflow creates its own virtual environment so it does
not try to install packages into the system Python.

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
- `DNSTWIST_JOBS`
  Optional concurrent seed-job count. The workflow now defaults to:
  `3`
- `DNSTWIST_THREADS`
  The workflow now defaults to:
  `12`
  Override if you want something else.
  Example:
  `16`
- `ACTIVE_IMPERSONATION_ENABLED`
  Optional. Set to:
  `true`
  if you want the workflow to generate active impersonation review reports after
  the DNSTwist lists are built.
- `ACTIVE_IMPERSONATION_TARGETS`
  Optional comma-separated subset for the active review stage.
  Example:
  `paypal,okta,microsoft`
- `ACTIVE_IMPERSONATION_MAX_CANDIDATES`
  Optional per-target cap for the active review stage so it does not probe every
  generated domain in one run.
  Example:
  `25`

If you leave `HARDENING_RUNNER_LABELS` unset, the workflow at
`.github/workflows/update_twisted.yml` will target any runner with the default
`self-hosted` and `linux` labels.

## Minimum Runner Checklist

Inside the container:

1. Install Python 3.11+
2. Install `python3-venv` and `python3-pip`
3. Install the GitHub Actions runner
4. Register it with this repo
5. Confirm the runner shows the default `self-hosted` and `linux` labels
6. Confirm it can resolve through `192.168.100.5`
7. Confirm `python3 -m pip` and `python3 -m venv` work on the runner host
8. Tune `DNSTWIST_JOBS` and `DNSTWIST_THREADS` together instead of cranking only one knob
9. If you leave the variables unset, the workflow will run with `DNSTWIST_JOBS=3` and `DNSTWIST_THREADS=12`
10. Leave `ACTIVE_IMPERSONATION_ENABLED` off until you are ready for the extra probe load

On Debian 13, this is usually enough:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git curl ca-certificates
```

## Quick Validation

From the runner host, this should work:

```bash
python3 -m venv .venv-hardening
. .venv-hardening/bin/activate
python -m pip install --upgrade pip
python -m pip install dnstwist dnspython requests
DNSTWIST_NAMESERVERS=192.168.100.5 DNSTWIST_JOBS=3 DNSTWIST_THREADS=12 python scripts/generate_twisted.py --target paypal
```

If that succeeds, the scheduled workflow should work too.

If you want to validate the active impersonation stage too, try a small scoped run:

```bash
ACTIVE_IMPERSONATION_MAX_CANDIDATES=10 python scripts/generate_active_impersonation.py --target paypal
```
