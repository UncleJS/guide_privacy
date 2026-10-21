# 10. Computers

Previous: [Phones](09-phones.md) | [Home](../README.md) | Next: [Files, cloud, and backups](11-files-cloud-backups.md)

## Who this is for

Anyone who uses a laptop or desktop. A computer holds far more data than a phone and usually has fewer protections turned on.

## What leaks

- **Unencrypted disk.** Anyone with physical access can read files from a lost or stolen computer.
- **Operating system telemetry.** The vendor collects diagnostics, usage data, and sometimes advertising data.
- **Shared accounts.** Family members, roommates, and visitors can see your files and browser sessions.
- **Employer or school management.** A managed device lets the administrator see activity, and install software.
- **Outdated software.** Unpatched flaws let malware steal data.
- **Screen and webcam.** Malware or apps can capture them.

## Steps

### 1. Keep it updated

- Turn on automatic updates for the OS, browser, and installed programs.
- Replace a computer that no longer gets security updates, or move to a supported operating system.
- Install software only from the official store or the vendor's site. Verify download addresses.

### 2. Encrypt the disk

- **Windows:** BitLocker (Pro and above) or Device Encryption (Home, where available). Store the recovery key in a safe place that is not on the same device. Note that the recovery key may be uploaded to your Microsoft account by default; decide whether that suits your threat model.
- **macOS:** FileVault.
- **Linux:** LUKS full-disk encryption, chosen at install time.
- Use a strong login password. Disk encryption protects a computer that is powered off; once you are signed in and the computer is on, the data is readable.

### 3. Use separate accounts

- Use a standard (non-administrator) account for daily work. Use an administrator account only to install or change system settings.
- Create separate accounts for other people in your household.
- Lock the screen when you step away and set a short idle timeout.

### 4. Reduce telemetry and advertising

- In OS privacy settings, turn off diagnostic data beyond the minimum, advertising ID, tailored experiences, and location services you do not need.
- Turn off activity history and cloud clipboard if you do not use them.
- Turn off personalized suggestions and web content in search and start menus.
- Remove pre-installed programs you do not use.
- Know that you cannot turn all telemetry off on most commercial operating systems. Linux distributions collect less by default.

### 5. Use a firewall and security tools

- Keep the built-in firewall on.
- Use the OS's built-in malware protection. Additional security suites add attack surface and often their own telemetry.
- Do not run untrusted software, macros, or browser extensions.

### 6. Protect peripherals

- Cover or disable the webcam when not in use, and review which apps can use the camera and microphone.
- Eject and wipe external drives before disposing of them.
- Be careful with USB devices from unknown sources.

### 7. Work and school devices

- Assume an employer or school device is monitored. Do not use it for personal accounts, medical research, or job searches.
- Use your own device for private activity, and do not install work management software on it unless required.
- Check the acceptable-use policy to learn what is monitored.

### 8. Sell, recycle, or give away

- Back up what you need, sign out of all accounts, then use the factory-reset function with encryption enabled so data cannot be recovered.

## What this does not fix

- Encryption protects against theft of a powered-off device; it does not protect against malware or an attacker who can make you unlock the computer.
- The OS vendor still receives some data.
- A managed device remains under someone else's control.

## Checklist

- [ ] OS and software update automatically.
- [ ] Full-disk encryption on, recovery key stored safely.
- [ ] Daily use under a non-administrator account.
- [ ] Privacy and telemetry settings reviewed.
- [ ] Firewall and built-in malware protection on.
- [ ] No personal activity on work or school devices.

---

Previous: [Phones](09-phones.md) | [Home](../README.md) | Next: [Files, cloud, and backups](11-files-cloud-backups.md)
