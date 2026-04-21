# DNSTwist Hardening Lists

**Generated:** 2026-04-21 01:22:00 UTC

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
- Nameservers: system/default resolver

## Running With Your Own Resolver

If you want DNSTwist to query a resolver you control, set `DNSTWIST_NAMESERVERS` or pass `--nameservers` when running the script.

Example:

```bash
DNSTWIST_NAMESERVERS=192.168.100.5 python3 scripts/generate_twisted.py
```

If that resolver lives on a private address like `192.168.100.5`, the scheduled workflow should run on a **self-hosted runner inside your home network**. GitHub-hosted runners cannot reach private LAN IPs.

## Categories

| Category | Exact Hosts | File | Raw URL |
|----------|-------------|------|---------|
| Brand Impersonation | 4,678 | [brand_impersonation.txt](categories/brand_impersonation.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/categories/brand_impersonation.txt) |

## Per-Target Lists

| Target | Seeds | Exact Hosts | File | Raw URL |
|--------|-------|-------------|------|---------|
| Adobe | 2 | 178 | [adobe.txt](lists/brand_impersonation/adobe.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/adobe.txt) |
| Amazon | 1 | 258 | [amazon.txt](lists/brand_impersonation/amazon.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/amazon.txt) |
| Apple | 2 | 326 | [apple.txt](lists/brand_impersonation/apple.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/apple.txt) |
| Atlassian | 1 | 46 | [atlassian.txt](lists/brand_impersonation/atlassian.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/atlassian.txt) |
| Box | 1 | 100 | [box.txt](lists/brand_impersonation/box.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/box.txt) |
| Cloudflare | 1 | 140 | [cloudflare.txt](lists/brand_impersonation/cloudflare.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/cloudflare.txt) |
| DocuSign | 1 | 85 | [docusign.txt](lists/brand_impersonation/docusign.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/docusign.txt) |
| Dropbox | 2 | 124 | [dropbox.txt](lists/brand_impersonation/dropbox.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/dropbox.txt) |
| Duo | 1 | 104 | [duo.txt](lists/brand_impersonation/duo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/duo.txt) |
| FedEx | 1 | 116 | [fedex.txt](lists/brand_impersonation/fedex.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/fedex.txt) |
| Figma | 1 | 80 | [figma.txt](lists/brand_impersonation/figma.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/figma.txt) |
| GitHub | 1 | 158 | [github.txt](lists/brand_impersonation/github.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/github.txt) |
| Google | 2 | 552 | [google.txt](lists/brand_impersonation/google.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/google.txt) |
| Intuit | 1 | 141 | [intuit.txt](lists/brand_impersonation/intuit.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/intuit.txt) |
| Jira | 1 | 90 | [jira.txt](lists/brand_impersonation/jira.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/jira.txt) |
| Microsoft | 5 | 900 | [microsoft.txt](lists/brand_impersonation/microsoft.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/microsoft.txt) |
| Notion | 1 | 13 | [notion.txt](lists/brand_impersonation/notion.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/notion.txt) |
| Okta | 1 | 107 | [okta.txt](lists/brand_impersonation/okta.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/okta.txt) |
| PayPal | 1 | 212 | [paypal.txt](lists/brand_impersonation/paypal.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/paypal.txt) |
| QuickBooks | 1 | 201 | [quickbooks.txt](lists/brand_impersonation/quickbooks.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/quickbooks.txt) |
| Salesforce | 1 | 115 | [salesforce.txt](lists/brand_impersonation/salesforce.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/salesforce.txt) |
| Slack | 1 | 89 | [slack.txt](lists/brand_impersonation/slack.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/slack.txt) |
| Stripe | 1 | 95 | [stripe.txt](lists/brand_impersonation/stripe.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/stripe.txt) |
| Trello | 1 | 61 | [trello.txt](lists/brand_impersonation/trello.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/trello.txt) |
| TurboTax | 1 | 150 | [turbotax.txt](lists/brand_impersonation/turbotax.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/turbotax.txt) |
| UPS | 1 | 95 | [ups.txt](lists/brand_impersonation/ups.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/ups.txt) |
| Zendesk | 1 | 61 | [zendesk.txt](lists/brand_impersonation/zendesk.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/zendesk.txt) |
| Zoom | 1 | 81 | [zoom.txt](lists/brand_impersonation/zoom.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/zoom.txt) |

## Recommended Use

1. Start with one or two brands you care about most
2. Watch DNS logs for a while before applying the aggregated category
3. Prefer a resolver you control so DNSTwist lookups are consistent and fast
4. Treat this as a security hardening layer, not a replacement for the main phishing lists
