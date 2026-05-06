# Active Impersonation Review

**Generated:** 2026-05-06T08:08:12.927646+00:00

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
- Candidate domains audited: `5547`
- Visible findings kept: `5187`
- Canonical brand redirects filtered out: `360`
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
| 0 | 13 | 2595 | 881 | 1698 | 0 |

## Blocking Lists

Only `HIGH_MATCH` domains that do **not** canonical-redirect to the real brand are added to these exact-host blocklists.

| Output | Entries | File |
|--------|---------|------|
| Hosts | 0 | [categories/active_impersonation.txt](categories/active_impersonation.txt) |
| RPZ | 0 | [categories/active_impersonation.rpz](categories/active_impersonation.rpz) |

## Per-Target Summary

| Target | Seeds | Audited | Visible | Blocklist | Filtered Redirects | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|---------|-----------|--------------------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 181 | 181 | 0 | 0 | 0 | 0 | 95 | 73 | 0 |  |
| Amazon | 1 | 258 | 118 | 0 | 140 | 0 | 0 | 39 | 70 | 0 |  |
| Apple | 2 | 345 | 327 | 0 | 18 | 0 | 0 | 163 | 133 | 0 |  |
| Atlassian | 1 | 47 | 42 | 0 | 5 | 0 | 0 | 29 | 9 | 0 |  |
| Auth0 | 1 | 187 | 183 | 0 | 4 | 0 | 0 | 5 | 73 | 0 |  |
| Box | 1 | 103 | 103 | 0 | 0 | 0 | 0 | 72 | 27 | 0 |  |
| Cloudflare | 1 | 153 | 151 | 0 | 2 | 0 | 0 | 54 | 91 | 0 |  |
| Coinbase | 1 | 253 | 252 | 0 | 1 | 0 | 0 | 32 | 36 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 88 | 88 | 0 | 0 | 0 | 0 | 51 | 27 | 0 |  |
| DocuSign | 1 | 88 | 83 | 0 | 5 | 0 | 0 | 48 | 23 | 0 |  |
| Dropbox | 2 | 129 | 128 | 0 | 1 | 0 | 4 | 78 | 39 | 0 |  |
| Duo | 1 | 119 | 119 | 0 | 0 | 0 | 0 | 76 | 28 | 0 |  |
| FedEx | 1 | 121 | 121 | 0 | 0 | 0 | 0 | 10 | 54 | 0 |  |
| Figma | 1 | 82 | 82 | 0 | 0 | 0 | 0 | 54 | 18 | 0 |  |
| GitHub | 1 | 162 | 156 | 0 | 6 | 0 | 0 | 94 | 47 | 0 |  |
| GitLab | 1 | 83 | 82 | 0 | 1 | 0 | 0 | 39 | 39 | 0 |  |
| Google | 2 | 565 | 554 | 0 | 11 | 0 | 9 | 232 | 259 | 0 |  |
| Intuit | 1 | 140 | 140 | 0 | 0 | 0 | 0 | 71 | 45 | 0 |  |
| Jira | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 77 | 17 | 0 |  |
| Microsoft | 5 | 933 | 865 | 0 | 68 | 0 | 0 | 513 | 265 | 0 |  |
| Notion | 1 | 13 | 13 | 0 | 0 | 0 | 0 | 9 | 1 | 0 |  |
| Okta | 1 | 110 | 110 | 0 | 0 | 0 | 0 | 64 | 30 | 0 |  |
| OneLogin | 1 | 32 | 32 | 0 | 0 | 0 | 0 | 17 | 12 | 0 |  |
| PayPal | 1 | 216 | 207 | 0 | 9 | 0 | 0 | 89 | 15 | 0 |  |
| Ping Identity | 1 | 29 | 29 | 0 | 0 | 0 | 0 | 1 | 26 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 116 | 101 | 0 | 15 | 0 | 0 | 50 | 38 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 177 | 137 | 0 | 40 | 0 | 0 | 98 | 23 | 0 |  |
| Slack | 1 | 92 | 92 | 0 | 0 | 0 | 0 | 56 | 24 | 0 |  |
| Stripe | 1 | 98 | 92 | 0 | 6 | 0 | 0 | 60 | 25 | 0 |  |
| Trello | 1 | 61 | 60 | 0 | 1 | 0 | 0 | 39 | 11 | 0 |  |
| TurboTax | 1 | 151 | 127 | 0 | 24 | 0 | 0 | 63 | 50 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 70 | 23 | 0 |  |
| Venmo | 1 | 74 | 73 | 0 | 1 | 0 | 0 | 41 | 17 | 0 |  |
| Zendesk | 1 | 62 | 60 | 0 | 2 | 0 | 0 | 42 | 17 | 0 |  |
| Zoom | 1 | 81 | 81 | 0 | 0 | 0 | 0 | 64 | 13 | 0 |  |
| eBay | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |

## Per-Target Blocking Lists

No block-worthy domains were emitted in this run.

## Top Suspicious Matches

| Target | Domain | Status | Score | Baseline | Redirect | Title | Content |
|--------|--------|--------|-------|----------|----------|-------|---------|
| Google | `xn--gogl-jpa1d.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogl-jpa1d.com` | 1.00 | 0.12 |
| Google | `xn--gogle-1ta.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-1ta.com` | 1.00 | 0.08 |
| Google | `xn--ooge-21a88g.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--ooge-21a88g.com` | 1.00 | 0.08 |
| Google | `xn--gogle-g91b.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-g91b.com` | 1.00 | 0.05 |
| Google | `xn--googl-lsa.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-lsa.com` | 1.00 | 0.05 |
| Google | `xn--goog-8va9v.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--goog-8va9v.com` | 1.00 | 0.04 |
| Google | `xn--googl-9cc.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-9cc.com` | 1.00 | 0.04 |
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
