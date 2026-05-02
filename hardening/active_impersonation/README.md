# Active Impersonation Review

**Generated:** 2026-05-02T07:26:23.178915+00:00

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
- Candidate domains audited: `5524`
- Visible findings kept: `5152`
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
| 0 | 13 | 2481 | 919 | 1739 | 0 |

## Blocking Lists

Only `HIGH_MATCH` domains that do **not** canonical-redirect to the real brand are added to these exact-host blocklists.

| Output | Entries | File |
|--------|---------|------|
| Hosts | 0 | [categories/active_impersonation.txt](categories/active_impersonation.txt) |
| RPZ | 0 | [categories/active_impersonation.rpz](categories/active_impersonation.rpz) |

## Per-Target Summary

| Target | Seeds | Audited | Visible | Blocklist | Filtered Redirects | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|---------|-----------|--------------------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 182 | 182 | 0 | 0 | 0 | 0 | 90 | 77 | 0 |  |
| Amazon | 1 | 258 | 118 | 0 | 140 | 0 | 0 | 39 | 71 | 0 |  |
| Apple | 2 | 344 | 326 | 0 | 18 | 0 | 0 | 160 | 135 | 0 |  |
| Atlassian | 1 | 47 | 41 | 0 | 6 | 0 | 0 | 25 | 9 | 0 |  |
| Auth0 | 1 | 188 | 184 | 0 | 4 | 0 | 0 | 3 | 75 | 0 |  |
| Box | 1 | 103 | 103 | 0 | 0 | 0 | 0 | 68 | 26 | 0 |  |
| Cloudflare | 1 | 144 | 142 | 0 | 2 | 0 | 0 | 45 | 90 | 0 |  |
| Coinbase | 1 | 249 | 248 | 0 | 1 | 0 | 0 | 33 | 33 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 88 | 88 | 0 | 0 | 0 | 0 | 43 | 29 | 0 |  |
| DocuSign | 1 | 87 | 82 | 0 | 5 | 0 | 0 | 48 | 22 | 0 |  |
| Dropbox | 2 | 129 | 128 | 0 | 1 | 0 | 4 | 79 | 41 | 0 |  |
| Duo | 1 | 119 | 119 | 0 | 0 | 0 | 0 | 61 | 28 | 0 |  |
| FedEx | 1 | 118 | 118 | 0 | 0 | 0 | 0 | 48 | 51 | 0 |  |
| Figma | 1 | 82 | 82 | 0 | 0 | 0 | 0 | 44 | 24 | 0 |  |
| GitHub | 1 | 162 | 156 | 0 | 6 | 0 | 0 | 92 | 44 | 0 |  |
| GitLab | 1 | 80 | 79 | 0 | 1 | 0 | 0 | 30 | 44 | 0 |  |
| Google | 2 | 565 | 554 | 0 | 11 | 0 | 9 | 225 | 261 | 0 |  |
| Intuit | 1 | 139 | 139 | 0 | 0 | 0 | 0 | 72 | 43 | 0 |  |
| Jira | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 69 | 21 | 0 |  |
| Microsoft | 5 | 937 | 868 | 0 | 69 | 0 | 0 | 505 | 272 | 0 |  |
| Notion | 1 | 13 | 13 | 0 | 0 | 0 | 0 | 10 | 0 | 0 |  |
| Okta | 1 | 109 | 109 | 0 | 0 | 0 | 0 | 62 | 31 | 0 |  |
| OneLogin | 1 | 32 | 32 | 0 | 0 | 0 | 0 | 16 | 13 | 0 |  |
| PayPal | 1 | 215 | 206 | 0 | 9 | 0 | 0 | 86 | 17 | 0 |  |
| Ping Identity | 1 | 29 | 29 | 0 | 0 | 0 | 0 | 1 | 26 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 118 | 103 | 0 | 15 | 0 | 0 | 51 | 40 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 177 | 127 | 0 | 50 | 0 | 0 | 81 | 25 | 0 |  |
| Slack | 1 | 92 | 92 | 0 | 0 | 0 | 0 | 53 | 27 | 0 |  |
| Stripe | 1 | 95 | 89 | 0 | 6 | 0 | 0 | 54 | 26 | 0 |  |
| Trello | 1 | 61 | 60 | 0 | 1 | 0 | 0 | 33 | 11 | 0 |  |
| TurboTax | 1 | 148 | 124 | 0 | 24 | 0 | 0 | 66 | 46 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 98 | 98 | 0 | 0 | 0 | 0 | 55 | 25 | 0 |  |
| Venmo | 1 | 74 | 73 | 0 | 1 | 0 | 0 | 38 | 22 | 0 |  |
| Zendesk | 1 | 61 | 59 | 0 | 2 | 0 | 0 | 37 | 20 | 0 |  |
| Zoom | 1 | 82 | 82 | 0 | 0 | 0 | 0 | 59 | 14 | 0 |  |
| eBay | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |

## Per-Target Blocking Lists

No block-worthy domains were emitted in this run.

## Top Suspicious Matches

| Target | Domain | Status | Score | Baseline | Redirect | Title | Content |
|--------|--------|--------|-------|----------|----------|-------|---------|
| Google | `xn--gogl-jpa1d.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogl-jpa1d.com` | 1.00 | 0.13 |
| Google | `xn--gogle-1ta.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-1ta.com` | 1.00 | 0.10 |
| Google | `xn--ooge-21a88g.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--ooge-21a88g.com` | 1.00 | 0.10 |
| Google | `xn--googl-9cc.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-9cc.com` | 1.00 | 0.05 |
| Google | `xn--googl-lsa.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-lsa.com` | 1.00 | 0.05 |
| Google | `xn--gogle-g91b.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-g91b.com` | 1.00 | 0.04 |
| Google | `xn--goog-8va9v.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--goog-8va9v.com` | 1.00 | 0.04 |
| Google | `xn--ooge-9wa5r.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--ooge-9wa5r.com` | 1.00 | 0.04 |
| Google | `xn--googe-m6a.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googe-m6a.com` | 1.00 | 0.03 |
| Dropbox | `dr.opbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `dr.opbox.com` | 0.90 | 0.02 |
| Dropbox | `d.ropbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `d.ropbox.com` | 0.95 | 0.01 |
| Dropbox | `ropbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `ropbox.com` | 0.95 | 0.01 |
| Dropbox | `tropbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `tropbox.com` | 0.91 | 0.01 |

## Operational Notes

1. Canonical redirects to the real brand are intentionally excluded from both the report rows and the blocklists
2. The blocking lists are conservative and only include `HIGH_MATCH` domains
3. Review `MEDIUM_MATCH` findings manually before promoting them anywhere
4. Re-run the report when you regenerate hardening lists or change target coverage
