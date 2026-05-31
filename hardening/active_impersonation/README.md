# Active Impersonation Review

**Generated:** 2026-05-31T08:41:32.531022+00:00

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
- Candidate domains audited: `5428`
- Visible findings kept: `5059`
- Canonical brand redirects filtered out: `369`
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
| 0 | 19 | 2151 | 854 | 2035 | 0 |

## Blocking Lists

Only `HIGH_MATCH` domains that do **not** canonical-redirect to the real brand are added to these exact-host blocklists.

| Output | Entries | File |
|--------|---------|------|
| Hosts | 0 | [categories/active_impersonation.txt](categories/active_impersonation.txt) |
| RPZ | 0 | [categories/active_impersonation.rpz](categories/active_impersonation.rpz) |

## Per-Target Summary

| Target | Seeds | Audited | Visible | Blocklist | Filtered Redirects | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|---------|-----------|--------------------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 181 | 181 | 0 | 0 | 0 | 0 | 88 | 78 | 0 |  |
| Amazon | 1 | 259 | 119 | 0 | 140 | 0 | 0 | 37 | 71 | 0 |  |
| Apple | 2 | 347 | 329 | 0 | 18 | 0 | 0 | 146 | 147 | 0 |  |
| Atlassian | 1 | 47 | 42 | 0 | 5 | 0 | 0 | 25 | 11 | 0 |  |
| Auth0 | 1 | 187 | 183 | 0 | 4 | 0 | 0 | 4 | 73 | 0 |  |
| Box | 1 | 103 | 103 | 0 | 0 | 0 | 0 | 73 | 26 | 0 |  |
| Cloudflare | 1 | 164 | 162 | 0 | 2 | 0 | 9 | 40 | 106 | 0 |  |
| Coinbase | 1 | 255 | 254 | 0 | 1 | 0 | 0 | 32 | 40 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 88 | 88 | 0 | 0 | 0 | 0 | 48 | 32 | 0 |  |
| DocuSign | 1 | 90 | 85 | 0 | 5 | 0 | 0 | 27 | 46 | 0 |  |
| Dropbox | 2 | 133 | 132 | 0 | 1 | 0 | 1 | 59 | 63 | 0 |  |
| Duo | 1 | 120 | 120 | 0 | 0 | 0 | 0 | 71 | 30 | 0 |  |
| FedEx | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Figma | 1 | 83 | 83 | 0 | 0 | 0 | 0 | 45 | 27 | 0 |  |
| GitHub | 1 | 156 | 150 | 0 | 6 | 0 | 0 | 73 | 59 | 0 |  |
| GitLab | 1 | 81 | 80 | 0 | 1 | 0 | 0 | 36 | 40 | 0 |  |
| Google | 2 | 562 | 551 | 0 | 11 | 0 | 9 | 183 | 301 | 0 |  |
| Intuit | 1 | 140 | 140 | 0 | 0 | 0 | 0 | 62 | 55 | 0 |  |
| Jira | 1 | 100 | 100 | 0 | 0 | 0 | 0 | 70 | 26 | 0 |  |
| Microsoft | 5 | 928 | 859 | 0 | 69 | 0 | 0 | 393 | 381 | 0 |  |
| Notion | 1 | 10 | 10 | 0 | 0 | 0 | 0 | 7 | 1 | 0 |  |
| Okta | 1 | 109 | 108 | 0 | 1 | 0 | 0 | 61 | 31 | 0 |  |
| OneLogin | 1 | 31 | 31 | 0 | 0 | 0 | 0 | 13 | 14 | 0 |  |
| PayPal | 1 | 213 | 205 | 0 | 8 | 0 | 0 | 59 | 42 | 0 |  |
| Ping Identity | 1 | 31 | 31 | 0 | 0 | 0 | 0 | 1 | 29 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 117 | 102 | 0 | 15 | 0 | 0 | 36 | 50 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 179 | 131 | 0 | 48 | 0 | 0 | 88 | 25 | 0 |  |
| Slack | 1 | 91 | 91 | 0 | 0 | 0 | 0 | 54 | 26 | 0 |  |
| Stripe | 1 | 98 | 92 | 0 | 6 | 0 | 0 | 51 | 33 | 0 |  |
| Trello | 1 | 60 | 59 | 0 | 1 | 0 | 0 | 33 | 17 | 0 |  |
| TurboTax | 1 | 150 | 126 | 0 | 24 | 0 | 0 | 49 | 61 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 100 | 100 | 0 | 0 | 0 | 0 | 60 | 32 | 0 |  |
| Venmo | 1 | 75 | 74 | 0 | 1 | 0 | 0 | 36 | 22 | 0 |  |
| Zendesk | 1 | 59 | 57 | 0 | 2 | 0 | 0 | 35 | 20 | 0 |  |
| Zoom | 1 | 81 | 81 | 0 | 0 | 0 | 0 | 56 | 20 | 0 |  |
| eBay | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |

## Per-Target Blocking Lists

No block-worthy domains were emitted in this run.

## Top Suspicious Matches

| Target | Domain | Status | Score | Baseline | Redirect | Title | Content |
|--------|--------|--------|-------|----------|----------|-------|---------|
| Cloudflare | `clojdflare.com` | MEDIUM_MATCH | 3 | `cloudflare.com` | `clojdflare.com` | 1.00 | 0.54 |
| Cloudflare | `cloucflare.com` | MEDIUM_MATCH | 3 | `cloudflare.com` | `cloucflare.com` | 1.00 | 0.54 |
| Cloudflare | `cloudfkare.com` | MEDIUM_MATCH | 3 | `cloudflare.com` | `cloudfkare.com` | 1.00 | 0.54 |
| Cloudflare | `cloudflafe.com` | MEDIUM_MATCH | 3 | `cloudflare.com` | `cloudflafe.com` | 1.00 | 0.54 |
| Cloudflare | `cooudflare.com` | MEDIUM_MATCH | 3 | `cloudflare.com` | `cooudflare.com` | 1.00 | 0.54 |
| Cloudflare | `cpoudflare.com` | MEDIUM_MATCH | 3 | `cloudflare.com` | `cpoudflare.com` | 1.00 | 0.54 |
| Cloudflare | `lcoudflare.com` | MEDIUM_MATCH | 3 | `cloudflare.com` | `lcoudflare.com` | 1.00 | 0.54 |
| Cloudflare | `vloudflare.com` | MEDIUM_MATCH | 3 | `cloudflare.com` | `vloudflare.com` | 1.00 | 0.54 |
| Cloudflare | `xloudflare.com` | MEDIUM_MATCH | 3 | `cloudflare.com` | `xloudflare.com` | 1.00 | 0.54 |
| Google | `xn--gogl-jpa1d.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogl-jpa1d.com` | 1.00 | 0.12 |
| Google | `xn--gool-dxa1756b.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gool-dxa1756b.com` | 1.00 | 0.09 |
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
