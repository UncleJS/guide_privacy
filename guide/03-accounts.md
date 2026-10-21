# 03. Accounts

[![CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey)](../LICENSE.md)
[![Online Privacy Guide](https://img.shields.io/badge/guide-online%20privacy-blue)](../README.md)
[![Part 1: everyday](https://img.shields.io/badge/part-1%20everyday-brightgreen)](../README.md#everyday-chapters)
[![Disclaimer](https://img.shields.io/badge/read%20first-disclaimer-red)](disclaimer.md)
![Last reviewed 2026-10-21](https://img.shields.io/badge/last%20reviewed-2026--10--21-informational)

Previous: [Threat models](02-threat-models.md) | [Home](../README.md) | Next: [Email](04-email.md)

---
<a name="toc"></a>

## Table of contents

- [Who this is for](#who-this-is-for)
- [What leaks](#what-leaks)
- [Steps](#steps)
- [What this does not fix](#what-this-does-not-fix)
- [Checklist](#checklist)

## Who this is for

Everyone. Account takeover is the most common serious privacy failure, and the fixes are inexpensive.

[↑ Back to TOC](#toc)

## What leaks

- **Reused passwords.** When one site is breached, attackers try the same email and password everywhere else (credential stuffing).
- **Phishing.** A convincing fake login page captures your password and often your one-time code.
- **Weak recovery.** An attacker who cannot guess your password can often reset it through a recovery email, phone number, or security question.
- **SIM swapping.** Someone persuades your mobile carrier to move your number to their SIM and then receives your SMS codes.

[↑ Back to TOC](#toc)

## Steps

### 1. Use a password manager

**Default:** a reputable password manager that is audited, actively maintained, and supports passkeys. Built-in managers from Apple, Google, or your browser are acceptable and better than reusing passwords. Standalone managers work across more platforms.

- Generate a random password for every account. You do not need to remember them.
- Protect the manager with one long passphrase: four or more random words, not related to you.
- Write the passphrase down once and keep the paper somewhere safe at home until you have memorized it.
- Turn on 2FA for the manager account itself.
- Export an encrypted backup or print the recovery key and store it offline.

### 2. Prefer passkeys where offered

A passkey is a cryptographic credential stored on your device or in your password manager. It cannot be phished through a fake site, and there is no password to steal. Turn it on for your email, your main cloud account, banking, and anything important.

### 3. Add phishing-resistant 2FA

Order of strength, strongest first:

1. **Hardware security key** (FIDO2/WebAuthn). Buy two and register both; keep one in a safe place.
2. **Passkey** on a device you control.
3. **Authenticator app** with time-based codes. Phishable, but far better than nothing.
4. **SMS code.** Use only when nothing else is offered. SIM swapping defeats it.

Start with your primary email account, because it resets everything else.

### 4. Lock down recovery

- Remove recovery phone numbers and emails that you no longer control.
- Replace security questions with random answers stored in your password manager. Real answers are often public.
- Save the one-time backup codes for important accounts in the password manager or on paper.
- Add a PIN or passcode to your mobile carrier account and ask for port-out protection.

### 5. Recognize phishing

- Do not click links in unexpected messages. Open the site or app directly.
- Check that the address matches the real domain exactly.
- Be suspicious of urgency ("your account will be closed").
- A password manager will not auto-fill on a fake domain, which is a useful warning sign.

### 6. Prune accounts

- Delete accounts you no longer use. Each one is a future breach.
- Use "Sign in with" buttons sparingly. They save effort but link your accounts together under one provider.

[↑ Back to TOC](#toc)

## What this does not fix

- A password manager cannot protect you from malware on your device.
- Two-factor authentication does not stop a provider from reading your data.
- Passkeys depend on the account that syncs them. Secure that account first.

[↑ Back to TOC](#toc)

## Checklist

- [ ] Password manager installed, protected by a strong passphrase and 2FA.
- [ ] Unique random password on every important account.
- [ ] Passkeys or hardware keys on email, cloud, banking.
- [ ] Backup codes stored safely.
- [ ] Recovery emails and phone numbers up to date.
- [ ] Carrier PIN and port-out protection set.
- [ ] Unused accounts deleted or scheduled for deletion.

[↑ Back to TOC](#toc)

Previous: [Threat models](02-threat-models.md) | [Home](../README.md) | Next: [Email](04-email.md)

---

© 2026 UncleJS — Licensed under CC BY-NC-SA 4.0
