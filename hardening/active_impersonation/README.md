# Active Impersonation Review

**Generated:** 2026-04-28T07:58:11.074230+00:00

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
- Candidate domains audited: `5685`
- Visible findings kept: `5321`
- Canonical brand redirects filtered out: `364`
- Blocklist entries emitted: `10`
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
| 10 | 13 | 2708 | 878 | 1712 | 0 |

## Blocking Lists

Only `HIGH_MATCH` domains that do **not** canonical-redirect to the real brand are added to these exact-host blocklists.

| Output | Entries | File |
|--------|---------|------|
| Hosts | 10 | [categories/active_impersonation.txt](categories/active_impersonation.txt) |
| RPZ | 10 | [categories/active_impersonation.rpz](categories/active_impersonation.rpz) |

## Per-Target Summary

| Target | Seeds | Audited | Visible | Blocklist | Filtered Redirects | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|---------|-----------|--------------------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 181 | 181 | 0 | 0 | 0 | 0 | 99 | 72 | 0 |  |
| Amazon | 1 | 258 | 118 | 0 | 140 | 0 | 0 | 38 | 72 | 0 |  |
| Apple | 2 | 346 | 329 | 0 | 17 | 0 | 0 | 166 | 134 | 0 |  |
| Atlassian | 1 | 45 | 40 | 0 | 5 | 0 | 0 | 29 | 9 | 0 |  |
| Auth0 | 1 | 188 | 184 | 0 | 4 | 0 | 0 | 4 | 73 | 0 |  |
| Box | 1 | 103 | 103 | 0 | 0 | 0 | 0 | 69 | 28 | 0 |  |
| Cloudflare | 1 | 149 | 147 | 0 | 2 | 0 | 0 | 52 | 85 | 0 |  |
| Coinbase | 1 | 257 | 256 | 0 | 1 | 0 | 0 | 32 | 38 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 89 | 89 | 0 | 0 | 0 | 0 | 51 | 28 | 0 |  |
| DocuSign | 1 | 87 | 82 | 0 | 5 | 0 | 0 | 49 | 25 | 0 |  |
| Dropbox | 2 | 129 | 128 | 0 | 1 | 0 | 4 | 80 | 39 | 0 |  |
| Duo | 1 | 119 | 119 | 0 | 0 | 0 | 0 | 71 | 27 | 0 |  |
| FedEx | 1 | 121 | 121 | 0 | 0 | 0 | 0 | 58 | 54 | 0 |  |
| Figma | 1 | 86 | 86 | 0 | 0 | 0 | 0 | 56 | 20 | 0 |  |
| GitHub | 1 | 162 | 156 | 0 | 6 | 0 | 0 | 96 | 43 | 0 |  |
| GitLab | 1 | 80 | 79 | 0 | 1 | 0 | 0 | 39 | 35 | 0 |  |
| Google | 2 | 566 | 555 | 0 | 11 | 0 | 9 | 225 | 251 | 0 |  |
| Intuit | 1 | 142 | 142 | 0 | 0 | 0 | 0 | 76 | 41 | 0 |  |
| Jira | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 73 | 20 | 0 |  |
| Microsoft | 5 | 938 | 869 | 0 | 69 | 0 | 0 | 525 | 259 | 0 |  |
| Notion | 1 | 15 | 15 | 0 | 0 | 0 | 0 | 11 | 2 | 0 |  |
| Okta | 1 | 109 | 109 | 0 | 0 | 0 | 0 | 61 | 30 | 0 |  |
| OneLogin | 1 | 32 | 32 | 0 | 0 | 0 | 0 | 16 | 13 | 0 |  |
| PayPal | 1 | 214 | 205 | 0 | 9 | 0 | 0 | 86 | 15 | 0 |  |
| Ping Identity | 1 | 29 | 29 | 0 | 0 | 0 | 0 | 1 | 26 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 121 | 106 | 0 | 15 | 0 | 0 | 52 | 43 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 177 | 136 | 0 | 41 | 0 | 0 | 99 | 22 | 0 |  |
| Slack | 1 | 92 | 92 | 0 | 0 | 0 | 0 | 56 | 21 | 0 |  |
| Stripe | 1 | 100 | 94 | 0 | 6 | 0 | 0 | 60 | 25 | 0 |  |
| Trello | 1 | 61 | 60 | 0 | 1 | 0 | 0 | 36 | 12 | 0 |  |
| TurboTax | 1 | 152 | 128 | 0 | 24 | 0 | 0 | 73 | 44 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 68 | 24 | 0 |  |
| Venmo | 1 | 72 | 71 | 0 | 1 | 0 | 0 | 41 | 17 | 0 |  |
| Zendesk | 1 | 62 | 60 | 0 | 2 | 0 | 0 | 42 | 17 | 0 |  |
| Zoom | 1 | 82 | 82 | 0 | 0 | 0 | 0 | 63 | 13 | 0 |  |
| eBay | 1 | 123 | 120 | 10 | 3 | 10 | 0 | 55 | 35 | 0 |  |

## Per-Target Blocking Lists

| Target | Entries | Hosts | RPZ |
|--------|---------|-------|-----|
| eBay | 10 | [lists/ebay.txt](lists/ebay.txt) | [lists/ebay.rpz](lists/ebay.rpz) |

## Top Suspicious Matches

| Target | Domain | Status | Score | Baseline | Redirect | Title | Content |
|--------|--------|--------|-------|----------|----------|-------|---------|
| eBay | `e-bay.com` | HIGH_MATCH | 9 | `ebay.com` | `www.ebay.com` | 1.00 | 1.00 |
| eBay | `ebnay.com` | HIGH_MATCH | 9 | `ebay.com` | `www.ebay.com` | 1.00 | 1.00 |
| eBay | `3ebay.com` | HIGH_MATCH | 8 | `ebay.com` | `www.ebay.com` | 1.00 | 1.00 |
| eBay | `ebaya.com` | HIGH_MATCH | 8 | `ebay.com` | `www.ebay.com` | 1.00 | 1.00 |
| eBay | `ebaycom.com` | HIGH_MATCH | 8 | `ebay.com` | `www.ebay.com` | 1.00 | 1.00 |
| eBay | `ebayd.com` | HIGH_MATCH | 8 | `ebay.com` | `www.ebay.com` | 1.00 | 1.00 |
| eBay | `ebayn.com` | HIGH_MATCH | 8 | `ebay.com` | `www.ebay.com` | 1.00 | 1.00 |
| eBay | `ebays.com` | HIGH_MATCH | 8 | `ebay.com` | `www.ebay.com` | 1.00 | 1.00 |
| eBay | `ebayt.com` | HIGH_MATCH | 8 | `ebay.com` | `www.ebay.com` | 1.00 | 1.00 |
| eBay | `sebay.com` | HIGH_MATCH | 8 | `ebay.com` | `www.ebay.com` | 1.00 | 1.00 |
| Google | `xn--gogl-jpa1d.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogl-jpa1d.com` | 1.00 | 0.14 |
| Google | `xn--gogle-1ta.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-1ta.com` | 1.00 | 0.10 |
| Google | `xn--ooge-21a88g.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--ooge-21a88g.com` | 1.00 | 0.10 |
| Google | `xn--googl-9cc.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-9cc.com` | 1.00 | 0.05 |
| Google | `xn--googl-lsa.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-lsa.com` | 1.00 | 0.05 |
| Google | `xn--gogle-g91b.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogle-g91b.com` | 1.00 | 0.04 |
| Google | `xn--goog-8va9v.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--goog-8va9v.com` | 1.00 | 0.04 |
| Google | `xn--googe-m6a.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googe-m6a.com` | 1.00 | 0.04 |
| Google | `xn--ooge-9wa5r.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--ooge-9wa5r.com` | 1.00 | 0.04 |
| Dropbox | `dr.opbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `dr.opbox.com` | 0.90 | 0.02 |
| Dropbox | `d.ropbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `d.ropbox.com` | 0.95 | 0.01 |
| Dropbox | `ropbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `ropbox.com` | 0.95 | 0.01 |
| Dropbox | `tropbox.com` | MEDIUM_MATCH | 3 | `dropbox.com` | `tropbox.com` | 0.91 | 0.01 |

## Operational Notes

1. Canonical redirects to the real brand are intentionally excluded from both the report rows and the blocklists
2. The blocking lists are conservative and only include `HIGH_MATCH` domains
3. Review `MEDIUM_MATCH` findings manually before promoting them anywhere
4. Re-run the report when you regenerate hardening lists or change target coverage
