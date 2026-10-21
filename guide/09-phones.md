# 09. Phones

Previous: [Social media](08-social-media.md) | [Home](../README.md) | Next: [Computers](10-computers.md)

## Who this is for

Everyone with a smartphone. Your phone holds your location history, contacts, photos, messages, and the keys to most of your accounts.

## What leaks

- **Location.** From GPS, Wi-Fi networks, Bluetooth beacons, cell towers, and apps. Many apps collect and sell it.
- **App data.** Apps request contacts, microphone, camera, photos, and tracking identifiers.
- **Advertising ID.** A device-level identifier that lets ad networks follow you across apps.
- **Backups.** Cloud backups can expose more than the phone itself, depending on encryption.
- **Lock screen.** Notifications, widgets, and assistant features can display or act on private data.
- **Carrier.** Your mobile provider knows which towers you connect to, your number, and often your name.

## Steps

### 1. Updates and lock

- Turn on automatic operating system and app updates. Replace a phone that no longer receives security updates.
- Use a six-digit passcode or longer, or an alphanumeric one. Biometrics are convenient; know that in some situations you can be compelled to unlock a device with a fingerprint or face more easily than with a passcode ([chapter 19](19-device-seizure.md)).
- Enable the "find my device" feature so a lost phone can be located and wiped.
- Set the screen to lock quickly and hide notification content on the lock screen.

### 2. Permissions

Review permissions app by app, and by permission type.

- **Location:** choose "while using the app", or "never". Turn off precise location when an approximate position is enough. Turn off "always".
- **Contacts, photos, microphone, camera:** deny by default and grant only when needed. Prefer "selected photos" over the full library.
- **Bluetooth and nearby devices:** deny unless the app uses a device.
- **Notifications:** disable for apps that do not need them.
- Remove apps you do not use. Each is a data source and an attack surface.

### 3. Reduce tracking

- Turn off the advertising identifier or reset it periodically, and opt out of personalized ads.
- On iPhone, set apps to ask before tracking. On Android, delete the advertising ID where the option is offered.
- Turn off location-based ads and "significant locations" history if you do not use them.
- Turn off Wi-Fi and Bluetooth scanning for location in system settings.

### 4. Install apps from official stores

- Use the official app store of your platform. Sideloading increases malware risk.
- Check the developer, the permissions requested, and recent reviews before installing.
- Prefer the website over an app when you only need a service once; browsers give sites less access than apps.

### 5. Backups

- Know where your phone backs up and what the provider can read.
- Turn on end-to-end encrypted backups if your platform offers them; on iPhone, this is Advanced Data Protection. Understand the recovery trade-offs before enabling.
- Keep a local, encrypted backup if you want one that the cloud provider cannot read.

### 6. Carrier and number

- Add a PIN to the carrier account and request port-out protection ([chapter 03](03-accounts.md)).
- Treat your number as semi-public. It is used for SMS codes and ends up in data broker records.
- Consider a secondary number for sign-ups and delivery services.

### 7. Lost or stolen

- Lock or erase the device remotely. Change passwords for accounts that were signed in.
- Report to your carrier to block the SIM.
- Review account sessions and revoke the lost device.

## What this does not fix

- The operating system vendor and apps still collect data you permit them to collect.
- A carrier can locate your phone while it is connected to the network.
- Spyware installed with physical access or through a malicious link can defeat all of the above. See [chapter 23](23-if-compromised.md).

## Checklist

- [ ] Automatic updates on, supported phone.
- [ ] Strong passcode and quick auto-lock; lock-screen notifications hidden.
- [ ] Permissions reviewed; location set to "while using" or off.
- [ ] Ad tracking limited; unused apps removed.
- [ ] Backups understood and encrypted where possible.
- [ ] Carrier PIN and port-out protection set.
- [ ] Lost-phone plan ready.

---

Previous: [Social media](08-social-media.md) | [Home](../README.md) | Next: [Computers](10-computers.md)
