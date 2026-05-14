# Active Impersonation Review

**Generated:** 2026-05-14T08:22:18.572157+00:00

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
- Candidate domains audited: `5529`
- Visible findings kept: `5177`
- Canonical brand redirects filtered out: `352`
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
| 0 | 9 | 2200 | 915 | 2053 | 0 |

## Blocking Lists

Only `HIGH_MATCH` domains that do **not** canonical-redirect to the real brand are added to these exact-host blocklists.

| Output | Entries | File |
|--------|---------|------|
| Hosts | 0 | [categories/active_impersonation.txt](categories/active_impersonation.txt) |
| RPZ | 0 | [categories/active_impersonation.rpz](categories/active_impersonation.rpz) |

## Per-Target Summary

| Target | Seeds | Audited | Visible | Blocklist | Filtered Redirects | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|---------|-----------|--------------------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 182 | 182 | 0 | 0 | 0 | 0 | 94 | 76 | 0 |  |
| Amazon | 1 | 258 | 118 | 0 | 140 | 0 | 0 | 36 | 73 | 0 |  |
| Apple | 2 | 344 | 326 | 0 | 18 | 0 | 0 | 145 | 147 | 0 |  |
| Atlassian | 1 | 46 | 40 | 0 | 6 | 0 | 0 | 23 | 14 | 0 |  |
| Auth0 | 1 | 186 | 182 | 0 | 4 | 0 | 0 | 4 | 72 | 0 |  |
| Box | 1 | 103 | 103 | 0 | 0 | 0 | 0 | 71 | 26 | 0 |  |
| Cloudflare | 1 | 150 | 148 | 0 | 2 | 0 | 0 | 46 | 98 | 0 |  |
| Coinbase | 1 | 253 | 252 | 0 | 1 | 0 | 0 | 28 | 38 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 88 | 88 | 0 | 0 | 0 | 0 | 48 | 30 | 0 |  |
| DocuSign | 1 | 87 | 82 | 0 | 5 | 0 | 0 | 32 | 36 | 0 |  |
| Dropbox | 2 | 129 | 128 | 0 | 1 | 0 | 1 | 56 | 61 | 0 |  |
| Duo | 1 | 118 | 118 | 0 | 0 | 0 | 0 | 70 | 31 | 0 |  |
| FedEx | 1 | 122 | 122 | 0 | 0 | 0 | 0 | 3 | 60 | 0 |  |
| Figma | 1 | 81 | 81 | 0 | 0 | 0 | 0 | 46 | 25 | 0 |  |
| GitHub | 1 | 155 | 149 | 0 | 6 | 0 | 0 | 67 | 60 | 0 |  |
| GitLab | 1 | 80 | 79 | 0 | 1 | 0 | 0 | 35 | 39 | 0 |  |
| Google | 2 | 564 | 553 | 0 | 11 | 0 | 8 | 180 | 308 | 0 |  |
| Intuit | 1 | 139 | 139 | 0 | 0 | 0 | 0 | 67 | 45 | 0 |  |
| Jira | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 67 | 25 | 0 |  |
| Microsoft | 5 | 941 | 872 | 0 | 69 | 0 | 0 | 402 | 387 | 0 |  |
| Notion | 1 | 11 | 11 | 0 | 0 | 0 | 0 | 8 | 1 | 0 |  |
| Okta | 1 | 111 | 111 | 0 | 0 | 0 | 0 | 60 | 36 | 0 |  |
| OneLogin | 1 | 31 | 31 | 0 | 0 | 0 | 0 | 13 | 13 | 0 |  |
| PayPal | 1 | 217 | 209 | 0 | 8 | 0 | 0 | 68 | 38 | 0 |  |
| Ping Identity | 1 | 29 | 29 | 0 | 0 | 0 | 0 | 1 | 26 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 116 | 101 | 0 | 15 | 0 | 0 | 36 | 51 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 177 | 146 | 0 | 31 | 0 | 0 | 103 | 27 | 0 |  |
| Slack | 1 | 90 | 90 | 0 | 0 | 0 | 0 | 52 | 26 | 0 |  |
| Stripe | 1 | 96 | 90 | 0 | 6 | 0 | 0 | 52 | 31 | 0 |  |
| Trello | 1 | 61 | 60 | 0 | 1 | 0 | 0 | 33 | 18 | 0 |  |
| TurboTax | 1 | 151 | 127 | 0 | 24 | 0 | 0 | 75 | 34 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 59 | 31 | 0 |  |
| Venmo | 1 | 74 | 73 | 0 | 1 | 0 | 0 | 38 | 22 | 0 |  |
| Zendesk | 1 | 60 | 58 | 0 | 2 | 0 | 0 | 33 | 23 | 0 |  |
| Zoom | 1 | 81 | 81 | 0 | 0 | 0 | 0 | 49 | 25 | 0 |  |
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
