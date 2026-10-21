# 21. Anonymity tools

[![CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey)](../LICENSE.md)
[![Online Privacy Guide](https://img.shields.io/badge/guide-online%20privacy-blue)](../README.md)
[![Part 2: higher-risk](https://img.shields.io/badge/part-2%20higher--risk-orange)](../README.md#higher-risk-chapters)
[![Disclaimer](https://img.shields.io/badge/read%20first-disclaimer-red)](disclaimer.md)
![Last reviewed 2026-10-21](https://img.shields.io/badge/last%20reviewed-2026--10--21-informational)

Previous: [Metadata](20-metadata.md) | [Home](../README.md) | Next: [Travel and public space](22-travel-and-public-space.md)

---
<a name="toc"></a>

## Table of contents

- [Who this is for](#who-this-is-for)
- [What leaks](#what-leaks)
- [How the tools differ](#how-the-tools-differ)
- [The mistakes that undo anonymity](#the-mistakes-that-undo-anonymity)
- [Steps](#steps)
- [What this does not fix](#what-this-does-not-fix)
- [Checklist](#checklist)

## Who this is for

People who need to hide their network location, or who need to read or publish without the destination, or a local observer, learning who they are. This chapter explains what Tor and VPNs protect, what they do not, and the mistakes that most often undo them. It does not cover ways to attack other people's systems or evade law enforcement in the course of a crime.

[↑ Back to TOC](#toc)

## What leaks

Your IP address ties your activity to a household or device. Website operators, network observers, and providers can see it. An anonymity tool changes who sees what, but the identifying details you reveal inside the connection (accounts, names, habits) are unaffected.

[↑ Back to TOC](#toc)

## How the tools differ

| | VPN | Tor |
|---|---|---|
| **How it works** | One encrypted tunnel to a provider's server | Traffic relayed through three volunteer-run nodes |
| **Who sees your real IP** | The VPN provider | The first relay (a guard), not the destination |
| **Who sees your destination** | The VPN provider | The last relay (exit) sees the destination, but not who you are |
| **Trust required** | Full trust in one company | Trust that no one controls or observes enough of the network |
| **Speed** | Fast | Slower |
| **Typical use** | Hide traffic from local networks and your internet provider | Browse or publish with a reduced link to your identity |
| **Weak spot** | The provider's logs and legal obligations | Traffic correlation, user mistakes, browser fingerprinting |

### VPNs

A VPN is a trust transfer: your provider stops seeing your traffic, and the VPN company sees it. Use one for protection on untrusted Wi-Fi or to avoid your provider's logging, with the limits in [chapter 06](06-search-dns-network.md). A VPN is not an anonymity tool for dealing with an adversary who can compel the VPN company, who can monitor both ends of the connection, or who can identify you through your accounts.

### Tor

Tor (The Onion Router) is designed to separate who you are from what you do online. The Tor Browser sends traffic through the Tor network and makes all users look alike to reduce fingerprinting.

Tor protects best when you:

- Use the official Tor Browser, kept up to date, and nothing else, for that activity.
- Leave the default window size and settings, and do not install extra extensions.
- Do not sign in to accounts that identify you.
- Do not download and open files while online. Documents can load content that reveals your IP address.
- Use HTTPS sites. The exit relay can read unencrypted traffic.
- Use bridges if Tor is blocked or if using Tor itself is risky or unusual where you are.

Onion services (.onion addresses) provide end-to-end protection inside the Tor network for both the visitor and the site.

[↑ Back to TOC](#toc)

## The mistakes that undo anonymity

- **Signing in** to a personal account, even once.
- **Using the same identity** inside and outside Tor, or the same handle across identities.
- **Mixing activity,** such as using Tor and a regular browser in the same session or on the same network at times that match a real-world event.
- **Revealing identifying details** in what you write, such as place names, schedules, work, or distinctive phrases.
- **Opening documents or links** outside the Tor Browser.
- **Altering Tor Browser** with extensions, and shrinking or maximizing the window.
- **Traffic correlation.** An observer who sees both your connection into Tor and the destination can match timing and volume. This is hard to prevent and is why high-risk users also separate devices and networks.
- **Metadata in files** you upload.
- **Being known to use Tor.** Your internet provider sees that you connect to the Tor network, though not what you do. In some places that alone draws attention; bridges can help.
- **Compromised device.** If the device has spyware, no network tool helps.

[↑ Back to TOC](#toc)

## Steps

1. **Decide what you need to hide:** your location from a site, the sites from your provider, your identity from a platform, or all of these. The answer determines the tool.
2. **Choose the tool:** a VPN for local network and provider privacy; Tor for reducing the link between you and your destination.
3. **Install from the official source.** Verify the download as the Tor Project instructs.
4. **Keep it updated,** and restart when prompted.
5. **Use it with discipline,** following the rules above, with a separate identity for the activity ([chapter 18](18-compartments.md)).
6. **Consider a dedicated device or a live operating system** designed for this purpose if your risk is high. Understand the setup and its limits first; mistakes are common.
7. **Combine with care.** Using a VPN with Tor adds complexity and can reduce protection if done wrongly. Follow the Tor Project's guidance.
8. **Check where you stand.** Test your setup with the Tor Project's check page and review what the sites you use can see.

[↑ Back to TOC](#toc)

## What this does not fix

- Tor and VPNs do not protect an identity that you reveal yourself.
- They do not protect content that is not encrypted end to end.
- They do not make you immune to a global observer who can correlate traffic.
- They do not protect against malware on your device.

[↑ Back to TOC](#toc)

## Checklist

- [ ] I know what I need to hide, and from whom.
- [ ] I chose the appropriate tool and installed it from the official source.
- [ ] I keep identities separate and never sign in to personal accounts through it.
- [ ] I do not open downloaded files outside a safe environment.
- [ ] I know the risks of being seen to use the tool where I am.

[↑ Back to TOC](#toc)

Previous: [Metadata](20-metadata.md) | [Home](../README.md) | Next: [Travel and public space](22-travel-and-public-space.md)

---

© 2026 UncleJS — Licensed under CC BY-NC-SA 4.0
