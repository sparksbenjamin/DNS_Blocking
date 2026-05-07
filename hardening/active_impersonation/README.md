# Active Impersonation Review

**Generated:** 2026-05-07T08:19:53.642210+00:00

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
- Candidate domains audited: `5460`
- Visible findings kept: `5093`
- Canonical brand redirects filtered out: `367`
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
| 0 | 13 | 2485 | 834 | 1761 | 0 |

## Blocking Lists

Only `HIGH_MATCH` domains that do **not** canonical-redirect to the real brand are added to these exact-host blocklists.

| Output | Entries | File |
|--------|---------|------|
| Hosts | 0 | [categories/active_impersonation.txt](categories/active_impersonation.txt) |
| RPZ | 0 | [categories/active_impersonation.rpz](categories/active_impersonation.rpz) |

## Per-Target Summary

| Target | Seeds | Audited | Visible | Blocklist | Filtered Redirects | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|---------|-----------|--------------------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 175 | 175 | 0 | 0 | 0 | 0 | 88 | 73 | 0 |  |
| Amazon | 1 | 257 | 117 | 0 | 140 | 0 | 0 | 36 | 72 | 0 |  |
| Apple | 2 | 342 | 324 | 0 | 18 | 0 | 0 | 160 | 135 | 0 |  |
| Atlassian | 1 | 43 | 38 | 0 | 5 | 0 | 0 | 26 | 9 | 0 |  |
| Auth0 | 1 | 185 | 181 | 0 | 4 | 0 | 0 | 4 | 72 | 0 |  |
| Box | 1 | 102 | 102 | 0 | 0 | 0 | 0 | 68 | 29 | 0 |  |
| Cloudflare | 1 | 146 | 144 | 0 | 2 | 0 | 0 | 47 | 92 | 0 |  |
| Coinbase | 1 | 250 | 249 | 0 | 1 | 0 | 0 | 30 | 33 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 86 | 86 | 0 | 0 | 0 | 0 | 47 | 30 | 0 |  |
| DocuSign | 1 | 87 | 82 | 0 | 5 | 0 | 0 | 51 | 20 | 0 |  |
| Dropbox | 2 | 124 | 123 | 0 | 1 | 0 | 4 | 77 | 40 | 0 |  |
| Duo | 1 | 118 | 118 | 0 | 0 | 0 | 0 | 75 | 27 | 0 |  |
| FedEx | 1 | 120 | 120 | 0 | 0 | 0 | 0 | 54 | 55 | 0 |  |
| Figma | 1 | 79 | 79 | 0 | 0 | 0 | 0 | 48 | 22 | 0 |  |
| GitHub | 1 | 157 | 151 | 0 | 6 | 0 | 0 | 88 | 47 | 0 |  |
| GitLab | 1 | 77 | 76 | 0 | 1 | 0 | 0 | 37 | 35 | 0 |  |
| Google | 2 | 561 | 550 | 0 | 11 | 0 | 9 | 224 | 261 | 0 |  |
| Intuit | 1 | 140 | 140 | 0 | 0 | 0 | 0 | 68 | 47 | 0 |  |
| Jira | 1 | 96 | 96 | 0 | 0 | 0 | 0 | 70 | 22 | 0 |  |
| Microsoft | 5 | 924 | 856 | 0 | 68 | 0 | 0 | 481 | 285 | 0 |  |
| Notion | 1 | 13 | 13 | 0 | 0 | 0 | 0 | 9 | 0 | 0 |  |
| Okta | 1 | 109 | 109 | 0 | 0 | 0 | 0 | 62 | 33 | 0 |  |
| OneLogin | 1 | 32 | 32 | 0 | 0 | 0 | 0 | 16 | 13 | 0 |  |
| PayPal | 1 | 215 | 206 | 0 | 9 | 0 | 0 | 86 | 16 | 0 |  |
| Ping Identity | 1 | 29 | 29 | 0 | 0 | 0 | 0 | 1 | 26 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 116 | 101 | 0 | 15 | 0 | 0 | 48 | 40 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 176 | 129 | 0 | 47 | 0 | 0 | 92 | 22 | 0 |  |
| Slack | 1 | 89 | 89 | 0 | 0 | 0 | 0 | 56 | 22 | 0 |  |
| Stripe | 1 | 96 | 90 | 0 | 6 | 0 | 0 | 57 | 24 | 0 |  |
| Trello | 1 | 58 | 57 | 0 | 1 | 0 | 0 | 35 | 13 | 0 |  |
| TurboTax | 1 | 151 | 127 | 0 | 24 | 0 | 0 | 49 | 65 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 97 | 97 | 0 | 0 | 0 | 0 | 64 | 26 | 0 |  |
| Venmo | 1 | 72 | 71 | 0 | 1 | 0 | 0 | 41 | 17 | 0 |  |
| Zendesk | 1 | 57 | 55 | 0 | 2 | 0 | 0 | 37 | 16 | 0 |  |
| Zoom | 1 | 81 | 81 | 0 | 0 | 0 | 0 | 53 | 22 | 0 |  |
| eBay | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |

## Per-Target Blocking Lists

No block-worthy domains were emitted in this run.

## Top Suspicious Matches

| Target | Domain | Status | Score | Baseline | Redirect | Title | Content |
|--------|--------|--------|-------|----------|----------|-------|---------|
| Google | `xn--gogl-jpa1d.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogl-jpa1d.com` | 1.00 | 0.12 |
| Google | `xn--gogle-1ta.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-1ta.com` | 1.00 | 0.07 |
| Google | `xn--googl-9cc.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-9cc.com` | 1.00 | 0.07 |
| Google | `xn--ooge-21a88g.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--ooge-21a88g.com` | 1.00 | 0.07 |
| Google | `xn--googl-lsa.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-lsa.com` | 1.00 | 0.05 |
| Google | `xn--gogle-g91b.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-g91b.com` | 1.00 | 0.04 |
| Google | `xn--goog-8va9v.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--goog-8va9v.com` | 1.00 | 0.03 |
| Google | `xn--googe-m6a.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googe-m6a.com` | 1.00 | 0.03 |
| Google | `xn--ooge-9wa5r.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--ooge-9wa5r.com` | 1.00 | 0.03 |
| Dropbox | `dr.opbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `dr.opbox.com` | 0.90 | 0.02 |
| Dropbox | `d.ropbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `d.ropbox.com` | 0.95 | 0.01 |
| Dropbox | `ropbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `ropbox.com` | 0.95 | 0.01 |
| Dropbox | `tropbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `tropbox.com` | 0.91 | 0.01 |

## Operational Notes

1. Canonical redirects to the real brand are intentionally excluded from both the report rows and the blocklists
2. The blocking lists are conservative and only include `HIGH_MATCH` domains
3. Review `MEDIUM_MATCH` findings manually before promoting them anywhere
4. Re-run the report when you regenerate hardening lists or change target coverage
