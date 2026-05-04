# Active Impersonation Review

**Generated:** 2026-05-04T08:19:19.032964+00:00

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
- Candidate domains audited: `5552`
- Visible findings kept: `5187`
- Canonical brand redirects filtered out: `365`
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
| 0 | 13 | 2565 | 915 | 1694 | 0 |

## Blocking Lists

Only `HIGH_MATCH` domains that do **not** canonical-redirect to the real brand are added to these exact-host blocklists.

| Output | Entries | File |
|--------|---------|------|
| Hosts | 0 | [categories/active_impersonation.txt](categories/active_impersonation.txt) |
| RPZ | 0 | [categories/active_impersonation.rpz](categories/active_impersonation.rpz) |

## Per-Target Summary

| Target | Seeds | Audited | Visible | Blocklist | Filtered Redirects | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|---------|-----------|--------------------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 181 | 181 | 0 | 0 | 0 | 0 | 89 | 75 | 0 |  |
| Amazon | 1 | 258 | 118 | 0 | 140 | 0 | 0 | 38 | 72 | 0 |  |
| Apple | 2 | 344 | 326 | 0 | 18 | 0 | 0 | 158 | 132 | 0 |  |
| Atlassian | 1 | 47 | 42 | 0 | 5 | 0 | 0 | 25 | 8 | 0 |  |
| Auth0 | 1 | 188 | 184 | 0 | 4 | 0 | 0 | 5 | 73 | 0 |  |
| Box | 1 | 103 | 103 | 0 | 0 | 0 | 0 | 68 | 29 | 0 |  |
| Cloudflare | 1 | 153 | 151 | 0 | 2 | 0 | 0 | 53 | 92 | 0 |  |
| Coinbase | 1 | 253 | 252 | 0 | 1 | 0 | 0 | 32 | 36 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 88 | 88 | 0 | 0 | 0 | 0 | 45 | 28 | 0 |  |
| DocuSign | 1 | 88 | 83 | 0 | 5 | 0 | 0 | 48 | 22 | 0 |  |
| Dropbox | 2 | 129 | 128 | 0 | 1 | 0 | 4 | 80 | 40 | 0 |  |
| Duo | 1 | 118 | 118 | 0 | 0 | 0 | 0 | 73 | 26 | 0 |  |
| FedEx | 1 | 120 | 120 | 0 | 0 | 0 | 0 | 56 | 53 | 0 |  |
| Figma | 1 | 81 | 81 | 0 | 0 | 0 | 0 | 48 | 17 | 0 |  |
| GitHub | 1 | 162 | 156 | 0 | 6 | 0 | 0 | 94 | 45 | 0 |  |
| GitLab | 1 | 82 | 81 | 0 | 1 | 0 | 0 | 40 | 37 | 0 |  |
| Google | 2 | 566 | 555 | 0 | 11 | 0 | 9 | 228 | 260 | 0 |  |
| Intuit | 1 | 141 | 141 | 0 | 0 | 0 | 0 | 71 | 44 | 0 |  |
| Jira | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 72 | 17 | 0 |  |
| Microsoft | 5 | 935 | 867 | 0 | 68 | 0 | 0 | 508 | 261 | 0 |  |
| Notion | 1 | 13 | 13 | 0 | 0 | 0 | 0 | 11 | 0 | 0 |  |
| Okta | 1 | 111 | 111 | 0 | 0 | 0 | 0 | 64 | 31 | 0 |  |
| OneLogin | 1 | 32 | 32 | 0 | 0 | 0 | 0 | 16 | 13 | 0 |  |
| PayPal | 1 | 216 | 207 | 0 | 9 | 0 | 0 | 86 | 16 | 0 |  |
| Ping Identity | 1 | 29 | 29 | 0 | 0 | 0 | 0 | 1 | 26 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 119 | 104 | 0 | 15 | 0 | 0 | 53 | 38 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 175 | 130 | 0 | 45 | 0 | 0 | 92 | 21 | 0 |  |
| Slack | 1 | 92 | 92 | 0 | 0 | 0 | 0 | 51 | 22 | 0 |  |
| Stripe | 1 | 98 | 92 | 0 | 6 | 0 | 0 | 53 | 25 | 0 |  |
| Trello | 1 | 61 | 60 | 0 | 1 | 0 | 0 | 35 | 11 | 0 |  |
| TurboTax | 1 | 151 | 127 | 0 | 24 | 0 | 0 | 65 | 48 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 100 | 100 | 0 | 0 | 0 | 0 | 66 | 23 | 0 |  |
| Venmo | 1 | 74 | 73 | 0 | 1 | 0 | 0 | 39 | 17 | 0 |  |
| Zendesk | 1 | 63 | 61 | 0 | 2 | 0 | 0 | 39 | 21 | 0 |  |
| Zoom | 1 | 82 | 82 | 0 | 0 | 0 | 0 | 63 | 15 | 0 |  |
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
