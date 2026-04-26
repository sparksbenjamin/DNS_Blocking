# Active Impersonation Review

**Generated:** 2026-04-26T07:24:07.442460+00:00

This report scores live DNSTwist lookalike domains against the real brand sites using lightweight fingerprinting. It is a **review artifact**, not an auto-promoted blocklist.

Quick links:

- [Back to Hardening](../README.md)
- [Back to Repo Root](../../README.md)

## What This Means

- **HIGH_MATCH** - the candidate looks materially like the baseline and deserves immediate review
- **MEDIUM_MATCH** - some signals line up, but it still needs analyst judgment
- **LOW_MATCH / INCONCLUSIVE** - weak resemblance or not enough content to decide
- **OFFLINE / ERROR** - the candidate did not respond cleanly during this run

## Settings

- Targets audited: `40`
- Candidate domains audited: `5430`
- Max workers: `10`
- Target jobs: `2`
- Connect timeout: `3.0` seconds
- Read timeout: `5.0` seconds
- Max response bytes: `262144`
- Max domains per target: `unlimited`
- TSV report: [results.tsv](results.tsv)
- JSON report: [report.json](report.json)

## Overall Summary

| HIGH | MEDIUM | LOW | INCONCLUSIVE | OFFLINE | ERROR |
|------|--------|-----|--------------|---------|-------|
| 228 | 132 | 2418 | 1074 | 1578 | 0 |

## Per-Target Summary

| Target | Seeds | Audited | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 180 | 0 | 0 | 82 | 71 | 0 |  |
| Amazon | 1 | 258 | 0 | 117 | 58 | 71 | 0 |  |
| Apple | 2 | 346 | 17 | 1 | 136 | 135 | 0 |  |
| Atlassian | 1 | 46 | 6 | 0 | 31 | 7 | 0 |  |
| Auth0 | 1 | 188 | 4 | 0 | 4 | 73 | 0 |  |
| Box | 1 | 103 | 0 | 0 | 67 | 26 | 0 |  |
| Cloudflare | 1 | 150 | 2 | 0 | 50 | 88 | 0 |  |
| Coinbase | 1 | 255 | 1 | 0 | 30 | 36 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 90 | 0 | 0 | 52 | 21 | 0 |  |
| DocuSign | 1 | 87 | 5 | 0 | 47 | 26 | 0 |  |
| Dropbox | 2 | 129 | 1 | 4 | 73 | 42 | 0 |  |
| Duo | 1 | 116 | 0 | 0 | 60 | 28 | 0 |  |
| FedEx | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Figma | 1 | 84 | 0 | 0 | 48 | 19 | 0 |  |
| GitHub | 1 | 162 | 6 | 0 | 88 | 44 | 0 |  |
| GitLab | 1 | 81 | 1 | 0 | 35 | 36 | 0 |  |
| Google | 2 | 567 | 10 | 10 | 215 | 253 | 0 |  |
| Intuit | 1 | 142 | 0 | 0 | 79 | 31 | 0 |  |
| Jira | 1 | 99 | 0 | 0 | 65 | 19 | 0 |  |
| Microsoft | 5 | 935 | 68 | 0 | 489 | 253 | 0 |  |
| Notion | 1 | 13 | 0 | 0 | 10 | 0 | 0 |  |
| Okta | 1 | 110 | 0 | 0 | 54 | 31 | 0 |  |
| OneLogin | 1 | 32 | 0 | 0 | 17 | 12 | 0 |  |
| PayPal | 1 | 216 | 9 | 0 | 82 | 14 | 0 |  |
| Ping Identity | 1 | 29 | 0 | 0 | 0 | 26 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 117 | 15 | 0 | 51 | 35 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 177 | 49 | 0 | 81 | 22 | 0 |  |
| Slack | 1 | 92 | 0 | 0 | 48 | 21 | 0 |  |
| Stripe | 1 | 98 | 6 | 0 | 57 | 23 | 0 |  |
| Trello | 1 | 61 | 1 | 0 | 36 | 11 | 0 |  |
| TurboTax | 1 | 151 | 24 | 0 | 72 | 37 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 99 | 0 | 0 | 69 | 20 | 0 |  |
| Venmo | 1 | 73 | 1 | 0 | 38 | 17 | 0 |  |
| Zendesk | 1 | 62 | 2 | 0 | 36 | 17 | 0 |  |
| Zoom | 1 | 82 | 0 | 0 | 58 | 13 | 0 |  |
| eBay | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |

## Top Suspicious Matches

| Target | Domain | Status | Score | Baseline | Redirect | Title | Content |
|--------|--------|--------|-------|----------|----------|-------|---------|
| Apple | `aple.com` | HIGH_MATCH | 11 | `apple.com` | `www.apple.com` | 1.00 | 1.00 |
| Apple | `apole.com` | HIGH_MATCH | 11 | `apple.com` | `www.apple.com` | 1.00 | 1.00 |
| Apple | `appke.com` | HIGH_MATCH | 11 | `apple.com` | `www.apple.com` | 1.00 | 1.00 |
| Apple | `appl-e.com` | HIGH_MATCH | 11 | `apple.com` | `www.apple.com` | 1.00 | 1.00 |
| Apple | `appl.com` | HIGH_MATCH | 11 | `apple.com` | `www.apple.com` | 1.00 | 1.00 |
| Apple | `appla.com` | HIGH_MATCH | 11 | `apple.com` | `www.apple.com` | 1.00 | 1.00 |
| Apple | `applle.com` | HIGH_MATCH | 11 | `apple.com` | `www.apple.com` | 1.00 | 1.00 |
| Apple | `applw.com` | HIGH_MATCH | 11 | `apple.com` | `www.apple.com` | 1.00 | 1.00 |
| Apple | `aptle.com` | HIGH_MATCH | 11 | `apple.com` | `www.apple.com` | 1.00 | 1.00 |
| Shopify | `ashopify.com` | HIGH_MATCH | 11 | `shopify.com` | `www.shopify.com` | 1.00 | 1.00 |
| Auth0 | `autho.com` | HIGH_MATCH | 11 | `auth0.com` | `auth0.com` | 1.00 | 1.00 |
| Apple | `axple.com` | HIGH_MATCH | 11 | `apple.com` | `www.apple.com` | 1.00 | 1.00 |
| Cloudflare | `cloudfare.com` | HIGH_MATCH | 11 | `cloudflare.com` | `www.cloudflare.com` | 1.00 | 1.00 |
| Shopify | `dhopify.com` | HIGH_MATCH | 11 | `shopify.com` | `www.shopify.com` | 1.00 | 1.00 |
| Shopify | `dshopify.com` | HIGH_MATCH | 11 | `shopify.com` | `www.shopify.com` | 1.00 | 1.00 |
| Shopify | `ehopify.com` | HIGH_MATCH | 11 | `shopify.com` | `www.shopify.com` | 1.00 | 1.00 |
| GitHub | `git-hub.com` | HIGH_MATCH | 11 | `github.com` | `github.com` | 1.00 | 1.00 |
| GitHub | `gitgub.com` | HIGH_MATCH | 11 | `github.com` | `github.com` | 1.00 | 1.00 |
| GitHub | `githuh.com` | HIGH_MATCH | 11 | `github.com` | `github.com` | 1.00 | 1.00 |
| Google | `gogle.com` | HIGH_MATCH | 11 | `google.com` | `www.google.com` | 1.00 | 1.00 |
| Google | `googel.com` | HIGH_MATCH | 11 | `google.com` | `www.google.com` | 1.00 | 1.00 |
| Google | `googl.com` | HIGH_MATCH | 11 | `google.com` | `www.google.com` | 1.00 | 1.00 |
| Google | `gooogle.com` | HIGH_MATCH | 11 | `google.com` | `www.google.com` | 1.00 | 1.00 |
| GitHub | `guthub.com` | HIGH_MATCH | 11 | `github.com` | `github.com` | 1.00 | 1.00 |
| Apple | `icloude.com` | HIGH_MATCH | 11 | `apple.com` | `www.apple.com` | 1.00 | 1.00 |

## Operational Notes

1. Use this report to review and promote domains manually into a curated blocklist if needed
2. A redirect to the real brand is suspicious, but not sufficient proof on its own
3. Similar content and matching certificate/banner signals raise confidence
4. Re-run the report when you regenerate hardening lists or change target coverage
