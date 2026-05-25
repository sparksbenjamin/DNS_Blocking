# Active Impersonation Review

**Generated:** 2026-05-25T09:25:28.910849+00:00

This stage scores live DNSTwist lookalike domains against the real brand sites using lightweight fingerprinting, then emits conservative blocking lists from only the highest-confidence non-canonical findings.

Quick links:

- [Back to Hardening](../README.md)
- [Back to Repo Root](../../README.md)

## What This Means

- **HIGH_MATCH** - the candidate looks materially like the baseline and deserves immediate review
- **MEDIUM_MATCH** - some signals line up, but it still needs analyst judgment
- **LOW_MATCH / INCONCLUSIVE** - weak resemblance or not enough content to decide
- **OFFLINE / ERROR** - the candidate did not respond cleanly during this run

Domains that only canonical-redirect to the real brand are filtered out of the visible findings and are **not** added to the blocking lists.

## Settings

- Targets audited: `40`
- Candidate domains audited: `5410`
- Visible findings kept: `5089`
- Canonical brand redirects filtered out: `321`
- Blocklist entries emitted: `2`
- Max workers: `10`
- Target jobs: `2`
- Connect timeout: `3.0` seconds
- Read timeout: `5.0` seconds
- Max response bytes: `262144`
- Max domains per target: `unlimited`
- TSV report: [results.tsv](results.tsv)
- JSON report: [report.json](report.json)
- Aggregated hosts blocklist: [categories/active_impersonation.txt](categories/active_impersonation.txt)
- Aggregated RPZ blocklist: [categories/active_impersonation.rpz](categories/active_impersonation.rpz)

## Overall Summary

| HIGH | MEDIUM | LOW | INCONCLUSIVE | OFFLINE | ERROR |
|------|--------|-----|--------------|---------|-------|
| 2 | 9 | 2173 | 893 | 2012 | 0 |

## Blocking Lists

Only `HIGH_MATCH` domains that do **not** canonical-redirect to the real brand are added to these exact-host blocklists.

| Output | Entries | File |
|--------|---------|------|
| Hosts | 2 | [categories/active_impersonation.txt](categories/active_impersonation.txt) |
| RPZ | 2 | [categories/active_impersonation.rpz](categories/active_impersonation.rpz) |

## Per-Target Summary

| Target | Seeds | Audited | Visible | Blocklist | Filtered Redirects | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|---------|-----------|--------------------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 183 | 183 | 0 | 0 | 0 | 0 | 82 | 80 | 0 |  |
| Amazon | 1 | 258 | 118 | 0 | 140 | 0 | 0 | 38 | 71 | 0 |  |
| Apple | 2 | 345 | 327 | 0 | 18 | 0 | 0 | 145 | 145 | 0 |  |
| Atlassian | 1 | 47 | 42 | 0 | 5 | 0 | 0 | 20 | 14 | 0 |  |
| Auth0 | 1 | 187 | 183 | 0 | 4 | 0 | 0 | 5 | 73 | 0 |  |
| Box | 1 | 103 | 103 | 0 | 0 | 0 | 0 | 71 | 27 | 0 |  |
| Cloudflare | 1 | 152 | 150 | 0 | 2 | 0 | 0 | 43 | 100 | 0 |  |
| Coinbase | 1 | 252 | 251 | 0 | 1 | 0 | 0 | 31 | 36 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 87 | 87 | 0 | 0 | 0 | 0 | 46 | 29 | 0 |  |
| DocuSign | 1 | 91 | 86 | 0 | 5 | 0 | 0 | 31 | 43 | 0 |  |
| Dropbox | 2 | 132 | 131 | 0 | 1 | 0 | 1 | 56 | 64 | 0 |  |
| Duo | 1 | 119 | 119 | 0 | 0 | 0 | 0 | 73 | 28 | 0 |  |
| FedEx | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Figma | 1 | 83 | 83 | 0 | 0 | 0 | 0 | 41 | 26 | 0 |  |
| GitHub | 1 | 156 | 150 | 0 | 6 | 0 | 0 | 72 | 58 | 0 |  |
| GitLab | 1 | 81 | 80 | 0 | 1 | 0 | 0 | 36 | 39 | 0 |  |
| Google | 2 | 563 | 552 | 0 | 11 | 0 | 8 | 180 | 303 | 0 |  |
| Intuit | 1 | 139 | 139 | 0 | 0 | 0 | 0 | 58 | 59 | 0 |  |
| Jira | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 66 | 26 | 0 |  |
| Microsoft | 5 | 930 | 861 | 0 | 69 | 0 | 0 | 392 | 378 | 0 |  |
| Notion | 1 | 10 | 10 | 0 | 0 | 0 | 0 | 7 | 1 | 0 |  |
| Okta | 1 | 110 | 110 | 0 | 0 | 0 | 0 | 63 | 31 | 0 |  |
| OneLogin | 1 | 31 | 31 | 0 | 0 | 0 | 0 | 14 | 16 | 0 |  |
| PayPal | 1 | 214 | 206 | 0 | 8 | 0 | 0 | 65 | 37 | 0 |  |
| Ping Identity | 1 | 30 | 30 | 0 | 0 | 0 | 0 | 1 | 28 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 117 | 102 | 0 | 15 | 0 | 0 | 40 | 49 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 178 | 177 | 2 | 1 | 2 | 0 | 132 | 27 | 0 |  |
| Slack | 1 | 91 | 91 | 0 | 0 | 0 | 0 | 49 | 24 | 0 |  |
| Stripe | 1 | 97 | 91 | 0 | 6 | 0 | 0 | 46 | 33 | 0 |  |
| Trello | 1 | 60 | 59 | 0 | 1 | 0 | 0 | 27 | 19 | 0 |  |
| TurboTax | 1 | 150 | 126 | 0 | 24 | 0 | 0 | 58 | 51 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 100 | 100 | 0 | 0 | 0 | 0 | 58 | 34 | 0 |  |
| Venmo | 1 | 75 | 74 | 0 | 1 | 0 | 0 | 38 | 21 | 0 |  |
| Zendesk | 1 | 59 | 57 | 0 | 2 | 0 | 0 | 36 | 20 | 0 |  |
| Zoom | 1 | 81 | 81 | 0 | 0 | 0 | 0 | 53 | 22 | 0 |  |
| eBay | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |

## Per-Target Blocking Lists

| Target | Entries | Hosts | RPZ |
|--------|---------|-------|-----|
| Shopify | 2 | [lists/shopify.txt](lists/shopify.txt) | [lists/shopify.rpz](lists/shopify.rpz) |

## Top Suspicious Matches

| Target | Domain | Status | Score | Baseline | Redirect | Title | Content |
|--------|--------|--------|-------|----------|----------|-------|---------|
| Shopify | `shopefy.com` | HIGH_MATCH | 9 | `shopify.com` | `shopefy.com` | 1.00 | 1.00 |
| Shopify | `shopivy.com` | HIGH_MATCH | 9 | `shopify.com` | `shopivy.com` | 1.00 | 1.00 |
| Google | `xn--gogl-jpa1d.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogl-jpa1d.com` | 1.00 | 0.11 |
| Google | `xn--gogle-1ta.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-1ta.com` | 1.00 | 0.06 |
| Google | `xn--ooge-21a88g.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--ooge-21a88g.com` | 1.00 | 0.06 |
| Google | `xn--googl-9cc.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-9cc.com` | 1.00 | 0.05 |
| Google | `xn--gogle-g91b.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-g91b.com` | 1.00 | 0.04 |
| Google | `xn--googl-lsa.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-lsa.com` | 1.00 | 0.04 |
| Dropbox | `dr.opbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `dr.opbox.com` | 0.90 | 0.03 |
| Google | `xn--goog-8va9v.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--goog-8va9v.com` | 1.00 | 0.03 |
| Google | `xn--ooge-9wa5r.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--ooge-9wa5r.com` | 1.00 | 0.03 |

## Operational Notes

1. Canonical redirects to the real brand are intentionally excluded from both the report rows and the blocklists
2. The blocking lists are conservative and only include `HIGH_MATCH` domains
3. Review `MEDIUM_MATCH` findings manually before promoting them anywhere
4. Re-run the report when you regenerate hardening lists or change target coverage
