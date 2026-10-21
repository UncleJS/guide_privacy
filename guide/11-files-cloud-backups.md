# 11. Files, cloud, and backups

Previous: [Computers](10-computers.md) | [Home](../README.md) | Next: [Payments](12-payments.md)

## Who this is for

Anyone who stores photos, documents, or backups online or on external drives.

## What leaks

- **Provider access.** Most cloud services can read your files, scan them for policy violations, and hand them over when legally required.
- **Account compromise.** A hacked cloud account exposes years of photos, documents, and device backups at once.
- **Shared links.** "Anyone with the link" files can be forwarded, indexed, or guessed.
- **Photo metadata.** Photos carry location, time, and device data.
- **Forgotten copies.** Old backups, synced folders, and trash bins keep files you thought were deleted.
- **Third-party apps.** Apps given access to your cloud storage can read everything they are allowed to.

## Steps

### 1. Decide what belongs in the cloud

Sort files into three groups:

- **Fine in a mainstream cloud:** low-sensitivity documents, shared family photos, reference material.
- **Encrypt before uploading, or use an end-to-end encrypted service:** identity documents, tax and medical records, financial files, sensitive photos, legal documents.
- **Keep offline:** recovery keys, seed phrases, and anything where a leak would cause serious harm.

### 2. Use end-to-end encrypted storage for sensitive files

- Choose a service where files are encrypted on your device and the provider has no key (zero-knowledge). Check whether the service is audited and open about its design.
- Alternatively, encrypt files locally with a vetted tool before uploading them to any provider, and keep the key away from the provider.
- Keep the recovery key offline. Losing it means losing the files.

### 3. Secure the cloud account

- Protect it with a passkey or hardware key ([chapter 03](03-accounts.md)).
- Review which apps and devices have access, and revoke the ones you do not use.
- Turn on notifications for sign-in from new devices.
- If your platform offers end-to-end encrypted backups, understand the recovery trade-off before enabling them ([chapter 09](09-phones.md)).

### 4. Share carefully

- Share with specific people rather than "anyone with the link".
- Set expiry dates and passwords on links where supported.
- Review shared items periodically and remove old shares.
- Remove edit access when view access is enough.

### 5. Handle photos

- Turn off location tags in the camera app if you do not need them.
- Remove metadata from images before sharing them publicly or with people you do not trust.
- Review shared albums and who can see them.
- Know that "hidden" or "recently deleted" albums still sit in the same account and are synced.

### 6. Back up on purpose

Use the 3-2-1 rule: three copies, on two kinds of storage, with one off-site.

- Keep one backup on an encrypted external drive. Disconnect it when you are not backing up, which protects it from ransomware.
- Test restoring a file now and then. A backup you cannot restore is not a backup.
- Store the off-site copy encrypted, or at a place you trust.

### 7. Delete properly

- Empty the trash and check for synced copies on other devices.
- Deleting from a cloud service may not remove the file immediately from backups.
- Before disposing of a drive, use full-disk encryption from the start; for an unencrypted drive, a standard overwrite is not reliable on solid-state drives. Physical destruction or encrypted-from-the-start storage is the dependable approach.

## What this does not fix

- A provider that holds encryption keys can read your files if compelled or compromised.
- Files shared with others stay with them.
- Metadata (file names, sizes, timestamps, sharing relationships) may remain visible even with end-to-end encrypted storage.

## Checklist

- [ ] I know which files must not be stored in a mainstream cloud unencrypted.
- [ ] Cloud account has a passkey or hardware key and reviewed app access.
- [ ] Shared links reviewed; "anyone with the link" reduced.
- [ ] Photo location tags off, or removed before sharing.
- [ ] A working encrypted backup following 3-2-1.

---

Previous: [Computers](10-computers.md) | [Home](../README.md) | Next: [Payments](12-payments.md)
