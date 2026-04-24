# 🛡️ DNS Filters & Blocking Lists
![Auto Update](https://img.shields.io/badge/Update-Automated-success)
![License](https://img.shields.io/github/license/sparksbenjamin/DNS_Blocking)
![Lists](https://img.shields.io/badge/Lists-120+-blue)
![Last Updated](https://img.shields.io/github/last-commit/sparksbenjamin/DNS_Blocking)

Welcome to **DNS Filters & Blocking Lists** — a repo of standard blocklists, exact-host security feeds, and Unbound-ready RPZ outputs.

Our goal is to make DNS filtering **accessible, easy to understand, and ready to deploy** for everyone — whether you’re a home user, network admin, or privacy-focused professional.

---

## 📘 Why Use DNS Filtering?

DNS filtering allows you to block unwanted or harmful content at the network level — preventing devices from resolving specific domains.

✅ Block ads, trackers, and malware  
🚀 Improve network performance  
🧒 Enforce safe browsing policies  
🕵️ Enhance privacy by reducing tracking

---

## 🔒 Worried About DNS Bypassing?

You can enforce strict DNS routing and block or redirect outbound DNS-over-HTTPS (DoH), DNS-over-TLS (DoT), and QUIC traffic.

➡️ [Learn how to prevent DNS bypassing](DNS_Bypass.md)

---

## 🗂️ What’s Included

This repository provides **curated and enriched DNS blocking outputs** across multiple categories and delivery formats.  
Lists are **automatically updated on a schedule** and validated for syntax, policy drift, and source health.

### 📂 Services
#### [Online Services](services/README.md)
Home-safe, Pi-hole and AdGuard-friendly blocklists using registrable domains by default.

### 🛡️ [Security](security/README.md)
Exact-host security feeds for phishing, malware, scams, dynamic DNS, and badware hosters.

### 🧱 [RPZ](rpz/README.md)
Resolver-native RPZ zone files for Unbound and other policy-zone capable DNS servers.

### 🛡️ [Hardening](hardening/README.md)
Optional DNSTwist-based lookalike and brand-impersonation lists for higher-sensitivity blocking, plus an opt-in active impersonation review stage.

### 🌐 [Tunneling](tunneling/README.md)
Lists VPN and proxy providers that can be blocked or restricted.

- [VPNs](tunneling/vpns.txt)  
- [Proxies](tunneling/proxies.txt)

## ⚙️ How to Use

Pick the output tier that matches how aggressive you want the blocking to be:

- `services/` for standard DNS blocking
- `security/` for exact-host security feeds
- `rpz/` for Unbound-native policy zones
- `hardening/` for DNSTwist-based brand impersonation blocking and live-lookalike review

You can import the `.txt` lists directly into Pi-hole or AdGuard Home, and the `.rpz` files into Unbound or another RPZ-capable resolver.

### Pi-hole
### Ad-Guard
### Group-policy


## ⭐ If this project helps you, please star the repo!
