# 06. Search, DNS, and network

Previous: [Browsers](05-browsers.md) | [Home](../README.md) | Next: [Messaging](07-messaging.md)

## Who this is for

Everyone. Your internet provider, the Wi-Fi network owner, and search engines each see parts of your activity.

## What leaks

- **Search queries.** Search engines keep what you type, often tied to an account, cookie, or IP address. Queries reveal health, finances, relationships, and plans.
- **DNS lookups.** Before connecting to a site, your device asks a DNS resolver for its address. That resolver, usually your internet provider's, sees the names of the sites you visit.
- **Connection metadata.** Even over HTTPS, your provider sees the destination server's address and the volume and timing of traffic. It does not see page content.
- **Public Wi-Fi.** The operator can see connection metadata, and a malicious network can try to redirect you to fake pages. HTTPS limits the damage.

## Steps

### 1. Choose a search engine on purpose

**Default:** a search engine that does not tie queries to a profile, or one you use only while signed out. Privacy-focused engines reduce profiling but may give less relevant results for niche queries. Whichever you choose:

- Sign out of your search provider's account while searching, or use a browser profile that is not signed in.
- Turn off search history and ad personalization in the account's privacy dashboard.
- Avoid putting sensitive details (names, addresses, medical conditions) into any search box when a general query will do.

### 2. Encrypt DNS

- Enable "DNS over HTTPS" or "DNS over TLS" in your browser or operating system.
- Pick a resolver with a public privacy policy. A trusted resolver sees your lookups instead of your internet provider, so you are choosing whom to trust, not removing trust.
- Encrypted DNS hides lookups from the local network but not the destination address, which the provider can still see.

### 3. Secure your home Wi-Fi

- Use WPA3 if your devices support it, otherwise WPA2 with a long random passphrase.
- Change the router's default administrator password and Wi-Fi name.
- Turn off remote administration and WPS.
- Install router updates, or replace a router that no longer receives them.
- Use a guest network for visitors and smart-home devices ([chapter 13](13-home-and-devices.md)).

### 4. Use public Wi-Fi carefully

- Prefer your mobile data connection for sensitive tasks.
- Check that sites use HTTPS. Browsers show a warning on invalid certificates; do not click through it.
- Turn off automatic connection to open networks.
- Do not enter passwords on a captive portal page you do not recognize.

### 5. Understand what a VPN does

A VPN sends your traffic through an encrypted tunnel to a server run by the VPN company.

**What it does:**
- Hides your traffic from the local network, such as café Wi-Fi.
- Hides the sites you visit from your internet provider.
- Shows websites the VPN server's IP address instead of yours.

**What it does not do:**
- It does not make you anonymous. The VPN company sees what your provider would have seen.
- It does not stop cookies, fingerprinting, or sign-in tracking.
- It does not protect you from malware or phishing.
- It does not make a poorly encrypted site safe.

**If you use one:** choose a provider with a clear no-logs policy backed by independent audits, avoid free VPNs that earn money from your data, and prefer a provider that you can pay for without linking it to your identity if that matters to you. A VPN is a network-privacy tool; treat it that way.

## What this does not fix

- Search engines, DNS resolvers, and VPN providers each see something. You choose who sees it; you do not remove the viewer.
- None of these steps hide your activity from sites you sign in to.

## Checklist

- [ ] Search engine chosen; search history and ad personalization off.
- [ ] Encrypted DNS enabled.
- [ ] Router uses WPA2/WPA3, has a changed admin password, and gets updates.
- [ ] I avoid sensitive tasks on public Wi-Fi.
- [ ] If I use a VPN, I know what it hides and what it does not.

---

Previous: [Browsers](05-browsers.md) | [Home](../README.md) | Next: [Messaging](07-messaging.md)
