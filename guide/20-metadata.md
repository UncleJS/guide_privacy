# 20. Metadata

Previous: [Device seizure](19-device-seizure.md) | [Home](../README.md) | Next: [Anonymity tools](21-anonymity-tools.md)

## Who this is for

People whose risk comes from being known to be in contact with someone, or at some place, rather than from what they said. Sources and journalists, lawyers and clients, support-group members, activists, and people leaving abusive situations commonly face this.

## What metadata is

Metadata is data about communication and activity, not the content. Examples:

- **Who** you contact: phone numbers, email addresses, usernames.
- **When** and how often: timestamps, duration, patterns.
- **Where** from: IP address, cell tower, Wi-Fi network, GPS.
- **How:** device type, app, operating system.
- **How big:** message or file size, which can imply what was sent.
- **File metadata:** author, device, editing history, and location in documents and photos.

Metadata is revealing because it can be gathered at scale, it is not usually encrypted, and it shows relationships and routines. A pattern of calls to a clinic, a lawyer, or a reporter says a lot without any content.

## Who can see it

| Observer | Typically sees |
|----------|----------------|
| Mobile carrier | Your number, who you call and text by SMS, approximate location from towers |
| Internet provider | Sites and servers you connect to, timing, and volume |
| Messaging provider | Account, contacts, IP address, timing, sometimes group membership |
| Email provider | Sender, recipient, subject, time, size, IP address |
| Network owner (Wi-Fi) | Devices, destinations, timing |
| Websites and apps | IP address, device details, activity on their service |
| Another party | Whatever you sent them, including document metadata |

## Steps

### 1. Choose services that collect less

- Prefer messengers that minimize stored metadata, and that offer features such as sealed sender or usernames instead of numbers ([chapter 07](07-messaging.md)).
- Read the provider's transparency report and law-enforcement guide. They show what it holds and discloses.
- Use a username instead of a phone number where the app offers it.

### 2. Separate contact paths

- Use a number or account that is not linked to your legal name for sensitive contacts, as far as local rules allow. Many countries require registration for SIM cards.
- Keep sensitive communication on a separate account, device, and network from everyday use ([chapter 18](18-compartments.md)).
- Avoid calling or texting sensitive contacts from your usual phone number when the carrier record is the risk.

### 3. Reduce location trails

- Turn off location services, and Wi-Fi and Bluetooth scanning, when not needed ([chapter 09](09-phones.md)).
- A phone connected to the mobile network is locatable by the carrier. Leaving it at home or powered off is the only complete way to avoid that record, and an absent phone is itself a pattern.
- Be aware of other trails: transport cards, toll tags, payment records, license-plate readers, camera networks.

### 4. Clean files before sharing

- Remove metadata from documents, images, and PDFs before sharing. Check author names, tracked changes, comments, GPS data, and hidden text.
- Share a copy exported in a flat format, not the original file.
- Be careful with printed documents: many printers add near-invisible tracking dots that identify the device and the time.
- Do not share screenshots with visible notifications, tabs, or usernames.

### 5. Vary patterns

- Predictable timing, locations, and routes make you easy to link. Where safe and practical, change them.
- Do not contact a sensitive person immediately after an event that links you to it.
- Be careful about the chain: if your contact is monitored, you become visible through them.

### 6. Use tools that hide the network layer, with care

- Tor and VPNs hide parts of the network metadata, and they have their own limits ([chapter 21](21-anonymity-tools.md)).
- They do not hide the account you sign in to, or what you say.

### 7. Agree on a protocol with sensitive contacts

- Choose the channel, the schedule, and the conventions in advance, ideally in person.
- Say what to do if one of you thinks the channel is compromised.
- Keep sensitive conversations short and purposeful.

## What this does not fix

- A provider that must log, or is compelled to, still has the record.
- Telephone and mobile-network metadata cannot be hidden from the carrier while the service is used.
- If the person you contact is exposed, your contact with them is exposed.

## Checklist

- [ ] I know who can see which metadata about my sensitive contacts.
- [ ] I use an account and channel that fits my threat for sensitive contacts.
- [ ] Files are cleaned before sharing.
- [ ] I considered location trails and payment records.
- [ ] I agreed a protocol with the people involved.

---

Previous: [Device seizure](19-device-seizure.md) | [Home](../README.md) | Next: [Anonymity tools](21-anonymity-tools.md)
