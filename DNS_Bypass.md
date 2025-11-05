# Disabling DNS Bypassing

## Purpose
DNS bypassing allows users or applications to circumvent your network’s DNS-based controls by:
- Using custom (external) DNS servers instead of the ones you manage.
- Using encrypted DNS protocols such as DNS over HTTPS (DoH) or DNS over TLS (DoT).
- Leveraging newer transport protocols such as QUIC that can obscure DNS or web traffic.

Preventing DNS bypassing ensures:
- Network and content-filtering rules are applied consistently.
- Threat detection and logging remain accurate and complete.
- Visibility and control over all DNS activity are maintained.

---

## 1. Firewall Rules

### a. Block Outbound DNS
**Why:**  
If devices can send DNS queries directly to external servers, they can easily bypass your internal DNS filtering.

**How:**  
- Block **UDP port 53** and **TCP port 53** for all destinations except your internal DNS servers.
- Example rule:  
  - **Action:** Deny  
  - **Protocol:** UDP/TCP  
  - **Port:** 53  
  - **Destination:** Any (except internal DNS IPs)

This ensures all DNS queries go through your controlled resolver.

---

### b. Block the QUIC Protocol
**Why:**  
QUIC uses UDP (typically port 443) and can bypass traditional filtering or inspection because it encrypts most of its session data. Many browsers (like Google Chrome) use QUIC by default.

**How:**  
- Block or reject **UDP port 443** on your firewall to force browsers and apps back to TCP-based HTTPS connections that your filtering system can inspect.  
- If supported, use **application-aware firewall policies** to block QUIC directly by name.

---

### c. Block DNS over HTTPS (DoH) / DNS over TLS (DoT)
**Why:**  
These protocols encrypt DNS queries, hiding them from your DNS-based monitoring or filtering tools.

**How:**  
- **Block TCP port 853**, which is used by DNS over TLS (DoT).  
- **Block known DoH resolver domains** (such as `dns.google`, `cloudflare-dns.com`, etc.).  
- **Use a DNS blocking list** that includes known DoH endpoints.  
  - This is typically the easiest and most effective approach.
  - Many public lists exist and can be imported into tools like Pi-hole, Unbound, or AdGuard Home.  
- Optionally, enable **deep packet inspection (DPI)** or **application-level blocking** if your firewall supports it.
- Monitor for encrypted DNS traffic on **non-standard ports** that may be used by certain applications.

**Why this works:**  
By blocking known DoH endpoints and DoT ports, you prevent clients from resolving names outside your controlled DNS system while maintaining visibility and control.

---

## 2. NAT Rule – Redirect DNS Traffic

**Purpose:**  
Even with DNS blocking in place, some devices might still try to use external DNS servers. A NAT (Network Address Translation) rule forces all DNS requests back to your internal DNS server.

**How:**  
- Create a **destination NAT (port-forward) rule** that redirects all outbound DNS traffic (UDP/TCP 53) to your internal DNS server.  
- Example:  
  - Any device sending a DNS request → redirected to `192.168.1.10` (your DNS server)  
- Make sure this rule appears **before** any general blocking rule for outbound DNS traffic.  
- Test the setup by manually configuring a device to use a public DNS (like 8.8.8.8) and verifying it still resolves through your internal server.

**Why this works:**  
The NAT redirection captures all DNS queries, ensuring that even manually configured DNS settings cannot bypass your internal resolver.

---

## 3. DHCP DNS Configuration

**Purpose:**  
Automatically assign your internal DNS server to all network clients.

**How:**  
- In your DHCP server (typically your firewall or router), set the **DNS server option** to point to your internal DNS IP.  
- Ensure all connected devices receive this configuration automatically.

**Benefit:**  
- Simplifies client configuration and ensures consistent DNS behavior.
- Prevents users from inadvertently or deliberately using unauthorized DNS servers.

---

## 4. Additional Best Practices

These steps can further strengthen your DNS control and simplify long-term maintenance:

- **Restrict outbound DNS entirely** — only your DNS servers should be allowed to send DNS requests externally.  
- **Monitor and log all DNS queries** — ensure your DNS server keeps logs for visibility and troubleshooting.  
- **Apply filtering and security at your internal DNS server** — use blacklists, threat feeds, or upstream resolvers that block malicious domains.  
- **Educate users** — explain that encrypted DNS is blocked for security and compliance reasons, not to limit privacy.  
- **Test periodically** — try connecting to external DNS servers, using DoH or DoT, and verify that your protections are working.  
- **Review IoT and mobile devices** — some use hardcoded DNS or encrypted channels. Adjust rules or VLAN placement as needed.  
- **Document your DNS policy** — having written procedures helps ensure consistency and quick recovery after maintenance or outages.

---

## Summary

In simple terms:
- All devices on your network should use **your** DNS servers.  
- You should **block or redirect** any other DNS traffic or encrypted DNS protocols.  
- For **DoH**, the most reliable and maintenance-friendly solution is to **use a DNS blocklist** to block known resolver domains.  
- Configure **DHCP** to point devices to your internal DNS automatically.  
- Regularly **monitor, test, and document** your DNS enforcement to maintain visibility and security.

By following these practices, you ensure that your DNS filtering, threat protection, and monitoring remain effective and that no user or application can “escape” your network’s DNS policies.

---
