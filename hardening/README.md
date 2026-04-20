# DNSTwist Hardening Lists

**Generated:** 2026-04-20 23:15:40 UTC

This section contains optional high-sensitivity blocklists generated from curated brand seeds with [dnstwist](https://github.com/elceef/dnstwist).

These lists are designed for **hardening against brand impersonation and typo-squatting**, not for normal service blocking. They are intentionally kept separate from the standard `services/` lists.

## What DNSTwist Does

`dnstwist` generates lookalike permutations for a brand domain and checks which ones appear to be live. That makes it useful for catching typo-squatting, homoglyph tricks, and brand impersonation domains.

## Important Notes

- **Aggressive by design** - these lists can block domains that are unrelated to your environment but happen to look like a protected brand
- **Exact hostnames are preserved** - these are not collapsed to registrable roots
- **Best used for high-risk brands** - identity providers, mail brands, payment brands, and collaboration tools
- **Review before broad deployment** - especially if you use wildcard-heavy allow/block policies

## Generation Settings

- Source tool: [dnstwist](https://github.com/elceef/dnstwist)
- Mode: registered lookalike domains only
- Output format: hosts file (`0.0.0.0 hostname`)
- Nameservers: `192.168.100.5`

## Running With Your Own Resolver

If you want DNSTwist to query a resolver you control, set `DNSTWIST_NAMESERVERS` or pass `--nameservers` when running the script.

Example:

```bash
DNSTWIST_NAMESERVERS=192.168.100.5 python3 scripts/generate_twisted.py
```

If that resolver lives on a private address like `192.168.100.5`, the scheduled workflow should run on a **self-hosted runner inside your home network**. GitHub-hosted runners cannot reach private LAN IPs.

Runner setup details:
[RUNNER_SETUP.md](RUNNER_SETUP.md)

## Categories

| Category | Exact Hosts | File | Raw URL |
|----------|-------------|------|---------|
| Brand Impersonation | 2,553 | [brand_impersonation.txt](categories/brand_impersonation.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/categories/brand_impersonation.txt) |

## Per-Target Lists

| Target | Seeds | Exact Hosts | File | Raw URL |
|--------|-------|-------------|------|---------|
| Adobe | 2 | 177 | [adobe.txt](lists/brand_impersonation/adobe.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/adobe.txt) |
| Amazon | 1 | 255 | [amazon.txt](lists/brand_impersonation/amazon.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/amazon.txt) |
| Apple | 2 | 333 | [apple.txt](lists/brand_impersonation/apple.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/apple.txt) |
| DocuSign | 1 | 85 | [docusign.txt](lists/brand_impersonation/docusign.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/docusign.txt) |
| Dropbox | 2 | 127 | [dropbox.txt](lists/brand_impersonation/dropbox.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/dropbox.txt) |
| Google | 2 | 257 | [google.txt](lists/brand_impersonation/google.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/google.txt) |
| Microsoft | 5 | 909 | [microsoft.txt](lists/brand_impersonation/microsoft.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/microsoft.txt) |
| Okta | 1 | 108 | [okta.txt](lists/brand_impersonation/okta.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/okta.txt) |
| PayPal | 1 | 213 | [paypal.txt](lists/brand_impersonation/paypal.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/paypal.txt) |
| Slack | 1 | 89 | [slack.txt](lists/brand_impersonation/slack.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/slack.txt) |

## Recommended Use

1. Start with one or two brands you care about most
2. Watch DNS logs for a while before applying the aggregated category
3. Prefer a resolver you control so DNSTwist lookups are consistent and fast
4. Treat this as a security hardening layer, not a replacement for the main phishing lists
