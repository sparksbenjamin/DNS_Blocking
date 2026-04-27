# 🛡️ DNS Filters & Blocking Lists
![Auto Update](https://img.shields.io/badge/Update-Automated-success)
![License](https://img.shields.io/github/license/sparksbenjamin/DNS_Blocking)
![Lists](https://img.shields.io/badge/Lists-1200%2B-blue)
![Last Updated](https://img.shields.io/github/last-commit/sparksbenjamin/DNS_Blocking)

DNS blocklists for people who want a practical one-stop shop instead of hunting down a dozen separate feeds.

This repo now ships:
- standard Pi-hole / AdGuard-friendly hosts lists
- exact-host security feeds
- Unbound-ready RPZ zone files
- optional brand-impersonation and live-impersonation hardening layers

## Start Here

If you do not want to think about categories yet, start with one of these:

| Profile | Best For | File | Raw URL |
|---------|----------|------|---------|
| `Home Safe` | Most home users | [services/recommended/home_safe.txt](services/recommended/home_safe.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/recommended/home_safe.txt) |
| `Family` | Shared devices and kid-safe networks | [services/recommended/family.txt](services/recommended/family.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/recommended/family.txt) |
| `Aggressive` | Lock-it-down hosts blocking | [services/recommended/aggressive.txt](services/recommended/aggressive.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/recommended/aggressive.txt) |
| `Security` | Exact-host phishing and malware blocking | [security/recommended/security.txt](security/recommended/security.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/recommended/security.txt) |
| `Security RPZ` | Unbound / RPZ-capable resolvers | [rpz/recommended/security.rpz](rpz/recommended/security.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/recommended/security.rpz) |

## Why Trust This Repo

- Public Suffix List-aware normalization prevents junk outputs like bare `co.uk` or `gov.tw`.
- Repo-local source policies strip noisy shared infrastructure and known bad broad matches before lists are written.
- Generated outputs are validated for syntax, exclusion policy, and count drift on every run.
- Standard hosts, exact-host security, and RPZ outputs are built from the same source graph so they stay aligned.
- Hardening and active impersonation layers are split out, so more aggressive protection does not contaminate the default lists.

Quality and validation reports:
- [services/quality_report.json](services/quality_report.json)
- [security/quality_report.json](security/quality_report.json)
- [rpz/quality_report.json](rpz/quality_report.json)

## Install In 60 Seconds

### Pi-hole
1. Go to `Settings` → `Blocklists`
2. Paste one of the raw URLs above
3. Save and run gravity

### AdGuard Home
1. Go to `Filters` → `DNS blocklists`
2. Add a custom blocklist
3. Paste one of the raw URLs above

### Unbound
1. Use the RPZ profile or category file under [rpz](rpz/README.md)
2. Include it from your RPZ config
3. Reload Unbound

## What’s Included

### [Services](services/README.md)
Standard hosts-style lists for broad compatibility and easier troubleshooting.

### [Security](security/README.md)
Exact-host security lists for phishing, malware, scams, dynamic DNS, and badware hosters.

### [RPZ](rpz/README.md)
Resolver-native policy zones for Unbound and other RPZ-aware DNS servers.

### [Hardening](hardening/README.md)
Optional DNSTwist-derived lookalike blocking and separate active impersonation review outputs.

### [Tunneling](tunneling/README.md)
VPN and proxy domain lists if you want to restrict common bypass routes.

## Optional Add-Ons

These are useful, but they are intentionally not the default starting point:

| Add-On | Why You’d Use It | File |
|--------|------------------|------|
| `DNS / VPN Bypass` | Block common DoH, VPN, and proxy-bypass endpoints | [services/categories/dns_bypass.txt](services/categories/dns_bypass.txt) |
| `URL Shorteners` | Reduce redirector and shortlink abuse | [services/categories/url_shortener.txt](services/categories/url_shortener.txt) |
| `Brand Impersonation` | DNSTwist-derived lookalike blocking | [hardening/categories/brand_impersonation.txt](hardening/categories/brand_impersonation.txt) |
| `Active Impersonation` | Conservatively promoted live impersonation blocklist | [hardening/active_impersonation/categories/active_impersonation.txt](hardening/active_impersonation/categories/active_impersonation.txt) |

## Notes

- If you are new here, start with one recommended profile, not ten category feeds.
- If something breaks, move down a level: `Aggressive` → `Family` → `Home Safe`.
- If you want source-level control, every generated layer also ships per-source files in its own README.

## Related Docs

- [Prevent DNS bypassing](DNS_Bypass.md)
- [Services README](services/README.md)
- [Security README](security/README.md)
- [RPZ README](rpz/README.md)
- [Hardening README](hardening/README.md)
- [Active Impersonation Review](hardening/active_impersonation/README.md)
