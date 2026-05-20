# Active Impersonation Review

**Generated:** 2026-05-20T08:55:53.447503+00:00

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
- Candidate domains audited: `5564`
- Visible findings kept: `5201`
- Canonical brand redirects filtered out: `363`
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
| 0 | 9 | 2180 | 891 | 2121 | 0 |

## Blocking Lists

Only `HIGH_MATCH` domains that do **not** canonical-redirect to the real brand are added to these exact-host blocklists.

| Output | Entries | File |
|--------|---------|------|
| Hosts | 0 | [categories/active_impersonation.txt](categories/active_impersonation.txt) |
| RPZ | 0 | [categories/active_impersonation.rpz](categories/active_impersonation.rpz) |

## Per-Target Summary

| Target | Seeds | Audited | Visible | Blocklist | Filtered Redirects | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|---------|-----------|--------------------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 184 | 184 | 0 | 0 | 0 | 0 | 88 | 79 | 0 |  |
| Amazon | 1 | 258 | 118 | 0 | 140 | 0 | 0 | 36 | 72 | 0 |  |
| Apple | 2 | 345 | 327 | 0 | 18 | 0 | 0 | 143 | 149 | 0 |  |
| Atlassian | 1 | 47 | 42 | 0 | 5 | 0 | 0 | 23 | 15 | 0 |  |
| Auth0 | 1 | 186 | 182 | 0 | 4 | 0 | 0 | 5 | 72 | 0 |  |
| Box | 1 | 102 | 102 | 0 | 0 | 0 | 0 | 71 | 28 | 0 |  |
| Cloudflare | 1 | 153 | 151 | 0 | 2 | 0 | 0 | 42 | 100 | 0 |  |
| Coinbase | 1 | 258 | 257 | 0 | 1 | 0 | 0 | 28 | 45 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 87 | 87 | 0 | 0 | 0 | 0 | 49 | 30 | 0 |  |
| DocuSign | 1 | 89 | 84 | 0 | 5 | 0 | 0 | 32 | 42 | 0 |  |
| Dropbox | 2 | 131 | 130 | 0 | 1 | 0 | 1 | 58 | 66 | 0 |  |
| Duo | 1 | 120 | 120 | 0 | 0 | 0 | 0 | 73 | 30 | 0 |  |
| FedEx | 1 | 128 | 128 | 0 | 0 | 0 | 0 | 4 | 68 | 0 |  |
| Figma | 1 | 83 | 83 | 0 | 0 | 0 | 0 | 47 | 27 | 0 |  |
| GitHub | 1 | 156 | 150 | 0 | 6 | 0 | 0 | 73 | 58 | 0 |  |
| GitLab | 1 | 83 | 82 | 0 | 1 | 0 | 0 | 37 | 40 | 0 |  |
| Google | 2 | 566 | 555 | 0 | 11 | 0 | 8 | 175 | 313 | 0 |  |
| Intuit | 1 | 140 | 140 | 0 | 0 | 0 | 0 | 64 | 52 | 0 |  |
| Jira | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 69 | 26 | 0 |  |
| Microsoft | 5 | 939 | 870 | 0 | 69 | 0 | 0 | 409 | 380 | 0 |  |
| Notion | 1 | 12 | 12 | 0 | 0 | 0 | 0 | 6 | 5 | 0 |  |
| Okta | 1 | 111 | 111 | 0 | 0 | 0 | 0 | 61 | 35 | 0 |  |
| OneLogin | 1 | 32 | 32 | 0 | 0 | 0 | 0 | 12 | 16 | 0 |  |
| PayPal | 1 | 213 | 205 | 0 | 8 | 0 | 0 | 63 | 41 | 0 |  |
| Ping Identity | 1 | 31 | 31 | 0 | 0 | 0 | 0 | 1 | 29 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 117 | 102 | 0 | 15 | 0 | 0 | 39 | 50 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 178 | 135 | 0 | 43 | 0 | 0 | 89 | 27 | 0 |  |
| Slack | 1 | 90 | 90 | 0 | 0 | 0 | 0 | 54 | 23 | 0 |  |
| Stripe | 1 | 98 | 92 | 0 | 6 | 0 | 0 | 51 | 35 | 0 |  |
| Trello | 1 | 60 | 59 | 0 | 1 | 0 | 0 | 32 | 18 | 0 |  |
| TurboTax | 1 | 151 | 127 | 0 | 24 | 0 | 0 | 68 | 44 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 100 | 100 | 0 | 0 | 0 | 0 | 53 | 37 | 0 |  |
| Venmo | 1 | 73 | 72 | 0 | 1 | 0 | 0 | 35 | 21 | 0 |  |
| Zendesk | 1 | 63 | 61 | 0 | 2 | 0 | 0 | 36 | 24 | 0 |  |
| Zoom | 1 | 81 | 81 | 0 | 0 | 0 | 0 | 54 | 24 | 0 |  |
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
