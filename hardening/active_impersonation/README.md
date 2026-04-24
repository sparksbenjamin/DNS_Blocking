# Active Impersonation Review

**Generated:** 2026-04-24T20:22:20.001811+00:00

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
- Candidate domains audited: `5527`
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
| 230 | 134 | 2568 | 891 | 1704 | 0 |

## Per-Target Summary

| Target | Seeds | Audited | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 180 | 0 | 0 | 94 | 77 | 0 |  |
| Amazon | 1 | 257 | 0 | 117 | 62 | 70 | 0 |  |
| Apple | 2 | 350 | 17 | 1 | 157 | 145 | 0 |  |
| Atlassian | 1 | 45 | 6 | 0 | 30 | 7 | 0 |  |
| Auth0 | 1 | 187 | 4 | 0 | 5 | 72 | 0 |  |
| Box | 1 | 103 | 0 | 0 | 72 | 26 | 0 |  |
| Cloudflare | 1 | 147 | 2 | 0 | 50 | 84 | 0 |  |
| Coinbase | 1 | 250 | 0 | 1 | 32 | 33 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 89 | 0 | 0 | 53 | 21 | 0 |  |
| DocuSign | 1 | 85 | 5 | 0 | 50 | 24 | 0 |  |
| Dropbox | 2 | 129 | 1 | 4 | 75 | 44 | 0 |  |
| Duo | 1 | 118 | 0 | 0 | 69 | 27 | 0 |  |
| FedEx | 1 | 119 | 0 | 0 | 12 | 53 | 0 |  |
| Figma | 1 | 84 | 0 | 0 | 54 | 17 | 0 |  |
| GitHub | 1 | 162 | 6 | 0 | 93 | 41 | 0 |  |
| GitLab | 1 | 79 | 1 | 0 | 38 | 36 | 0 |  |
| Google | 2 | 567 | 10 | 10 | 236 | 255 | 0 |  |
| Intuit | 1 | 142 | 0 | 0 | 67 | 49 | 0 |  |
| Jira | 1 | 99 | 0 | 0 | 74 | 20 | 0 |  |
| Microsoft | 5 | 934 | 69 | 0 | 520 | 266 | 0 |  |
| Notion | 1 | 13 | 0 | 0 | 8 | 1 | 0 |  |
| Okta | 1 | 110 | 0 | 0 | 61 | 31 | 0 |  |
| OneLogin | 1 | 32 | 0 | 0 | 19 | 12 | 0 |  |
| PayPal | 1 | 213 | 9 | 0 | 85 | 19 | 0 |  |
| Ping Identity | 1 | 28 | 0 | 0 | 1 | 25 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 117 | 15 | 0 | 48 | 40 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 177 | 51 | 1 | 87 | 23 | 0 |  |
| Slack | 1 | 91 | 0 | 0 | 59 | 20 | 0 |  |
| Stripe | 1 | 96 | 6 | 0 | 60 | 22 | 0 |  |
| Trello | 1 | 61 | 1 | 0 | 38 | 12 | 0 |  |
| TurboTax | 1 | 150 | 24 | 0 | 57 | 54 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 99 | 0 | 0 | 65 | 25 | 0 |  |
| Venmo | 1 | 71 | 1 | 0 | 36 | 22 | 0 |  |
| Zendesk | 1 | 61 | 2 | 0 | 40 | 17 | 0 |  |
| Zoom | 1 | 82 | 0 | 0 | 61 | 14 | 0 |  |
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
| Apple | `icloudo.com` | HIGH_MATCH | 11 | `apple.com` | `www.apple.com` | 1.00 | 1.00 |

## Operational Notes

1. Use this report to review and promote domains manually into a curated blocklist if needed
2. A redirect to the real brand is suspicious, but not sufficient proof on its own
3. Similar content and matching certificate/banner signals raise confidence
4. Re-run the report when you regenerate hardening lists or change target coverage
