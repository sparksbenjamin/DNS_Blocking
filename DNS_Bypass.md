# Disabling DNS Bypassing

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
