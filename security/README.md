# Exact-Host Security Blocklists

**Generated:** 2026-04-24 18:35:46 UTC

**Audience:** Security-focused / higher churn

**False-Positive Risk:** Elevated

Security-focused host blocking for phishing, malware, scam, dynamic DNS, and badware hoster feeds. These lists preserve exact hostnames so URL-derived feeds stay precise instead of collapsing to broad registrable roots.

## Output Tiers

- **[services](../services/README.md)** - home-safe, registrable-domain blocklists
- **[security](../security/README.md)** - exact-host security blocklists
- **[rpz](../rpz/README.md)** - Unbound-friendly RPZ policies
- **[hardening](../hardening/README.md)** - DNSTwist-derived brand impersonation blocklists
- **[active impersonation review](../hardening/active_impersonation/README.md)** - scored live-lookalike review reports

## Quick Start

Use these lists when you want stronger protection against exact phishing or malware hosts and you are comfortable with faster list churn.

## Aggregated Categories

Exact-host category bundles built from higher-sensitivity security feeds.

| Category | Entries | Sources | File | Raw URL |
|----------|---------|---------|------|---------|
| 🗄️ Badware Hosters | 1,201 | 1 | [badware_hoster.txt](categories/badware_hoster.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/categories/badware_hoster.txt) |
| 🌐 Dynamic DNS | 1,486 | 1 | [dynamic_dns.txt](categories/dynamic_dns.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/categories/dynamic_dns.txt) |
| 🦠 Malware & Threats | 8,821 | 3 | [malware.txt](categories/malware.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/categories/malware.txt) |
| 🎣 Phishing & Scam Sites | 409,966 | 3 | [phishing.txt](categories/phishing.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/categories/phishing.txt) |
| 💸 Scam & Fraud | 211,702 | 3 | [scam.txt](categories/scam.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/categories/scam.txt) |

## Individual Sources

Each source is also available separately if you want tighter source attribution or to tune false-positive handling.

### Badware Hoster

| Source | Entries | File | Raw URL |
|--------|---------|------|---------|
| HaGeZi Badware Hoster | 1,201 | [hagezi_hoster.txt](lists/badware_hoster/hagezi_hoster.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/lists/badware_hoster/hagezi_hoster.txt) |

### Dynamic Dns

| Source | Entries | File | Raw URL |
|--------|---------|------|---------|
| HaGeZi Dynamic DNS | 1,486 | [hagezi_dyndns.txt](lists/dynamic_dns/hagezi_dyndns.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/lists/dynamic_dns/hagezi_dyndns.txt) |

### Malware

| Source | Entries | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Ransomware | 1,904 | [blp_ransomware.txt](lists/malware/blp_ransomware.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/lists/malware/blp_ransomware.txt) |
| ThreatFox | 631 | [threatfox.txt](lists/malware/threatfox.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/lists/malware/threatfox.txt) |
| URLhaus | 6,708 | [urlhaus.txt](lists/malware/urlhaus.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/lists/malware/urlhaus.txt) |

### Phishing

| Source | Entries | File | Raw URL |
|--------|---------|------|---------|
| OpenPhish | 225 | [openphish.txt](lists/phishing/openphish.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/lists/phishing/openphish.txt) |
| PhishTank | 26,680 | [phishtank.txt](lists/phishing/phishtank.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/lists/phishing/phishtank.txt) |
| Phishing Army | 385,179 | [phishing_army.txt](lists/phishing/phishing_army.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/lists/phishing/phishing_army.txt) |

### Scam

| Source | Entries | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Fraud | 195,905 | [blp_fraud.txt](lists/scam/blp_fraud.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/lists/scam/blp_fraud.txt) |
| Block List Project Scam | 1,274 | [blp_scam.txt](lists/scam/blp_scam.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/lists/scam/blp_scam.txt) |
| HaGeZi Fake | 14,596 | [hagezi_fake.txt](lists/scam/hagezi_fake.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/security/lists/scam/hagezi_fake.txt) |

## Usage

### Pi-hole / AdGuard Home
1. Import the **Raw URL** of the exact-host list you want
2. Start with the aggregated categories before stacking individual feeds
3. Watch query logs closely after enabling them

### When to use this layer
1. You want stronger phishing and malware coverage
2. You are comfortable whitelisting exact hosts when needed
3. You prefer precision over broad domain collapsing

## Format Details

- **Hosts file format** - `0.0.0.0 hostname`
- **Exact hostnames preserved** - designed for URL-derived security feeds
- **Higher churn** - entries can appear and disappear faster than the standard layer
- **Best paired with logging and allowlisting** when you run it broadly

## Data Sources

- **[AdGuard](https://adguard.com/)** - service blocklists for social media, gaming, streaming, and more
- **[Phishing Army](https://phishing.army/)** - active phishing domains
- **[OpenPhish](https://openphish.com/)** - phishing URLs converted to exact hosts
- **[PhishTank](https://phishtank.org/)** - verified phishing URLs converted to exact hosts
- **[ThreatFox](https://threatfox.abuse.ch/)** - malware indicators from abuse.ch
- **[URLhaus](https://urlhaus.abuse.ch/)** - malware distribution URLs converted to exact hosts
- **[The Block List Project](https://github.com/blocklistproject/Lists)** - scam, fraud, ransomware, and tracking feeds
- **[HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists)** - dynamic DNS, badware hoster, and fake-domain feeds
- **[UKLANS cache-domains](https://github.com/uklans/cache-domains)** - gaming CDN/cache hostnames
- **[StevenBlack](https://github.com/StevenBlack/hosts)** and **[Chad Mayfield](https://github.com/chadmayfield/my-pihole-blocklists)** - adult-content feeds

## Notes

- Start with the aggregated categories before stacking many source files
- Whitelist when needed and watch your resolver logs after major changes
- Exact-host security and RPZ layers are more aggressive than the standard services layer
- Source feeds change over time, so entry counts will drift
