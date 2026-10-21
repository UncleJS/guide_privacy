# 04. Email

Previous: [Accounts](03-accounts.md) | [Home](../README.md) | Next: [Browsers](05-browsers.md)

## Who this is for

Everyone. Email is the master key for password resets, so it is both your most important account and a rich source of data about you.

## What leaks

- **Content.** Standard email is readable by your provider and often by the provider of the person you write to. It travels between servers in a form the servers can read, even when the connection is encrypted in transit.
- **Metadata.** Sender, recipient, subject, time, and size are visible to providers and anyone with access to them.
- **Tracking pixels.** Marketing emails embed tiny images that report when you opened the message, your IP address, and your device.
- **Linkage.** Using one address for every sign-up lets companies and data brokers join your profiles.
- **Receipts and subscriptions.** Your inbox is a detailed record of your purchases, travel, health, and finances.

## Steps

### 1. Choose a primary inbox on purpose

**Default:** a reputable provider that you pay for or whose business model does not depend on scanning your mail, offers strong account security (passkeys or hardware keys), and lets you export your data. Large free providers have strong security teams, which protects against criminals, but their business model includes data about you. Choose based on your threat model ([chapter 02](02-threat-models.md)).

- A custom domain gives you portability: you can move providers without changing your address.
- Keep one long-lived address for banking and government, and do not use it for casual sign-ups.

### 2. Use aliases for sign-ups

An alias is a separate address that forwards to your inbox. Many providers offer them, and so do standalone alias services.

- Create a distinct alias for each category (shopping, newsletters, forums) or for each site.
- If one alias starts to receive spam or appears in a breach, delete it. You learn which company leaked or sold it.
- Use aliases for your most sensitive services only if you can still receive password resets. Test that before relying on it.

### 3. Block tracking

- Turn off automatic image loading in your mail client or load remote images only on request.
- Use your provider's tracker-blocking feature if it has one.
- Unsubscribe from marketing mail you do not read. Use only the unsubscribe link in mail you actually signed up for; for unknown senders, mark as spam instead.

### 4. Harden the account

Follow [chapter 03](03-accounts.md): passkey or hardware key, no SMS recovery, and a reviewed list of recovery addresses. Also:

- Review connected apps and delete the ones you no longer use.
- Review forwarding rules and filters. Attackers who gain access often add a hidden forward.
- Review which devices are signed in and sign out the unknown ones.

### 5. Encrypt when content matters

End-to-end encrypted email works best when both sides use the same encrypted provider. For other cases:

- Send sensitive attachments through an end-to-end encrypted file-sharing service or a messaging app ([chapter 07](07-messaging.md)).
- OpenPGP works but is difficult to use safely. Consider it only if the recipient already uses it.

## What this does not fix

- Aliases hide your main address, not your identity. The destination service still sees your name, IP address, and behavior.
- Encrypted providers protect message content. They do not hide the fact that you sent mail, and metadata such as recipients and subject lines may still be visible, depending on the provider.
- Your recipients can forward, screenshot, or store what you send.

## Checklist

- [ ] Primary inbox chosen deliberately, with strong sign-in protection.
- [ ] Aliases used for sign-ups and newsletters.
- [ ] Remote images blocked by default.
- [ ] Forwarding rules, connected apps, and signed-in devices reviewed.
- [ ] A plan for sending sensitive content outside normal email.

---

Previous: [Accounts](03-accounts.md) | [Home](../README.md) | Next: [Browsers](05-browsers.md)
