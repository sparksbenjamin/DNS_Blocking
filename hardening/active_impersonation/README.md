# Active Impersonation Review

**Generated:** 2026-05-15T08:36:21.691763+00:00

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
- Candidate domains audited: `5407`
- Visible findings kept: `5046`
- Canonical brand redirects filtered out: `361`
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
| 0 | 9 | 2154 | 848 | 2035 | 0 |

## Blocking Lists

Only `HIGH_MATCH` domains that do **not** canonical-redirect to the real brand are added to these exact-host blocklists.

| Output | Entries | File |
|--------|---------|------|
| Hosts | 0 | [categories/active_impersonation.txt](categories/active_impersonation.txt) |
| RPZ | 0 | [categories/active_impersonation.rpz](categories/active_impersonation.rpz) |

## Per-Target Summary

| Target | Seeds | Audited | Visible | Blocklist | Filtered Redirects | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|---------|-----------|--------------------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 182 | 182 | 0 | 0 | 0 | 0 | 92 | 78 | 0 |  |
| Amazon | 1 | 258 | 118 | 0 | 140 | 0 | 0 | 39 | 71 | 0 |  |
| Apple | 2 | 344 | 326 | 0 | 18 | 0 | 0 | 143 | 151 | 0 |  |
| Atlassian | 1 | 46 | 40 | 0 | 6 | 0 | 0 | 21 | 14 | 0 |  |
| Auth0 | 1 | 186 | 182 | 0 | 4 | 0 | 0 | 5 | 72 | 0 |  |
| Box | 1 | 103 | 103 | 0 | 0 | 0 | 0 | 71 | 27 | 0 |  |
| Cloudflare | 1 | 150 | 148 | 0 | 2 | 0 | 0 | 40 | 101 | 0 |  |
| Coinbase | 1 | 253 | 252 | 0 | 1 | 0 | 0 | 24 | 42 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 88 | 88 | 0 | 0 | 0 | 0 | 49 | 31 | 0 |  |
| DocuSign | 1 | 87 | 82 | 0 | 5 | 0 | 0 | 27 | 38 | 0 |  |
| Dropbox | 2 | 129 | 128 | 0 | 1 | 0 | 1 | 55 | 65 | 0 |  |
| Duo | 1 | 118 | 118 | 0 | 0 | 0 | 0 | 67 | 31 | 0 |  |
| FedEx | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Figma | 1 | 81 | 81 | 0 | 0 | 0 | 0 | 47 | 23 | 0 |  |
| GitHub | 1 | 155 | 149 | 0 | 6 | 0 | 0 | 71 | 59 | 0 |  |
| GitLab | 1 | 80 | 79 | 0 | 1 | 0 | 0 | 37 | 38 | 0 |  |
| Google | 2 | 564 | 553 | 0 | 11 | 0 | 8 | 187 | 304 | 0 |  |
| Intuit | 1 | 139 | 139 | 0 | 0 | 0 | 0 | 64 | 48 | 0 |  |
| Jira | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 69 | 25 | 0 |  |
| Microsoft | 5 | 941 | 872 | 0 | 69 | 0 | 0 | 402 | 390 | 0 |  |
| Notion | 1 | 11 | 11 | 0 | 0 | 0 | 0 | 8 | 1 | 0 |  |
| Okta | 1 | 111 | 111 | 0 | 0 | 0 | 0 | 62 | 33 | 0 |  |
| OneLogin | 1 | 31 | 31 | 0 | 0 | 0 | 0 | 12 | 14 | 0 |  |
| PayPal | 1 | 217 | 209 | 0 | 8 | 0 | 0 | 66 | 41 | 0 |  |
| Ping Identity | 1 | 29 | 29 | 0 | 0 | 0 | 0 | 1 | 27 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 116 | 101 | 0 | 15 | 0 | 0 | 37 | 51 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 177 | 137 | 0 | 40 | 0 | 0 | 92 | 26 | 0 |  |
| Slack | 1 | 90 | 90 | 0 | 0 | 0 | 0 | 53 | 24 | 0 |  |
| Stripe | 1 | 96 | 90 | 0 | 6 | 0 | 0 | 49 | 35 | 0 |  |
| Trello | 1 | 61 | 60 | 0 | 1 | 0 | 0 | 32 | 19 | 0 |  |
| TurboTax | 1 | 151 | 127 | 0 | 24 | 0 | 0 | 48 | 60 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 60 | 30 | 0 |  |
| Venmo | 1 | 74 | 73 | 0 | 1 | 0 | 0 | 37 | 23 | 0 |  |
| Zendesk | 1 | 60 | 58 | 0 | 2 | 0 | 0 | 35 | 21 | 0 |  |
| Zoom | 1 | 81 | 81 | 0 | 0 | 0 | 0 | 52 | 22 | 0 |  |
| eBay | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |

## Per-Target Blocking Lists

No block-worthy domains were emitted in this run.

## Top Suspicious Matches

| Target | Domain | Status | Score | Baseline | Redirect | Title | Content |
|--------|--------|--------|-------|----------|----------|-------|---------|
| Google | `xn--gogl-jpa1d.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogl-jpa1d.com` | 1.00 | 0.13 |
| Google | `xn--gogle-1ta.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-1ta.com` | 1.00 | 0.08 |
| Google | `xn--ooge-21a88g.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--ooge-21a88g.com` | 1.00 | 0.08 |
| Google | `xn--googl-lsa.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-lsa.com` | 1.00 | 0.05 |
| Google | `xn--gogle-g91b.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-g91b.com` | 1.00 | 0.04 |
| Google | `xn--goog-8va9v.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--goog-8va9v.com` | 1.00 | 0.04 |
| Google | `xn--googl-9cc.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-9cc.com` | 1.00 | 0.04 |
| Google | `xn--ooge-9wa5r.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--ooge-9wa5r.com` | 1.00 | 0.04 |
| Dropbox | `dr.opbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `dr.opbox.com` | 0.90 | 0.03 |

## Operational Notes

1. Canonical redirects to the real brand are intentionally excluded from both the report rows and the blocklists
2. The blocking lists are conservative and only include `HIGH_MATCH` domains
3. Review `MEDIUM_MATCH` findings manually before promoting them anywhere
4. Re-run the report when you regenerate hardening lists or change target coverage
