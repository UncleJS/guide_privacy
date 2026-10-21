# 16. Account takeover

Previous: [Data brokers and breaches](15-data-brokers-and-breaches.md) | [Home](../README.md) | Next: [Targeted threats](17-targeted-threats.md)

## Who this is for

Anyone who suspects that someone else has signed in to one of their accounts, or who has lost access to an account. This is the most common serious incident for individuals. If you suspect something more persistent, such as spyware or a person with ongoing access to your devices, read [chapter 23](23-if-compromised.md) as well.

## Signs of a takeover

- Password reset or sign-in alerts you did not request.
- Messages, posts, or purchases you did not make.
- Unknown devices or locations in your account's security page.
- Changed recovery email, phone number, or 2FA settings.
- Forwarding rules or filters you did not create (email).
- Friends report strange messages from you.
- You are suddenly locked out.

## Steps

### 1. Work from a clean device

If you think your computer or phone may be infected, start from a different device that you trust. Changing a password on a compromised device hands the new one to the attacker.

### 2. Regain control

1. Open the provider's official recovery page by typing the address, not from a link in a message.
2. Reset the password. Use a new random password from your password manager.
3. Sign out of all other sessions and devices.
4. Revoke app and token access you do not recognize.
5. Remove unknown 2FA methods, recovery emails, and phone numbers. Turn on a strong 2FA method ([chapter 03](03-accounts.md)).
6. Check email forwarding rules, filters, delegated access, and auto-replies.
7. Check payment methods, shipping addresses, and subscriptions.

If you are locked out, use the provider's account recovery process, and keep proof of ownership ready: previous passwords, devices you used, and dates. Be patient; recovery can take days.

### 3. Work out the blast radius

- Start with your **primary email**. If it was taken over, any account that uses it for resets is at risk. Secure it first.
- Change passwords on accounts that share the same or similar password.
- Check accounts the attacker could reach through the compromised one: cloud storage, banking, social media, shopping.
- Check whether the compromised account held saved card details or identity documents.

### 4. Tell the right people

- Warn your contacts that messages from the account may be fraudulent, using another channel.
- Report to the provider. Many have an "account compromised" flow.
- Contact your bank if financial data or accounts were involved, and see [chapter 12](12-payments.md).
- If identity details were exposed, consider a credit freeze and fraud alert ([chapter 15](15-data-brokers-and-breaches.md)).
- Report scams and identity theft to the authority in your country.

### 5. Find the cause

Take a few minutes to learn how it happened, so it does not happen again:

- **Reused password from a breach:** use unique passwords.
- **Phishing:** use passkeys or hardware keys, and slow down on urgent messages.
- **SIM swap:** add a carrier PIN, and move from SMS codes to an authenticator or key.
- **Malware:** scan the device, reinstall the OS if needed, and update everything.
- **Someone you know:** see [chapter 14](14-households.md) and [chapter 23](23-if-compromised.md).

### 6. Prevent a repeat

- Complete the [account checklist](03-accounts.md).
- Set alerts for sign-ins and security changes.
- Store backup codes safely.
- Review your recovery options every six months.

## What this does not fix

- Data the attacker saw cannot be unseen. Act as though contacts, messages, and files were read.
- Some providers cannot restore a deleted account or data.

## Checklist

- [ ] Used a trusted device.
- [ ] Reset password; signed out other sessions; revoked unknown apps.
- [ ] Reviewed recovery options, forwarding rules, and payment methods.
- [ ] Secured the primary email and any accounts that share its password.
- [ ] Notified contacts, provider, and bank as needed.
- [ ] Identified the likely cause and fixed it.

---

Previous: [Data brokers and breaches](15-data-brokers-and-breaches.md) | [Home](../README.md) | Next: [Targeted threats](17-targeted-threats.md)
