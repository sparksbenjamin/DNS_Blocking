# DNS Filters & Blocking Lists
![Auto Update](https://img.shields.io/badge/Update-Automated-success)
![License](https://img.shields.io/github/license/sparksbenjamin/DNS_Blocking)
![Lists](https://img.shields.io/badge/Lists-120+-blue)
![Last Updated](https://img.shields.io/github/last-commit/sparksbenjamin/DNS_Blocking)

Welcome to **DNS Filters & Blocking Lists** – your one-stop repository for comprehensive DNS filtering solutions. Our goal is to make DNS filtering **accessible, easy to understand, and ready-to-use** for everyone, whether you're a home user, network admin, or privacy-conscious professional.

---

## 📌 Why Use DNS Filtering?

DNS filtering allows you to block unwanted content at the network level by preventing your devices from resolving certain domains. This approach helps you:

- **Block ads, trackers, and malware** automatically.
- **Improve network performance** by reducing unwanted traffic.
- **Enforce safe browsing** for children or employees.
- **Enhance privacy** by reducing exposure to tracking domains.

---
# Disabling DNS Bypassing – Notes

## Purpose
DNS bypassing allows users or applications to circumvent network restrictions by using custom DNS servers, encrypted DNS (DoH/DoT), or tunneling methods. Disabling DNS bypassing helps ensure:  

- Consistent application of network security policies.  
- Proper content filtering and threat prevention.  
- Monitoring and control of all DNS traffic within your network.  

---

## 1. Firewall Rules

### a. Block Outbound DNS
- **Why:** Prevents clients from using external DNS servers instead of your controlled DNS.  
- **How:** Block **UDP/TCP port 53** for all outbound traffic that is not going to your DNS server.  

**Example Rule:**  
Deny UDP/TCP 53 to any external IP except your DNS server
### b. Block Quick UDP Internet Connections (QUIC)
- **Why:** QUIC (used by modern browsers like Chrome) can bypass traditional filtering.  
- **How:** Block **UDP port 443** for QUIC traffic or inspect traffic at firewall/application layer.  

### c. Block DNS over HTTPS (DoH) / DNS over TLS (DoT)
- **Why:** Encrypted DNS bypasses normal DNS monitoring.  
- **How:**  
  - Block TCP port **853** (DoT).  
  - Block HTTPS DoH endpoints (can be domain-based, e.g., `cloudflare-dns.com`).  
  - Optionally use firewall DPI (Deep Packet Inspection) to detect DoH traffic.  

---

## 2. NAT Rule – Redirect DNS Traffic
- **Purpose:** Ensure all DNS queries go through your DNS server even if a client tries to use another server.  
- **How:**  
  - Create a NAT rule on your firewall/router to redirect all **port 53 traffic** to your internal DNS server.  
  - This guarantees that external DNS servers cannot be used.  

**Example:**  
Any outbound DNS request -> NAT redirect -> Internal DNS Server

---

## 3. DHCP DNS Configuration
- **Purpose:** Automatically configure client devices to use your internal DNS server.  
- **How:**  
  - Set your DNS server as the **default DNS** in your DHCP settings.  
  - All devices that connect will receive the correct DNS automatically.  

**Benefit:** Even devices without manual configuration are forced to use your DNS, reducing bypass attempts.  

---
## 🗂 What’s Included

This repository provides curated DNS blocklists for different categories:


### 📂 Services

| Category | Description | Link |
|-----------|--------------|------|
| **Services** | Blocks known services. | [View list](services/README.md) |
| **Tunneling** | Blocks known Proxy and VPN providers. | [View list](tunneling/README.md) |
