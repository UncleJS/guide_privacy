# 02. Threat models

[![CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey)](../LICENSE.md)
[![Online Privacy Guide](https://img.shields.io/badge/guide-online%20privacy-blue)](../README.md)
[![Foundations](https://img.shields.io/badge/part-foundations-blue)](../README.md#everyday-chapters)
[![Disclaimer](https://img.shields.io/badge/read%20first-disclaimer-red)](disclaimer.md)
![Last reviewed 2026-10-21](https://img.shields.io/badge/last%20reviewed-2026--10--21-informational)

Previous: [Privacy, security, anonymity](01-privacy-security-anonymity.md) | [Home](../README.md) | Next: [Accounts](03-accounts.md)

---
<a name="toc"></a>

## Table of contents

- [Who this is for](#who-this-is-for)
- [The five questions](#the-five-questions)
- [Common adversaries](#common-adversaries)
- [Risk levels](#risk-levels)
- [Write yours down](#write-yours-down)
- [What this does not fix](#what-this-does-not-fix)
- [Checklist](#checklist)

## Who this is for

Everyone, before buying or installing anything. A threat model is a short written answer to five questions. It keeps your effort aimed at risks you actually face.

[↑ Back to TOC](#toc)

## The five questions

1. **What am I protecting?** Messages, location, identity, finances, photos, health information, a relationship, a job.
2. **Who might want it?** See the adversary list below.
3. **How likely is that, and how bad would it be?** Rare but severe risks and common but mild ones need different responses.
4. **How hard will it be to protect against?** Include inconvenience. A measure you abandon protects nothing.
5. **What am I willing to give up?** Convenience, money, time, sharing with friends.

[↑ Back to TOC](#toc)

## Common adversaries

| Adversary | What they want | Typical capability | Where to look |
|-----------|----------------|--------------------|---------------|
| **Advertisers and data brokers** | Profiles to sell or target ads | Trackers, apps, purchased data | Chapters 05, 06, 08, 09, 15 |
| **Platforms and service providers** | Data to run and monetize the service | Everything you do on their service | Chapters 04, 07, 08, 11 |
| **Criminals** | Money, accounts, identity | Phishing, credential stuffing, SIM swapping, malware | Chapters 03, 16 |
| **Thieves and finders** | Hardware, and any data on it | Physical access to a lost or stolen device | Chapters 09, 10 |
| **People you know** | Access to your accounts, devices, or location | Physical access, shared passwords, shared accounts | Chapters 09, 10, 14 |
| **Employers and schools** | Monitoring of work or school activity | Managed devices and accounts | Chapter 10 |
| **Governments and law enforcement** | Evidence or intelligence | Legal process, device seizure, network surveillance, malware (for a small number of targets) | Chapters 17 to 23 |
| **Harassers and stalkers** | Your location, identity, or distress | Public records, social media, doxxing | Chapters 08, 15, 18 |

[↑ Back to TOC](#toc)

## Risk levels

Pick the level that best fits today. Levels are cumulative: each one includes everything in the levels below it. You can move between levels as your situation changes, and you can sit at different levels for different parts of your life (for example, level 2 for shopping and level 4 for a sensitive project).

### Overview

| Level | Name | Who is trying to get at you | Typical person | Where to start |
|-------|------|-----------------------------|----------------|----------------|
| 0 | Unprepared | Anyone, and nothing stops them | Default settings, reused passwords, no updates | Chapters 03 and 10 first |
| 1 | Baseline | Opportunistic criminals, scams, trackers | Most people who do the basics | Chapters 03 to 10 |
| 2 | Careful | Data brokers, advertisers, thieves who take a device | People who want less exposure and protection if a laptop or phone is lost | Chapters 03 to 16 |
| 3 | Elevated | One person or group with some access or motive | Someone with a controlling ex-partner, a monitoring employer, or a persistent harasser | Chapters 03 to 16, then 17 and 18 |
| 4 | High | Organized, patient adversaries who target you by name | Journalists, lawyers, activists, executives, security researchers, people leaving dangerous situations | All of Part 1, then Part 2 |
| 5 | Severe | Well-resourced adversaries with legal power or advanced tools | People in conflict zones, under authoritarian governments, or targeted by organized crime | Part 1 and Part 2, plus expert help |
| 6 | Extreme | Nation-state level, with custom exploits and physical access | A very small number of people | Expert help; this guide is a starting point only |

### What each level means

**Level 0: Unprepared.** Default settings, reused passwords, outdated software, unencrypted devices. Anyone with a leaked password list, a stolen laptop, or a convincing phishing message can get in. Most people start here. Fix it with the account and computer basics ([chapter 03](03-accounts.md), [chapter 10](10-computers.md)).

**Level 1: Baseline.** You block the common, automated attacks. Unique passwords in a password manager, 2FA, automatic updates, disk encryption turned on, a firewall, and a browser that blocks trackers. This stops most scams and breaches from becoming disasters.

**Level 2: Careful.** You also reduce the data that leaks by design and limit the damage from losing a device. You review app permissions, use aliases, opt out of data brokers, keep encrypted backups, use a standard (non-administrator) account day to day, and set a firmware or boot password where the machine supports it. A stolen, powered-off laptop reveals nothing.

**Level 3: Elevated.** Someone you know, an employer, or a persistent harasser may try to learn about you. You are not a target of a state, but a single person with some access is a real concern. You assume that someone may have had physical access to a device, so you distrust old devices and shared accounts. You use separate devices or accounts for sensitive activity, hardware security keys on your key accounts, and you check for monitoring software ([chapter 14](14-households.md), [chapter 23](23-if-compromised.md)). Read [chapter 17](17-targeted-threats.md) and [chapter 18](18-compartments.md).

**Level 4: High.** Someone competent will spend time targeting you specifically with tailored phishing, impersonation, legal pressure, or surveillance of your contacts. You work from a threat model written for a named adversary. You use hardware keys everywhere, compartmentalized identities and devices, a dedicated clean computer for sensitive work, locked-down boot settings, encrypted storage that stays closed when not in use, and a plan for device seizure and travel ([chapters 17 to 22](17-targeted-threats.md)). You have a helpline and a lawyer you can reach.

**Level 5: Severe.** The adversary can use legal process, network-level surveillance, or advanced tools, and mistakes can be costly. You use tightly controlled devices that only run what you need, purpose-built operating systems, isolated virtual machines or separate hardware for each role, verified downloads, firmware protections, and strict operational habits. Technical measures are only part of it: you need ongoing guidance from an organization or a specialist, because the situation changes and a single mistake can matter ([further reading](further-reading.md)).

**Level 6: Extreme.** The adversary can buy or build custom exploits, intercept supply chains, and has physical access. No individual can reliably stop this with consumer tools. If you believe you are here, the most important step is to talk to a specialist before relying on any advice in this guide, because some choices that help at lower levels (such as carrying a device you cannot replace) can hurt at this one. Use this guide to raise the cost of attack and to avoid easy mistakes, and treat devices that may have been exposed as compromised.

### Computer security by level

Computers are the single most valuable target, because they hold your data and the keys to your accounts. This table summarizes the computer measures that [chapter 10](10-computers.md) explains in detail.

| Level | Disk encryption | Sign-in and accounts | Updates and software | Boot and firmware | Backups and physical |
|-------|-----------------|----------------------|----------------------|-------------------|----------------------|
| 0 | Off | Shared or no password, always administrator | Ignored | Defaults | None |
| 1 | On, recovery key saved safely | Strong login password, auto-lock | Automatic updates, official sources only | Defaults | One encrypted backup |
| 2 | On, with a strong passphrase; shut down (not just sleep) when traveling | Standard account for daily use, separate admin account, password manager | Remove unused software, built-in firewall on | Firmware password or setup password where available; Secure Boot on | 3-2-1 backups, one offline |
| 3 | On, recovery key not stored in the same cloud account as the sign-in | Separate account or device for sensitive work, hardware key for login where supported | Check for unfamiliar software, profiles, and remote-access tools; reinstall if in doubt | Secure Boot with a firmware password; disable unneeded boot options | Physical lock or tamper-evident storage; trusted repair only |
| 4 | On, with a long passphrase and a pre-boot unlock; no biometrics for the disk | Dedicated clean computer for sensitive work, hardware keys everywhere | Minimal, verified software; managed update cadence | Measured or verified boot, firmware updates from the vendor, disabled external boot | Tamper-evident seals, separate travel computer, encrypted volumes for sensitive files |
| 5 | On, with a strong passphrase and a separate hidden or removable key where law allows | Separate machines or isolated virtual machines for each role, no shared accounts | Hardened, security-focused OS; verified downloads; strict allowlist | Verified boot with your own keys where practical; firmware protections | Assume loss; no sensitive data left unattended; supply-chain care when buying |
| 6 | Not enough alone | Expert-designed | Expert-designed | Expert-designed | Expert-designed |

[↑ Back to TOC](#toc)

## Write yours down

A model can be short:

> I protect my email, photos, and location history. The main risks are criminals and advertisers. My ex-partner knew my old passwords. I will accept some inconvenience for login security but not for messaging.

Revisit it when your life changes: a new job, a move, a breakup, public attention, or travel.

[↑ Back to TOC](#toc)

## What this does not fix

A threat model does not reduce risk by itself. It directs your effort, and it is imperfect: you will miss some risks. Revisit it after any incident.

[↑ Back to TOC](#toc)

## Checklist

- [ ] I wrote a short threat model in my own words.
- [ ] I chose a risk level (0 to 6) for each part of my life that matters.
- [ ] I know what my computer should look like at that level.
- [ ] I know which chapters apply to that level.
- [ ] I have a date to review the model again.

[↑ Back to TOC](#toc)

Previous: [Privacy, security, anonymity](01-privacy-security-anonymity.md) | [Home](../README.md) | Next: [Accounts](03-accounts.md)

---

© 2026 UncleJS — Licensed under CC BY-NC-SA 4.0
