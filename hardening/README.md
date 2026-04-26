# DNSTwist Hardening Lists

**Generated:** 2026-04-26 06:12:13 UTC

This section contains optional high-sensitivity blocklists generated from curated brand seeds with [dnstwist](https://github.com/elceef/dnstwist).

These lists are designed for **hardening against brand impersonation and typo-squatting**, not for normal service blocking. They are intentionally kept separate from the standard `services/` lists.

There is also a separate review layer at [active_impersonation/README.md](active_impersonation/README.md). That stage does **not** create another blocklist. Instead, it scores live lookalike domains against the real brand sites so you can review which ones look materially suspicious before promoting them anywhere.

Quick links:

- [Brand Impersonation Lists](#categories)
- [Active Impersonation Review](active_impersonation/README.md)

## What DNSTwist Does

`dnstwist` generates lookalike permutations for a brand domain and checks which ones appear to be live. That makes it useful for catching typo-squatting, homoglyph tricks, and brand impersonation domains.

## Important Notes

- **Aggressive by design** - these lists can block domains that are unrelated to your environment but happen to look like a protected brand
- **Exact hostnames are preserved** - these are not collapsed to registrable roots
- **Best used for high-risk brands** - identity providers, mail brands, payment brands, and collaboration tools
- **Review before broad deployment** - especially if you use wildcard-heavy allow/block policies

## Active Impersonation Review

If you want more than “this domain is a live DNSTwist permutation,” run `scripts/generate_active_impersonation.py` after the hardening lists are generated, or use the separate `Update Active Impersonation Review` workflow.

That report stage:
- checks whether the real brand site is reachable
- fingerprints live lookalikes with lightweight HTTP, TLS, and content signals
- scores which domains most closely resemble the real site
- writes review artifacts under `hardening/active_impersonation/`

This is useful when you want a tighter triage loop instead of auto-blocking every live permutation.

If you do not see generated review files under `hardening/active_impersonation/`, the most likely reason is that the separate review workflow has not run yet or has not committed a report yet.

## Generation Settings

- Source tool: [dnstwist](https://github.com/elceef/dnstwist)
- Mode: registered lookalike domains only
- Output format: hosts file (`0.0.0.0 hostname`)
- Concurrent seed jobs: `3`
- Nameservers: system/default resolver

## Running With Your Own Resolver

If you want DNSTwist to query a resolver you control, set `DNSTWIST_NAMESERVERS` or pass `--nameservers` when running the script. You can also raise `DNSTWIST_JOBS` to run multiple seed domains concurrently.

Example:

```bash
DNSTWIST_NAMESERVERS=192.168.100.5 DNSTWIST_JOBS=2 python3 scripts/generate_twisted.py
```

If that resolver lives on a private address like `192.168.100.5`, the scheduled workflow should run on a **self-hosted runner inside your home network**. GitHub-hosted runners cannot reach private LAN IPs.

## Categories

| Category | Exact Hosts | File | Raw URL |
|----------|-------------|------|---------|
| Brand Impersonation | 6,108 | [brand_impersonation.txt](categories/brand_impersonation.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/categories/brand_impersonation.txt) |

## Per-Target Lists

| Target | Seeds | Exact Hosts | File | Raw URL |
|--------|-------|-------------|------|---------|
| Adobe | 2 | 180 | [adobe.txt](lists/brand_impersonation/adobe.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/adobe.txt) |
| Amazon | 1 | 258 | [amazon.txt](lists/brand_impersonation/amazon.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/amazon.txt) |
| Apple | 2 | 346 | [apple.txt](lists/brand_impersonation/apple.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/apple.txt) |
| Atlassian | 1 | 46 | [atlassian.txt](lists/brand_impersonation/atlassian.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/atlassian.txt) |
| Auth0 | 1 | 188 | [auth0.txt](lists/brand_impersonation/auth0.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/auth0.txt) |
| Box | 1 | 103 | [box.txt](lists/brand_impersonation/box.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/box.txt) |
| Cloudflare | 1 | 150 | [cloudflare.txt](lists/brand_impersonation/cloudflare.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/cloudflare.txt) |
| Coinbase | 1 | 255 | [coinbase.txt](lists/brand_impersonation/coinbase.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/coinbase.txt) |
| DHL | 1 | 104 | [dhl.txt](lists/brand_impersonation/dhl.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/dhl.txt) |
| Docker | 1 | 90 | [docker.txt](lists/brand_impersonation/docker.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/docker.txt) |
| DocuSign | 1 | 87 | [docusign.txt](lists/brand_impersonation/docusign.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/docusign.txt) |
| Dropbox | 2 | 129 | [dropbox.txt](lists/brand_impersonation/dropbox.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/dropbox.txt) |
| Duo | 1 | 116 | [duo.txt](lists/brand_impersonation/duo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/duo.txt) |
| FedEx | 1 | 119 | [fedex.txt](lists/brand_impersonation/fedex.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/fedex.txt) |
| Figma | 1 | 84 | [figma.txt](lists/brand_impersonation/figma.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/figma.txt) |
| GitHub | 1 | 162 | [github.txt](lists/brand_impersonation/github.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/github.txt) |
| GitLab | 1 | 81 | [gitlab.txt](lists/brand_impersonation/gitlab.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/gitlab.txt) |
| Google | 2 | 567 | [google.txt](lists/brand_impersonation/google.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/google.txt) |
| Intuit | 1 | 142 | [intuit.txt](lists/brand_impersonation/intuit.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/intuit.txt) |
| Jira | 1 | 99 | [jira.txt](lists/brand_impersonation/jira.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/jira.txt) |
| Microsoft | 5 | 935 | [microsoft.txt](lists/brand_impersonation/microsoft.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/microsoft.txt) |
| Notion | 1 | 13 | [notion.txt](lists/brand_impersonation/notion.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/notion.txt) |
| Okta | 1 | 110 | [okta.txt](lists/brand_impersonation/okta.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/okta.txt) |
| OneLogin | 1 | 32 | [onelogin.txt](lists/brand_impersonation/onelogin.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/onelogin.txt) |
| PayPal | 1 | 216 | [paypal.txt](lists/brand_impersonation/paypal.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/paypal.txt) |
| Ping Identity | 1 | 29 | [pingidentity.txt](lists/brand_impersonation/pingidentity.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/pingidentity.txt) |
| QuickBooks | 1 | 201 | [quickbooks.txt](lists/brand_impersonation/quickbooks.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/quickbooks.txt) |
| Salesforce | 1 | 117 | [salesforce.txt](lists/brand_impersonation/salesforce.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/salesforce.txt) |
| ServiceNow | 1 | 38 | [servicenow.txt](lists/brand_impersonation/servicenow.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/servicenow.txt) |
| Shopify | 1 | 177 | [shopify.txt](lists/brand_impersonation/shopify.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/shopify.txt) |
| Slack | 1 | 92 | [slack.txt](lists/brand_impersonation/slack.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/slack.txt) |
| Stripe | 1 | 98 | [stripe.txt](lists/brand_impersonation/stripe.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/stripe.txt) |
| Trello | 1 | 61 | [trello.txt](lists/brand_impersonation/trello.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/trello.txt) |
| TurboTax | 1 | 151 | [turbotax.txt](lists/brand_impersonation/turbotax.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/turbotax.txt) |
| UPS | 1 | 100 | [ups.txt](lists/brand_impersonation/ups.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/ups.txt) |
| USPS | 1 | 99 | [usps.txt](lists/brand_impersonation/usps.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/usps.txt) |
| Venmo | 1 | 73 | [venmo.txt](lists/brand_impersonation/venmo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/venmo.txt) |
| Zendesk | 1 | 62 | [zendesk.txt](lists/brand_impersonation/zendesk.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/zendesk.txt) |
| Zoom | 1 | 82 | [zoom.txt](lists/brand_impersonation/zoom.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/zoom.txt) |
| eBay | 1 | 124 | [ebay.txt](lists/brand_impersonation/ebay.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/hardening/lists/brand_impersonation/ebay.txt) |

## Recommended Use

1. Start with one or two brands you care about most
2. Watch DNS logs for a while before applying the aggregated category
3. Prefer a resolver you control so DNSTwist lookups are consistent and fast
4. Treat this as a security hardening layer, not a replacement for the main phishing lists
