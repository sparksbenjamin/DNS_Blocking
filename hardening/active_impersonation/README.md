# Active Impersonation Review

**Generated:** 2026-06-05T09:12:03.844929+00:00

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
- Candidate domains audited: `5689`
- Visible findings kept: `5326`
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
| 0 | 19 | 2284 | 950 | 2073 | 0 |

## Blocking Lists

Only `HIGH_MATCH` domains that do **not** canonical-redirect to the real brand are added to these exact-host blocklists.

| Output | Entries | File |
|--------|---------|------|
| Hosts | 0 | [categories/active_impersonation.txt](categories/active_impersonation.txt) |
| RPZ | 0 | [categories/active_impersonation.rpz](categories/active_impersonation.rpz) |

## Per-Target Summary

| Target | Seeds | Audited | Visible | Blocklist | Filtered Redirects | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|---------|-----------|--------------------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 181 | 181 | 0 | 0 | 0 | 0 | 91 | 78 | 0 |  |
| Amazon | 1 | 260 | 120 | 0 | 140 | 0 | 0 | 40 | 71 | 0 |  |
| Apple | 2 | 348 | 330 | 0 | 18 | 0 | 0 | 148 | 149 | 0 |  |
| Atlassian | 1 | 47 | 42 | 0 | 5 | 0 | 0 | 25 | 11 | 0 |  |
| Auth0 | 1 | 187 | 183 | 0 | 4 | 0 | 0 | 5 | 73 | 0 |  |
| Box | 1 | 103 | 103 | 0 | 0 | 0 | 0 | 74 | 25 | 0 |  |
| Cloudflare | 1 | 172 | 170 | 0 | 2 | 0 | 9 | 46 | 108 | 0 |  |
| Coinbase | 1 | 256 | 255 | 0 | 1 | 0 | 0 | 32 | 39 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 86 | 86 | 0 | 0 | 0 | 0 | 48 | 30 | 0 |  |
| DocuSign | 1 | 90 | 85 | 0 | 5 | 0 | 0 | 36 | 41 | 0 |  |
| Dropbox | 2 | 133 | 132 | 0 | 1 | 0 | 1 | 62 | 63 | 0 |  |
| Duo | 1 | 120 | 120 | 0 | 0 | 0 | 0 | 75 | 27 | 0 |  |
| FedEx | 1 | 127 | 127 | 0 | 0 | 0 | 0 | 5 | 71 | 0 |  |
| Figma | 1 | 82 | 82 | 0 | 0 | 0 | 0 | 47 | 24 | 0 |  |
| GitHub | 1 | 156 | 150 | 0 | 6 | 0 | 0 | 77 | 55 | 0 |  |
| GitLab | 1 | 81 | 80 | 0 | 1 | 0 | 0 | 39 | 38 | 0 |  |
| Google | 2 | 560 | 549 | 0 | 11 | 0 | 9 | 192 | 294 | 0 |  |
| Intuit | 1 | 140 | 140 | 0 | 0 | 0 | 0 | 68 | 48 | 0 |  |
| Jira | 1 | 100 | 100 | 0 | 0 | 0 | 0 | 69 | 27 | 0 |  |
| Microsoft | 5 | 928 | 859 | 0 | 69 | 0 | 0 | 410 | 367 | 0 |  |
| Notion | 1 | 10 | 10 | 0 | 0 | 0 | 0 | 8 | 0 | 0 |  |
| Okta | 1 | 109 | 108 | 0 | 1 | 0 | 0 | 63 | 29 | 0 |  |
| OneLogin | 1 | 31 | 31 | 0 | 0 | 0 | 0 | 14 | 13 | 0 |  |
| PayPal | 1 | 214 | 206 | 0 | 8 | 0 | 0 | 66 | 41 | 0 |  |
| Ping Identity | 1 | 31 | 31 | 0 | 0 | 0 | 0 | 1 | 28 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 117 | 102 | 0 | 15 | 0 | 0 | 35 | 48 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 178 | 136 | 0 | 42 | 0 | 0 | 94 | 23 | 0 |  |
| Slack | 1 | 92 | 92 | 0 | 0 | 0 | 0 | 55 | 26 | 0 |  |
| Stripe | 1 | 99 | 93 | 0 | 6 | 0 | 0 | 57 | 31 | 0 |  |
| Trello | 1 | 61 | 60 | 0 | 1 | 0 | 0 | 32 | 18 | 0 |  |
| TurboTax | 1 | 150 | 126 | 0 | 24 | 0 | 0 | 74 | 35 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 98 | 98 | 0 | 0 | 0 | 0 | 60 | 32 | 0 |  |
| Venmo | 1 | 74 | 73 | 0 | 1 | 0 | 0 | 38 | 19 | 0 |  |
| Zendesk | 1 | 61 | 59 | 0 | 2 | 0 | 0 | 35 | 23 | 0 |  |
| Zoom | 1 | 80 | 80 | 0 | 0 | 0 | 0 | 63 | 13 | 0 |  |
| eBay | 1 | 127 | 127 | 0 | 0 | 0 | 0 | 0 | 55 | 0 |  |

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
