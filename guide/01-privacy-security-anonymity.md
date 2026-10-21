# 01. Privacy, security, and anonymity

Previous: [How to read](00-how-to-read.md) | [Home](../README.md) | Next: [Threat models](02-threat-models.md)

## Who this is for

Everyone. Choosing tools without knowing which goal you are pursuing leads to wasted effort and false confidence.

## Three different goals

| Goal | Question it answers | Example |
|------|---------------------|---------|
| **Security** | Can someone who should not get in, get in? | A strong, unique password and phishing-resistant 2FA keep an attacker out of your email. |
| **Privacy** | Who is allowed to see or collect what I do, and what can they do with it? | Turning off ad personalization limits what an advertising network learns about you. |
| **Anonymity** | Can my actions be linked to my real identity? | Posting under a pseudonym that no one can connect to you. |

They overlap but are not the same. A few examples of where they diverge:

- **Encrypted but not private.** A messaging app can encrypt the content of your messages and still show the company who you talk to, when, and from which IP address.
- **Secure but not anonymous.** Your bank account can be well protected against takeover and still reveal everything you buy to the bank.
- **Private but not secure.** A privacy-friendly service with a weak password protects nothing if someone guesses the password.
- **Anonymous but not private.** An anonymous account can still be profiled by the platform it posts on.

## What leaks

Information leaks through four broad channels:

1. **What you hand over:** names, emails, phone numbers, photos, payment details, anything you type into a form.
2. **What your devices reveal:** IP address, device model, installed fonts, location, app usage.
3. **What your behavior reveals:** browsing, purchases, search terms, the times you are active.
4. **What other people reveal about you:** contacts uploaded from friends' phones, photos you appear in, shared family accounts.

Most of this guide is about reducing channels 1 to 3 and being aware of channel 4.

## Steps

1. For each tool or habit you consider, ask which of the three goals it serves.
2. Name the party you are protecting against (see [chapter 02](02-threat-models.md)).
3. Prefer measures that serve more than one goal at low cost, such as a password manager (security and privacy) or keeping apps updated (security).

## What this does not fix

Naming the goals does not protect you by itself. It prevents the common mistake of treating a VPN, private browsing window, or "encrypted" label as a cure for a problem it does not address.

## Checklist

- [ ] I can state in one sentence whether I mostly want security, privacy, or anonymity.
- [ ] I know that encryption of content is not the same as hiding who I talk to.
- [ ] I will not rely on a single tool to cover all three goals.

---

Previous: [How to read](00-how-to-read.md) | [Home](../README.md) | Next: [Threat models](02-threat-models.md)
