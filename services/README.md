# Threat Intelligence & Content Blocklists

**Generated:** 2026-04-26 05:17:14 UTC

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

## Aggregated Categories

One-click blocklists combining multiple sources for everyday blocking.

| Category | Root Domains | Sources | File | Raw URL |
|----------|---------|---------|------|---------|
| 🔞 Adult Content | 86,133 | 3 | [adult.txt](categories/adult.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/adult.txt) |
| 📁 Ai | 19 | 9 | [ai.txt](categories/ai.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/ai.txt) |
| 🗄️ Badware Hosters | 1,195 | 1 | [badware_hoster.txt](categories/badware_hoster.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/badware_hoster.txt) |
| 📁 Cdn | 30 | 1 | [cdn.txt](categories/cdn.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/cdn.txt) |
| 📁 Dating | 7 | 3 | [dating.txt](categories/dating.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/dating.txt) |
| 🛜 DNS Providers | 2 | 2 | [dns.txt](categories/dns.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/dns.txt) |
| 🌐 Dynamic DNS | 1,480 | 1 | [dynamic_dns.txt](categories/dynamic_dns.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/dynamic_dns.txt) |
| 📁 Gambling | 33 | 4 | [gambling.txt](categories/gambling.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/gambling.txt) |
| 🎮 Gaming Platforms | 172 | 33 | [gaming.txt](categories/gaming.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/gaming.txt) |
| 📁 Hosting | 33 | 4 | [hosting.txt](categories/hosting.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/hosting.txt) |
| 🦠 Malware & Threats | 3,255 | 3 | [malware.txt](categories/malware.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/malware.txt) |
| 📁 Messenger | 55 | 12 | [messenger.txt](categories/messenger.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/messenger.txt) |
| 🎣 Phishing & Scam Sites | 299,961 | 3 | [phishing.txt](categories/phishing.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/phishing.txt) |
| 📁 Privacy | 6 | 2 | [privacy.txt](categories/privacy.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/privacy.txt) |
| 💸 Scam & Fraud | 129,081 | 3 | [scam.txt](categories/scam.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/scam.txt) |
| 📁 Shopping | 571 | 10 | [shopping.txt](categories/shopping.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/shopping.txt) |
| 📱 Social Networks | 836 | 26 | [social_network.txt](categories/social_network.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/social_network.txt) |
| 📁 Software | 13 | 2 | [software.txt](categories/software.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/software.txt) |
| 📺 Streaming Services | 455 | 41 | [streaming.txt](categories/streaming.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/streaming.txt) |
| 🛰️ Tracking & Analytics | 14,763 | 1 | [tracking.txt](categories/tracking.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/categories/tracking.txt) |

## Individual Sources

For granular control, each source is available separately if you want source-level attribution or need to disable one feed.

### Adult

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Chad Mayfield Porn | 5,881 | [chadmayfield_porn.txt](lists/adult/chadmayfield_porn.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/adult/chadmayfield_porn.txt) |
| Grindr | 1 | [grindr.txt](lists/adult/grindr.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/adult/grindr.txt) |
| StevenBlack Porn | 83,451 | [stevenblack_porn.txt](lists/adult/stevenblack_porn.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/adult/stevenblack_porn.txt) |

### Ai

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

### Badware Hoster

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| HaGeZi Badware Hoster | 1,195 | [hagezi_hoster.txt](lists/badware_hoster/hagezi_hoster.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/badware_hoster/hagezi_hoster.txt) |

### Cdn

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Cloudflare | 30 | [cloudflare.txt](lists/cdn/cloudflare.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/cdn/cloudflare.txt) |

### Dating

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Plenty of Fish | 1 | [plenty_of_fish.txt](lists/dating/plenty_of_fish.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/plenty_of_fish.txt) |
| Tinder | 3 | [tinder.txt](lists/dating/tinder.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/tinder.txt) |
| Wizz | 3 | [wizz.txt](lists/dating/wizz.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dating/wizz.txt) |

### Dns

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Cloud Flare DNS | 1 | [CFDNS.txt](lists/dns/CFDNS.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dns/CFDNS.txt) |
| Google DNS | 1 | [googleDNS.txt](lists/dns/googleDNS.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dns/googleDNS.txt) |

### Dynamic Dns

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| HaGeZi Dynamic DNS | 1,480 | [hagezi_dyndns.txt](lists/dynamic_dns/hagezi_dyndns.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/dynamic_dns/hagezi_dyndns.txt) |

### Gambling

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Betano | 7 | [betano.txt](lists/gambling/betano.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gambling/betano.txt) |
| Betfair | 6 | [betfair.txt](lists/gambling/betfair.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gambling/betfair.txt) |
| Betway | 16 | [betway.txt](lists/gambling/betway.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gambling/betway.txt) |
| Blaze | 4 | [blaze.txt](lists/gambling/blaze.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gambling/blaze.txt) |

### Gaming

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
| PlayStation | 11 | [playstation.txt](lists/gaming/playstation.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/gaming/playstation.txt) |
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

### Hosting

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Box | 4 | [box.txt](lists/hosting/box.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/hosting/box.txt) |
| Dropbox | 22 | [dropbox.txt](lists/hosting/dropbox.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/hosting/dropbox.txt) |
| Flickr | 6 | [flickr.txt](lists/hosting/flickr.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/hosting/flickr.txt) |
| Imgur | 1 | [imgur.txt](lists/hosting/imgur.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/hosting/imgur.txt) |

### Malware

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Ransomware | 1,669 | [blp_ransomware.txt](lists/malware/blp_ransomware.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/malware/blp_ransomware.txt) |
| ThreatFox | 219 | [threatfox.txt](lists/malware/threatfox.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/malware/threatfox.txt) |
| URLhaus | 1,438 | [urlhaus.txt](lists/malware/urlhaus.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/malware/urlhaus.txt) |

### Messenger

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

### Phishing

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| OpenPhish | 220 | [openphish.txt](lists/phishing/openphish.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/phishing/openphish.txt) |
| PhishTank | 18,272 | [phishtank.txt](lists/phishing/phishtank.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/phishing/phishtank.txt) |
| Phishing Army | 283,566 | [phishing_army.txt](lists/phishing/phishing_army.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/phishing/phishing_army.txt) |

### Privacy

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Privacy | 1 | [privacy.txt](lists/privacy/privacy.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/privacy/privacy.txt) |
| Proton | 5 | [proton.txt](lists/privacy/proton.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/privacy/proton.txt) |

### Scam

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Fraud | 114,109 | [blp_fraud.txt](lists/scam/blp_fraud.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/scam/blp_fraud.txt) |
| Block List Project Scam | 726 | [blp_scam.txt](lists/scam/blp_scam.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/scam/blp_scam.txt) |
| HaGeZi Fake | 14,267 | [hagezi_fake.txt](lists/scam/hagezi_fake.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/scam/hagezi_fake.txt) |

### Shopping

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| AliExpress | 4 | [aliexpress.txt](lists/shopping/aliexpress.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/aliexpress.txt) |
| Amazon | 185 | [amazon.txt](lists/shopping/amazon.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/amazon.txt) |
| CoolApk | 3 | [coolapk.txt](lists/shopping/coolapk.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/coolapk.txt) |
| Lazada | 9 | [lazada.txt](lists/shopping/lazada.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/lazada.txt) |
| Mercado Libre | 20 | [mercado_libre.txt](lists/shopping/mercado_libre.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/mercado_libre.txt) |
| Shein | 4 | [shein.txt](lists/shopping/shein.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/shein.txt) |
| Shopee | 20 | [shopee.txt](lists/shopping/shopee.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/shopee.txt) |
| Temu | 3 | [temu.txt](lists/shopping/temu.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/temu.txt) |
| Xiaohongshu | 5 | [xiaohongshu.txt](lists/shopping/xiaohongshu.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/xiaohongshu.txt) |
| eBay | 318 | [ebay.txt](lists/shopping/ebay.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/shopping/ebay.txt) |

### Social Network

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| 4chan | 3 | [4chan.txt](lists/social_network/4chan.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/4chan.txt) |
| 500px | 2 | [500px.txt](lists/social_network/500px.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/500px.txt) |
| 9GAG | 2 | [9gag.txt](lists/social_network/9gag.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/9gag.txt) |
| Amino | 1 | [amino.txt](lists/social_network/amino.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/amino.txt) |
| Bluesky | 2 | [bluesky.txt](lists/social_network/bluesky.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/bluesky.txt) |
| Clubhouse | 2 | [clubhouse.txt](lists/social_network/clubhouse.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/clubhouse.txt) |
| Discord | 27 | [discord.txt](lists/social_network/discord.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/social_network/discord.txt) |
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

### Software

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Google Play Store | 3 | [playstore.txt](lists/software/playstore.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/software/playstore.txt) |
| Nvidia | 10 | [nvidia.txt](lists/software/nvidia.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/software/nvidia.txt) |

### Streaming

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
| YouTube | 174 | [youtube.txt](lists/streaming/youtube.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/youtube.txt) |
| iHeartRadio | 11 | [iheartradio.txt](lists/streaming/iheartradio.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/iheartradio.txt) |
| iQIYI | 8 | [iqiyi.txt](lists/streaming/iqiyi.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/streaming/iqiyi.txt) |

### Tracking

| Source | Root Domains | File | Raw URL |
|--------|---------|------|---------|
| Block List Project Tracking | 14,763 | [blp_tracking.txt](lists/tracking/blp_tracking.txt) | [Raw](https://raw.githubusercontent.com/sparksbenjamin/DNS_Blocking/main/services/lists/tracking/blp_tracking.txt) |

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
- **[The Block List Project](https://github.com/blocklistproject/Lists)** - scam, fraud, ransomware, and tracking feeds
- **[HaGeZi DNS Blocklists](https://github.com/hagezi/dns-blocklists)** - dynamic DNS, badware hoster, and fake-domain feeds
- **[UKLANS cache-domains](https://github.com/uklans/cache-domains)** - gaming CDN/cache hostnames
- **[StevenBlack](https://github.com/StevenBlack/hosts)** and **[Chad Mayfield](https://github.com/chadmayfield/my-pihole-blocklists)** - adult-content feeds

## Notes

- Start with the aggregated categories before stacking many source files
- Whitelist when needed and watch your resolver logs after major changes
- Exact-host security and RPZ layers are more aggressive than the standard services layer
- Source feeds change over time, so entry counts will drift
