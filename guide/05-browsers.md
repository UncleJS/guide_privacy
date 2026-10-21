# 05. Browsers

Previous: [Email](04-email.md) | [Home](../README.md) | Next: [Search, DNS, and network](06-search-dns-network.md)

## Who this is for

Everyone. The browser is where most tracking happens, and a few settings remove a large share of it.

## What leaks

- **Third-party cookies and trackers.** Ad networks and analytics scripts embedded in many sites recognize you as you move between them.
- **Fingerprinting.** Sites combine your browser version, screen size, fonts, language, graphics hardware, and time zone to build an identifier that survives cookie deletion.
- **IP address.** Every site sees it. It reveals approximate location and your internet provider.
- **Sign-in state.** Being signed in to a large account while you browse lets that company connect the sites you visit to your identity.
- **Extensions.** An extension can read every page you visit.

## Steps

### 1. Pick a mainstream browser with strong default protections

**Default:** a current, regularly updated browser that blocks third-party tracking by default and updates automatically. Firefox and Brave block more by default; Safari offers intelligent tracking prevention; Chrome and Edge offer controls but require more configuration and are run by advertising-funded companies. Regardless of the choice:

- Turn on automatic updates and restart when prompted. Browser flaws are among the most exploited.
- Do not use a niche browser that lags behind security updates.

### 2. Adjust the key settings

- Block third-party cookies.
- Enable "enhanced tracking protection" or the equivalent.
- Turn on HTTPS-only mode so the browser refuses unencrypted connections.
- Turn off sending usage data, personalized ads, and "help improve" telemetry if you are comfortable doing so.
- Clear cookies and site data on exit for sites you do not use regularly, or use separate browser profiles.
- Turn off the built-in password manager only if you use a dedicated one ([chapter 03](03-accounts.md)); do not run both.

### 3. Keep extensions to a minimum

- Install a well-known content blocker, such as uBlock Origin where supported. It blocks ads and many trackers.
- Add extensions only when you can name the benefit. Each is an additional program with access to your pages.
- Check the developer, the update history, and the number of users. Remove extensions you no longer use.
- Be skeptical of extensions that promise to "protect your privacy" and ask for access to all sites. An unusual extension set can make your browser more distinctive.

### 4. Use profiles and containers

- Keep one profile for sign-in to large accounts (email, cloud, social) and another for general browsing. Companies cannot connect your browsing to your account if you are not signed in.
- In Firefox, container extensions keep sites isolated.
- Use a separate profile for work and personal life.

### 5. Understand private browsing

Private or incognito mode:

- Prevents the browser from saving history, cookies, and form data locally after the window closes.
- Does **not** hide your IP address, your activity from websites, your employer or school network, or your internet provider.
- Does **not** protect you from tracking within the session.

It is useful for avoiding traces on a shared device. It is not a privacy tool for the network.

### 6. Reduce fingerprinting

- Use the browser's fingerprinting protection if available.
- Keep the window at its default size. Resizing or maximizing changes your fingerprint.
- Avoid adding many extensions or custom fonts.
- Accept that complete resistance is hard; the Tor Browser is the strongest option, with trade-offs ([chapter 21](21-anonymity-tools.md)).

## What this does not fix

- A browser cannot hide your IP address from the sites you visit. See [chapter 06](06-search-dns-network.md).
- Blocking trackers does not stop a site you are signed in to from recording what you do on it.
- Malware on your device defeats browser protections.

## Checklist

- [ ] Browser updates automatically.
- [ ] Third-party cookies blocked, tracking protection on, HTTPS-only mode on.
- [ ] A content blocker installed; unused extensions removed.
- [ ] Separate profiles for account sign-in and general browsing.
- [ ] I know what private browsing does not protect.

---

Previous: [Email](04-email.md) | [Home](../README.md) | Next: [Search, DNS, and network](06-search-dns-network.md)
