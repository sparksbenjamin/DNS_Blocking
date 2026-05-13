# Active Impersonation Review

**Generated:** 2026-05-13T08:31:13.737590+00:00

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
- Candidate domains audited: `5427`
- Visible findings kept: `5071`
- Canonical brand redirects filtered out: `356`
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
| 0 | 10 | 2130 | 833 | 2098 | 0 |

## Blocking Lists

Only `HIGH_MATCH` domains that do **not** canonical-redirect to the real brand are added to these exact-host blocklists.

| Output | Entries | File |
|--------|---------|------|
| Hosts | 0 | [categories/active_impersonation.txt](categories/active_impersonation.txt) |
| RPZ | 0 | [categories/active_impersonation.rpz](categories/active_impersonation.rpz) |

## Per-Target Summary

| Target | Seeds | Audited | Visible | Blocklist | Filtered Redirects | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|---------|-----------|--------------------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 182 | 182 | 0 | 0 | 0 | 0 | 84 | 85 | 0 |  |
| Amazon | 1 | 258 | 118 | 0 | 140 | 0 | 0 | 37 | 73 | 0 |  |
| Apple | 2 | 345 | 327 | 0 | 18 | 0 | 0 | 147 | 144 | 0 |  |
| Atlassian | 1 | 47 | 41 | 0 | 6 | 0 | 0 | 23 | 14 | 0 |  |
| Auth0 | 1 | 187 | 183 | 0 | 4 | 0 | 0 | 4 | 73 | 0 |  |
| Box | 1 | 104 | 104 | 0 | 0 | 0 | 0 | 69 | 28 | 0 |  |
| Cloudflare | 1 | 151 | 149 | 0 | 2 | 0 | 0 | 41 | 101 | 0 |  |
| Coinbase | 1 | 253 | 252 | 0 | 1 | 0 | 0 | 29 | 37 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 88 | 88 | 0 | 0 | 0 | 0 | 47 | 33 | 0 |  |
| DocuSign | 1 | 88 | 83 | 0 | 5 | 0 | 0 | 29 | 45 | 0 |  |
| Dropbox | 2 | 129 | 128 | 0 | 1 | 0 | 1 | 54 | 71 | 0 |  |
| Duo | 1 | 119 | 119 | 0 | 0 | 0 | 0 | 69 | 32 | 0 |  |
| FedEx | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Figma | 1 | 84 | 84 | 0 | 0 | 0 | 0 | 46 | 28 | 0 |  |
| GitHub | 1 | 156 | 150 | 0 | 6 | 0 | 0 | 67 | 64 | 0 |  |
| GitLab | 1 | 82 | 81 | 0 | 1 | 0 | 0 | 34 | 42 | 0 |  |
| Google | 2 | 564 | 553 | 0 | 11 | 0 | 9 | 190 | 303 | 0 |  |
| Intuit | 1 | 141 | 141 | 0 | 0 | 0 | 0 | 65 | 48 | 0 |  |
| Jira | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 69 | 27 | 0 |  |
| Microsoft | 5 | 941 | 872 | 0 | 69 | 0 | 0 | 382 | 410 | 0 |  |
| Notion | 1 | 10 | 10 | 0 | 0 | 0 | 0 | 8 | 0 | 0 |  |
| Okta | 1 | 109 | 109 | 0 | 0 | 0 | 0 | 57 | 34 | 0 |  |
| OneLogin | 1 | 31 | 31 | 0 | 0 | 0 | 0 | 14 | 14 | 0 |  |
| PayPal | 1 | 217 | 209 | 0 | 8 | 0 | 0 | 65 | 41 | 0 |  |
| Ping Identity | 1 | 29 | 29 | 0 | 0 | 0 | 0 | 1 | 27 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 119 | 104 | 0 | 15 | 0 | 0 | 36 | 55 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 176 | 141 | 0 | 35 | 0 | 0 | 96 | 27 | 0 |  |
| Slack | 1 | 94 | 94 | 0 | 0 | 0 | 0 | 52 | 30 | 0 |  |
| Stripe | 1 | 98 | 92 | 0 | 6 | 0 | 0 | 51 | 33 | 0 |  |
| Trello | 1 | 61 | 60 | 0 | 1 | 0 | 0 | 32 | 19 | 0 |  |
| TurboTax | 1 | 151 | 127 | 0 | 24 | 0 | 0 | 61 | 50 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 59 | 33 | 0 |  |
| Venmo | 1 | 74 | 73 | 0 | 1 | 0 | 0 | 39 | 22 | 0 |  |
| Zendesk | 1 | 61 | 59 | 0 | 2 | 0 | 0 | 28 | 29 | 0 |  |
| Zoom | 1 | 80 | 80 | 0 | 0 | 0 | 0 | 45 | 26 | 0 |  |
| eBay | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |

## Per-Target Blocking Lists

No block-worthy domains were emitted in this run.

## Top Suspicious Matches

| Target | Domain | Status | Score | Baseline | Redirect | Title | Content |
|--------|--------|--------|-------|----------|----------|-------|---------|
| Google | `xn--gogl-jpa1d.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogl-jpa1d.com` | 1.00 | 0.13 |
| Google | `xn--gogle-1ta.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-1ta.com` | 1.00 | 0.08 |
| Google | `xn--ooge-21a88g.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--ooge-21a88g.com` | 1.00 | 0.08 |
| Google | `xn--googl-lsa.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-lsa.com` | 1.00 | 0.06 |
| Google | `xn--gogle-g91b.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-g91b.com` | 1.00 | 0.04 |
| Google | `xn--goog-8va9v.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--goog-8va9v.com` | 1.00 | 0.04 |
| Google | `xn--googl-9cc.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-9cc.com` | 1.00 | 0.04 |
| Google | `xn--ooge-9wa5r.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--ooge-9wa5r.com` | 1.00 | 0.04 |
| Dropbox | `dr.opbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `dr.opbox.com` | 0.90 | 0.03 |
| Google | `xn--googe-m6a.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googe-m6a.com` | 1.00 | 0.03 |

## Operational Notes

1. Canonical redirects to the real brand are intentionally excluded from both the report rows and the blocklists
2. The blocking lists are conservative and only include `HIGH_MATCH` domains
3. Review `MEDIUM_MATCH` findings manually before promoting them anywhere
4. Re-run the report when you regenerate hardening lists or change target coverage
