# RPZ Security Policies

**Generated:** 2026-04-27 13:57:35 UTC

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

## Aggregated Categories

RPZ category bundles for exact-host security blocking.

| Category | Entries | Sources | File | Raw URL |
|----------|---------|---------|------|---------|
| [🗄️ Badware Hosters](#badware-hoster) | 1,195 | 1 | [badware_hoster.rpz](categories/badware_hoster.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/categories/badware_hoster.rpz) |
| [🌐 Dynamic DNS](#dynamic-dns) | 1,023 | 1 | [dynamic_dns.rpz](categories/dynamic_dns.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/categories/dynamic_dns.rpz) |
| [🦠 Malware & Threats](#malware) | 8,690 | 3 | [malware.rpz](categories/malware.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/categories/malware.rpz) |
| [🎣 Phishing & Scam Sites](#phishing) | 409,863 | 3 | [phishing.rpz](categories/phishing.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/categories/phishing.rpz) |
| [💸 Scam & Fraud](#scam) | 211,451 | 3 | [scam.rpz](categories/scam.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/categories/scam.rpz) |

## Individual Sources

Per-source RPZ files are available if you want to map individual feeds into separate policy zones.

### Badware Hoster

| Source | Entries | File | Raw URL |
|--------|---------|------|---------|
| HaGeZi Badware Hoster | 1,195 | [hagezi_hoster.rpz](lists/badware_hoster/hagezi_hoster.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/badware_hoster/hagezi_hoster.rpz) |

### Dynamic Dns

| Source | Entries | File | Raw URL |
|--------|---------|------|---------|
| HaGeZi Dynamic DNS | 1,023 | [hagezi_dyndns.rpz](lists/dynamic_dns/hagezi_dyndns.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/dynamic_dns/hagezi_dyndns.rpz) |

### Malware

| Source | Entries | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Ransomware | 1,904 | [blp_ransomware.rpz](lists/malware/blp_ransomware.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/malware/blp_ransomware.rpz) |
| ThreatFox | 656 | [threatfox.rpz](lists/malware/threatfox.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/malware/threatfox.rpz) |
| URLhaus | 6,603 | [urlhaus.rpz](lists/malware/urlhaus.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/malware/urlhaus.rpz) |

### Phishing

| Source | Entries | File | Raw URL |
|--------|---------|------|---------|
| OpenPhish | 237 | [openphish.rpz](lists/phishing/openphish.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/phishing/openphish.rpz) |
| PhishTank | 26,678 | [phishtank.rpz](lists/phishing/phishtank.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/phishing/phishtank.rpz) |
| Phishing Army | 385,059 | [phishing_army.rpz](lists/phishing/phishing_army.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/phishing/phishing_army.rpz) |

### Scam

| Source | Entries | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Fraud | 195,904 | [blp_fraud.rpz](lists/scam/blp_fraud.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/scam/blp_fraud.rpz) |
| Block List Project Scam | 1,274 | [blp_scam.rpz](lists/scam/blp_scam.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/scam/blp_scam.rpz) |
| HaGeZi Fake | 14,346 | [hagezi_fake.rpz](lists/scam/hagezi_fake.rpz) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/rpz/lists/scam/hagezi_fake.rpz) |

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

- Start with the aggregated categories before stacking many source files
- Whitelist when needed and watch your resolver logs after major changes
- Exact-host security and RPZ layers are more aggressive than the standard services layer
- Source feeds change over time, so entry counts will drift
