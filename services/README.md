# Threat Intelligence & Content Blocklists

**Generated:** 2026-05-05 05:19:44 UTC

**Audience:** Home-safe / standard

**False-Positive Risk:** Moderate

Home-safe default layer for Pi-hole, AdGuard Home, and similar DNS blockers. Lists stay registrable-domain based by default so they are easier to reason about and less likely to overblock.

## Output Tiers

- **[services](../services/README.md)** - home-safe, registrable-domain blocklists
- **[security](../security/README.md)** - exact-host security blocklists
- **[rpz](../rpz/README.md)** - Unbound-friendly RPZ policies
- **[hardening](../hardening/README.md)** - DNSTwist-derived brand impersonation blocklists
- **[active impersonation review](../hardening/active_impersonation/README.md)** - scored live-lookalike review reports

## Quick Start (Recommended)

Use the aggregated category lists below if you want broad blocking with lower churn and easier troubleshooting.

## Recommended Entry Points

Use these starter bundles if you want a fast, opinionated default instead of picking categories one by one.

| Bundle | Best For | Root Domains | Includes | File | Raw URL |
|--------|----------|---------|----------|------|---------|
| **Home Safe** | Most home users | 781,967 | Abuse & Malvertising, Badware Hosters, Dynamic DNS, Malware & Threats, Phishing & Scam Sites, Redirectors, Scam & Fraud, Tracking & Analytics | [home_safe.txt](recommended/home_safe.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/recommended/home_safe.txt) |
| **Family** | Shared devices and kid-safe networks | 879,956 | Abuse & Malvertising, Adult Content, Badware Hosters, Dating Services, Drugs, Dynamic DNS, Gambling & Betting, Malware & Threats, Phishing & Scam Sites, Redirectors, Scam & Fraud, Tracking & Analytics, Vaping | [family.txt](recommended/family.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/recommended/family.txt) |
| **Aggressive** | Lock-it-down blocking | 885,631 | Abuse & Malvertising, Adult Content, Badware Hosters, Crypto & Cryptojacking, Dating Services, Drugs, Dynamic DNS, Gambling & Betting, Malware & Threats, Phishing & Scam Sites, Piracy, Redirectors, Scam & Fraud, Torrent, Tracking & Analytics, Vaping | [aggressive.txt](recommended/aggressive.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/recommended/aggressive.txt) |

## Why Trust This Layer

- Public Suffix List-aware domain normalization prevents bad roots like `co.uk` from leaking into generated outputs
- Repo-local source policies remove noisy shared infrastructure and known false-positive patterns before lists are written
- Validation reports are published at [quality_report.json](quality_report.json) and check syntax, exclusions, and count drift
- Standard, exact-host, and RPZ outputs are generated from the same source graph so the repo stays internally consistent

## Aggregated Categories

One-click blocklists combining multiple sources for everyday blocking.

| Category | Root Domains | Sources | File | Raw URL |
|----------|---------|---------|------|---------|
| [🚨 Abuse & Malvertising](#abuse) | 240,662 | 1 | [abuse.txt](categories/abuse.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/abuse.txt) |
| [🔞 Adult Content](#adult) | 78,667 | 3 | [adult.txt](categories/adult.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/adult.txt) |
| [🤖 AI Assistants](#ai) | 19 | 9 | [ai.txt](categories/ai.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/ai.txt) |
| [🗄️ Badware Hosters](#badware-hoster) | 1,316 | 1 | [badware_hoster.txt](categories/badware_hoster.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/badware_hoster.txt) |
| [☁️ CDNs & Edge](#cdn) | 24 | 1 | [cdn.txt](categories/cdn.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/cdn.txt) |
| [🪙 Crypto & Cryptojacking](#crypto) | 8,130 | 1 | [crypto.txt](categories/crypto.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/crypto.txt) |
| [💕 Dating Services](#dating) | 1,303 | 1060 | [dating.txt](categories/dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/dating.txt) |
| [🛜 DNS Providers](#dns) | 2 | 2 | [dns.txt](categories/dns.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/dns.txt) |
| [🛡️ DNS / VPN Bypass](#dns-bypass) | 18,907 | 1 | [dns_bypass.txt](categories/dns_bypass.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/dns_bypass.txt) |
| [💊 Drugs](#drugs) | 18,320 | 1 | [drugs.txt](categories/drugs.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/drugs.txt) |
| [🌐 Dynamic DNS](#dynamic-dns) | 1,022 | 1 | [dynamic_dns.txt](categories/dynamic_dns.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/dynamic_dns.txt) |
| [🎰 Gambling & Betting](#gambling) | 33 | 4 | [gambling.txt](categories/gambling.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/gambling.txt) |
| [🎮 Gaming Platforms](#gaming) | 171 | 33 | [gaming.txt](categories/gaming.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/gaming.txt) |
| [🗃️ Hosting & File Platforms](#hosting) | 33 | 4 | [hosting.txt](categories/hosting.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/hosting.txt) |
| [🦠 Malware & Threats](#malware) | 3,374 | 3 | [malware.txt](categories/malware.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/malware.txt) |
| [💬 Messaging Apps](#messenger) | 55 | 12 | [messenger.txt](categories/messenger.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/messenger.txt) |
| [🎣 Phishing & Scam Sites](#phishing) | 302,095 | 3 | [phishing.txt](categories/phishing.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/phishing.txt) |
| [🏴‍☠️ Piracy](#piracy) | 1,065 | 1 | [piracy.txt](categories/piracy.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/piracy.txt) |
| [🕶️ Privacy Tools](#privacy) | 6 | 2 | [privacy.txt](categories/privacy.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/privacy.txt) |
| [↪️ Redirectors](#redirect) | 99,201 | 1 | [redirect.txt](categories/redirect.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/redirect.txt) |
| [💸 Scam & Fraud](#scam) | 129,164 | 3 | [scam.txt](categories/scam.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/scam.txt) |
| [🛍️ Shopping & Marketplaces](#shopping) | 567 | 10 | [shopping.txt](categories/shopping.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/shopping.txt) |
| [📡 Smart TV Telemetry](#smart-tv) | 70 | 1 | [smart_tv.txt](categories/smart_tv.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/smart_tv.txt) |
| [📱 Social Networks](#social-network) | 835 | 26 | [social_network.txt](categories/social_network.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/social_network.txt) |
| [🧰 Software & Updates](#software) | 13 | 2 | [software.txt](categories/software.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/software.txt) |
| [📺 Streaming Services](#streaming) | 454 | 41 | [streaming.txt](categories/streaming.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/streaming.txt) |
| [🧲 Torrent](#torrent) | 2,192 | 1 | [torrent.txt](categories/torrent.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/torrent.txt) |
| [🛰️ Tracking & Analytics](#tracking) | 14,761 | 1 | [tracking.txt](categories/tracking.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/tracking.txt) |
| [🔗 URL Shorteners](#url-shortener) | 9,930 | 1 | [url_shortener.txt](categories/url_shortener.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/url_shortener.txt) |
| [💨 Vaping](#vaping) | 32 | 1 | [vaping.txt](categories/vaping.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/vaping.txt) |

## Individual Sources

For granular control, each source is available separately if you want source-level attribution or need to disable one feed.

### Abuse & Malvertising

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Abuse | 240,662 | [blp_abuse.txt](lists/abuse/blp_abuse.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/abuse/blp_abuse.txt) |

### Adult Content

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Chad Mayfield Porn | 5,539 | [chadmayfield_porn.txt](lists/adult/chadmayfield_porn.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/adult/chadmayfield_porn.txt) |
| Grindr | 1 | [grindr.txt](lists/adult/grindr.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/adult/grindr.txt) |
| StevenBlack Porn | 76,108 | [stevenblack_porn.txt](lists/adult/stevenblack_porn.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/adult/stevenblack_porn.txt) |

### AI Assistants

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| ChatGPT | 4 | [chatgpt.txt](lists/ai/chatgpt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/ai/chatgpt.txt) |
| Claude | 2 | [claude.txt](lists/ai/claude.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/ai/claude.txt) |
| Copilot | 4 | [copilot.txt](lists/ai/copilot.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/ai/copilot.txt) |
| DeepSeek | 1 | [deepseek.txt](lists/ai/deepseek.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/ai/deepseek.txt) |
| Gemini | 2 | [gemini.txt](lists/ai/gemini.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/ai/gemini.txt) |
| Grok | 2 | [grok.txt](lists/ai/grok.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/ai/grok.txt) |
| Manus | 2 | [manus.txt](lists/ai/manus.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/ai/manus.txt) |
| Meta AI | 1 | [meta_ai.txt](lists/ai/meta_ai.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/ai/meta_ai.txt) |
| Perplexity | 1 | [perplexity.txt](lists/ai/perplexity.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/ai/perplexity.txt) |

### Badware Hosters

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| HaGeZi Badware Hoster | 1,316 | [hagezi_hoster.txt](lists/badware_hoster/hagezi_hoster.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/badware_hoster/hagezi_hoster.txt) |

### CDNs & Edge

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Cloudflare | 24 | [cloudflare.txt](lists/cdn/cloudflare.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/cdn/cloudflare.txt) |

### Crypto & Cryptojacking

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Crypto | 8,130 | [blp_crypto.txt](lists/crypto/blp_crypto.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/crypto/blp_crypto.txt) |

### Dating Services

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| 100 Best Dating Sites | 1 | [100_best_dating_sites.txt](lists/dating/100_best_dating_sites.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/100_best_dating_sites.txt) |
| 100 Best Single Sites | 1 | [100_best_single_sites.txt](lists/dating/100_best_single_sites.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/100_best_single_sites.txt) |
| 100 Top Dating Sites | 1 | [100_top_dating_sites.txt](lists/dating/100_top_dating_sites.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/100_top_dating_sites.txt) |
| 1000 Dating Sites | 1 | [1000_dating_sites.txt](lists/dating/1000_dating_sites.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/1000_dating_sites.txt) |
| 101Date | 1 | [101date.txt](lists/dating/101date.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/101date.txt) |
| 10Meilleurssitesderencontre | 1 | [10meilleurssitesderencontre.txt](lists/dating/10meilleurssitesderencontre.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/10meilleurssitesderencontre.txt) |
| 121Christiandating | 1 | [121christiandating.txt](lists/dating/121christiandating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/121christiandating.txt) |
| 121Cosplaydating | 1 | [121cosplaydating.txt](lists/dating/121cosplaydating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/121cosplaydating.txt) |
| 121Gaydating | 1 | [121gaydating.txt](lists/dating/121gaydating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/121gaydating.txt) |
| 123Date | 1 | [123date.txt](lists/dating/123date.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/123date.txt) |
| 123Jerencontre | 1 | [123jerencontre.txt](lists/dating/123jerencontre.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/123jerencontre.txt) |
| 12Meet | 1 | [12meet.txt](lists/dating/12meet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/12meet.txt) |
| 12Meetsenior | 1 | [12meetsenior.txt](lists/dating/12meetsenior.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/12meetsenior.txt) |
| 1St International | 1 | [1st_international.txt](lists/dating/1st_international.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/1st_international.txt) |
| 1St Russian Bride | 1 | [1st_russian_bride.txt](lists/dating/1st_russian_bride.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/1st_russian_bride.txt) |
| 2 Brides | 1 | [2_brides.txt](lists/dating/2_brides.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/2_brides.txt) |
| 25Dates | 1 | [25dates.txt](lists/dating/25dates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/25dates.txt) |
| 2Be2 | 1 | [2be2.txt](lists/dating/2be2.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/2be2.txt) |
| 2Become1 | 1 | [2become1.txt](lists/dating/2become1.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/2become1.txt) |
| 2Wives | 1 | [2wives.txt](lists/dating/2wives.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/2wives.txt) |
| 30Millionsderencontres | 1 | [30millionsderencontres.txt](lists/dating/30millionsderencontres.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/30millionsderencontres.txt) |
| 40 2 60 | 1 | [40_2_60.txt](lists/dating/40_2_60.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/40_2_60.txt) |
| 40Plusengeil | 1 | [40plusengeil.txt](lists/dating/40plusengeil.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/40plusengeil.txt) |
| 411 Singles | 1 | [411_singles.txt](lists/dating/411_singles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/411_singles.txt) |
| 5 A 7 | 1 | [5_a_7.txt](lists/dating/5_a_7.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/5_a_7.txt) |
| 50Datingnorway | 1 | [50datingnorway.txt](lists/dating/50datingnorway.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/50datingnorway.txt) |
| 8At8 | 1 | [8at8.txt](lists/dating/8at8.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/8at8.txt) |
| 97Tibo | 1 | [97tibo.txt](lists/dating/97tibo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/97tibo.txt) |
| Abcdatingadvisor | 1 | [abcdatingadvisor.txt](lists/dating/abcdatingadvisor.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/abcdatingadvisor.txt) |
| Abledlove | 1 | [abledlove.txt](lists/dating/abledlove.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/abledlove.txt) |
| Ablesingles | 1 | [ablesingles.txt](lists/dating/ablesingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ablesingles.txt) |
| Academicsingles | 1 | [academicsingles.txt](lists/dating/academicsingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/academicsingles.txt) |
| Academysingles | 1 | [academysingles.txt](lists/dating/academysingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/academysingles.txt) |
| Accords Franco Russes | 1 | [accords_franco_russes.txt](lists/dating/accords_franco_russes.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/accords_franco_russes.txt) |
| Adam And Eva | 1 | [adam_and_eva.txt](lists/dating/adam_and_eva.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/adam_and_eva.txt) |
| Adultdatelink | 1 | [adultdatelink.txt](lists/dating/adultdatelink.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/adultdatelink.txt) |
| Adultgaypersonals | 1 | [adultgaypersonals.txt](lists/dating/adultgaypersonals.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/adultgaypersonals.txt) |
| Adxpartner | 1 | [adxpartner.txt](lists/dating/adxpartner.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/adxpartner.txt) |
| Affection | 1 | [affection.txt](lists/dating/affection.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/affection.txt) |
| Affiny | 1 | [affiny.txt](lists/dating/affiny.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/affiny.txt) |
| Afrointroductions | 1 | [afrointroductions.txt](lists/dating/afrointroductions.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/afrointroductions.txt) |
| Afroromance | 1 | [afroromance.txt](lists/dating/afroromance.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/afroromance.txt) |
| Agapechristiansingles | 1 | [agapechristiansingles.txt](lists/dating/agapechristiansingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/agapechristiansingles.txt) |
| Agematch | 1 | [agematch.txt](lists/dating/agematch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/agematch.txt) |
| Alena Marriage Agency | 1 | [alena_marriage_agency.txt](lists/dating/alena_marriage_agency.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/alena_marriage_agency.txt) |
| Allianceinter | 1 | [allianceinter.txt](lists/dating/allianceinter.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/allianceinter.txt) |
| Alompartner | 1 | [alompartner.txt](lists/dating/alompartner.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/alompartner.txt) |
| Alovoa | 1 | [alovoa.txt](lists/dating/alovoa.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/alovoa.txt) |
| Amateurmatch | 1 | [amateurmatch.txt](lists/dating/amateurmatch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/amateurmatch.txt) |
| Ambiancematchmaking | 1 | [ambiancematchmaking.txt](lists/dating/ambiancematchmaking.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ambiancematchmaking.txt) |
| Ameety | 1 | [ameety.txt](lists/dating/ameety.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ameety.txt) |
| Amelie Agence | 1 | [amelie_agence.txt](lists/dating/amelie_agence.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/amelie_agence.txt) |
| Americandatingplanet | 1 | [americandatingplanet.txt](lists/dating/americandatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/americandatingplanet.txt) |
| Amiez | 1 | [amiez.txt](lists/dating/amiez.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/amiez.txt) |
| Amigos | 1 | [amigos.txt](lists/dating/amigos.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/amigos.txt) |
| Amigosamores | 1 | [amigosamores.txt](lists/dating/amigosamores.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/amigosamores.txt) |
| Amiouplus | 1 | [amiouplus.txt](lists/dating/amiouplus.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/amiouplus.txt) |
| Amistarium | 1 | [amistarium.txt](lists/dating/amistarium.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/amistarium.txt) |
| Amour | 1 | [amour.txt](lists/dating/amour.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/amour.txt) |
| Amourfactory | 1 | [amourfactory.txt](lists/dating/amourfactory.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/amourfactory.txt) |
| Amourland | 1 | [amourland.txt](lists/dating/amourland.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/amourland.txt) |
| Amours Bio | 1 | [amours_bio.txt](lists/dating/amours_bio.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/amours_bio.txt) |
| Amourtimes | 1 | [amourtimes.txt](lists/dating/amourtimes.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/amourtimes.txt) |
| Amputeeangels | 1 | [amputeeangels.txt](lists/dating/amputeeangels.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/amputeeangels.txt) |
| Anastasiadate | 1 | [anastasiadate.txt](lists/dating/anastasiadate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/anastasiadate.txt) |
| Annonce De Rencontre | 1 | [annonce_de_rencontre.txt](lists/dating/annonce_de_rencontre.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/annonce_de_rencontre.txt) |
| Annuncipersesso | 1 | [annuncipersesso.txt](lists/dating/annuncipersesso.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/annuncipersesso.txt) |
| Aondenamoro | 1 | [aondenamoro.txt](lists/dating/aondenamoro.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/aondenamoro.txt) |
| Apiteamn | 1 | [apiteamn.txt](lists/dating/apiteamn.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/apiteamn.txt) |
| Appart Ages | 1 | [appart_ages.txt](lists/dating/appart_ages.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/appart_ages.txt) |
| Arabdatingplanet | 1 | [arabdatingplanet.txt](lists/dating/arabdatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/arabdatingplanet.txt) |
| Arabiandate | 1 | [arabiandate.txt](lists/dating/arabiandate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/arabiandate.txt) |
| Armadillo | 1 | [armadillo.txt](lists/dating/armadillo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/armadillo.txt) |
| Asexualitic | 1 | [asexualitic.txt](lists/dating/asexualitic.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asexualitic.txt) |
| Asiafind | 1 | [asiafind.txt](lists/dating/asiafind.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asiafind.txt) |
| Asiafriendfinder | 1 | [asiafriendfinder.txt](lists/dating/asiafriendfinder.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asiafriendfinder.txt) |
| Asiame | 1 | [asiame.txt](lists/dating/asiame.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asiame.txt) |
| Asian Meet | 1 | [asian_meet.txt](lists/dating/asian_meet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asian_meet.txt) |
| Asiandating | 1 | [asiandating.txt](lists/dating/asiandating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asiandating.txt) |
| Asiandatingplanet | 1 | [asiandatingplanet.txt](lists/dating/asiandatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asiandatingplanet.txt) |
| Asianfaces | 1 | [asianfaces.txt](lists/dating/asianfaces.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asianfaces.txt) |
| Asianfriendfinder | 1 | [asianfriendfinder.txt](lists/dating/asianfriendfinder.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asianfriendfinder.txt) |
| Asiangirls4U | 1 | [asiangirls4u.txt](lists/dating/asiangirls4u.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asiangirls4u.txt) |
| Asianhearts | 1 | [asianhearts.txt](lists/dating/asianhearts.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asianhearts.txt) |
| Asianlovesearch | 1 | [asianlovesearch.txt](lists/dating/asianlovesearch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asianlovesearch.txt) |
| Asianmatching | 1 | [asianmatching.txt](lists/dating/asianmatching.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asianmatching.txt) |
| Asianpeoplemeet | 1 | [asianpeoplemeet.txt](lists/dating/asianpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asianpeoplemeet.txt) |
| Asianwomendate | 1 | [asianwomendate.txt](lists/dating/asianwomendate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asianwomendate.txt) |
| Asianwomenplanet | 1 | [asianwomenplanet.txt](lists/dating/asianwomenplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/asianwomenplanet.txt) |
| Ata Rencontre | 1 | [ata_rencontre.txt](lists/dating/ata_rencontre.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ata_rencontre.txt) |
| Australiadatingplanet | 1 | [australiadatingplanet.txt](lists/dating/australiadatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/australiadatingplanet.txt) |
| B2D8 | 1 | [b2d8.txt](lists/dating/b2d8.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/b2d8.txt) |
| Babes2Date | 1 | [babes2date.txt](lists/dating/babes2date.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/babes2date.txt) |
| Babyboomerpeoplemeet | 1 | [babyboomerpeoplemeet.txt](lists/dating/babyboomerpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/babyboomerpeoplemeet.txt) |
| Badoo | 2 | [badoo.txt](lists/dating/badoo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/badoo.txt) |
| Baltic Women | 1 | [baltic_women.txt](lists/dating/baltic_women.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/baltic_women.txt) |
| Bangatrans | 1 | [bangatrans.txt](lists/dating/bangatrans.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bangatrans.txt) |
| Baseballovers | 1 | [baseballovers.txt](lists/dating/baseballovers.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/baseballovers.txt) |
| Bbpeoplemeet | 2 | [bbpeoplemeet.txt](lists/dating/bbpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bbpeoplemeet.txt) |
| Bbwcupid | 1 | [bbwcupid.txt](lists/dating/bbwcupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bbwcupid.txt) |
| Be2 | 10 | [be2.txt](lists/dating/be2.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/be2.txt) |
| Beboo | 1 | [beboo.txt](lists/dating/beboo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/beboo.txt) |
| Becoquin | 1 | [becoquin.txt](lists/dating/becoquin.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/becoquin.txt) |
| Behappy2Day | 1 | [behappy2day.txt](lists/dating/behappy2day.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/behappy2day.txt) |
| Benaughty | 1 | [benaughty.txt](lists/dating/benaughty.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/benaughty.txt) |
| Beshert | 1 | [beshert.txt](lists/dating/beshert.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/beshert.txt) |
| Bestprice | 1 | [bestprice.txt](lists/dating/bestprice.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bestprice.txt) |
| Bestrussianwoman | 1 | [bestrussianwoman.txt](lists/dating/bestrussianwoman.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bestrussianwoman.txt) |
| Bez Kompleksov | 1 | [bez_kompleksov.txt](lists/dating/bez_kompleksov.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bez_kompleksov.txt) |
| Bezzabran | 1 | [bezzabran.txt](lists/dating/bezzabran.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bezzabran.txt) |
| Bi Dating | 1 | [bi_dating.txt](lists/dating/bi_dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bi_dating.txt) |
| Bicupid | 1 | [bicupid.txt](lists/dating/bicupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bicupid.txt) |
| Bigchurch | 1 | [bigchurch.txt](lists/dating/bigchurch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bigchurch.txt) |
| Bikerdatelink | 1 | [bikerdatelink.txt](lists/dating/bikerdatelink.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bikerdatelink.txt) |
| Bikerplanet | 1 | [bikerplanet.txt](lists/dating/bikerplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bikerplanet.txt) |
| Bildkontakte | 1 | [bildkontakte.txt](lists/dating/bildkontakte.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bildkontakte.txt) |
| Bisexualfling | 1 | [bisexualfling.txt](lists/dating/bisexualfling.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bisexualfling.txt) |
| Blackbabyboomermeet | 1 | [blackbabyboomermeet.txt](lists/dating/blackbabyboomermeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/blackbabyboomermeet.txt) |
| Blacklesbianclub | 1 | [blacklesbianclub.txt](lists/dating/blacklesbianclub.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/blacklesbianclub.txt) |
| Blackpeoplemeet | 1 | [blackpeoplemeet.txt](lists/dating/blackpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/blackpeoplemeet.txt) |
| Blackprofessionalpeoplemeet | 1 | [blackprofessionalpeoplemeet.txt](lists/dating/blackprofessionalpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/blackprofessionalpeoplemeet.txt) |
| Blackscene | 1 | [blackscene.txt](lists/dating/blackscene.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/blackscene.txt) |
| Blackwhite | 1 | [blackwhite.txt](lists/dating/blackwhite.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/blackwhite.txt) |
| Blackwhitedatingreviews | 1 | [blackwhitedatingreviews.txt](lists/dating/blackwhitedatingreviews.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/blackwhitedatingreviews.txt) |
| Blossoms | 1 | [blossoms.txt](lists/dating/blossoms.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/blossoms.txt) |
| Blueswingers | 1 | [blueswingers.txt](lists/dating/blueswingers.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/blueswingers.txt) |
| Bonplanrencontre | 1 | [bonplanrencontre.txt](lists/dating/bonplanrencontre.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bonplanrencontre.txt) |
| Boo | 2 | [boo.txt](lists/dating/boo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/boo.txt) |
| Bookofmatches | 1 | [bookofmatches.txt](lists/dating/bookofmatches.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bookofmatches.txt) |
| Brazil Bbw | 1 | [brazil_bbw.txt](lists/dating/brazil_bbw.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/brazil_bbw.txt) |
| Brazilcupid | 1 | [brazilcupid.txt](lists/dating/brazilcupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/brazilcupid.txt) |
| Bride | 1 | [bride.txt](lists/dating/bride.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bride.txt) |
| Briefdating | 1 | [briefdating.txt](lists/dating/briefdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/briefdating.txt) |
| Bum | 1 | [bum.txt](lists/dating/bum.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bum.txt) |
| Bumble | 3 | [bumble.txt](lists/dating/bumble.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bumble.txt) |
| Buscoamigos | 1 | [buscoamigos.txt](lists/dating/buscoamigos.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/buscoamigos.txt) |
| Bustysingles | 1 | [bustysingles.txt](lists/dating/bustysingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/bustysingles.txt) |
| Buzzarab | 1 | [buzzarab.txt](lists/dating/buzzarab.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/buzzarab.txt) |
| C Date | 2 | [c_date.txt](lists/dating/c_date.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/c_date.txt) |
| C Dating | 1 | [c_dating.txt](lists/dating/c_dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/c_dating.txt) |
| Californiaflirt | 1 | [californiaflirt.txt](lists/dating/californiaflirt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/californiaflirt.txt) |
| Campus | 1 | [campus.txt](lists/dating/campus.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/campus.txt) |
| Casual Date | 1 | [casual_date.txt](lists/dating/casual_date.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/casual_date.txt) |
| Casual Fling | 1 | [casual_fling.txt](lists/dating/casual_fling.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/casual_fling.txt) |
| Casualdating | 1 | [casualdating.txt](lists/dating/casualdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/casualdating.txt) |
| Casualdating Club | 1 | [casualdating_club.txt](lists/dating/casualdating_club.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/casualdating_club.txt) |
| Casualdating4U | 1 | [casualdating4u.txt](lists/dating/casualdating4u.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/casualdating4u.txt) |
| Casualdating69 | 1 | [casualdating69.txt](lists/dating/casualdating69.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/casualdating69.txt) |
| Casualfriendfinder | 1 | [casualfriendfinder.txt](lists/dating/casualfriendfinder.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/casualfriendfinder.txt) |
| Casualrandki | 1 | [casualrandki.txt](lists/dating/casualrandki.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/casualrandki.txt) |
| Casualxhookups | 1 | [casualxhookups.txt](lists/dating/casualxhookups.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/casualxhookups.txt) |
| Catholicmates | 1 | [catholicmates.txt](lists/dating/catholicmates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/catholicmates.txt) |
| Catholicpeoplemeet | 1 | [catholicpeoplemeet.txt](lists/dating/catholicpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/catholicpeoplemeet.txt) |
| Celibapatch | 1 | [celibapatch.txt](lists/dating/celibapatch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/celibapatch.txt) |
| Celibatairesduweb | 1 | [celibatairesduweb.txt](lists/dating/celibatairesduweb.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/celibatairesduweb.txt) |
| Celibest | 1 | [celibest.txt](lists/dating/celibest.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/celibest.txt) |
| Celibouest | 1 | [celibouest.txt](lists/dating/celibouest.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/celibouest.txt) |
| Celibparis | 1 | [celibparis.txt](lists/dating/celibparis.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/celibparis.txt) |
| Chatdate | 1 | [chatdate.txt](lists/dating/chatdate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/chatdate.txt) |
| Chattijd | 1 | [chattijd.txt](lists/dating/chattijd.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/chattijd.txt) |
| Chemistry | 1 | [chemistry.txt](lists/dating/chemistry.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/chemistry.txt) |
| Chinesedating | 1 | [chinesedating.txt](lists/dating/chinesedating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/chinesedating.txt) |
| Chinesefriendfinder | 1 | [chinesefriendfinder.txt](lists/dating/chinesefriendfinder.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/chinesefriendfinder.txt) |
| Chinesekisses | 1 | [chinesekisses.txt](lists/dating/chinesekisses.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/chinesekisses.txt) |
| Chinesepeoplemeet | 1 | [chinesepeoplemeet.txt](lists/dating/chinesepeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/chinesepeoplemeet.txt) |
| Chinesepersonals | 1 | [chinesepersonals.txt](lists/dating/chinesepersonals.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/chinesepersonals.txt) |
| Christianamericansingles | 1 | [christianamericansingles.txt](lists/dating/christianamericansingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/christianamericansingles.txt) |
| Christiancafe | 1 | [christiancafe.txt](lists/dating/christiancafe.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/christiancafe.txt) |
| Christianconnection | 1 | [christianconnection.txt](lists/dating/christianconnection.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/christianconnection.txt) |
| Christiancupid | 1 | [christiancupid.txt](lists/dating/christiancupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/christiancupid.txt) |
| Christiandatingforfree | 1 | [christiandatingforfree.txt](lists/dating/christiandatingforfree.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/christiandatingforfree.txt) |
| Christiandisableddating | 1 | [christiandisableddating.txt](lists/dating/christiandisableddating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/christiandisableddating.txt) |
| Christianlifestyle | 1 | [christianlifestyle.txt](lists/dating/christianlifestyle.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/christianlifestyle.txt) |
| Christianmingle | 1 | [christianmingle.txt](lists/dating/christianmingle.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/christianmingle.txt) |
| Citassenioronline | 1 | [citassenioronline.txt](lists/dating/citassenioronline.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/citassenioronline.txt) |
| Clickandflirt | 1 | [clickandflirt.txt](lists/dating/clickandflirt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/clickandflirt.txt) |
| Clubeamizade | 1 | [clubeamizade.txt](lists/dating/clubeamizade.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/clubeamizade.txt) |
| Clubedamizade | 1 | [clubedamizade.txt](lists/dating/clubedamizade.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/clubedamizade.txt) |
| Clubs De Rencontres | 1 | [clubs_de_rencontres.txt](lists/dating/clubs_de_rencontres.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/clubs_de_rencontres.txt) |
| Clubsadomasoquismo | 1 | [clubsadomasoquismo.txt](lists/dating/clubsadomasoquismo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/clubsadomasoquismo.txt) |
| Coffee Meets Bagel | 1 | [coffee_meets_bagel.txt](lists/dating/coffee_meets_bagel.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/coffee_meets_bagel.txt) |
| Comunidadbondage | 1 | [comunidadbondage.txt](lists/dating/comunidadbondage.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/comunidadbondage.txt) |
| Conexionbisexual | 1 | [conexionbisexual.txt](lists/dating/conexionbisexual.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/conexionbisexual.txt) |
| Conexiongay | 1 | [conexiongay.txt](lists/dating/conexiongay.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/conexiongay.txt) |
| Conexiontrios | 1 | [conexiontrios.txt](lists/dating/conexiontrios.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/conexiontrios.txt) |
| Connectingsingles | 1 | [connectingsingles.txt](lists/dating/connectingsingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/connectingsingles.txt) |
| Contactos Casuales | 1 | [contactos_casuales.txt](lists/dating/contactos_casuales.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/contactos_casuales.txt) |
| Contactsingles | 1 | [contactsingles.txt](lists/dating/contactsingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/contactsingles.txt) |
| Cooldating | 1 | [cooldating.txt](lists/dating/cooldating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/cooldating.txt) |
| Coolsitesforsingles | 1 | [coolsitesforsingles.txt](lists/dating/coolsitesforsingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/coolsitesforsingles.txt) |
| Cougar | 1 | [cougar.txt](lists/dating/cougar.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/cougar.txt) |
| Countrysinglesplace | 1 | [countrysinglesplace.txt](lists/dating/countrysinglesplace.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/countrysinglesplace.txt) |
| Couplesdating | 1 | [couplesdating.txt](lists/dating/couplesdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/couplesdating.txt) |
| Crossdressinglover | 1 | [crossdressinglover.txt](lists/dating/crossdressinglover.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/crossdressinglover.txt) |
| Csajokespasik | 1 | [csajokespasik.txt](lists/dating/csajokespasik.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/csajokespasik.txt) |
| Cuckold Lovers | 1 | [cuckold_lovers.txt](lists/dating/cuckold_lovers.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/cuckold_lovers.txt) |
| Cuddlyconnect | 1 | [cuddlyconnect.txt](lists/dating/cuddlyconnect.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/cuddlyconnect.txt) |
| Cupid | 1 | [cupid.txt](lists/dating/cupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/cupid.txt) |
| Cupid Match | 1 | [cupid_match.txt](lists/dating/cupid_match.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/cupid_match.txt) |
| Cupidbay | 1 | [cupidbay.txt](lists/dating/cupidbay.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/cupidbay.txt) |
| Cupidmedia | 1 | [cupidmedia.txt](lists/dating/cupidmedia.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/cupidmedia.txt) |
| Cupido | 1 | [cupido.txt](lists/dating/cupido.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/cupido.txt) |
| Czech Bride | 1 | [czech_bride.txt](lists/dating/czech_bride.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/czech_bride.txt) |
| D8U | 1 | [d8u.txt](lists/dating/d8u.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/d8u.txt) |
| Date In Aachen | 1 | [date_in_aachen.txt](lists/dating/date_in_aachen.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_aachen.txt) |
| Date In Augsburg | 1 | [date_in_augsburg.txt](lists/dating/date_in_augsburg.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_augsburg.txt) |
| Date In Berlin | 1 | [date_in_berlin.txt](lists/dating/date_in_berlin.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_berlin.txt) |
| Date In Bielefeld | 1 | [date_in_bielefeld.txt](lists/dating/date_in_bielefeld.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_bielefeld.txt) |
| Date In Bochum | 1 | [date_in_bochum.txt](lists/dating/date_in_bochum.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_bochum.txt) |
| Date In Bonn | 1 | [date_in_bonn.txt](lists/dating/date_in_bonn.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_bonn.txt) |
| Date In Bremen | 1 | [date_in_bremen.txt](lists/dating/date_in_bremen.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_bremen.txt) |
| Date In Chemnitz | 1 | [date_in_chemnitz.txt](lists/dating/date_in_chemnitz.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_chemnitz.txt) |
| Date In Dortmund | 1 | [date_in_dortmund.txt](lists/dating/date_in_dortmund.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_dortmund.txt) |
| Date In Dresden | 1 | [date_in_dresden.txt](lists/dating/date_in_dresden.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_dresden.txt) |
| Date In Duesseldorf | 1 | [date_in_duesseldorf.txt](lists/dating/date_in_duesseldorf.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_duesseldorf.txt) |
| Date In Duisburg | 1 | [date_in_duisburg.txt](lists/dating/date_in_duisburg.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_duisburg.txt) |
| Date In Essen | 1 | [date_in_essen.txt](lists/dating/date_in_essen.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_essen.txt) |
| Date In Frankfurt | 1 | [date_in_frankfurt.txt](lists/dating/date_in_frankfurt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_frankfurt.txt) |
| Date In Halle | 1 | [date_in_halle.txt](lists/dating/date_in_halle.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_halle.txt) |
| Date In Hamburg | 1 | [date_in_hamburg.txt](lists/dating/date_in_hamburg.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_hamburg.txt) |
| Date In Hannover | 1 | [date_in_hannover.txt](lists/dating/date_in_hannover.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_hannover.txt) |
| Date In Karlsruhe | 1 | [date_in_karlsruhe.txt](lists/dating/date_in_karlsruhe.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_karlsruhe.txt) |
| Date In Kiel | 1 | [date_in_kiel.txt](lists/dating/date_in_kiel.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_kiel.txt) |
| Date In Koeln | 1 | [date_in_koeln.txt](lists/dating/date_in_koeln.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_koeln.txt) |
| Date In Leipzig | 1 | [date_in_leipzig.txt](lists/dating/date_in_leipzig.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_leipzig.txt) |
| Date In Mannheim | 1 | [date_in_mannheim.txt](lists/dating/date_in_mannheim.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_mannheim.txt) |
| Date In Muenchen | 1 | [date_in_muenchen.txt](lists/dating/date_in_muenchen.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_muenchen.txt) |
| Date In Muenster | 1 | [date_in_muenster.txt](lists/dating/date_in_muenster.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_muenster.txt) |
| Date In Nuernberg | 1 | [date_in_nuernberg.txt](lists/dating/date_in_nuernberg.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_nuernberg.txt) |
| Date In Potsdam | 1 | [date_in_potsdam.txt](lists/dating/date_in_potsdam.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_potsdam.txt) |
| Date In Rostock | 1 | [date_in_rostock.txt](lists/dating/date_in_rostock.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_rostock.txt) |
| Date In Stuttgart | 1 | [date_in_stuttgart.txt](lists/dating/date_in_stuttgart.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_stuttgart.txt) |
| Date In Wiesbaden | 1 | [date_in_wiesbaden.txt](lists/dating/date_in_wiesbaden.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_wiesbaden.txt) |
| Date In Wuppertal | 1 | [date_in_wuppertal.txt](lists/dating/date_in_wuppertal.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_wuppertal.txt) |
| Date In Zuerich | 1 | [date_in_zuerich.txt](lists/dating/date_in_zuerich.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_in_zuerich.txt) |
| Date Local Gays | 1 | [date_local_gays.txt](lists/dating/date_local_gays.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/date_local_gays.txt) |
| Dateasian | 1 | [dateasian.txt](lists/dating/dateasian.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dateasian.txt) |
| Dateasians | 1 | [dateasians.txt](lists/dating/dateasians.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dateasians.txt) |
| Datebrowse | 1 | [datebrowse.txt](lists/dating/datebrowse.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datebrowse.txt) |
| Dateforeal | 1 | [dateforeal.txt](lists/dating/dateforeal.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dateforeal.txt) |
| Datefromukraine | 1 | [datefromukraine.txt](lists/dating/datefromukraine.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datefromukraine.txt) |
| Datehotcougar | 1 | [datehotcougar.txt](lists/dating/datehotcougar.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datehotcougar.txt) |
| Dateinasia | 1 | [dateinasia.txt](lists/dating/dateinasia.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dateinasia.txt) |
| Dateinspire | 1 | [dateinspire.txt](lists/dating/dateinspire.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dateinspire.txt) |
| Dateland | 1 | [dateland.txt](lists/dating/dateland.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dateland.txt) |
| Dateleicestershiresingles | 1 | [dateleicestershiresingles.txt](lists/dating/dateleicestershiresingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dateleicestershiresingles.txt) |
| Datelinknetworks | 1 | [datelinknetworks.txt](lists/dating/datelinknetworks.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datelinknetworks.txt) |
| Datememe | 1 | [datememe.txt](lists/dating/datememe.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datememe.txt) |
| Datemypet | 1 | [datemypet.txt](lists/dating/datemypet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datemypet.txt) |
| Dateplaza | 1 | [dateplaza.txt](lists/dating/dateplaza.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dateplaza.txt) |
| Datereadingsingles | 1 | [datereadingsingles.txt](lists/dating/datereadingsingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datereadingsingles.txt) |
| Daterfinder | 1 | [daterfinder.txt](lists/dating/daterfinder.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/daterfinder.txt) |
| Datesabroad | 1 | [datesabroad.txt](lists/dating/datesabroad.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datesabroad.txt) |
| Dateseniors | 1 | [dateseniors.txt](lists/dating/dateseniors.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dateseniors.txt) |
| Dateseniorukrainian | 1 | [dateseniorukrainian.txt](lists/dating/dateseniorukrainian.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dateseniorukrainian.txt) |
| Datesforyou | 1 | [datesforyou.txt](lists/dating/datesforyou.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datesforyou.txt) |
| Datesuffolksingles | 1 | [datesuffolksingles.txt](lists/dating/datesuffolksingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datesuffolksingles.txt) |
| Datetheuk | 1 | [datetheuk.txt](lists/dating/datetheuk.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datetheuk.txt) |
| Datetonight | 1 | [datetonight.txt](lists/dating/datetonight.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datetonight.txt) |
| Datewesternislessingles | 1 | [datewesternislessingles.txt](lists/dating/datewesternislessingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datewesternislessingles.txt) |
| Datewithgays | 1 | [datewithgays.txt](lists/dating/datewithgays.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datewithgays.txt) |
| Datewiz | 1 | [datewiz.txt](lists/dating/datewiz.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datewiz.txt) |
| Dating | 1 | [dating.txt](lists/dating/dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dating.txt) |
| Dating Central | 1 | [dating_central.txt](lists/dating/dating_central.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dating_central.txt) |
| Dating Finder | 1 | [dating_finder.txt](lists/dating/dating_finder.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dating_finder.txt) |
| Dating Guides | 1 | [dating_guides.txt](lists/dating/dating_guides.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dating_guides.txt) |
| Dating In California | 1 | [dating_in_california.txt](lists/dating/dating_in_california.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dating_in_california.txt) |
| Dating Italy | 1 | [dating_italy.txt](lists/dating/dating_italy.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dating_italy.txt) |
| Dating Jedi | 1 | [dating_jedi.txt](lists/dating/dating_jedi.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dating_jedi.txt) |
| Dating Senior | 1 | [dating_senior.txt](lists/dating/dating_senior.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dating_senior.txt) |
| Dating Site | 1 | [dating_site.txt](lists/dating/dating_site.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dating_site.txt) |
| Dating South Africa | 1 | [dating_south_africa.txt](lists/dating/dating_south_africa.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dating_south_africa.txt) |
| Dating4Bisexuals | 1 | [dating4bisexuals.txt](lists/dating/dating4bisexuals.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dating4bisexuals.txt) |
| Datingagency | 1 | [datingagency.txt](lists/dating/datingagency.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingagency.txt) |
| Datinganerd | 1 | [datinganerd.txt](lists/dating/datinganerd.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datinganerd.txt) |
| Datingapp | 1 | [datingapp.txt](lists/dating/datingapp.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingapp.txt) |
| Datingbisexualsingles | 1 | [datingbisexualsingles.txt](lists/dating/datingbisexualsingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingbisexualsingles.txt) |
| Datingbookreview | 1 | [datingbookreview.txt](lists/dating/datingbookreview.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingbookreview.txt) |
| Datingbuzz | 3 | [datingbuzz.txt](lists/dating/datingbuzz.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingbuzz.txt) |
| Datingcafe | 1 | [datingcafe.txt](lists/dating/datingcafe.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingcafe.txt) |
| Datingfactory | 2 | [datingfactory.txt](lists/dating/datingfactory.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingfactory.txt) |
| Datingfantastic | 1 | [datingfantastic.txt](lists/dating/datingfantastic.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingfantastic.txt) |
| Datingforseniors | 2 | [datingforseniors.txt](lists/dating/datingforseniors.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingforseniors.txt) |
| Datinggayblacksingles | 1 | [datinggayblacksingles.txt](lists/dating/datinggayblacksingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datinggayblacksingles.txt) |
| Datinggold | 1 | [datinggold.txt](lists/dating/datinggold.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datinggold.txt) |
| Datingguide | 1 | [datingguide.txt](lists/dating/datingguide.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingguide.txt) |
| Datinghaven | 1 | [datinghaven.txt](lists/dating/datinghaven.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datinghaven.txt) |
| Datinginterracialsingles | 1 | [datinginterracialsingles.txt](lists/dating/datinginterracialsingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datinginterracialsingles.txt) |
| Datingline | 1 | [datingline.txt](lists/dating/datingline.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingline.txt) |
| Datingme | 1 | [datingme.txt](lists/dating/datingme.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingme.txt) |
| Datingoman | 1 | [datingoman.txt](lists/dating/datingoman.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingoman.txt) |
| Datingonline | 1 | [datingonline.txt](lists/dating/datingonline.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingonline.txt) |
| Datingplanet | 1 | [datingplanet.txt](lists/dating/datingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingplanet.txt) |
| Datingpro | 1 | [datingpro.txt](lists/dating/datingpro.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingpro.txt) |
| Datingrichgirls | 1 | [datingrichgirls.txt](lists/dating/datingrichgirls.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingrichgirls.txt) |
| Datingrussianangels | 1 | [datingrussianangels.txt](lists/dating/datingrussianangels.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingrussianangels.txt) |
| Datingscout | 1 | [datingscout.txt](lists/dating/datingscout.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingscout.txt) |
| Datingscript | 1 | [datingscript.txt](lists/dating/datingscript.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingscript.txt) |
| Datingsite | 1 | [datingsite.txt](lists/dating/datingsite.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingsite.txt) |
| Datingsites | 1 | [datingsites.txt](lists/dating/datingsites.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingsites.txt) |
| Datingsites Reviewed | 1 | [datingsites_reviewed.txt](lists/dating/datingsites_reviewed.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingsites_reviewed.txt) |
| Datingsitesreviews | 1 | [datingsitesreviews.txt](lists/dating/datingsitesreviews.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingsitesreviews.txt) |
| Datingsitexperts | 1 | [datingsitexperts.txt](lists/dating/datingsitexperts.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingsitexperts.txt) |
| Datingsmokers | 1 | [datingsmokers.txt](lists/dating/datingsmokers.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingsmokers.txt) |
| Datinguk | 1 | [datinguk.txt](lists/dating/datinguk.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datinguk.txt) |
| Datingvoormensenmeteenbeperking | 1 | [datingvoormensenmeteenbeperking.txt](lists/dating/datingvoormensenmeteenbeperking.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingvoormensenmeteenbeperking.txt) |
| Datingwebsite | 1 | [datingwebsite.txt](lists/dating/datingwebsite.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingwebsite.txt) |
| Datingwithherpes | 1 | [datingwithherpes.txt](lists/dating/datingwithherpes.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingwithherpes.txt) |
| Datingzero | 1 | [datingzero.txt](lists/dating/datingzero.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingzero.txt) |
| Datingzest | 1 | [datingzest.txt](lists/dating/datingzest.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/datingzest.txt) |
| Deafdatingzone | 1 | [deafdatingzone.txt](lists/dating/deafdatingzone.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/deafdatingzone.txt) |
| Deailinks | 1 | [deailinks.txt](lists/dating/deailinks.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/deailinks.txt) |
| Democraticpeoplemeet | 1 | [democraticpeoplemeet.txt](lists/dating/democraticpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/democraticpeoplemeet.txt) |
| Derya | 1 | [derya.txt](lists/dating/derya.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/derya.txt) |
| Dfg | 1 | [dfg.txt](lists/dating/dfg.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dfg.txt) |
| Dial | 93 | [dial.txt](lists/dating/dial.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dial.txt) |
| Dial2A | 1 | [dial2a.txt](lists/dating/dial2a.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dial2a.txt) |
| Dial2B | 1 | [dial2b.txt](lists/dating/dial2b.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dial2b.txt) |
| Dialweb | 1 | [dialweb.txt](lists/dating/dialweb.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dialweb.txt) |
| Diamond Dating | 1 | [diamond_dating.txt](lists/dating/diamond_dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/diamond_dating.txt) |
| Dilkarishta | 1 | [dilkarishta.txt](lists/dating/dilkarishta.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dilkarishta.txt) |
| Dirtysexdates | 1 | [dirtysexdates.txt](lists/dating/dirtysexdates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dirtysexdates.txt) |
| Disabilitydating | 1 | [disabilitydating.txt](lists/dating/disabilitydating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/disabilitydating.txt) |
| Disabilitymatch | 1 | [disabilitymatch.txt](lists/dating/disabilitymatch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/disabilitymatch.txt) |
| Disabledlove | 1 | [disabledlove.txt](lists/dating/disabledlove.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/disabledlove.txt) |
| Disabledpassions | 1 | [disabledpassions.txt](lists/dating/disabledpassions.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/disabledpassions.txt) |
| Disabledsinglesusa | 1 | [disabledsinglesusa.txt](lists/dating/disabledsinglesusa.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/disabledsinglesusa.txt) |
| Ditchordate | 1 | [ditchordate.txt](lists/dating/ditchordate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ditchordate.txt) |
| Divorceddatelink | 1 | [divorceddatelink.txt](lists/dating/divorceddatelink.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/divorceddatelink.txt) |
| Divorcedpeoplemeet | 1 | [divorcedpeoplemeet.txt](lists/dating/divorcedpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/divorcedpeoplemeet.txt) |
| Divorcedsingles | 1 | [divorcedsingles.txt](lists/dating/divorcedsingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/divorcedsingles.txt) |
| Dogdatingplanet | 1 | [dogdatingplanet.txt](lists/dating/dogdatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dogdatingplanet.txt) |
| Dogging | 1 | [dogging.txt](lists/dating/dogging.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dogging.txt) |
| Domerencontre | 1 | [domerencontre.txt](lists/dating/domerencontre.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/domerencontre.txt) |
| Donneimmature | 1 | [donneimmature.txt](lists/dating/donneimmature.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/donneimmature.txt) |
| Drawingdownthemoon | 1 | [drawingdownthemoon.txt](lists/dating/drawingdownthemoon.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/drawingdownthemoon.txt) |
| Dxbexpats | 1 | [dxbexpats.txt](lists/dating/dxbexpats.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/dxbexpats.txt) |
| E Amour | 1 | [e_amour.txt](lists/dating/e_amour.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/e_amour.txt) |
| Easternhoneys | 1 | [easternhoneys.txt](lists/dating/easternhoneys.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/easternhoneys.txt) |
| Easy Chat | 1 | [easy_chat.txt](lists/dating/easy_chat.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/easy_chat.txt) |
| Edarling | 1 | [edarling.txt](lists/dating/edarling.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/edarling.txt) |
| Edate | 1 | [edate.txt](lists/dating/edate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/edate.txt) |
| Edating | 1 | [edating.txt](lists/dating/edating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/edating.txt) |
| Edenlady | 1 | [edenlady.txt](lists/dating/edenlady.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/edenlady.txt) |
| Edesirs | 1 | [edesirs.txt](lists/dating/edesirs.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/edesirs.txt) |
| Elitedatingcompany | 1 | [elitedatingcompany.txt](lists/dating/elitedatingcompany.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/elitedatingcompany.txt) |
| Elitekink | 1 | [elitekink.txt](lists/dating/elitekink.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/elitekink.txt) |
| Elitemate | 1 | [elitemate.txt](lists/dating/elitemate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/elitemate.txt) |
| Elitesingles | 1 | [elitesingles.txt](lists/dating/elitesingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/elitesingles.txt) |
| Elovedates | 1 | [elovedates.txt](lists/dating/elovedates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/elovedates.txt) |
| Encount | 1 | [encount.txt](lists/dating/encount.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/encount.txt) |
| Encuentroadulto | 2 | [encuentroadulto.txt](lists/dating/encuentroadulto.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/encuentroadulto.txt) |
| Encuentrosparagays | 1 | [encuentrosparagays.txt](lists/dating/encuentrosparagays.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/encuentrosparagays.txt) |
| Engagedencounter | 1 | [engagedencounter.txt](lists/dating/engagedencounter.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/engagedencounter.txt) |
| Entrefemmes | 1 | [entrefemmes.txt](lists/dating/entrefemmes.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/entrefemmes.txt) |
| Entremetteurs | 1 | [entremetteurs.txt](lists/dating/entremetteurs.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/entremetteurs.txt) |
| Epolishwife | 1 | [epolishwife.txt](lists/dating/epolishwife.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/epolishwife.txt) |
| Erwinsdate | 1 | [erwinsdate.txt](lists/dating/erwinsdate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/erwinsdate.txt) |
| Espace Live | 1 | [espace_live.txt](lists/dating/espace_live.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/espace_live.txt) |
| Eterocuriosi | 1 | [eterocuriosi.txt](lists/dating/eterocuriosi.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/eterocuriosi.txt) |
| Europe Tchat Rencontre | 1 | [europe_tchat_rencontre.txt](lists/dating/europe_tchat_rencontre.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/europe_tchat_rencontre.txt) |
| Europeandating | 1 | [europeandating.txt](lists/dating/europeandating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/europeandating.txt) |
| Europeandatingplanet | 1 | [europeandatingplanet.txt](lists/dating/europeandatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/europeandatingplanet.txt) |
| Everflirt | 1 | [everflirt.txt](lists/dating/everflirt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/everflirt.txt) |
| Ex Patriates | 1 | [ex_patriates.txt](lists/dating/ex_patriates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ex_patriates.txt) |
| Facetoface | 1 | [facetoface.txt](lists/dating/facetoface.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/facetoface.txt) |
| Farmersonly | 1 | [farmersonly.txt](lists/dating/farmersonly.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/farmersonly.txt) |
| Fastmatch | 1 | [fastmatch.txt](lists/dating/fastmatch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/fastmatch.txt) |
| Fdating | 1 | [fdating.txt](lists/dating/fdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/fdating.txt) |
| Fetishcontacts | 1 | [fetishcontacts.txt](lists/dating/fetishcontacts.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/fetishcontacts.txt) |
| Filipinadatingsites | 1 | [filipinadatingsites.txt](lists/dating/filipinadatingsites.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/filipinadatingsites.txt) |
| Filipinawife | 1 | [filipinawife.txt](lists/dating/filipinawife.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/filipinawife.txt) |
| Filipinocupid | 1 | [filipinocupid.txt](lists/dating/filipinocupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/filipinocupid.txt) |
| Filipinofriendfinder | 1 | [filipinofriendfinder.txt](lists/dating/filipinofriendfinder.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/filipinofriendfinder.txt) |
| Filipinokisses | 1 | [filipinokisses.txt](lists/dating/filipinokisses.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/filipinokisses.txt) |
| Findanewlover | 1 | [findanewlover.txt](lists/dating/findanewlover.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/findanewlover.txt) |
| Findashemalelover | 1 | [findashemalelover.txt](lists/dating/findashemalelover.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/findashemalelover.txt) |
| Finder | 1 | [finder.txt](lists/dating/finder.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/finder.txt) |
| Findme | 1 | [findme.txt](lists/dating/findme.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/findme.txt) |
| Findmymatches | 1 | [findmymatches.txt](lists/dating/findmymatches.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/findmymatches.txt) |
| Finya | 1 | [finya.txt](lists/dating/finya.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/finya.txt) |
| Firstaffair | 1 | [firstaffair.txt](lists/dating/firstaffair.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/firstaffair.txt) |
| Fitness Singles | 1 | [fitness_singles.txt](lists/dating/fitness_singles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/fitness_singles.txt) |
| Fjortis | 1 | [fjortis.txt](lists/dating/fjortis.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/fjortis.txt) |
| Fling | 1 | [fling.txt](lists/dating/fling.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/fling.txt) |
| Flippedapp | 1 | [flippedapp.txt](lists/dating/flippedapp.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/flippedapp.txt) |
| Flirt Fever | 1 | [flirt_fever.txt](lists/dating/flirt_fever.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/flirt_fever.txt) |
| Flirt Jetzt | 1 | [flirt_jetzt.txt](lists/dating/flirt_jetzt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/flirt_jetzt.txt) |
| Flirtcafe | 1 | [flirtcafe.txt](lists/dating/flirtcafe.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/flirtcafe.txt) |
| Flirtdiscreti | 1 | [flirtdiscreti.txt](lists/dating/flirtdiscreti.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/flirtdiscreti.txt) |
| Flirtejetzt | 1 | [flirtejetzt.txt](lists/dating/flirtejetzt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/flirtejetzt.txt) |
| Flirthits | 1 | [flirthits.txt](lists/dating/flirthits.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/flirthits.txt) |
| Flirtic | 1 | [flirtic.txt](lists/dating/flirtic.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/flirtic.txt) |
| Flirtmoi | 1 | [flirtmoi.txt](lists/dating/flirtmoi.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/flirtmoi.txt) |
| Flirtpiraten | 1 | [flirtpiraten.txt](lists/dating/flirtpiraten.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/flirtpiraten.txt) |
| Flirtschiff | 1 | [flirtschiff.txt](lists/dating/flirtschiff.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/flirtschiff.txt) |
| Flirttool | 1 | [flirttool.txt](lists/dating/flirttool.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/flirttool.txt) |
| Foreignbridesru | 1 | [foreignbridesru.txt](lists/dating/foreignbridesru.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/foreignbridesru.txt) |
| Fotochat | 1 | [fotochat.txt](lists/dating/fotochat.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/fotochat.txt) |
| Francekam | 1 | [francekam.txt](lists/dating/francekam.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/francekam.txt) |
| Freegaydatingapps | 1 | [freegaydatingapps.txt](lists/dating/freegaydatingapps.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/freegaydatingapps.txt) |
| Freemeet | 1 | [freemeet.txt](lists/dating/freemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/freemeet.txt) |
| Friendfinder | 1 | [friendfinder.txt](lists/dating/friendfinder.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/friendfinder.txt) |
| Friendscout24 | 2 | [friendscout24.txt](lists/dating/friendscout24.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/friendscout24.txt) |
| Frienifits | 1 | [frienifits.txt](lists/dating/frienifits.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/frienifits.txt) |
| Fruitz | 1 | [fruitz.txt](lists/dating/fruitz.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/fruitz.txt) |
| Frumster | 1 | [frumster.txt](lists/dating/frumster.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/frumster.txt) |
| Funkyfish Dating | 1 | [funkyfish_dating.txt](lists/dating/funkyfish_dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/funkyfish_dating.txt) |
| Funkyfishdating | 1 | [funkyfishdating.txt](lists/dating/funkyfishdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/funkyfishdating.txt) |
| Furfling | 1 | [furfling.txt](lists/dating/furfling.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/furfling.txt) |
| Fusion101 | 1 | [fusion101.txt](lists/dating/fusion101.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/fusion101.txt) |
| Gay Personals | 1 | [gay_personals.txt](lists/dating/gay_personals.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gay_personals.txt) |
| Gaybdsmdate | 2 | [gaybdsmdate.txt](lists/dating/gaybdsmdate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gaybdsmdate.txt) |
| Gaychatr | 1 | [gaychatr.txt](lists/dating/gaychatr.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gaychatr.txt) |
| Gaychristiandating | 1 | [gaychristiandating.txt](lists/dating/gaychristiandating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gaychristiandating.txt) |
| Gaycupid | 1 | [gaycupid.txt](lists/dating/gaycupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gaycupid.txt) |
| Gaydatingbuddies | 1 | [gaydatingbuddies.txt](lists/dating/gaydatingbuddies.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gaydatingbuddies.txt) |
| Gayinterracialdating | 1 | [gayinterracialdating.txt](lists/dating/gayinterracialdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gayinterracialdating.txt) |
| Gaymeetmarket | 1 | [gaymeetmarket.txt](lists/dating/gaymeetmarket.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gaymeetmarket.txt) |
| Gaymenonlinedating | 1 | [gaymenonlinedating.txt](lists/dating/gaymenonlinedating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gaymenonlinedating.txt) |
| Gayonlinedatingsites | 1 | [gayonlinedatingsites.txt](lists/dating/gayonlinedatingsites.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gayonlinedatingsites.txt) |
| Gaysocialnetwork | 1 | [gaysocialnetwork.txt](lists/dating/gaysocialnetwork.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gaysocialnetwork.txt) |
| Gaysugardaddydating | 1 | [gaysugardaddydating.txt](lists/dating/gaysugardaddydating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gaysugardaddydating.txt) |
| Gayukonlinepersonals | 1 | [gayukonlinepersonals.txt](lists/dating/gayukonlinepersonals.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gayukonlinepersonals.txt) |
| Geekmemore | 1 | [geekmemore.txt](lists/dating/geekmemore.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/geekmemore.txt) |
| Genxpeoplemeet | 1 | [genxpeoplemeet.txt](lists/dating/genxpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/genxpeoplemeet.txt) |
| Girlsdateforfree | 1 | [girlsdateforfree.txt](lists/dating/girlsdateforfree.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/girlsdateforfree.txt) |
| Girlsinbloemfontein | 1 | [girlsinbloemfontein.txt](lists/dating/girlsinbloemfontein.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/girlsinbloemfontein.txt) |
| Girlsneedsex | 1 | [girlsneedsex.txt](lists/dating/girlsneedsex.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/girlsneedsex.txt) |
| Gleeden | 1 | [gleeden.txt](lists/dating/gleeden.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gleeden.txt) |
| Globalladies | 1 | [globalladies.txt](lists/dating/globalladies.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/globalladies.txt) |
| Gma | 1 | [gma.txt](lists/dating/gma.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gma.txt) |
| Goflirtaround | 1 | [goflirtaround.txt](lists/dating/goflirtaround.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/goflirtaround.txt) |
| Gomatch | 1 | [gomatch.txt](lists/dating/gomatch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gomatch.txt) |
| Gopromenad | 1 | [gopromenad.txt](lists/dating/gopromenad.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gopromenad.txt) |
| Gorgeous Networks | 1 | [gorgeous_networks.txt](lists/dating/gorgeous_networks.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gorgeous_networks.txt) |
| Gothlover | 1 | [gothlover.txt](lists/dating/gothlover.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gothlover.txt) |
| Gothscene | 1 | [gothscene.txt](lists/dating/gothscene.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gothscene.txt) |
| Gotthem | 1 | [gotthem.txt](lists/dating/gotthem.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gotthem.txt) |
| Granny Date | 1 | [granny_date.txt](lists/dating/granny_date.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/granny_date.txt) |
| Grannydatingclub | 1 | [grannydatingclub.txt](lists/dating/grannydatingclub.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/grannydatingclub.txt) |
| Grannysexfriend | 1 | [grannysexfriend.txt](lists/dating/grannysexfriend.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/grannysexfriend.txt) |
| Gratissexkontakt | 1 | [gratissexkontakt.txt](lists/dating/gratissexkontakt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/gratissexkontakt.txt) |
| Groony | 1 | [groony.txt](lists/dating/groony.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/groony.txt) |
| Guapasmaduras | 1 | [guapasmaduras.txt](lists/dating/guapasmaduras.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/guapasmaduras.txt) |
| Guayu | 1 | [guayu.txt](lists/dating/guayu.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/guayu.txt) |
| Guidedenuit | 1 | [guidedenuit.txt](lists/dating/guidedenuit.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/guidedenuit.txt) |
| HER | 1 | [her.txt](lists/dating/her.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/her.txt) |
| Hallokoko | 1 | [hallokoko.txt](lists/dating/hallokoko.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/hallokoko.txt) |
| Happysingles | 1 | [happysingles.txt](lists/dating/happysingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/happysingles.txt) |
| Harmonylove | 1 | [harmonylove.txt](lists/dating/harmonylove.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/harmonylove.txt) |
| Hasimausi | 1 | [hasimausi.txt](lists/dating/hasimausi.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/hasimausi.txt) |
| Heavenly Match | 1 | [heavenly_match.txt](lists/dating/heavenly_match.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/heavenly_match.txt) |
| Heliumdating | 1 | [heliumdating.txt](lists/dating/heliumdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/heliumdating.txt) |
| Herkert | 1 | [herkert.txt](lists/dating/herkert.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/herkert.txt) |
| Hickeyapp | 1 | [hickeyapp.txt](lists/dating/hickeyapp.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/hickeyapp.txt) |
| Hily | 1 | [hily.txt](lists/dating/hily.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/hily.txt) |
| Hinge | 1 | [hinge.txt](lists/dating/hinge.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/hinge.txt) |
| Hitlovenow | 1 | [hitlovenow.txt](lists/dating/hitlovenow.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/hitlovenow.txt) |
| Hiv Single | 1 | [hiv_single.txt](lists/dating/hiv_single.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/hiv_single.txt) |
| Hivdatingplanet | 1 | [hivdatingplanet.txt](lists/dating/hivdatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/hivdatingplanet.txt) |
| Hommepansement | 1 | [hommepansement.txt](lists/dating/hommepansement.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/hommepansement.txt) |
| Homodate | 1 | [homodate.txt](lists/dating/homodate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/homodate.txt) |
| Hotbuddies | 1 | [hotbuddies.txt](lists/dating/hotbuddies.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/hotbuddies.txt) |
| Hubpeople | 2 | [hubpeople.txt](lists/dating/hubpeople.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/hubpeople.txt) |
| Hubz | 1 | [hubz.txt](lists/dating/hubz.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/hubz.txt) |
| Hushlove | 1 | [hushlove.txt](lists/dating/hushlove.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/hushlove.txt) |
| I Rencontre | 1 | [i_rencontre.txt](lists/dating/i_rencontre.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/i_rencontre.txt) |
| Ichwilldichjetzt | 1 | [ichwilldichjetzt.txt](lists/dating/ichwilldichjetzt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ichwilldichjetzt.txt) |
| Icouple | 1 | [icouple.txt](lists/dating/icouple.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/icouple.txt) |
| Idate | 1 | [idate.txt](lists/dating/idate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/idate.txt) |
| Iktoos | 1 | [iktoos.txt](lists/dating/iktoos.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/iktoos.txt) |
| Ilove | 3 | [ilove.txt](lists/dating/ilove.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ilove.txt) |
| Ilovemessenger | 1 | [ilovemessenger.txt](lists/dating/ilovemessenger.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ilovemessenger.txt) |
| Iltuoamore | 1 | [iltuoamore.txt](lists/dating/iltuoamore.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/iltuoamore.txt) |
| Ima Dating | 1 | [ima_dating.txt](lists/dating/ima_dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ima_dating.txt) |
| Imgix | 1 | [imgix.txt](lists/dating/imgix.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/imgix.txt) |
| Incontramilf | 1 | [incontramilf.txt](lists/dating/incontramilf.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/incontramilf.txt) |
| Incontri | 1 | [incontri.txt](lists/dating/incontri.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/incontri.txt) |
| Incontri Adulti | 1 | [incontri_adulti.txt](lists/dating/incontri_adulti.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/incontri_adulti.txt) |
| Incontricasual | 2 | [incontricasual.txt](lists/dating/incontricasual.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/incontricasual.txt) |
| Incontrilatex | 1 | [incontrilatex.txt](lists/dating/incontrilatex.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/incontrilatex.txt) |
| Incontriromantici | 1 | [incontriromantici.txt](lists/dating/incontriromantici.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/incontriromantici.txt) |
| Incontrisugardaddy | 1 | [incontrisugardaddy.txt](lists/dating/incontrisugardaddy.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/incontrisugardaddy.txt) |
| Incontriveloci | 1 | [incontriveloci.txt](lists/dating/incontriveloci.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/incontriveloci.txt) |
| Incontrixadulti | 1 | [incontrixadulti.txt](lists/dating/incontrixadulti.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/incontrixadulti.txt) |
| Indiadatingplanet | 1 | [indiadatingplanet.txt](lists/dating/indiadatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/indiadatingplanet.txt) |
| Indiamatch | 1 | [indiamatch.txt](lists/dating/indiamatch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/indiamatch.txt) |
| Indian4Love | 1 | [indian4love.txt](lists/dating/indian4love.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/indian4love.txt) |
| Indiandatelink | 1 | [indiandatelink.txt](lists/dating/indiandatelink.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/indiandatelink.txt) |
| Inmyprimedatelink | 1 | [inmyprimedatelink.txt](lists/dating/inmyprimedatelink.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/inmyprimedatelink.txt) |
| Inter Mariage | 1 | [inter_mariage.txt](lists/dating/inter_mariage.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/inter_mariage.txt) |
| Internationalcupid | 1 | [internationalcupid.txt](lists/dating/internationalcupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/internationalcupid.txt) |
| Internationaldatingplanet | 1 | [internationaldatingplanet.txt](lists/dating/internationaldatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/internationaldatingplanet.txt) |
| Interracialcougardating | 1 | [interracialcougardating.txt](lists/dating/interracialcougardating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/interracialcougardating.txt) |
| Interracialcupid | 1 | [interracialcupid.txt](lists/dating/interracialcupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/interracialcupid.txt) |
| Interracialdating | 1 | [interracialdating.txt](lists/dating/interracialdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/interracialdating.txt) |
| Interracialdatingcentral | 1 | [interracialdatingcentral.txt](lists/dating/interracialdatingcentral.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/interracialdatingcentral.txt) |
| Interracialgaydating | 1 | [interracialgaydating.txt](lists/dating/interracialgaydating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/interracialgaydating.txt) |
| Interracialism | 1 | [interracialism.txt](lists/dating/interracialism.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/interracialism.txt) |
| Interracialmatcher | 1 | [interracialmatcher.txt](lists/dating/interracialmatcher.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/interracialmatcher.txt) |
| Italianpeoplemeet | 1 | [italianpeoplemeet.txt](lists/dating/italianpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/italianpeoplemeet.txt) |
| Itocd | 1 | [itocd.txt](lists/dating/itocd.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/itocd.txt) |
| Iwantu | 1 | [iwantu.txt](lists/dating/iwantu.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/iwantu.txt) |
| Japancupid | 1 | [japancupid.txt](lists/dating/japancupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/japancupid.txt) |
| Japandatingsite | 1 | [japandatingsite.txt](lists/dating/japandatingsite.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/japandatingsite.txt) |
| Jasez | 1 | [jasez.txt](lists/dating/jasez.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jasez.txt) |
| Jaumo | 1 | [jaumo.txt](lists/dating/jaumo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jaumo.txt) |
| Jazzfmdating | 1 | [jazzfmdating.txt](lists/dating/jazzfmdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jazzfmdating.txt) |
| Jdate | 1 | [jdate.txt](lists/dating/jdate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jdate.txt) |
| Jecontacte | 1 | [jecontacte.txt](lists/dating/jecontacte.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jecontacte.txt) |
| Jetztflirten | 2 | [jetztflirten.txt](lists/dating/jetztflirten.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jetztflirten.txt) |
| Jewishcafe | 1 | [jewishcafe.txt](lists/dating/jewishcafe.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jewishcafe.txt) |
| Jewishdating247 | 1 | [jewishdating247.txt](lists/dating/jewishdating247.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jewishdating247.txt) |
| Jewishfriendfinder | 1 | [jewishfriendfinder.txt](lists/dating/jewishfriendfinder.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jewishfriendfinder.txt) |
| Jewishfriends | 1 | [jewishfriends.txt](lists/dating/jewishfriends.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jewishfriends.txt) |
| Jpeoplemeet | 1 | [jpeoplemeet.txt](lists/dating/jpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jpeoplemeet.txt) |
| Jsingles | 1 | [jsingles.txt](lists/dating/jsingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jsingles.txt) |
| Jsoulmate | 1 | [jsoulmate.txt](lists/dating/jsoulmate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jsoulmate.txt) |
| Jswsn | 1 | [jswsn.txt](lists/dating/jswsn.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jswsn.txt) |
| Jubilant | 1 | [jubilant.txt](lists/dating/jubilant.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jubilant.txt) |
| Juicy | 1 | [juicy.txt](lists/dating/juicy.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/juicy.txt) |
| Jumpdates | 1 | [jumpdates.txt](lists/dating/jumpdates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jumpdates.txt) |
| Juniques | 1 | [juniques.txt](lists/dating/juniques.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/juniques.txt) |
| Just Single Parents | 1 | [just_single_parents.txt](lists/dating/just_single_parents.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/just_single_parents.txt) |
| Just2Match | 1 | [just2match.txt](lists/dating/just2match.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/just2match.txt) |
| Justbewild | 1 | [justbewild.txt](lists/dating/justbewild.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/justbewild.txt) |
| Justcamming | 1 | [justcamming.txt](lists/dating/justcamming.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/justcamming.txt) |
| Jwed | 1 | [jwed.txt](lists/dating/jwed.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/jwed.txt) |
| K9 | 1 | [k9.txt](lists/dating/k9.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/k9.txt) |
| Kansas Singles | 1 | [kansas_singles.txt](lists/dating/kansas_singles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/kansas_singles.txt) |
| Kelrencontre | 1 | [kelrencontre.txt](lists/dating/kelrencontre.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/kelrencontre.txt) |
| Komonskliek | 1 | [komonskliek.txt](lists/dating/komonskliek.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/komonskliek.txt) |
| Koreancupid | 1 | [koreancupid.txt](lists/dating/koreancupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/koreancupid.txt) |
| Kroow | 1 | [kroow.txt](lists/dating/kroow.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/kroow.txt) |
| Kuumatpaikat | 1 | [kuumatpaikat.txt](lists/dating/kuumatpaikat.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/kuumatpaikat.txt) |
| Laisvas | 1 | [laisvas.txt](lists/dating/laisvas.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/laisvas.txt) |
| Latamdate | 1 | [latamdate.txt](lists/dating/latamdate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/latamdate.txt) |
| Latinamericancupid | 1 | [latinamericancupid.txt](lists/dating/latinamericancupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/latinamericancupid.txt) |
| Latinlove | 1 | [latinlove.txt](lists/dating/latinlove.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/latinlove.txt) |
| Latinopeoplemeet | 1 | [latinopeoplemeet.txt](lists/dating/latinopeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/latinopeoplemeet.txt) |
| Latinoswingers | 1 | [latinoswingers.txt](lists/dating/latinoswingers.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/latinoswingers.txt) |
| Latinwomenonline | 1 | [latinwomenonline.txt](lists/dating/latinwomenonline.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/latinwomenonline.txt) |
| Lavalife | 1 | [lavalife.txt](lists/dating/lavalife.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lavalife.txt) |
| Lavaplace | 1 | [lavaplace.txt](lists/dating/lavaplace.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lavaplace.txt) |
| Lavenderslove | 1 | [lavenderslove.txt](lists/dating/lavenderslove.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lavenderslove.txt) |
| Ldsplanet | 1 | [ldsplanet.txt](lists/dating/ldsplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ldsplanet.txt) |
| Leboncoup | 1 | [leboncoup.txt](lists/dating/leboncoup.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/leboncoup.txt) |
| Lekdate | 1 | [lekdate.txt](lists/dating/lekdate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lekdate.txt) |
| Lesbian | 1 | [lesbian.txt](lists/dating/lesbian.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lesbian.txt) |
| Lesbianasenmexico | 1 | [lesbianasenmexico.txt](lists/dating/lesbianasenmexico.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lesbianasenmexico.txt) |
| Lesbianchatonline | 1 | [lesbianchatonline.txt](lists/dating/lesbianchatonline.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lesbianchatonline.txt) |
| Lesbianmatchmaker | 1 | [lesbianmatchmaker.txt](lists/dating/lesbianmatchmaker.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lesbianmatchmaker.txt) |
| Lesbians In America | 1 | [lesbians_in_america.txt](lists/dating/lesbians_in_america.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lesbians_in_america.txt) |
| Lesbians In Canada | 1 | [lesbians_in_canada.txt](lists/dating/lesbians_in_canada.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lesbians_in_canada.txt) |
| Lesbidating | 1 | [lesbidating.txt](lists/dating/lesbidating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lesbidating.txt) |
| Lesbiemates | 1 | [lesbiemates.txt](lists/dating/lesbiemates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lesbiemates.txt) |
| Lesbiskdating | 1 | [lesbiskdating.txt](lists/dating/lesbiskdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lesbiskdating.txt) |
| Letsbond | 1 | [letsbond.txt](lists/dating/letsbond.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/letsbond.txt) |
| Letsmeet | 2 | [letsmeet.txt](lists/dating/letsmeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/letsmeet.txt) |
| Letsmeetup | 1 | [letsmeetup.txt](lists/dating/letsmeetup.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/letsmeetup.txt) |
| Lexa | 1 | [lexa.txt](lists/dating/lexa.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lexa.txt) |
| Lgbt Dating | 1 | [lgbt_dating.txt](lists/dating/lgbt_dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lgbt_dating.txt) |
| Libimseti | 1 | [libimseti.txt](lists/dating/libimseti.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/libimseti.txt) |
| Lilaherzen | 1 | [lilaherzen.txt](lists/dating/lilaherzen.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lilaherzen.txt) |
| Lipsticklesbians | 1 | [lipsticklesbians.txt](lists/dating/lipsticklesbians.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lipsticklesbians.txt) |
| Localgilfs | 1 | [localgilfs.txt](lists/dating/localgilfs.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/localgilfs.txt) |
| Localhottiesnow | 1 | [localhottiesnow.txt](lists/dating/localhottiesnow.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/localhottiesnow.txt) |
| Localmaturedating | 1 | [localmaturedating.txt](lists/dating/localmaturedating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/localmaturedating.txt) |
| Localmeets | 1 | [localmeets.txt](lists/dating/localmeets.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/localmeets.txt) |
| Lonelyparentsdate | 1 | [lonelyparentsdate.txt](lists/dating/lonelyparentsdate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lonelyparentsdate.txt) |
| Lonelywivesdatelink | 1 | [lonelywivesdatelink.txt](lists/dating/lonelywivesdatelink.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lonelywivesdatelink.txt) |
| Loopylove | 1 | [loopylove.txt](lists/dating/loopylove.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/loopylove.txt) |
| Loquovipgay | 1 | [loquovipgay.txt](lists/dating/loquovipgay.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/loquovipgay.txt) |
| Lottoie | 1 | [lottoie.txt](lists/dating/lottoie.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lottoie.txt) |
| Lovagency | 1 | [lovagency.txt](lists/dating/lovagency.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lovagency.txt) |
| Love | 1 | [love.txt](lists/dating/love.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/love.txt) |
| Love You2 | 1 | [love_you2.txt](lists/dating/love_you2.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/love_you2.txt) |
| Love2Knowu | 1 | [love2knowu.txt](lists/dating/love2knowu.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/love2knowu.txt) |
| Loveandfriends | 2 | [loveandfriends.txt](lists/dating/loveandfriends.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/loveandfriends.txt) |
| Loveandseek | 3 | [loveandseek.txt](lists/dating/loveandseek.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/loveandseek.txt) |
| Lovearts | 1 | [lovearts.txt](lists/dating/lovearts.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lovearts.txt) |
| Loveawake | 1 | [loveawake.txt](lists/dating/loveawake.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/loveawake.txt) |
| Lovedating | 1 | [lovedating.txt](lists/dating/lovedating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lovedating.txt) |
| Loveismatch | 1 | [loveismatch.txt](lists/dating/loveismatch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/loveismatch.txt) |
| Lovelife | 1 | [lovelife.txt](lists/dating/lovelife.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lovelife.txt) |
| Lovely | 1 | [lovely.txt](lists/dating/lovely.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lovely.txt) |
| Lovemage | 1 | [lovemage.txt](lists/dating/lovemage.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lovemage.txt) |
| Loveme | 1 | [loveme.txt](lists/dating/loveme.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/loveme.txt) |
| Loveplanet | 1 | [loveplanet.txt](lists/dating/loveplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/loveplanet.txt) |
| Lover2Cu | 1 | [lover2cu.txt](lists/dating/lover2cu.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lover2cu.txt) |
| Lovespiritually | 1 | [lovespiritually.txt](lists/dating/lovespiritually.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lovespiritually.txt) |
| Lovestruck | 1 | [lovestruck.txt](lists/dating/lovestruck.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lovestruck.txt) |
| Lovetest | 1 | [lovetest.txt](lists/dating/lovetest.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lovetest.txt) |
| Lovez | 1 | [lovez.txt](lists/dating/lovez.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lovez.txt) |
| Lovinga | 1 | [lovinga.txt](lists/dating/lovinga.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lovinga.txt) |
| Lovoo | 1 | [lovoo.txt](lists/dating/lovoo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lovoo.txt) |
| Lulusloveshack | 1 | [lulusloveshack.txt](lists/dating/lulusloveshack.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lulusloveshack.txt) |
| Lusomeet | 2 | [lusomeet.txt](lists/dating/lusomeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lusomeet.txt) |
| Lustvolleflirts | 1 | [lustvolleflirts.txt](lists/dating/lustvolleflirts.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lustvolleflirts.txt) |
| Lyad | 1 | [lyad.txt](lists/dating/lyad.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/lyad.txt) |
| Maatje | 1 | [maatje.txt](lists/dating/maatje.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/maatje.txt) |
| Madacherie | 1 | [madacherie.txt](lists/dating/madacherie.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/madacherie.txt) |
| Makelove | 1 | [makelove.txt](lists/dating/makelove.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/makelove.txt) |
| Manwoman | 1 | [manwoman.txt](lists/dating/manwoman.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/manwoman.txt) |
| Mariadating | 1 | [mariadating.txt](lists/dating/mariadating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mariadating.txt) |
| Marihuanadating | 1 | [marihuanadating.txt](lists/dating/marihuanadating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/marihuanadating.txt) |
| Marriagemindedpeoplemeet | 1 | [marriagemindedpeoplemeet.txt](lists/dating/marriagemindedpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/marriagemindedpeoplemeet.txt) |
| Marriageservices | 1 | [marriageservices.txt](lists/dating/marriageservices.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/marriageservices.txt) |
| Marryy | 1 | [marryy.txt](lists/dating/marryy.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/marryy.txt) |
| Masochiste | 1 | [masochiste.txt](lists/dating/masochiste.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/masochiste.txt) |
| Match | 1 | [match.txt](lists/dating/match.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/match.txt) |
| Match Usa | 1 | [match_usa.txt](lists/dating/match_usa.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/match_usa.txt) |
| Match21 | 1 | [match21.txt](lists/dating/match21.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/match21.txt) |
| Matchmaker | 1 | [matchmaker.txt](lists/dating/matchmaker.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/matchmaker.txt) |
| Matchmet | 1 | [matchmet.txt](lists/dating/matchmet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/matchmet.txt) |
| Matrymonia | 1 | [matrymonia.txt](lists/dating/matrymonia.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/matrymonia.txt) |
| Mature | 1 | [mature.txt](lists/dating/mature.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mature.txt) |
| Maturebi | 1 | [maturebi.txt](lists/dating/maturebi.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/maturebi.txt) |
| Maturedating | 1 | [maturedating.txt](lists/dating/maturedating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/maturedating.txt) |
| Maturelovedates | 1 | [maturelovedates.txt](lists/dating/maturelovedates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/maturelovedates.txt) |
| Maturerelationship | 1 | [maturerelationship.txt](lists/dating/maturerelationship.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/maturerelationship.txt) |
| Maturesdating | 1 | [maturesdating.txt](lists/dating/maturesdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/maturesdating.txt) |
| Maxi Offerte | 1 | [maxi_offerte.txt](lists/dating/maxi_offerte.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/maxi_offerte.txt) |
| Mazaltov | 1 | [mazaltov.txt](lists/dating/mazaltov.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mazaltov.txt) |
| Mecacroquer | 1 | [mecacroquer.txt](lists/dating/mecacroquer.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mecacroquer.txt) |
| Meet Dating | 1 | [meet_dating.txt](lists/dating/meet_dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/meet_dating.txt) |
| Meeta Img | 1 | [meeta_img.txt](lists/dating/meeta_img.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/meeta_img.txt) |
| Meetarabic | 1 | [meetarabic.txt](lists/dating/meetarabic.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/meetarabic.txt) |
| Meetasiangirls | 1 | [meetasiangirls.txt](lists/dating/meetasiangirls.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/meetasiangirls.txt) |
| Meetattheairport | 1 | [meetattheairport.txt](lists/dating/meetattheairport.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/meetattheairport.txt) |
| Meetcupid | 1 | [meetcupid.txt](lists/dating/meetcupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/meetcupid.txt) |
| Meetic | 5 | [meetic.txt](lists/dating/meetic.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/meetic.txt) |
| Meeticaffinity | 1 | [meeticaffinity.txt](lists/dating/meeticaffinity.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/meeticaffinity.txt) |
| Meetlocalbisexuals | 1 | [meetlocalbisexuals.txt](lists/dating/meetlocalbisexuals.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/meetlocalbisexuals.txt) |
| Meetlocals | 1 | [meetlocals.txt](lists/dating/meetlocals.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/meetlocals.txt) |
| Meetme | 1 | [meetme.txt](lists/dating/meetme.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/meetme.txt) |
| Meetrussianbrides | 1 | [meetrussianbrides.txt](lists/dating/meetrussianbrides.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/meetrussianbrides.txt) |
| Meettattooedsingles | 1 | [meettattooedsingles.txt](lists/dating/meettattooedsingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/meettattooedsingles.txt) |
| Meetwife | 1 | [meetwife.txt](lists/dating/meetwife.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/meetwife.txt) |
| Megaflirt | 1 | [megaflirt.txt](lists/dating/megaflirt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/megaflirt.txt) |
| Megafriends | 1 | [megafriends.txt](lists/dating/megafriends.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/megafriends.txt) |
| Mejoramor | 1 | [mejoramor.txt](lists/dating/mejoramor.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mejoramor.txt) |
| Mektoube | 1 | [mektoube.txt](lists/dating/mektoube.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mektoube.txt) |
| Melindaspenpals | 1 | [melindaspenpals.txt](lists/dating/melindaspenpals.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/melindaspenpals.txt) |
| Meninlove | 1 | [meninlove.txt](lists/dating/meninlove.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/meninlove.txt) |
| Mennation | 1 | [mennation.txt](lists/dating/mennation.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mennation.txt) |
| Menwedding | 1 | [menwedding.txt](lists/dating/menwedding.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/menwedding.txt) |
| Mexflirt | 1 | [mexflirt.txt](lists/dating/mexflirt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mexflirt.txt) |
| Mexicancupid | 1 | [mexicancupid.txt](lists/dating/mexicancupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mexicancupid.txt) |
| Midsummerseve | 1 | [midsummerseve.txt](lists/dating/midsummerseve.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/midsummerseve.txt) |
| Mignons | 1 | [mignons.txt](lists/dating/mignons.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mignons.txt) |
| Milalol | 1 | [milalol.txt](lists/dating/milalol.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/milalol.txt) |
| Milfdatelink | 1 | [milfdatelink.txt](lists/dating/milfdatelink.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/milfdatelink.txt) |
| Millionairedatingplanet | 1 | [millionairedatingplanet.txt](lists/dating/millionairedatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/millionairedatingplanet.txt) |
| Minaflirts | 1 | [minaflirts.txt](lists/dating/minaflirts.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/minaflirts.txt) |
| Mingle2 | 1 | [mingle2.txt](lists/dating/mingle2.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mingle2.txt) |
| Minglematey | 1 | [minglematey.txt](lists/dating/minglematey.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/minglematey.txt) |
| Miss34 | 1 | [miss34.txt](lists/dating/miss34.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/miss34.txt) |
| Mixeddating | 1 | [mixeddating.txt](lists/dating/mixeddating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mixeddating.txt) |
| Mon Bled | 1 | [mon_bled.txt](lists/dating/mon_bled.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mon_bled.txt) |
| Monsecretsexy | 1 | [monsecretsexy.txt](lists/dating/monsecretsexy.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/monsecretsexy.txt) |
| Mtch | 1 | [mtch.txt](lists/dating/mtch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mtch.txt) |
| Muslimdatingplanet | 1 | [muslimdatingplanet.txt](lists/dating/muslimdatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/muslimdatingplanet.txt) |
| My Casual Date | 1 | [my_casual_date.txt](lists/dating/my_casual_date.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/my_casual_date.txt) |
| Mydate | 1 | [mydate.txt](lists/dating/mydate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mydate.txt) |
| Mydates | 1 | [mydates.txt](lists/dating/mydates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mydates.txt) |
| Myfunkyfish | 1 | [myfunkyfish.txt](lists/dating/myfunkyfish.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/myfunkyfish.txt) |
| Myladyboydate | 1 | [myladyboydate.txt](lists/dating/myladyboydate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/myladyboydate.txt) |
| Mylove | 1 | [mylove.txt](lists/dating/mylove.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mylove.txt) |
| Mynaughtyfriend | 1 | [mynaughtyfriend.txt](lists/dating/mynaughtyfriend.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mynaughtyfriend.txt) |
| Mysinglefriend | 1 | [mysinglefriend.txt](lists/dating/mysinglefriend.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mysinglefriend.txt) |
| Mytransgenderdate | 1 | [mytransgenderdate.txt](lists/dating/mytransgenderdate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/mytransgenderdate.txt) |
| Myvegetariandating | 1 | [myvegetariandating.txt](lists/dating/myvegetariandating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/myvegetariandating.txt) |
| Neckdate | 1 | [neckdate.txt](lists/dating/neckdate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/neckdate.txt) |
| Neiubim | 1 | [neiubim.txt](lists/dating/neiubim.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/neiubim.txt) |
| Nevermarrieddating | 1 | [nevermarrieddating.txt](lists/dating/nevermarrieddating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/nevermarrieddating.txt) |
| New Dating | 1 | [new_dating.txt](lists/dating/new_dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/new_dating.txt) |
| Newmeet | 1 | [newmeet.txt](lists/dating/newmeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/newmeet.txt) |
| Nipagonicobro | 1 | [nipagonicobro.txt](lists/dating/nipagonicobro.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/nipagonicobro.txt) |
| Noah | 1 | [noah.txt](lists/dating/noah.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/noah.txt) |
| Norrlandskontakten | 1 | [norrlandskontakten.txt](lists/dating/norrlandskontakten.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/norrlandskontakten.txt) |
| Nostringsattached | 1 | [nostringsattached.txt](lists/dating/nostringsattached.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/nostringsattached.txt) |
| Nudistonlinedating | 1 | [nudistonlinedating.txt](lists/dating/nudistonlinedating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/nudistonlinedating.txt) |
| Nylonwomendating | 1 | [nylonwomendating.txt](lists/dating/nylonwomendating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/nylonwomendating.txt) |
| Odessalove | 1 | [odessalove.txt](lists/dating/odessalove.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/odessalove.txt) |
| Oertlicheflirtmatches | 1 | [oertlicheflirtmatches.txt](lists/dating/oertlicheflirtmatches.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/oertlicheflirtmatches.txt) |
| Oesterreichhotchat | 1 | [oesterreichhotchat.txt](lists/dating/oesterreichhotchat.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/oesterreichhotchat.txt) |
| Oho | 1 | [oho.txt](lists/dating/oho.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/oho.txt) |
| OkCupid | 2 | [okcupid.txt](lists/dating/okcupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/okcupid.txt) |
| Oklute | 1 | [oklute.txt](lists/dating/oklute.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/oklute.txt) |
| Oknotify2 | 1 | [oknotify2.txt](lists/dating/oknotify2.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/oknotify2.txt) |
| Onadate | 1 | [onadate.txt](lists/dating/onadate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/onadate.txt) |
| Onebbw | 1 | [onebbw.txt](lists/dating/onebbw.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/onebbw.txt) |
| Onedate | 1 | [onedate.txt](lists/dating/onedate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/onedate.txt) |
| Onelovespot | 1 | [onelovespot.txt](lists/dating/onelovespot.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/onelovespot.txt) |
| Onenight Stand | 1 | [onenight_stand.txt](lists/dating/onenight_stand.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/onenight_stand.txt) |
| Onenightfriend | 1 | [onenightfriend.txt](lists/dating/onenightfriend.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/onenightfriend.txt) |
| Onenightonly | 1 | [onenightonly.txt](lists/dating/onenightonly.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/onenightonly.txt) |
| Onewife | 1 | [onewife.txt](lists/dating/onewife.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/onewife.txt) |
| Online Dating | 1 | [online_dating.txt](lists/dating/online_dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/online_dating.txt) |
| Onlinedating | 1 | [onlinedating.txt](lists/dating/onlinedating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/onlinedating.txt) |
| Onlinedatingpost | 1 | [onlinedatingpost.txt](lists/dating/onlinedatingpost.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/onlinedatingpost.txt) |
| Onlinedejt | 1 | [onlinedejt.txt](lists/dating/onlinedejt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/onlinedejt.txt) |
| Onlineforlove | 1 | [onlineforlove.txt](lists/dating/onlineforlove.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/onlineforlove.txt) |
| Onlysingleparents | 1 | [onlysingleparents.txt](lists/dating/onlysingleparents.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/onlysingleparents.txt) |
| Openrelationship | 1 | [openrelationship.txt](lists/dating/openrelationship.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/openrelationship.txt) |
| Originaldating | 1 | [originaldating.txt](lists/dating/originaldating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/originaldating.txt) |
| Ouf2Toi | 1 | [ouf2toi.txt](lists/dating/ouf2toi.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ouf2toi.txt) |
| Oulfa | 1 | [oulfa.txt](lists/dating/oulfa.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/oulfa.txt) |
| Ourtime | 1 | [ourtime.txt](lists/dating/ourtime.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ourtime.txt) |
| Over40Sdating | 1 | [over40sdating.txt](lists/dating/over40sdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/over40sdating.txt) |
| Over50Datingnorge | 1 | [over50datingnorge.txt](lists/dating/over50datingnorge.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/over50datingnorge.txt) |
| Over50Sdating | 1 | [over50sdating.txt](lists/dating/over50sdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/over50sdating.txt) |
| Over50Singlesmeet | 1 | [over50singlesmeet.txt](lists/dating/over50singlesmeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/over50singlesmeet.txt) |
| Parisvideochat | 1 | [parisvideochat.txt](lists/dating/parisvideochat.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/parisvideochat.txt) |
| Parom | 1 | [parom.txt](lists/dating/parom.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/parom.txt) |
| Parship | 3 | [parship.txt](lists/dating/parship.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/parship.txt) |
| Partner Services | 1 | [partner_services.txt](lists/dating/partner_services.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/partner_services.txt) |
| Partner24Online | 1 | [partner24online.txt](lists/dating/partner24online.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/partner24online.txt) |
| Passion | 1 | [passion.txt](lists/dating/passion.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/passion.txt) |
| Patakadates | 1 | [patakadates.txt](lists/dating/patakadates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/patakadates.txt) |
| Patchwork Paar | 1 | [patchwork_paar.txt](lists/dating/patchwork_paar.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/patchwork_paar.txt) |
| Peekabooheart | 1 | [peekabooheart.txt](lists/dating/peekabooheart.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/peekabooheart.txt) |
| Pegging | 2 | [pegging.txt](lists/dating/pegging.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/pegging.txt) |
| Peggingdates | 1 | [peggingdates.txt](lists/dating/peggingdates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/peggingdates.txt) |
| Pegginglovers | 1 | [pegginglovers.txt](lists/dating/pegginglovers.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/pegginglovers.txt) |
| Peoplemedia | 1 | [peoplemedia.txt](lists/dating/peoplemedia.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/peoplemedia.txt) |
| Peoplemeet | 1 | [peoplemeet.txt](lists/dating/peoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/peoplemeet.txt) |
| Perfect10Dating | 1 | [perfect10dating.txt](lists/dating/perfect10dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/perfect10dating.txt) |
| Perfectdates | 1 | [perfectdates.txt](lists/dating/perfectdates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/perfectdates.txt) |
| Perfectmatch | 1 | [perfectmatch.txt](lists/dating/perfectmatch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/perfectmatch.txt) |
| Petdatingplanet | 1 | [petdatingplanet.txt](lists/dating/petdatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/petdatingplanet.txt) |
| Petloversdatelink | 1 | [petloversdatelink.txt](lists/dating/petloversdatelink.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/petloversdatelink.txt) |
| Petpeoplemeet | 1 | [petpeoplemeet.txt](lists/dating/petpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/petpeoplemeet.txt) |
| Planetrockdating | 1 | [planetrockdating.txt](lists/dating/planetrockdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/planetrockdating.txt) |
| Plenty of Fish | 1 | [plenty_of_fish.txt](lists/dating/plenty_of_fish.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/plenty_of_fish.txt) |
| Polishdating | 1 | [polishdating.txt](lists/dating/polishdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/polishdating.txt) |
| Polovinka | 1 | [polovinka.txt](lists/dating/polovinka.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/polovinka.txt) |
| Polyamorosos | 1 | [polyamorosos.txt](lists/dating/polyamorosos.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/polyamorosos.txt) |
| Polyamorsenior | 2 | [polyamorsenior.txt](lists/dating/polyamorsenior.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/polyamorsenior.txt) |
| Pop6 | 1 | [pop6.txt](lists/dating/pop6.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/pop6.txt) |
| Portugays | 1 | [portugays.txt](lists/dating/portugays.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/portugays.txt) |
| Posdating | 1 | [posdating.txt](lists/dating/posdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/posdating.txt) |
| Positivesingles | 1 | [positivesingles.txt](lists/dating/positivesingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/positivesingles.txt) |
| Pre Dating | 1 | [pre_dating.txt](lists/dating/pre_dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/pre_dating.txt) |
| Privet | 1 | [privet.txt](lists/dating/privet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/privet.txt) |
| Proximeety | 2 | [proximeety.txt](lists/dating/proximeety.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/proximeety.txt) |
| Pure App | 1 | [pure_app.txt](lists/dating/pure_app.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/pure_app.txt) |
| Q2W | 1 | [q2w.txt](lists/dating/q2w.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/q2w.txt) |
| Quality Singles | 1 | [quality_singles.txt](lists/dating/quality_singles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/quality_singles.txt) |
| Questchat | 1 | [questchat.txt](lists/dating/questchat.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/questchat.txt) |
| RDV | 96 | [rdv.txt](lists/dating/rdv.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rdv.txt) |
| Radar Rencontres | 1 | [radar_rencontres.txt](lists/dating/radar_rencontres.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/radar_rencontres.txt) |
| Rande | 2 | [rande.txt](lists/dating/rande.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rande.txt) |
| Raw | 1 | [raw.txt](lists/dating/raw.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/raw.txt) |
| Rbrides | 1 | [rbrides.txt](lists/dating/rbrides.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rbrides.txt) |
| Rdvadultere | 1 | [rdvadultere.txt](lists/dating/rdvadultere.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rdvadultere.txt) |
| Realpeopledating | 1 | [realpeopledating.txt](lists/dating/realpeopledating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/realpeopledating.txt) |
| Register | 1 | [register.txt](lists/dating/register.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/register.txt) |
| Reifefrauen | 1 | [reifefrauen.txt](lists/dating/reifefrauen.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/reifefrauen.txt) |
| Relaxiones | 1 | [relaxiones.txt](lists/dating/relaxiones.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/relaxiones.txt) |
| Rencontre Agriculteur | 1 | [rencontre_agriculteur.txt](lists/dating/rencontre_agriculteur.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontre_agriculteur.txt) |
| Rencontre Bordeaux | 1 | [rencontre_bordeaux.txt](lists/dating/rencontre_bordeaux.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontre_bordeaux.txt) |
| Rencontre Gratuite | 1 | [rencontre_gratuite.txt](lists/dating/rencontre_gratuite.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontre_gratuite.txt) |
| Rencontre Homo | 1 | [rencontre_homo.txt](lists/dating/rencontre_homo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontre_homo.txt) |
| Rencontre Lille | 1 | [rencontre_lille.txt](lists/dating/rencontre_lille.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontre_lille.txt) |
| Rencontre Lyon | 1 | [rencontre_lyon.txt](lists/dating/rencontre_lyon.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontre_lyon.txt) |
| Rencontre Marseille | 1 | [rencontre_marseille.txt](lists/dating/rencontre_marseille.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontre_marseille.txt) |
| Rencontre Nice | 1 | [rencontre_nice.txt](lists/dating/rencontre_nice.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontre_nice.txt) |
| Rencontre Nimes | 1 | [rencontre_nimes.txt](lists/dating/rencontre_nimes.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontre_nimes.txt) |
| Rencontre Strasbourg | 1 | [rencontre_strasbourg.txt](lists/dating/rencontre_strasbourg.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontre_strasbourg.txt) |
| Rencontre Toulon | 1 | [rencontre_toulon.txt](lists/dating/rencontre_toulon.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontre_toulon.txt) |
| Rencontrea | 1 | [rencontrea.txt](lists/dating/rencontrea.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontrea.txt) |
| Rencontreamoureuse | 1 | [rencontreamoureuse.txt](lists/dating/rencontreamoureuse.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontreamoureuse.txt) |
| Rencontreasiatique | 1 | [rencontreasiatique.txt](lists/dating/rencontreasiatique.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontreasiatique.txt) |
| Rencontrecavalier | 1 | [rencontrecavalier.txt](lists/dating/rencontrecavalier.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontrecavalier.txt) |
| Rencontrechretien | 1 | [rencontrechretien.txt](lists/dating/rencontrechretien.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontrechretien.txt) |
| Rencontrecoquine | 1 | [rencontrecoquine.txt](lists/dating/rencontrecoquine.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontrecoquine.txt) |
| Rencontrecougar | 1 | [rencontrecougar.txt](lists/dating/rencontrecougar.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontrecougar.txt) |
| Rencontregatineau | 1 | [rencontregatineau.txt](lists/dating/rencontregatineau.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontregatineau.txt) |
| Rencontregay | 1 | [rencontregay.txt](lists/dating/rencontregay.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontregay.txt) |
| Rencontrelibertine | 1 | [rencontrelibertine.txt](lists/dating/rencontrelibertine.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontrelibertine.txt) |
| Rencontremalentendant | 1 | [rencontremalentendant.txt](lists/dating/rencontremalentendant.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontremalentendant.txt) |
| Rencontremariage | 1 | [rencontremariage.txt](lists/dating/rencontremariage.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontremariage.txt) |
| Rencontrepiercing | 1 | [rencontrepiercing.txt](lists/dating/rencontrepiercing.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontrepiercing.txt) |
| Rencontres Coquines | 1 | [rencontres_coquines.txt](lists/dating/rencontres_coquines.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontres_coquines.txt) |
| Rencontres Discretes | 1 | [rencontres_discretes.txt](lists/dating/rencontres_discretes.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontres_discretes.txt) |
| Rencontres Echangistes | 1 | [rencontres_echangistes.txt](lists/dating/rencontres_echangistes.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontres_echangistes.txt) |
| Rencontres Nantes | 1 | [rencontres_nantes.txt](lists/dating/rencontres_nantes.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontres_nantes.txt) |
| Rencontres Rondes | 1 | [rencontres_rondes.txt](lists/dating/rencontres_rondes.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontres_rondes.txt) |
| Rencontres Toulouse | 1 | [rencontres_toulouse.txt](lists/dating/rencontres_toulouse.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontres_toulouse.txt) |
| Rencontresecrete | 1 | [rencontresecrete.txt](lists/dating/rencontresecrete.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontresecrete.txt) |
| Rencontreseniors | 1 | [rencontreseniors.txt](lists/dating/rencontreseniors.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontreseniors.txt) |
| Rencontresherbrooke | 1 | [rencontresherbrooke.txt](lists/dating/rencontresherbrooke.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontresherbrooke.txt) |
| Rencontresmariees | 1 | [rencontresmariees.txt](lists/dating/rencontresmariees.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontresmariees.txt) |
| Rencontresrondes | 1 | [rencontresrondes.txt](lists/dating/rencontresrondes.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rencontresrondes.txt) |
| Republicanpeoplemeet | 1 | [republicanpeoplemeet.txt](lists/dating/republicanpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/republicanpeoplemeet.txt) |
| Reseaucontact | 1 | [reseaucontact.txt](lists/dating/reseaucontact.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/reseaucontact.txt) |
| Retrouve Moi | 1 | [retrouve_moi.txt](lists/dating/retrouve_moi.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/retrouve_moi.txt) |
| Review | 1 | [review.txt](lists/dating/review.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/review.txt) |
| Roastdating | 1 | [roastdating.txt](lists/dating/roastdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/roastdating.txt) |
| Rollosfaciles | 1 | [rollosfaciles.txt](lists/dating/rollosfaciles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rollosfaciles.txt) |
| Romancedubai | 1 | [romancedubai.txt](lists/dating/romancedubai.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/romancedubai.txt) |
| Romancium | 1 | [romancium.txt](lists/dating/romancium.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/romancium.txt) |
| Romanticrelay | 1 | [romanticrelay.txt](lists/dating/romanticrelay.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/romanticrelay.txt) |
| Ropebondagemeetups | 1 | [ropebondagemeetups.txt](lists/dating/ropebondagemeetups.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ropebondagemeetups.txt) |
| Rsvp | 1 | [rsvp.txt](lists/dating/rsvp.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/rsvp.txt) |
| Ru Brides | 1 | [ru_brides.txt](lists/dating/ru_brides.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ru_brides.txt) |
| Ruralsingles | 1 | [ruralsingles.txt](lists/dating/ruralsingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ruralsingles.txt) |
| Russ Love | 1 | [russ_love.txt](lists/dating/russ_love.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/russ_love.txt) |
| Russian Dating | 1 | [russian_dating.txt](lists/dating/russian_dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/russian_dating.txt) |
| Russian Enigma | 1 | [russian_enigma.txt](lists/dating/russian_enigma.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/russian_enigma.txt) |
| Russiandatingplanet | 1 | [russiandatingplanet.txt](lists/dating/russiandatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/russiandatingplanet.txt) |
| Russischefrauen | 1 | [russischefrauen.txt](lists/dating/russischefrauen.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/russischefrauen.txt) |
| Sareuniteddating | 1 | [sareuniteddating.txt](lists/dating/sareuniteddating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sareuniteddating.txt) |
| Saucydates | 1 | [saucydates.txt](lists/dating/saucydates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/saucydates.txt) |
| Scambiocoppie | 1 | [scambiocoppie.txt](lists/dating/scambiocoppie.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/scambiocoppie.txt) |
| Scandimatch | 1 | [scandimatch.txt](lists/dating/scandimatch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/scandimatch.txt) |
| Schweizerhotchat | 1 | [schweizerhotchat.txt](lists/dating/schweizerhotchat.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/schweizerhotchat.txt) |
| Scotsgodating | 1 | [scotsgodating.txt](lists/dating/scotsgodating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/scotsgodating.txt) |
| Scottish Dating | 1 | [scottish_dating.txt](lists/dating/scottish_dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/scottish_dating.txt) |
| Sdvcloud | 1 | [sdvcloud.txt](lists/dating/sdvcloud.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sdvcloud.txt) |
| Searchbridal | 1 | [searchbridal.txt](lists/dating/searchbridal.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/searchbridal.txt) |
| Searchmate | 1 | [searchmate.txt](lists/dating/searchmate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/searchmate.txt) |
| Seasonsdating | 1 | [seasonsdating.txt](lists/dating/seasonsdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seasonsdating.txt) |
| Sechoisir | 1 | [sechoisir.txt](lists/dating/sechoisir.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sechoisir.txt) |
| Seekeo | 1 | [seekeo.txt](lists/dating/seekeo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seekeo.txt) |
| Seekingcougars | 1 | [seekingcougars.txt](lists/dating/seekingcougars.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seekingcougars.txt) |
| Sekscamera | 1 | [sekscamera.txt](lists/dating/sekscamera.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sekscamera.txt) |
| Senior Love Match | 1 | [senior_love_match.txt](lists/dating/senior_love_match.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/senior_love_match.txt) |
| Seniorbdsmusa | 1 | [seniorbdsmusa.txt](lists/dating/seniorbdsmusa.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorbdsmusa.txt) |
| Seniorbi | 1 | [seniorbi.txt](lists/dating/seniorbi.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorbi.txt) |
| Seniorblackpeoplemeet | 1 | [seniorblackpeoplemeet.txt](lists/dating/seniorblackpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorblackpeoplemeet.txt) |
| Seniorbondage | 1 | [seniorbondage.txt](lists/dating/seniorbondage.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorbondage.txt) |
| Seniorcasualdating | 1 | [seniorcasualdating.txt](lists/dating/seniorcasualdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorcasualdating.txt) |
| Seniorcrossdresser | 1 | [seniorcrossdresser.txt](lists/dating/seniorcrossdresser.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorcrossdresser.txt) |
| Seniorcrossdressusa | 1 | [seniorcrossdressusa.txt](lists/dating/seniorcrossdressusa.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorcrossdressusa.txt) |
| Seniordate | 1 | [seniordate.txt](lists/dating/seniordate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniordate.txt) |
| Seniordatelink | 1 | [seniordatelink.txt](lists/dating/seniordatelink.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniordatelink.txt) |
| Seniordating | 1 | [seniordating.txt](lists/dating/seniordating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniordating.txt) |
| Seniordatingagency | 2 | [seniordatingagency.txt](lists/dating/seniordatingagency.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniordatingagency.txt) |
| Seniordatingagency Scotland | 1 | [seniordatingagency_scotland.txt](lists/dating/seniordatingagency_scotland.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniordatingagency_scotland.txt) |
| Seniordatingagency Spain | 1 | [seniordatingagency_spain.txt](lists/dating/seniordatingagency_spain.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniordatingagency_spain.txt) |
| Seniordatingonline | 1 | [seniordatingonline.txt](lists/dating/seniordatingonline.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniordatingonline.txt) |
| Seniordatingplanet | 1 | [seniordatingplanet.txt](lists/dating/seniordatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniordatingplanet.txt) |
| Seniordatingsite | 1 | [seniordatingsite.txt](lists/dating/seniordatingsite.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniordatingsite.txt) |
| Seniordogging | 1 | [seniordogging.txt](lists/dating/seniordogging.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniordogging.txt) |
| Seniordomination | 1 | [seniordomination.txt](lists/dating/seniordomination.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniordomination.txt) |
| Seniorfetish | 1 | [seniorfetish.txt](lists/dating/seniorfetish.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorfetish.txt) |
| Seniorfriendfinder | 1 | [seniorfriendfinder.txt](lists/dating/seniorfriendfinder.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorfriendfinder.txt) |
| Seniorlesbians | 1 | [seniorlesbians.txt](lists/dating/seniorlesbians.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorlesbians.txt) |
| Seniorpeoplemeet | 1 | [seniorpeoplemeet.txt](lists/dating/seniorpeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorpeoplemeet.txt) |
| Seniorpolyamory | 1 | [seniorpolyamory.txt](lists/dating/seniorpolyamory.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorpolyamory.txt) |
| Seniorsbi | 1 | [seniorsbi.txt](lists/dating/seniorsbi.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorsbi.txt) |
| Seniorsingles | 1 | [seniorsingles.txt](lists/dating/seniorsingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorsingles.txt) |
| Seniorsinglesnear | 1 | [seniorsinglesnear.txt](lists/dating/seniorsinglesnear.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorsinglesnear.txt) |
| Seniorsinglesplace | 1 | [seniorsinglesplace.txt](lists/dating/seniorsinglesplace.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorsinglesplace.txt) |
| Seniorsubdomclub | 2 | [seniorsubdomclub.txt](lists/dating/seniorsubdomclub.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorsubdomclub.txt) |
| Seniorswingersclubusa | 1 | [seniorswingersclubusa.txt](lists/dating/seniorswingersclubusa.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorswingersclubusa.txt) |
| Seniorthreesomes | 1 | [seniorthreesomes.txt](lists/dating/seniorthreesomes.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorthreesomes.txt) |
| Seniorwhipping | 1 | [seniorwhipping.txt](lists/dating/seniorwhipping.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/seniorwhipping.txt) |
| Sentimente | 1 | [sentimente.txt](lists/dating/sentimente.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sentimente.txt) |
| Setravieso | 1 | [setravieso.txt](lists/dating/setravieso.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/setravieso.txt) |
| Sexy Tribu | 1 | [sexy_tribu.txt](lists/dating/sexy_tribu.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sexy_tribu.txt) |
| Shaadi | 1 | [shaadi.txt](lists/dating/shaadi.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/shaadi.txt) |
| Shaadicrowd | 1 | [shaadicrowd.txt](lists/dating/shaadicrowd.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/shaadicrowd.txt) |
| Show 640 | 1 | [show_640.txt](lists/dating/show_640.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/show_640.txt) |
| Sielsmaats | 1 | [sielsmaats.txt](lists/dating/sielsmaats.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sielsmaats.txt) |
| Silverdating | 1 | [silverdating.txt](lists/dating/silverdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/silverdating.txt) |
| Silvergaysingles | 1 | [silvergaysingles.txt](lists/dating/silvergaysingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/silvergaysingles.txt) |
| Silversurfersdating | 1 | [silversurfersdating.txt](lists/dating/silversurfersdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/silversurfersdating.txt) |
| Singaporelovelinks | 1 | [singaporelovelinks.txt](lists/dating/singaporelovelinks.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singaporelovelinks.txt) |
| Single Russian Woman | 1 | [single_russian_woman.txt](lists/dating/single_russian_woman.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/single_russian_woman.txt) |
| Single2 | 1 | [single2.txt](lists/dating/single2.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/single2.txt) |
| Single50Plus | 1 | [single50plus.txt](lists/dating/single50plus.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/single50plus.txt) |
| Singlebikerscanada | 1 | [singlebikerscanada.txt](lists/dating/singlebikerscanada.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singlebikerscanada.txt) |
| Singlebodybuilders | 1 | [singlebodybuilders.txt](lists/dating/singlebodybuilders.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singlebodybuilders.txt) |
| Singlematuredates | 1 | [singlematuredates.txt](lists/dating/singlematuredates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singlematuredates.txt) |
| Singlemomsanddads | 1 | [singlemomsanddads.txt](lists/dating/singlemomsanddads.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singlemomsanddads.txt) |
| Singleparentmatch | 1 | [singleparentmatch.txt](lists/dating/singleparentmatch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singleparentmatch.txt) |
| Singleparentmeet | 2 | [singleparentmeet.txt](lists/dating/singleparentmeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singleparentmeet.txt) |
| Singleparentscanada | 1 | [singleparentscanada.txt](lists/dating/singleparentscanada.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singleparentscanada.txt) |
| Singler | 1 | [singler.txt](lists/dating/singler.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singler.txt) |
| Singles | 1 | [singles.txt](lists/dating/singles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singles.txt) |
| Singles2Meet | 1 | [singles2meet.txt](lists/dating/singles2meet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singles2meet.txt) |
| Singlescrowd | 1 | [singlescrowd.txt](lists/dating/singlescrowd.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singlescrowd.txt) |
| Singlesdatingagency | 1 | [singlesdatingagency.txt](lists/dating/singlesdatingagency.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singlesdatingagency.txt) |
| Singlesintoronto | 1 | [singlesintoronto.txt](lists/dating/singlesintoronto.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singlesintoronto.txt) |
| Singlesmontreal | 1 | [singlesmontreal.txt](lists/dating/singlesmontreal.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singlesmontreal.txt) |
| Singlesolution | 1 | [singlesolution.txt](lists/dating/singlesolution.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singlesolution.txt) |
| Singletreffpunkt | 1 | [singletreffpunkt.txt](lists/dating/singletreffpunkt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/singletreffpunkt.txt) |
| Sinsflirt | 1 | [sinsflirt.txt](lists/dating/sinsflirt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sinsflirt.txt) |
| Sitederencontregratuit | 1 | [sitederencontregratuit.txt](lists/dating/sitederencontregratuit.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sitederencontregratuit.txt) |
| Skandinaviadating | 1 | [skandinaviadating.txt](lists/dating/skandinaviadating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/skandinaviadating.txt) |
| Skout | 1 | [skout.txt](lists/dating/skout.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/skout.txt) |
| Sladur | 1 | [sladur.txt](lists/dating/sladur.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sladur.txt) |
| Slowdating | 1 | [slowdating.txt](lists/dating/slowdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/slowdating.txt) |
| Smooch | 1 | [smooch.txt](lists/dating/smooch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/smooch.txt) |
| Smoothsingles | 1 | [smoothsingles.txt](lists/dating/smoothsingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/smoothsingles.txt) |
| Snap | 1 | [snap.txt](lists/dating/snap.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/snap.txt) |
| Sniffies | 1 | [sniffies.txt](lists/dating/sniffies.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sniffies.txt) |
| Soireesdannie | 1 | [soireesdannie.txt](lists/dating/soireesdannie.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/soireesdannie.txt) |
| Soirsexy | 1 | [soirsexy.txt](lists/dating/soirsexy.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/soirsexy.txt) |
| Soloperstanotte | 1 | [soloperstanotte.txt](lists/dating/soloperstanotte.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/soloperstanotte.txt) |
| Soloperunanotte | 1 | [soloperunanotte.txt](lists/dating/soloperunanotte.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/soloperunanotte.txt) |
| Soulfulencounters | 1 | [soulfulencounters.txt](lists/dating/soulfulencounters.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/soulfulencounters.txt) |
| Soulmate | 1 | [soulmate.txt](lists/dating/soulmate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/soulmate.txt) |
| Spark | 2 | [spark.txt](lists/dating/spark.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/spark.txt) |
| Specialbridge | 1 | [specialbridge.txt](lists/dating/specialbridge.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/specialbridge.txt) |
| Speed Dating Lyon | 1 | [speed_dating_lyon.txt](lists/dating/speed_dating_lyon.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/speed_dating_lyon.txt) |
| Speeddate | 1 | [speeddate.txt](lists/dating/speeddate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/speeddate.txt) |
| Speeddater | 1 | [speeddater.txt](lists/dating/speeddater.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/speeddater.txt) |
| Speeddating | 1 | [speeddating.txt](lists/dating/speeddating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/speeddating.txt) |
| Speeddatinglondon | 1 | [speeddatinglondon.txt](lists/dating/speeddatinglondon.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/speeddatinglondon.txt) |
| Speeddatingmontreal | 1 | [speeddatingmontreal.txt](lists/dating/speeddatingmontreal.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/speeddatingmontreal.txt) |
| Sportdatingplanet | 1 | [sportdatingplanet.txt](lists/dating/sportdatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sportdatingplanet.txt) |
| Sportydates | 1 | [sportydates.txt](lists/dating/sportydates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sportydates.txt) |
| Ssbbwdating | 1 | [ssbbwdating.txt](lists/dating/ssbbwdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ssbbwdating.txt) |
| Stastnatrefa | 1 | [stastnatrefa.txt](lists/dating/stastnatrefa.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/stastnatrefa.txt) |
| Suchejetzt | 1 | [suchejetzt.txt](lists/dating/suchejetzt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/suchejetzt.txt) |
| Sugarbook | 1 | [sugarbook.txt](lists/dating/sugarbook.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sugarbook.txt) |
| Sugarmatchmaking | 1 | [sugarmatchmaking.txt](lists/dating/sugarmatchmaking.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sugarmatchmaking.txt) |
| Sweetdiscreet | 1 | [sweetdiscreet.txt](lists/dating/sweetdiscreet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sweetdiscreet.txt) |
| Sweetmeet | 1 | [sweetmeet.txt](lists/dating/sweetmeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sweetmeet.txt) |
| Swissflirt | 1 | [swissflirt.txt](lists/dating/swissflirt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/swissflirt.txt) |
| Swissfriends | 1 | [swissfriends.txt](lists/dating/swissfriends.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/swissfriends.txt) |
| Sxeseis | 1 | [sxeseis.txt](lists/dating/sxeseis.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/sxeseis.txt) |
| Tadum | 1 | [tadum.txt](lists/dating/tadum.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tadum.txt) |
| Tagged | 1 | [tagged.txt](lists/dating/tagged.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tagged.txt) |
| Tagstat | 1 | [tagstat.txt](lists/dating/tagstat.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tagstat.txt) |
| Talksaferdating | 1 | [talksaferdating.txt](lists/dating/talksaferdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/talksaferdating.txt) |
| Tallfriends | 1 | [tallfriends.txt](lists/dating/tallfriends.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tallfriends.txt) |
| TanTan | 2 | [tantan.txt](lists/dating/tantan.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tantan.txt) |
| Tangodatingonline | 1 | [tangodatingonline.txt](lists/dating/tangodatingonline.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tangodatingonline.txt) |
| Tattoolovers | 1 | [tattoolovers.txt](lists/dating/tattoolovers.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tattoolovers.txt) |
| Tchatche | 1 | [tchatche.txt](lists/dating/tchatche.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tchatche.txt) |
| Teamo | 1 | [teamo.txt](lists/dating/teamo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/teamo.txt) |
| Teendatingplanet | 1 | [teendatingplanet.txt](lists/dating/teendatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/teendatingplanet.txt) |
| Tennesseeflirt | 1 | [tennesseeflirt.txt](lists/dating/tennesseeflirt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tennesseeflirt.txt) |
| Tennisdating | 1 | [tennisdating.txt](lists/dating/tennisdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tennisdating.txt) |
| Thai Dating | 1 | [thai_dating.txt](lists/dating/thai_dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/thai_dating.txt) |
| Thaicupid | 1 | [thaicupid.txt](lists/dating/thaicupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/thaicupid.txt) |
| Thaidate | 1 | [thaidate.txt](lists/dating/thaidate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/thaidate.txt) |
| Thaidating | 1 | [thaidating.txt](lists/dating/thaidating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/thaidating.txt) |
| Thailovelines | 1 | [thailovelines.txt](lists/dating/thailovelines.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/thailovelines.txt) |
| Thedataagency | 1 | [thedataagency.txt](lists/dating/thedataagency.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/thedataagency.txt) |
| Thedatingjudge | 1 | [thedatingjudge.txt](lists/dating/thedatingjudge.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/thedatingjudge.txt) |
| Thedatingnetwork | 1 | [thedatingnetwork.txt](lists/dating/thedatingnetwork.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/thedatingnetwork.txt) |
| Thematchmakerofmaine | 1 | [thematchmakerofmaine.txt](lists/dating/thematchmakerofmaine.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/thematchmakerofmaine.txt) |
| Thematureconnection | 1 | [thematureconnection.txt](lists/dating/thematureconnection.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/thematureconnection.txt) |
| Thepeggingclub | 2 | [thepeggingclub.txt](lists/dating/thepeggingclub.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/thepeggingclub.txt) |
| Thepickuppros | 1 | [thepickuppros.txt](lists/dating/thepickuppros.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/thepickuppros.txt) |
| Thethreesomeconnection | 1 | [thethreesomeconnection.txt](lists/dating/thethreesomeconnection.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/thethreesomeconnection.txt) |
| Thirtyflirty | 1 | [thirtyflirty.txt](lists/dating/thirtyflirty.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/thirtyflirty.txt) |
| Threesomeconnection | 1 | [threesomeconnection.txt](lists/dating/threesomeconnection.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/threesomeconnection.txt) |
| Threesomegroup | 2 | [threesomegroup.txt](lists/dating/threesomegroup.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/threesomegroup.txt) |
| Thunderboltcity | 1 | [thunderboltcity.txt](lists/dating/thunderboltcity.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/thunderboltcity.txt) |
| Tiilt | 1 | [tiilt.txt](lists/dating/tiilt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tiilt.txt) |
| Tinder | 3 | [tinder.txt](lists/dating/tinder.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tinder.txt) |
| Tinderoplus | 1 | [tinderoplus.txt](lists/dating/tinderoplus.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tinderoplus.txt) |
| Todomaduras | 1 | [todomaduras.txt](lists/dating/todomaduras.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/todomaduras.txt) |
| Togethernetworks | 1 | [togethernetworks.txt](lists/dating/togethernetworks.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/togethernetworks.txt) |
| Toietmoi | 1 | [toietmoi.txt](lists/dating/toietmoi.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/toietmoi.txt) |
| Tonga Soa | 1 | [tonga_soa.txt](lists/dating/tonga_soa.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tonga_soa.txt) |
| Top10Maturedatingsites | 1 | [top10maturedatingsites.txt](lists/dating/top10maturedatingsites.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/top10maturedatingsites.txt) |
| Top20 | 1 | [top20.txt](lists/dating/top20.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/top20.txt) |
| Top5Dating | 1 | [top5dating.txt](lists/dating/top5dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/top5dating.txt) |
| Topdatings | 1 | [topdatings.txt](lists/dating/topdatings.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/topdatings.txt) |
| Toplop | 1 | [toplop.txt](lists/dating/toplop.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/toplop.txt) |
| Toprencontres | 1 | [toprencontres.txt](lists/dating/toprencontres.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/toprencontres.txt) |
| Transen Dating | 1 | [transen_dating.txt](lists/dating/transen_dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/transen_dating.txt) |
| Tresor Sexe | 1 | [tresor_sexe.txt](lists/dating/tresor_sexe.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tresor_sexe.txt) |
| Triocontactos | 1 | [triocontactos.txt](lists/dating/triocontactos.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/triocontactos.txt) |
| Trioespana | 1 | [trioespana.txt](lists/dating/trioespana.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/trioespana.txt) |
| Trudating | 1 | [trudating.txt](lists/dating/trudating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/trudating.txt) |
| Tsdate | 1 | [tsdate.txt](lists/dating/tsdate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tsdate.txt) |
| Tsdates | 1 | [tsdates.txt](lists/dating/tsdates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tsdates.txt) |
| Tsdating | 1 | [tsdating.txt](lists/dating/tsdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tsdating.txt) |
| Turboflirt | 1 | [turboflirt.txt](lists/dating/turboflirt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/turboflirt.txt) |
| Tvtsdating | 1 | [tvtsdating.txt](lists/dating/tvtsdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tvtsdating.txt) |
| U Lover | 1 | [u_lover.txt](lists/dating/u_lover.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/u_lover.txt) |
| U Rencontres | 1 | [u_rencontres.txt](lists/dating/u_rencontres.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/u_rencontres.txt) |
| Uadating | 1 | [uadating.txt](lists/dating/uadating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/uadating.txt) |
| Uchat | 1 | [uchat.txt](lists/dating/uchat.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/uchat.txt) |
| Udolly | 1 | [udolly.txt](lists/dating/udolly.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/udolly.txt) |
| Ugay | 1 | [ugay.txt](lists/dating/ugay.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ugay.txt) |
| Uk Lottery | 1 | [uk_lottery.txt](lists/dating/uk_lottery.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/uk_lottery.txt) |
| Ukrainischefrauen | 1 | [ukrainischefrauen.txt](lists/dating/ukrainischefrauen.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ukrainischefrauen.txt) |
| Ultrarichmatch | 1 | [ultrarichmatch.txt](lists/dating/ultrarichmatch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/ultrarichmatch.txt) |
| Upforit | 1 | [upforit.txt](lists/dating/upforit.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/upforit.txt) |
| Uppdating | 1 | [uppdating.txt](lists/dating/uppdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/uppdating.txt) |
| Upward App | 1 | [upward_app.txt](lists/dating/upward_app.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/upward_app.txt) |
| Urbansocial | 1 | [urbansocial.txt](lists/dating/urbansocial.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/urbansocial.txt) |
| Usadatingplanet | 1 | [usadatingplanet.txt](lists/dating/usadatingplanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/usadatingplanet.txt) |
| Valentimatchmaking | 1 | [valentimatchmaking.txt](lists/dating/valentimatchmaking.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/valentimatchmaking.txt) |
| Vanessa69 | 1 | [vanessa69.txt](lists/dating/vanessa69.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/vanessa69.txt) |
| Veemance | 1 | [veemance.txt](lists/dating/veemance.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/veemance.txt) |
| Vegadating | 1 | [vegadating.txt](lists/dating/vegadating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/vegadating.txt) |
| Vegaia | 1 | [vegaia.txt](lists/dating/vegaia.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/vegaia.txt) |
| Vegandating | 1 | [vegandating.txt](lists/dating/vegandating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/vegandating.txt) |
| Vegandatinguk | 1 | [vegandatinguk.txt](lists/dating/vegandatinguk.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/vegandatinguk.txt) |
| Vegetariandating | 1 | [vegetariandating.txt](lists/dating/vegetariandating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/vegetariandating.txt) |
| Veggie Singles | 1 | [veggie_singles.txt](lists/dating/veggie_singles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/veggie_singles.txt) |
| Veggieflirt | 1 | [veggieflirt.txt](lists/dating/veggieflirt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/veggieflirt.txt) |
| Veggiepeoplemeet | 1 | [veggiepeoplemeet.txt](lists/dating/veggiepeoplemeet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/veggiepeoplemeet.txt) |
| Venntro | 1 | [venntro.txt](lists/dating/venntro.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/venntro.txt) |
| Vglove | 1 | [vglove.txt](lists/dating/vglove.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/vglove.txt) |
| Vibeline | 1 | [vibeline.txt](lists/dating/vibeline.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/vibeline.txt) |
| Vietfun | 1 | [vietfun.txt](lists/dating/vietfun.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/vietfun.txt) |
| Vietnamcupid | 1 | [vietnamcupid.txt](lists/dating/vietnamcupid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/vietnamcupid.txt) |
| Violetdates | 1 | [violetdates.txt](lists/dating/violetdates.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/violetdates.txt) |
| Virginiaonlinepersonals | 1 | [virginiaonlinepersonals.txt](lists/dating/virginiaonlinepersonals.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/virginiaonlinepersonals.txt) |
| Virtumatch | 1 | [virtumatch.txt](lists/dating/virtumatch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/virtumatch.txt) |
| Volosdate | 1 | [volosdate.txt](lists/dating/volosdate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/volosdate.txt) |
| W Ru | 1 | [w_ru.txt](lists/dating/w_ru.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/w_ru.txt) |
| Wantubad | 1 | [wantubad.txt](lists/dating/wantubad.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/wantubad.txt) |
| Waplog | 1 | [waplog.txt](lists/dating/waplog.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/waplog.txt) |
| Wearedogging | 1 | [wearedogging.txt](lists/dating/wearedogging.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/wearedogging.txt) |
| Webconnexions | 1 | [webconnexions.txt](lists/dating/webconnexions.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/webconnexions.txt) |
| Weekenddating | 1 | [weekenddating.txt](lists/dating/weekenddating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/weekenddating.txt) |
| Wellhello | 1 | [wellhello.txt](lists/dating/wellhello.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/wellhello.txt) |
| Westmidlandstransvestites | 1 | [westmidlandstransvestites.txt](lists/dating/westmidlandstransvestites.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/westmidlandstransvestites.txt) |
| Wheelchairdating | 1 | [wheelchairdating.txt](lists/dating/wheelchairdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/wheelchairdating.txt) |
| Whispers4U | 1 | [whispers4u.txt](lists/dating/whispers4u.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/whispers4u.txt) |
| Whitedate | 1 | [whitedate.txt](lists/dating/whitedate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/whitedate.txt) |
| Wiccandatingsite | 1 | [wiccandatingsite.txt](lists/dating/wiccandatingsite.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/wiccandatingsite.txt) |
| Widowedsinglesnear | 1 | [widowedsinglesnear.txt](lists/dating/widowedsinglesnear.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/widowedsinglesnear.txt) |
| Widowmatch | 1 | [widowmatch.txt](lists/dating/widowmatch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/widowmatch.txt) |
| Wildspank | 1 | [wildspank.txt](lists/dating/wildspank.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/wildspank.txt) |
| Wizz | 3 | [wizz.txt](lists/dating/wizz.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/wizz.txt) |
| Worldofsingles | 1 | [worldofsingles.txt](lists/dating/worldofsingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/worldofsingles.txt) |
| Worldsingles | 1 | [worldsingles.txt](lists/dating/worldsingles.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/worldsingles.txt) |
| Wuopo | 1 | [wuopo.txt](lists/dating/wuopo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/wuopo.txt) |
| Xdate | 1 | [xdate.txt](lists/dating/xdate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/xdate.txt) |
| Xdates18 | 1 | [xdates18.txt](lists/dating/xdates18.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/xdates18.txt) |
| Xflirt | 1 | [xflirt.txt](lists/dating/xflirt.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/xflirt.txt) |
| Xmeeting | 1 | [xmeeting.txt](lists/dating/xmeeting.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/xmeeting.txt) |
| Xpartner | 1 | [xpartner.txt](lists/dating/xpartner.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/xpartner.txt) |
| Xpress | 1 | [xpress.txt](lists/dating/xpress.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/xpress.txt) |
| Yes Messenger | 1 | [yes_messenger.txt](lists/dating/yes_messenger.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/yes_messenger.txt) |
| Yid | 1 | [yid.txt](lists/dating/yid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/yid.txt) |
| Youdate | 1 | [youdate.txt](lists/dating/youdate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/youdate.txt) |
| Youmeets | 1 | [youmeets.txt](lists/dating/youmeets.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/youmeets.txt) |
| Youmemarriage | 1 | [youmemarriage.txt](lists/dating/youmemarriage.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/youmemarriage.txt) |
| Youngukswingers | 1 | [youngukswingers.txt](lists/dating/youngukswingers.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/youngukswingers.txt) |
| Youngwidowedanddating | 1 | [youngwidowedanddating.txt](lists/dating/youngwidowedanddating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/youngwidowedanddating.txt) |
| Yourdatelink | 1 | [yourdatelink.txt](lists/dating/yourdatelink.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/yourdatelink.txt) |
| Yourfirstdating | 1 | [yourfirstdating.txt](lists/dating/yourfirstdating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/yourfirstdating.txt) |
| Yourjewishdate | 1 | [yourjewishdate.txt](lists/dating/yourjewishdate.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/yourjewishdate.txt) |
| Yoursecrethookup | 1 | [yoursecrethookup.txt](lists/dating/yoursecrethookup.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/yoursecrethookup.txt) |
| Zabido | 1 | [zabido.txt](lists/dating/zabido.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/zabido.txt) |
| Zarf | 1 | [zarf.txt](lists/dating/zarf.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/zarf.txt) |
| Zhenai91 | 1 | [zhenai91.txt](lists/dating/zhenai91.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/zhenai91.txt) |
| Znamost | 1 | [znamost.txt](lists/dating/znamost.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/znamost.txt) |
| Zonabdsm | 1 | [zonabdsm.txt](lists/dating/zonabdsm.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/zonabdsm.txt) |
| Zonabisexual | 1 | [zonabisexual.txt](lists/dating/zonabisexual.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/zonabisexual.txt) |
| Zoosk | 1 | [zoosk.txt](lists/dating/zoosk.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/zoosk.txt) |
| eHarmony | 3 | [eharmony.txt](lists/dating/eharmony.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/eharmony.txt) |
| happn | 1 | [happn.txt](lists/dating/happn.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/happn.txt) |

### DNS Providers

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Cloud Flare DNS | 1 | [CFDNS.txt](lists/dns/CFDNS.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dns/CFDNS.txt) |
| Google DNS | 1 | [googleDNS.txt](lists/dns/googleDNS.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dns/googleDNS.txt) |

### DNS / VPN Bypass

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| HaGeZi DoH VPN Proxy Bypass | 18,907 | [hagezi_doh_vpn_proxy_bypass.txt](lists/dns_bypass/hagezi_doh_vpn_proxy_bypass.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dns_bypass/hagezi_doh_vpn_proxy_bypass.txt) |

### Drugs

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Drugs | 18,320 | [blp_drugs.txt](lists/drugs/blp_drugs.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/drugs/blp_drugs.txt) |

### Dynamic DNS

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| HaGeZi Dynamic DNS | 1,022 | [hagezi_dyndns.txt](lists/dynamic_dns/hagezi_dyndns.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dynamic_dns/hagezi_dyndns.txt) |

### Gambling & Betting

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Betano | 7 | [betano.txt](lists/gambling/betano.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gambling/betano.txt) |
| Betfair | 6 | [betfair.txt](lists/gambling/betfair.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gambling/betfair.txt) |
| Betway | 16 | [betway.txt](lists/gambling/betway.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gambling/betway.txt) |
| Blaze | 4 | [blaze.txt](lists/gambling/blaze.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gambling/blaze.txt) |

### Gaming Platforms

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Activision Blizzard | 6 | [activision_blizzard.txt](lists/gaming/activision_blizzard.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/activision_blizzard.txt) |
| ArenaNet | 1 | [arenanet.txt](lists/gaming/arenanet.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/arenanet.txt) |
| Battle.net | 4 | [battle_net.txt](lists/gaming/battle_net.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/battle_net.txt) |
| Battlestate Games | 2 | [battlestate_games.txt](lists/gaming/battlestate_games.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/battlestate_games.txt) |
| Blizzard Entertainment | 14 | [blizzard_entertainment.txt](lists/gaming/blizzard_entertainment.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/blizzard_entertainment.txt) |
| City of Heroes | 1 | [city_of_heroes.txt](lists/gaming/city_of_heroes.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/city_of_heroes.txt) |
| Daybreak Games | 1 | [daybreak_games.txt](lists/gaming/daybreak_games.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/daybreak_games.txt) |
| Electronic Arts | 6 | [electronic_arts.txt](lists/gaming/electronic_arts.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/electronic_arts.txt) |
| Epic Games | 8 | [epic_games.txt](lists/gaming/epic_games.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/epic_games.txt) |
| Frontier Games | 1 | [frontier_games.txt](lists/gaming/frontier_games.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/frontier_games.txt) |
| GOG | 4 | [gog.txt](lists/gaming/gog.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/gog.txt) |
| IO Interactive | 3 | [io_interactive.txt](lists/gaming/io_interactive.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/io_interactive.txt) |
| League of Legends | 5 | [leagueoflegends.txt](lists/gaming/leagueoflegends.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/leagueoflegends.txt) |
| Minecraft | 3 | [minecraft.txt](lists/gaming/minecraft.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/minecraft.txt) |
| Neverwinter | 1 | [neverwinter.txt](lists/gaming/neverwinter.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/neverwinter.txt) |
| Nexus Mods | 1 | [nexusmods.txt](lists/gaming/nexusmods.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/nexusmods.txt) |
| Nintendo | 17 | [nintendo.txt](lists/gaming/nintendo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/nintendo.txt) |
| Origin | 9 | [origin.txt](lists/gaming/origin.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/origin.txt) |
| Path of Exile | 1 | [path_of_exile.txt](lists/gaming/path_of_exile.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/path_of_exile.txt) |
| PlayStation | 10 | [playstation.txt](lists/gaming/playstation.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/playstation.txt) |
| Renegade X | 2 | [renegade_x.txt](lists/gaming/renegade_x.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/renegade_x.txt) |
| Riot Games | 7 | [riot_games.txt](lists/gaming/riot_games.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/riot_games.txt) |
| Roblox | 13 | [roblox.txt](lists/gaming/roblox.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/roblox.txt) |
| Rockstar Games | 2 | [rockstar_games.txt](lists/gaming/rockstar_games.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/rockstar_games.txt) |
| Square Enix | 1 | [square_enix.txt](lists/gaming/square_enix.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/square_enix.txt) |
| Steam | 33 | [steam.txt](lists/gaming/steam.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/steam.txt) |
| The Elder Scrolls Online | 1 | [the_elder_scrolls_online.txt](lists/gaming/the_elder_scrolls_online.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/the_elder_scrolls_online.txt) |
| Ubisoft | 4 | [ubisoft.txt](lists/gaming/ubisoft.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/ubisoft.txt) |
| Valorant | 2 | [valorant.txt](lists/gaming/valorant.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/valorant.txt) |
| Warframe | 1 | [warframe.txt](lists/gaming/warframe.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/warframe.txt) |
| Wargaming | 9 | [wargaming.txt](lists/gaming/wargaming.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/wargaming.txt) |
| Warner Bros. Games | 1 | [warnerbrosgames.txt](lists/gaming/warnerbrosgames.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/warnerbrosgames.txt) |
| Xbox Live | 8 | [xboxlive.txt](lists/gaming/xboxlive.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/xboxlive.txt) |

### Hosting & File Platforms

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Box | 4 | [box.txt](lists/hosting/box.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/hosting/box.txt) |
| Dropbox | 22 | [dropbox.txt](lists/hosting/dropbox.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/hosting/dropbox.txt) |
| Flickr | 6 | [flickr.txt](lists/hosting/flickr.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/hosting/flickr.txt) |
| Imgur | 1 | [imgur.txt](lists/hosting/imgur.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/hosting/imgur.txt) |

### Malware & Threats

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Ransomware | 1,669 | [blp_ransomware.txt](lists/malware/blp_ransomware.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/malware/blp_ransomware.txt) |
| ThreatFox | 315 | [threatfox.txt](lists/malware/threatfox.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/malware/threatfox.txt) |
| URLhaus | 1,502 | [urlhaus.txt](lists/malware/urlhaus.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/malware/urlhaus.txt) |

### Messaging Apps

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| KakaoTalk | 2 | [kakaotalk.txt](lists/messenger/kakaotalk.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/messenger/kakaotalk.txt) |
| Kik | 1 | [kik.txt](lists/messenger/kik.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/messenger/kik.txt) |
| MAX | 1 | [max.txt](lists/messenger/max.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/messenger/max.txt) |
| Microsoft Teams | 3 | [microsoft_teams.txt](lists/messenger/microsoft_teams.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/messenger/microsoft_teams.txt) |
| Olvid | 2 | [olvid.txt](lists/messenger/olvid.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/messenger/olvid.txt) |
| Signal | 2 | [signal.txt](lists/messenger/signal.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/messenger/signal.txt) |
| Skype | 7 | [skype.txt](lists/messenger/skype.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/messenger/skype.txt) |
| Slack | 4 | [slack.txt](lists/messenger/slack.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/messenger/slack.txt) |
| Telegram (Web) | 17 | [telegram.txt](lists/messenger/telegram.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/messenger/telegram.txt) |
| Viber | 1 | [viber.txt](lists/messenger/viber.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/messenger/viber.txt) |
| WeChat | 4 | [wechat.txt](lists/messenger/wechat.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/messenger/wechat.txt) |
| WhatsApp | 11 | [whatsapp.txt](lists/messenger/whatsapp.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/messenger/whatsapp.txt) |

### Phishing & Scam Sites

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| OpenPhish | 226 | [openphish.txt](lists/phishing/openphish.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/phishing/openphish.txt) |
| PhishTank | 20,406 | [phishtank.txt](lists/phishing/phishtank.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/phishing/phishtank.txt) |
| Phishing Army | 283,515 | [phishing_army.txt](lists/phishing/phishing_army.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/phishing/phishing_army.txt) |

### Piracy

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Piracy | 1,065 | [blp_piracy.txt](lists/piracy/blp_piracy.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/piracy/blp_piracy.txt) |

### Privacy Tools

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Privacy | 1 | [privacy.txt](lists/privacy/privacy.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/privacy/privacy.txt) |
| Proton | 5 | [proton.txt](lists/privacy/proton.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/privacy/proton.txt) |

### Redirectors

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Redirect | 99,201 | [blp_redirect.txt](lists/redirect/blp_redirect.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/redirect/blp_redirect.txt) |

### Scam & Fraud

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Fraud | 114,108 | [blp_fraud.txt](lists/scam/blp_fraud.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/scam/blp_fraud.txt) |
| Block List Project Scam | 726 | [blp_scam.txt](lists/scam/blp_scam.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/scam/blp_scam.txt) |
| HaGeZi Fake | 14,351 | [hagezi_fake.txt](lists/scam/hagezi_fake.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/scam/hagezi_fake.txt) |

### Shopping & Marketplaces

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| AliExpress | 4 | [aliexpress.txt](lists/shopping/aliexpress.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/aliexpress.txt) |
| Amazon | 181 | [amazon.txt](lists/shopping/amazon.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/amazon.txt) |
| CoolApk | 3 | [coolapk.txt](lists/shopping/coolapk.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/coolapk.txt) |
| Lazada | 9 | [lazada.txt](lists/shopping/lazada.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/lazada.txt) |
| Mercado Libre | 20 | [mercado_libre.txt](lists/shopping/mercado_libre.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/mercado_libre.txt) |
| Shein | 4 | [shein.txt](lists/shopping/shein.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/shein.txt) |
| Shopee | 20 | [shopee.txt](lists/shopping/shopee.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/shopee.txt) |
| Temu | 3 | [temu.txt](lists/shopping/temu.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/temu.txt) |
| Xiaohongshu | 5 | [xiaohongshu.txt](lists/shopping/xiaohongshu.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/xiaohongshu.txt) |
| eBay | 318 | [ebay.txt](lists/shopping/ebay.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/ebay.txt) |

### Smart TV Telemetry

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Smart TV | 70 | [blp_smart_tv.txt](lists/smart_tv/blp_smart_tv.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/smart_tv/blp_smart_tv.txt) |

### Social Networks

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| 4chan | 3 | [4chan.txt](lists/social_network/4chan.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/4chan.txt) |
| 500px | 2 | [500px.txt](lists/social_network/500px.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/500px.txt) |
| 9GAG | 2 | [9gag.txt](lists/social_network/9gag.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/9gag.txt) |
| Amino | 1 | [amino.txt](lists/social_network/amino.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/amino.txt) |
| Bluesky | 2 | [bluesky.txt](lists/social_network/bluesky.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/bluesky.txt) |
| Clubhouse | 2 | [clubhouse.txt](lists/social_network/clubhouse.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/clubhouse.txt) |
| Discord | 26 | [discord.txt](lists/social_network/discord.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/discord.txt) |
| Douban | 3 | [douban.txt](lists/social_network/douban.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/douban.txt) |
| Facebook | 441 | [facebook.txt](lists/social_network/facebook.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/facebook.txt) |
| Instagram | 72 | [instagram.txt](lists/social_network/instagram.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/instagram.txt) |
| KOOK | 2 | [kook.txt](lists/social_network/kook.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/kook.txt) |
| LINE | 18 | [line.txt](lists/social_network/line.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/line.txt) |
| LinkedIn | 14 | [linkedin.txt](lists/social_network/linkedin.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/linkedin.txt) |
| Mail.ru | 3 | [mail_ru.txt](lists/social_network/mail_ru.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/mail_ru.txt) |
| Mastodon | 97 | [mastodon.txt](lists/social_network/mastodon.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/mastodon.txt) |
| OK.ru | 6 | [ok.txt](lists/social_network/ok.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/ok.txt) |
| Odysee | 4 | [odysee.txt](lists/social_network/odysee.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/odysee.txt) |
| OnlyFans | 1 | [onlyfans.txt](lists/social_network/onlyfans.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/onlyfans.txt) |
| Pinterest | 49 | [pinterest.txt](lists/social_network/pinterest.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/pinterest.txt) |
| Reddit | 5 | [reddit.txt](lists/social_network/reddit.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/reddit.txt) |
| Snapchat | 6 | [snapchat.txt](lists/social_network/snapchat.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/snapchat.txt) |
| TikTok | 31 | [tiktok.txt](lists/social_network/tiktok.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/tiktok.txt) |
| Tumblr | 1 | [tumblr.txt](lists/social_network/tumblr.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/tumblr.txt) |
| VK.com | 20 | [vk.txt](lists/social_network/vk.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/vk.txt) |
| X (formerly Twitter) | 23 | [twitter.txt](lists/social_network/twitter.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/twitter.txt) |
| Zhihu | 2 | [zhihu.txt](lists/social_network/zhihu.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/zhihu.txt) |

### Software & Updates

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Google Play Store | 3 | [playstore.txt](lists/software/playstore.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/software/playstore.txt) |
| Nvidia | 10 | [nvidia.txt](lists/software/nvidia.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/software/nvidia.txt) |

### Streaming Services

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Amazon Streaming | 19 | [amazon_streaming.txt](lists/streaming/amazon_streaming.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/amazon_streaming.txt) |
| Apple Streaming | 13 | [apple_streaming.txt](lists/streaming/apple_streaming.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/apple_streaming.txt) |
| Bigo Live | 4 | [bigo_live.txt](lists/streaming/bigo_live.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/bigo_live.txt) |
| Bilibili | 46 | [bilibili.txt](lists/streaming/bilibili.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/bilibili.txt) |
| Canais Globo | 1 | [canais_globo.txt](lists/streaming/canais_globo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/canais_globo.txt) |
| Claro | 22 | [claro.txt](lists/streaming/claro.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/claro.txt) |
| Crunchyroll | 2 | [crunchyroll.txt](lists/streaming/crunchyroll.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/crunchyroll.txt) |
| Dailymotion | 3 | [dailymotion.txt](lists/streaming/dailymotion.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/dailymotion.txt) |
| Deezer | 2 | [deezer.txt](lists/streaming/deezer.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/deezer.txt) |
| DirecTV Go | 1 | [directvgo.txt](lists/streaming/directvgo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/directvgo.txt) |
| Discovery+ | 2 | [discoveryplus.txt](lists/streaming/discoveryplus.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/discoveryplus.txt) |
| Disney+ | 7 | [disneyplus.txt](lists/streaming/disneyplus.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/disneyplus.txt) |
| ESPN | 17 | [espn.txt](lists/streaming/espn.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/espn.txt) |
| FIFA | 2 | [fifa.txt](lists/streaming/fifa.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/fifa.txt) |
| Globoplay | 3 | [globoplay.txt](lists/streaming/globoplay.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/globoplay.txt) |
| HBO Max | 13 | [hbomax.txt](lists/streaming/hbomax.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/hbomax.txt) |
| Hulu | 1 | [hulu.txt](lists/streaming/hulu.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/hulu.txt) |
| Lionsgate+ | 2 | [lionsgateplus.txt](lists/streaming/lionsgateplus.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/lionsgateplus.txt) |
| Looke | 2 | [looke.txt](lists/streaming/looke.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/looke.txt) |
| Nebula | 2 | [nebula.txt](lists/streaming/nebula.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/nebula.txt) |
| Netflix | 22 | [netflix.txt](lists/streaming/netflix.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/netflix.txt) |
| Paramount Plus | 2 | [paramountplus.txt](lists/streaming/paramountplus.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/paramountplus.txt) |
| Peacock TV | 2 | [peacock_tv.txt](lists/streaming/peacock_tv.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/peacock_tv.txt) |
| Plex | 4 | [plex.txt](lists/streaming/plex.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/plex.txt) |
| Pluto TV | 1 | [pluto_tv.txt](lists/streaming/pluto_tv.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/pluto_tv.txt) |
| QQ | 2 | [qq.txt](lists/streaming/qq.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/qq.txt) |
| Rakuten Viki | 3 | [rakuten_viki.txt](lists/streaming/rakuten_viki.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/rakuten_viki.txt) |
| Samsung TV Plus | 4 | [samsung_tv_plus.txt](lists/streaming/samsung_tv_plus.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/samsung_tv_plus.txt) |
| SoundCloud | 2 | [soundcloud.txt](lists/streaming/soundcloud.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/soundcloud.txt) |
| Spotify | 19 | [spotify.txt](lists/streaming/spotify.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/spotify.txt) |
| Spotify Video | 5 | [spotify_video.txt](lists/streaming/spotify_video.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/spotify_video.txt) |
| Tidal | 1 | [tidal.txt](lists/streaming/tidal.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/tidal.txt) |
| Twitch | 6 | [twitch.txt](lists/streaming/twitch.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/twitch.txt) |
| Vimeo | 17 | [vimeo.txt](lists/streaming/vimeo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/vimeo.txt) |
| Vivo Play | 3 | [vivo_play.txt](lists/streaming/vivo_play.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/vivo_play.txt) |
| Voot | 1 | [voot.txt](lists/streaming/voot.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/voot.txt) |
| Weibo | 7 | [weibo.txt](lists/streaming/weibo.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/weibo.txt) |
| YY | 1 | [yy.txt](lists/streaming/yy.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/yy.txt) |
| YouTube | 173 | [youtube.txt](lists/streaming/youtube.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/youtube.txt) |
| iHeartRadio | 11 | [iheartradio.txt](lists/streaming/iheartradio.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/iheartradio.txt) |
| iQIYI | 8 | [iqiyi.txt](lists/streaming/iqiyi.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/iqiyi.txt) |

### Torrent

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Torrent | 2,192 | [blp_torrent.txt](lists/torrent/blp_torrent.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/torrent/blp_torrent.txt) |

### Tracking & Analytics

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Tracking | 14,761 | [blp_tracking.txt](lists/tracking/blp_tracking.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/tracking/blp_tracking.txt) |

### URL Shorteners

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| HaGeZi URL Shortener | 9,930 | [hagezi_urlshortener.txt](lists/url_shortener/hagezi_urlshortener.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/url_shortener/hagezi_urlshortener.txt) |

### Vaping

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Vaping | 32 | [blp_vaping.txt](lists/vaping/blp_vaping.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/vaping/blp_vaping.txt) |

## Usage

### Pi-hole
1. Navigate to **Settings** → **Blocklists**
2. Paste the **Raw URL** of your desired list
3. Click **Save and Update**
4. Wait for gravity to update

### AdGuard Home
1. Go to **Filters** → **DNS blocklists**
2. Click **Add blocklist** → **Add a custom list**
3. Paste the **Raw URL** and provide a name
4. Click **Save**

## Format Details

- **Hosts file format** - `0.0.0.0 hostname` for broad compatibility
- **Registrable domains by default** - avoids invalid suffixes like `co.uk`
- **Exact hostnames preserved where needed** - mainly DNS endpoint overrides
- **One entry per line** with commented headers and generation metadata

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
