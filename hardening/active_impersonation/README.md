# Active Impersonation Review

**Generated:** 2026-05-21T09:01:55.228836+00:00

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
- Candidate domains audited: `5562`
- Visible findings kept: `5190`
- Canonical brand redirects filtered out: `372`
- Blocklist entries emitted: `0`
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
| 0 | 9 | 2209 | 862 | 2110 | 0 |

## Blocking Lists

Only `HIGH_MATCH` domains that do **not** canonical-redirect to the real brand are added to these exact-host blocklists.

| Output | Entries | File |
|--------|---------|------|
| Hosts | 0 | [categories/active_impersonation.txt](categories/active_impersonation.txt) |
| RPZ | 0 | [categories/active_impersonation.rpz](categories/active_impersonation.rpz) |

## Per-Target Summary

| Target | Seeds | Audited | Visible | Blocklist | Filtered Redirects | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|---------|-----------|--------------------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 183 | 183 | 0 | 0 | 0 | 0 | 90 | 78 | 0 |  |
| Amazon | 1 | 258 | 118 | 0 | 140 | 0 | 0 | 37 | 73 | 0 |  |
| Apple | 2 | 345 | 327 | 0 | 18 | 0 | 0 | 143 | 152 | 0 |  |
| Atlassian | 1 | 47 | 42 | 0 | 5 | 0 | 0 | 23 | 16 | 0 |  |
| Auth0 | 1 | 187 | 183 | 0 | 4 | 0 | 0 | 5 | 73 | 0 |  |
| Box | 1 | 102 | 102 | 0 | 0 | 0 | 0 | 70 | 26 | 0 |  |
| Cloudflare | 1 | 152 | 150 | 0 | 2 | 0 | 0 | 47 | 94 | 0 |  |
| Coinbase | 1 | 253 | 252 | 0 | 1 | 0 | 0 | 28 | 41 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 88 | 88 | 0 | 0 | 0 | 0 | 46 | 32 | 0 |  |
| DocuSign | 1 | 92 | 87 | 0 | 5 | 0 | 0 | 32 | 45 | 0 |  |
| Dropbox | 2 | 131 | 130 | 0 | 1 | 0 | 1 | 57 | 65 | 0 |  |
| Duo | 1 | 120 | 120 | 0 | 0 | 0 | 0 | 69 | 30 | 0 |  |
| FedEx | 1 | 130 | 130 | 0 | 0 | 0 | 0 | 51 | 68 | 0 |  |
| Figma | 1 | 84 | 84 | 0 | 0 | 0 | 0 | 48 | 26 | 0 |  |
| GitHub | 1 | 157 | 151 | 0 | 6 | 0 | 0 | 76 | 58 | 0 |  |
| GitLab | 1 | 81 | 80 | 0 | 1 | 0 | 0 | 37 | 39 | 0 |  |
| Google | 2 | 563 | 552 | 0 | 11 | 0 | 8 | 177 | 307 | 0 |  |
| Intuit | 1 | 140 | 140 | 0 | 0 | 0 | 0 | 62 | 56 | 0 |  |
| Jira | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 69 | 26 | 0 |  |
| Microsoft | 5 | 937 | 868 | 0 | 69 | 0 | 0 | 394 | 385 | 0 |  |
| Notion | 1 | 11 | 11 | 0 | 0 | 0 | 0 | 8 | 1 | 0 |  |
| Okta | 1 | 111 | 111 | 0 | 0 | 0 | 0 | 62 | 33 | 0 |  |
| OneLogin | 1 | 31 | 31 | 0 | 0 | 0 | 0 | 10 | 18 | 0 |  |
| PayPal | 1 | 214 | 206 | 0 | 8 | 0 | 0 | 62 | 38 | 0 |  |
| Ping Identity | 1 | 30 | 30 | 0 | 0 | 0 | 0 | 1 | 28 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 122 | 107 | 0 | 15 | 0 | 0 | 39 | 56 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 178 | 126 | 0 | 52 | 0 | 0 | 82 | 27 | 0 |  |
| Slack | 1 | 89 | 89 | 0 | 0 | 0 | 0 | 50 | 25 | 0 |  |
| Stripe | 1 | 99 | 93 | 0 | 6 | 0 | 0 | 50 | 36 | 0 |  |
| Trello | 1 | 60 | 59 | 0 | 1 | 0 | 0 | 31 | 20 | 0 |  |
| TurboTax | 1 | 151 | 127 | 0 | 24 | 0 | 0 | 64 | 45 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 100 | 100 | 0 | 0 | 0 | 0 | 57 | 35 | 0 |  |
| Venmo | 1 | 74 | 73 | 0 | 1 | 0 | 0 | 37 | 20 | 0 |  |
| Zendesk | 1 | 63 | 61 | 0 | 2 | 0 | 0 | 35 | 24 | 0 |  |
| Zoom | 1 | 80 | 80 | 0 | 0 | 0 | 0 | 60 | 14 | 0 |  |
| eBay | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |

## Per-Target Blocking Lists

No block-worthy domains were emitted in this run.

## Top Suspicious Matches

| Target | Domain | Status | Score | Baseline | Redirect | Title | Content |
|--------|--------|--------|-------|----------|----------|-------|---------|
| Google | `xn--gogl-jpa1d.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogl-jpa1d.com` | 1.00 | 0.14 |
| Google | `xn--gogle-1ta.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-1ta.com` | 1.00 | 0.10 |
| Google | `xn--ooge-21a88g.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--ooge-21a88g.com` | 1.00 | 0.10 |
| Google | `xn--googl-9cc.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-9cc.com` | 1.00 | 0.05 |
| Google | `xn--googl-lsa.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-lsa.com` | 1.00 | 0.05 |
| Google | `xn--gogle-g91b.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-g91b.com` | 1.00 | 0.04 |
| Google | `xn--goog-8va9v.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--goog-8va9v.com` | 1.00 | 0.04 |
| Google | `xn--ooge-9wa5r.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--ooge-9wa5r.com` | 1.00 | 0.04 |
| Dropbox | `dr.opbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `dr.opbox.com` | 0.90 | 0.03 |

## Operational Notes

1. Canonical redirects to the real brand are intentionally excluded from both the report rows and the blocklists
2. The blocking lists are conservative and only include `HIGH_MATCH` domains
3. Review `MEDIUM_MATCH` findings manually before promoting them anywhere
4. Re-run the report when you regenerate hardening lists or change target coverage
