# 07. Messaging

[![CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey)](../LICENSE.md)
[![Online Privacy Guide](https://img.shields.io/badge/guide-online%20privacy-blue)](../README.md)
[![Part 1: everyday](https://img.shields.io/badge/part-1%20everyday-brightgreen)](../README.md#everyday-chapters)
[![Disclaimer](https://img.shields.io/badge/read%20first-disclaimer-red)](disclaimer.md)
![Last reviewed 2026-10-21](https://img.shields.io/badge/last%20reviewed-2026--10--21-informational)

Previous: [Search, DNS, and network](06-search-dns-network.md) | [Home](../README.md) | Next: [Social media](08-social-media.md)

---
<a name="toc"></a>

## Table of contents

- [Who this is for](#who-this-is-for)
- [What leaks](#what-leaks)
- [Steps](#steps)
- [What this does not fix](#what-this-does-not-fix)
- [Checklist](#checklist)

## Who this is for

Everyone who sends messages. Choose the messenger for private conversations deliberately, because switching later means convincing your contacts too.

[↑ Back to TOC](#toc)

## What leaks

- **Content.** SMS and standard email can be read by carriers and providers. Some apps encrypt content only between you and the company, which means the company can read it.
- **Metadata.** Who talks to whom, when, how often, and from which IP address or phone number. Metadata is revealing even when content is encrypted.
- **Backups.** An end-to-end encrypted chat can be backed up to a cloud service in a form the provider can read.
- **Contacts.** Apps that upload your address book expose the people in it.
- **Notifications and previews.** Message text shown on a lock screen is readable by anyone nearby.

[↑ Back to TOC](#toc)

## Steps

### 1. Use end-to-end encryption by default

End-to-end encryption (E2EE) means only the sender and recipient devices can read the message.

**Default for sensitive conversations:** Signal. It is end-to-end encrypted by default, is open source, collects minimal metadata, and supports disappearing messages. It needs a phone number to register, though you can hide the number from other users with a username.

**Other common options:**

| Service | E2EE | Notes |
|---------|------|-------|
| SMS / RCS (non-E2EE) | No | Readable by carriers. Avoid for sensitive content. |
| iMessage | Yes, between Apple devices | Messages to non-Apple phones fall back to SMS. iCloud backups may not be end-to-end encrypted unless Advanced Data Protection is on. |
| WhatsApp | Yes for content | Owned by a company that collects extensive metadata. Backups are unencrypted unless you enable encrypted backups. |
| Telegram | Only in "secret chats" | Regular chats and all group chats are not end-to-end encrypted. |
| Others (Matrix, Session, Threema, Wire) | Varies | Check whether E2EE is default and what metadata the service holds. |

### 2. Configure the app

- Turn on disappearing messages for sensitive chats. They reduce what is kept on both devices, but a recipient can still copy or screenshot.
- Hide notification content on the lock screen.
- Verify safety numbers or security codes with important contacts, in person or over another channel, if impersonation is a concern.
- Use a screen lock on the app itself where offered.
- Review linked devices regularly and remove those you no longer use.

### 3. Handle backups deliberately

- Know where your chats are backed up and whether the backup is encrypted.
- Enable encrypted backups, or turn backups off for conversations you do not want stored.
- Remember that your contact may back up the conversation even if you do not.

### 4. Control your address book and number

- Deny contact access if you do not need it, or share only selected contacts.
- Use the app's phone-number privacy settings to restrict who can find you.
- For private use, consider a separate number or username. A number that is linked to your name through other services links your accounts together.

### 5. Group chats

- Check who is in the group before posting. Group sizes grow, and the weakest participant sets the group's privacy.
- Prefer smaller groups for sensitive topics.
- Ask before adding someone, and ask before sharing someone else's message.

[↑ Back to TOC](#toc)

## What this does not fix

- E2EE does not protect a conversation from the other person, or from a compromised device.
- A messaging company still knows when your account was created and may know your IP address and contacts.
- A seized or unlocked phone exposes the stored messages ([chapter 19](19-device-seizure.md)).

[↑ Back to TOC](#toc)

## Checklist

- [ ] An E2EE messenger as the default for sensitive chats.
- [ ] Disappearing messages and hidden lock-screen notifications set where useful.
- [ ] Backups understood and encrypted or turned off.
- [ ] Linked devices reviewed.
- [ ] Contacts and phone number visibility reviewed.

[↑ Back to TOC](#toc)

Previous: [Search, DNS, and network](06-search-dns-network.md) | [Home](../README.md) | Next: [Social media](08-social-media.md)

---

© 2026 UncleJS — Licensed under CC BY-NC-SA 4.0
