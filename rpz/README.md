# RPZ Security Policies

**Generated:** 2026-04-30 05:35:43 UTC

**Audience:** Advanced / Unbound RPZ

**False-Positive Risk:** Elevated

Unbound-friendly RPZ zone files generated from the same exact-host security layer. This is the advanced output for users who want native response-policy feeds instead of hosts-style blocklists.

## Output Tiers

- **[services](../services/README.md)** - home-safe, registrable-domain blocklists
- **[security](../security/README.md)** - exact-host security blocklists
- **[rpz](../rpz/README.md)** - Unbound-friendly RPZ policies
- **[hardening](../hardening/README.md)** - DNSTwist-derived brand impersonation blocklists
- **[active impersonation review](../hardening/active_impersonation/README.md)** - scored live-lookalike review reports

## Quick Start

Use these files when you run Unbound or another resolver that supports RPZ and you want policy-zone blocking instead of hosts-style imports.

## Recommended Entry Points

Use these starter bundles if you want a fast, opinionated default instead of picking categories one by one.

| Bundle | Best For | Entries | Includes | File | Raw URL |
|--------|----------|---------|----------|------|---------|
| **Security RPZ** | Unbound and RPZ-capable resolvers | 632,686 | Badware Hosters, Dynamic DNS, Malware & Threats, Phishing & Scam Sites, Scam & Fraud | [security.rpz](recommended/security.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/recommended/security.rpz) |

## Why Trust This Layer

- Public Suffix List-aware domain normalization prevents bad roots like `co.uk` from leaking into generated outputs
- Repo-local source policies remove noisy shared infrastructure and known false-positive patterns before lists are written
- Validation reports are published at [quality_report.json](quality_report.json) and check syntax, exclusions, and count drift
- Standard, exact-host, and RPZ outputs are generated from the same source graph so the repo stays internally consistent

## Aggregated Categories

RPZ category bundles for exact-host security blocking.

| Category | Entries | Sources | File | Raw URL |
|----------|---------|---------|------|---------|
| [🗄️ Badware Hosters](#badware-hoster) | 1,195 | 1 | [badware_hoster.rpz](categories/badware_hoster.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/categories/badware_hoster.rpz) |
| [🌐 Dynamic DNS](#dynamic-dns) | 1,023 | 1 | [dynamic_dns.rpz](categories/dynamic_dns.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/categories/dynamic_dns.rpz) |
| [🦠 Malware & Threats](#malware) | 8,493 | 3 | [malware.rpz](categories/malware.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/categories/malware.rpz) |
| [🎣 Phishing & Scam Sites](#phishing) | 410,539 | 3 | [phishing.rpz](categories/phishing.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/categories/phishing.rpz) |
| [💸 Scam & Fraud](#scam) | 211,540 | 3 | [scam.rpz](categories/scam.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/categories/scam.rpz) |

## Individual Sources

Per-source RPZ files are available if you want to map individual feeds into separate policy zones.

### Badware Hosters

| Source | Entries | File | Raw URL |
|--------|---------|------|---------|
| HaGeZi Badware Hoster | 1,195 | [hagezi_hoster.rpz](lists/badware_hoster/hagezi_hoster.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/badware_hoster/hagezi_hoster.rpz) |

### Dynamic DNS

| Source | Entries | File | Raw URL |
|--------|---------|------|---------|
| HaGeZi Dynamic DNS | 1,023 | [hagezi_dyndns.rpz](lists/dynamic_dns/hagezi_dyndns.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/dynamic_dns/hagezi_dyndns.rpz) |

### Malware & Threats

| Source | Entries | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Ransomware | 1,904 | [blp_ransomware.rpz](lists/malware/blp_ransomware.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/malware/blp_ransomware.rpz) |
| ThreatFox | 585 | [threatfox.rpz](lists/malware/threatfox.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/malware/threatfox.rpz) |
| URLhaus | 6,466 | [urlhaus.rpz](lists/malware/urlhaus.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/malware/urlhaus.rpz) |

### Phishing & Scam Sites

| Source | Entries | File | Raw URL |
|--------|---------|------|---------|
| OpenPhish | 263 | [openphish.rpz](lists/phishing/openphish.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/phishing/openphish.rpz) |
| PhishTank | 27,298 | [phishtank.rpz](lists/phishing/phishtank.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/phishing/phishtank.rpz) |
| Phishing Army | 385,060 | [phishing_army.rpz](lists/phishing/phishing_army.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/phishing/phishing_army.rpz) |

### Scam & Fraud

| Source | Entries | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Fraud | 195,904 | [blp_fraud.rpz](lists/scam/blp_fraud.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/scam/blp_fraud.rpz) |
| Block List Project Scam | 1,274 | [blp_scam.rpz](lists/scam/blp_scam.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/scam/blp_scam.rpz) |
| HaGeZi Fake | 14,435 | [hagezi_fake.rpz](lists/scam/hagezi_fake.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/scam/hagezi_fake.rpz) |

## Usage

### Unbound
1. Place the `.rpz` file somewhere your resolver can read it
2. Reference it from your RPZ configuration or local-zone include path
3. Reload Unbound after updating the file

### Why use RPZ here
1. Keeps exact-host security feeds in a resolver-native format
2. Makes feed separation easier than large monolithic includes
3. Fits well with local automation and scheduled updates

## Format Details

- **RPZ zone format** with `CNAME .` policy actions
- **Exact hostnames preserved** for URL-derived threat feeds
- **Advanced output** intended for Unbound or other RPZ-capable resolvers
- **Recommended after testing the matching `security/` hosts lists first**

## Data Sources

- **[AdGuard](https://adguard.com/)** - service blocklists for social media, gaming, streaming, and more
- **[Phishing Army](https://phishing.army/)** - active phishing domains
- **[OpenPhish](https://openphish.com/)** - phishing URLs converted to exact hosts
- **[PhishTank](https://phishtank.org/)** - verified phishing URLs converted to exact hosts
- **[ThreatFox](https://threatfox.abuse.ch/)** - malware indicators from abuse.ch
- **[URLhaus](https://urlhaus.abuse.ch/)** - malware distribution URLs converted to exact hosts
- **[The Block List Project](https://github.com/blocklistproject/Lists)** - curated category feeds for abuse, crypto, drugs, piracy, redirects, smart TV, torrent, tracking, vaping, and more
- **[HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists)** - dynamic DNS, badware hoster, fake-domain, DNS-bypass, and URL-shortener feeds
- **[UKLANS cache-domains](https://github.com/uklans/cache-domains)** - gaming CDN/cache hostnames
- **[StevenBlack](https://github.com/StevenBlack/hosts)** and **[Chad Mayfield](https://github.com/chadmayfield/my-pihole-blocklists)** - adult-content feeds

## Notes

- Start with the recommended bundles if you want the fewest decisions
- Move to aggregated categories when you want control without going fully source-by-source
- Whitelist when needed and watch your resolver logs after major changes
- Exact-host security and RPZ layers are more aggressive than the standard services layer
- Source feeds change over time, so entry counts will drift
