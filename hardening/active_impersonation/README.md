# Active Impersonation Review

**Generated:** 2026-04-24T21:10:32.923741+00:00

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
- Candidate domains audited: `5527`
- Visible findings kept: `5170`
- Canonical brand redirects filtered out: `357`
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
| 0 | 3 | 1577 | 475 | 3115 | 0 |

## Blocking Lists

Only `HIGH_MATCH` domains that do **not** canonical-redirect to the real brand are added to these exact-host blocklists.

| Output | Entries | File |
|--------|---------|------|
| Hosts | 0 | [categories/active_impersonation.txt](categories/active_impersonation.txt) |
| RPZ | 0 | [categories/active_impersonation.rpz](categories/active_impersonation.rpz) |

## Per-Target Summary

| Target | Seeds | Audited | Visible | Blocklist | Filtered Redirects | High | Medium | Low | Offline | Errors | Note |
|--------|-------|---------|---------|-----------|--------------------|------|--------|-----|---------|--------|------|
| Adobe | 2 | 180 | 180 | 0 | 0 | 0 | 0 | 68 | 108 | 0 |  |
| Amazon | 1 | 257 | 118 | 0 | 139 | 0 | 1 | 26 | 86 | 0 |  |
| Apple | 2 | 350 | 335 | 0 | 15 | 0 | 0 | 87 | 226 | 0 |  |
| Atlassian | 1 | 45 | 39 | 0 | 6 | 0 | 0 | 9 | 30 | 0 |  |
| Auth0 | 1 | 187 | 183 | 0 | 4 | 0 | 0 | 4 | 133 | 0 |  |
| Box | 1 | 103 | 103 | 0 | 0 | 0 | 0 | 61 | 35 | 0 |  |
| Cloudflare | 1 | 147 | 145 | 0 | 2 | 0 | 0 | 17 | 125 | 0 |  |
| Coinbase | 1 | 250 | 250 | 0 | 0 | 0 | 0 | 10 | 133 | 0 |  |
| DHL | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Docker | 1 | 89 | 89 | 0 | 0 | 0 | 0 | 52 | 25 | 0 |  |
| DocuSign | 1 | 85 | 80 | 0 | 5 | 0 | 0 | 25 | 47 | 0 |  |
| Dropbox | 2 | 129 | 128 | 0 | 1 | 0 | 0 | 38 | 83 | 0 |  |
| Duo | 1 | 118 | 118 | 0 | 0 | 0 | 0 | 64 | 30 | 0 |  |
| FedEx | 1 | 119 | 119 | 0 | 0 | 0 | 0 | 42 | 71 | 0 |  |
| Figma | 1 | 84 | 84 | 0 | 0 | 0 | 0 | 37 | 41 | 0 |  |
| GitHub | 1 | 162 | 156 | 0 | 6 | 0 | 0 | 44 | 102 | 0 |  |
| GitLab | 1 | 79 | 78 | 0 | 1 | 0 | 0 | 34 | 42 | 0 |  |
| Google | 2 | 567 | 558 | 0 | 9 | 0 | 2 | 111 | 427 | 0 |  |
| Intuit | 1 | 142 | 142 | 0 | 0 | 0 | 0 | 34 | 89 | 0 |  |
| Jira | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 65 | 28 | 0 |  |
| Microsoft | 5 | 934 | 866 | 0 | 68 | 0 | 0 | 247 | 567 | 0 |  |
| Notion | 1 | 13 | 13 | 0 | 0 | 0 | 0 | 6 | 5 | 0 |  |
| Okta | 1 | 110 | 110 | 0 | 0 | 0 | 0 | 50 | 48 | 0 |  |
| OneLogin | 1 | 32 | 32 | 0 | 0 | 0 | 0 | 11 | 20 | 0 |  |
| PayPal | 1 | 213 | 205 | 0 | 8 | 0 | 0 | 27 | 158 | 0 |  |
| Ping Identity | 1 | 28 | 28 | 0 | 0 | 0 | 0 | 0 | 27 | 0 |  |
| QuickBooks | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Salesforce | 1 | 117 | 103 | 0 | 14 | 0 | 0 | 32 | 67 | 0 |  |
| ServiceNow | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| Shopify | 1 | 177 | 132 | 0 | 45 | 0 | 0 | 77 | 42 | 0 |  |
| Slack | 1 | 91 | 91 | 0 | 0 | 0 | 0 | 45 | 35 | 0 |  |
| Stripe | 1 | 96 | 90 | 0 | 6 | 0 | 0 | 47 | 35 | 0 |  |
| Trello | 1 | 61 | 60 | 0 | 1 | 0 | 0 | 22 | 32 | 0 |  |
| TurboTax | 1 | 150 | 126 | 0 | 24 | 0 | 0 | 59 | 59 | 0 |  |
| UPS | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |
| USPS | 1 | 99 | 99 | 0 | 0 | 0 | 0 | 50 | 40 | 0 |  |
| Venmo | 1 | 71 | 70 | 0 | 1 | 0 | 0 | 20 | 40 | 0 |  |
| Zendesk | 1 | 61 | 59 | 0 | 2 | 0 | 0 | 24 | 34 | 0 |  |
| Zoom | 1 | 82 | 82 | 0 | 0 | 0 | 0 | 32 | 45 | 0 |  |
| eBay | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Skipped target because no reachable baselines were available. |

## Per-Target Blocking Lists

No block-worthy domains were emitted in this run.

## Top Suspicious Matches

| Target | Domain | Status | Score | Baseline | Redirect | Title | Content |
|--------|--------|--------|-------|----------|----------|-------|---------|
| Amazon | `cmazon.com` | MEDIUM_MATCH | 3 | `amazon.com` | `cmazon.com` | 0.90 | 0.30 |
| Google | `xn--gogl-jpa1d.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--gogl-jpa1d.com` | 1.00 | 0.13 |
| Google | `xn--googl-lsa.com` | MEDIUM_MATCH | 3 | `google.com` | `xn--googl-lsa.com` | 1.00 | 0.05 |

## Operational Notes

1. Canonical redirects to the real brand are intentionally excluded from both the report rows and the blocklists
2. The blocking lists are conservative and only include `HIGH_MATCH` domains
3. Review `MEDIUM_MATCH` findings manually before promoting them anywhere
4. Re-run the report when you regenerate hardening lists or change target coverage
