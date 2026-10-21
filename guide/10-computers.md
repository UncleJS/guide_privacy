# 10. Computers and computer security

Previous: [Phones](09-phones.md) | [Home](../README.md) | Next: [Files, cloud, and backups](11-files-cloud-backups.md)

## Who this is for

Anyone who uses a laptop or desktop. A computer holds far more data than a phone, usually has fewer protections turned on, and often runs the programs that handle your email, files, passwords, and banking. If an attacker gets into your computer, most other protections in this guide stop mattering.

This chapter is organized in three tiers that match the threat levels in [chapter 02](02-threat-models.md):

- **Baseline (levels 1 and 2):** steps 1 to 10. Do these on every computer.
- **Elevated (level 3):** steps 11 to 13. Add these if someone with access to your devices, or a determined attacker, is a concern.
- **High risk (levels 4 and 5):** steps 14 to 16. Add these for targeted threats; read them together with [chapters 17 to 22](17-targeted-threats.md).

## What leaks

- **Unencrypted disk.** Anyone with physical access can read files from a lost or stolen computer, using nothing more than a second computer or a bootable USB stick.
- **Weak sign-in.** A short or reused login password lets a thief or visitor in, and it often unlocks the password manager, browser, and cloud sync too.
- **Operating system telemetry.** The vendor collects diagnostics, usage data, and sometimes advertising data.
- **Shared accounts.** Family members, roommates, and visitors can see your files and browser sessions.
- **Employer or school management.** A managed device lets the administrator see activity and install software.
- **Outdated software.** Unpatched flaws let malware steal data or lock your files for ransom.
- **Malicious software.** Fake installers, pirated programs, rogue browser extensions, and booby-trapped documents install spyware, keyloggers, or remote-access tools.
- **Exposed services.** Remote desktop, file sharing, and similar features can let attackers in from the network.
- **Boot and firmware tampering.** Someone with physical access can alter the boot process or hardware to capture your passphrase the next time you type it.
- **Backups.** An unencrypted backup undoes disk encryption, and a backup that is always connected is encrypted by ransomware along with the original.
- **Screen and webcam.** Malware or apps can capture them.

## Baseline steps

### 1. Keep everything updated

- Turn on automatic updates for the OS, browser, and installed programs.
- Update firmware too: your laptop's UEFI/BIOS, and the firmware of the router, dock, and SSD where the vendor provides it. On Linux, `fwupd` delivers many vendor updates; on Windows and macOS, firmware arrives with system updates or the manufacturer's updater.
- Restart when asked. Many fixes only take effect after a restart.
- Replace a computer or operating system that no longer gets security updates. Running an unsupported system is the biggest avoidable risk on this list.
- Install software only from the official store, your distribution's repositories, or the vendor's own site. Check that you typed the address correctly and prefer a package manager, where available, to downloading installers from search results.

### 2. Encrypt the disk

Full-disk encryption protects your files when the computer is off, lost, or stolen. Without it, a thief can read your files in minutes, even if you have a strong login password, because the password does not protect the disk itself.

**Windows.**

- BitLocker is available on Windows Pro, Enterprise, and Education. Windows Home may offer "Device Encryption" on supported hardware; it needs a Microsoft account sign-in or a work or school account.
- Check status in Settings under Privacy and security (Device encryption or BitLocker), or by running `manage-bde -status` in an administrator terminal.
- By default, BitLocker unlocks automatically through the TPM chip and does not ask for a pre-boot PIN. That protects against someone who removes the drive but not against someone who can start your computer and attack the sign-in screen. For a stronger setup, require a startup PIN or passphrase (Group Policy: "Require additional authentication at startup"), and consider a longer PIN. Higher-threat users should do this.
- Save the recovery key. Device Encryption stores it in your Microsoft account by default. Decide whether you want that. If you do not, keep the key printed or in your password manager, and remove it from the cloud account. Never leave it on the same computer.
- Choose XTS-AES 256 for new drives if offered.
- VeraCrypt is a third-party option for full-disk or container encryption; it supports pre-boot authentication without a TPM, but it is more work to maintain through updates.

**macOS.**

- Turn on FileVault in System Settings under Privacy and Security. Apple silicon Macs encrypt their internal storage in hardware, but FileVault ties the keys to your login password, which is the part that protects you from someone who has your Mac.
- When setting up FileVault, choose whether to keep the recovery key in iCloud or to hold it yourself. Hold it yourself, printed or in your password manager, if you do not want the provider to be able to help recover it.
- Use a strong login password, and require it immediately after sleep or screen saver.

**Linux.**

- Choose full-disk encryption (LUKS) in the installer. Distributions such as Fedora, Ubuntu, and Debian offer it as an option; it is difficult to add cleanly afterward.
- Use a strong passphrase for the LUKS volume. Several words or a long sentence are better than a short complex password.
- Encrypt swap too (usually included in the installer's LUKS setup), and consider whether you need hibernation, because hibernation writes memory to disk.
- By default, `/boot` and the EFI partition are not encrypted. That is enough for most people. For higher threat levels, see steps 11 to 13.
- Check status with `lsblk -f` or `sudo cryptsetup status <name>`.

**Everywhere.**

- Disk encryption protects data only while the computer is **off**, or locked and **not just asleep**. When the computer is on or asleep, decryption keys stay in memory.
- If you will leave your laptop unattended, travel with it, or cross a border, **shut it down completely** instead of closing the lid. A powered-off machine is the strongest state.
- Disk encryption does not protect data from someone who knows your passphrase, or from you, once you are signed in.

### 3. Use strong sign-in

- Your login password is the password that matters most on a computer. Use a long passphrase (four or more random words) that is unique and not used elsewhere.
- Lock the screen when you step away (Windows key plus L, Control-Command-Q on macOS, or Super-L on many Linux desktops), and set a short idle timeout.
- Use biometrics such as a fingerprint or face for convenience only if your threat model allows it; they cannot replace the passphrase after a restart.
- On a shared household computer, do not give others your password. Create separate accounts instead.
- If your computer supports sign-in with a hardware security key, consider using it ([chapter 03](03-accounts.md)).

### 4. Separate accounts and limit privileges

- Use a standard (non-administrator) account for daily work, and an administrator account only to install or change system settings. On Linux and macOS, `sudo` prompts do the same job; do not stay in a root session.
- Create separate accounts for family members and visitors.
- Do not store the administrator or recovery passwords in the browser.
- Remove accounts that nobody uses, and disable the guest account if you do not need it.

### 5. Turn on built-in protections

- Keep the firewall on: Windows Defender Firewall, the macOS firewall, or `firewalld` or `ufw` on Linux. Treat unfamiliar networks as public networks.
- Use the built-in malware protection: Microsoft Defender and SmartScreen, macOS Gatekeeper, XProtect, and notarization checks. Leave them on. Additional security suites add attack surface and often their own telemetry.
- Keep Secure Boot on. It makes tampering with the boot software harder. On Linux, it works with most major distributions.
- Keep the operating system's sandboxing features on. On Linux, prefer packages from your distribution, and for desktop apps consider sandboxed Flatpaks.
- Do not turn off protections because an installer or a guide tells you to. That is a common malware technique.

### 6. Remove and disable what you do not use

- Uninstall programs, browser extensions, and drivers that you do not use.
- Turn off remote desktop (RDP), screen sharing, file sharing, SSH, and remote login unless you need them. If you do, restrict them to your local network or use a VPN, require strong authentication, and keep the software updated.
- Turn off Bluetooth, AirDrop or Nearby Share (set to contacts only or off), and Wi-Fi when you are not using them.
- Be wary of "remote support" tools. A caller who asks you to install one is almost always a scammer.

### 7. Use a password manager and protect the clipboard

- Install a password manager from the official source ([chapter 03](03-accounts.md)).
- Do not keep passwords in a text file, spreadsheet, or notes app.
- Clear the clipboard after you paste secrets; most password managers do this automatically.
- Be careful with browser auto-fill on shared computers.

### 8. Back up, and protect backups

- Follow the 3-2-1 rule from [chapter 11](11-files-cloud-backups.md): three copies, two kinds of storage, one off-site.
- Encrypt backups. Time Machine, File History with BitLocker on the backup drive, Borg, Restic, and similar tools support encryption. An unencrypted backup undoes disk encryption.
- Keep at least one backup disconnected, so ransomware cannot reach it.
- Test restoring a file now and then.

### 9. Handle risky files and software with care

- Do not open attachments or enable macros from unknown senders, and be careful with files that ask you to "enable editing" or "enable content".
- Avoid pirated software and "cracks". They are a common way to install malware.
- For links or files you must open but do not trust, use a throwaway virtual machine, or open them in your browser's viewer rather than installing the program.
- Verify the checksum or signature of downloads where the project provides one, particularly for security tools and operating system images.
- Keep browser extensions to the minimum ([chapter 05](05-browsers.md)).

### 10. Limit telemetry and protect the camera

- In OS privacy settings, turn off diagnostic data beyond the minimum, the advertising ID, tailored experiences, and location services you do not need.
- Turn off activity history, cloud clipboard, and personalized suggestions if you do not use them.
- Remove pre-installed programs you do not use.
- Know that you cannot turn all telemetry off on most commercial operating systems. Linux distributions collect less by default.
- Cover or disable the webcam when not in use, and review which apps may use the camera and microphone.
- Eject and encrypt external drives before disposing of them, or physically destroy them.

## Elevated steps (level 3 and above)

Use these when someone you know, an employer, or a persistent adversary might get physical access to your computer, or when a thief with time and tools is a realistic concern.

### 11. Harden startup

- **Set a firmware (UEFI/BIOS) password.** It stops someone from changing boot settings or booting from a USB stick. On older Intel Macs, set a firmware password; on Apple silicon Macs, use the Startup Security Utility and keep Activation Lock on.
- **Turn on Secure Boot** and disable booting from USB, network, and optical drives unless you need them. Re-enable only when required.
- **Require a pre-boot passphrase or PIN.** BitLocker with a startup PIN, or LUKS with a passphrase typed at boot, is much stronger than TPM-only unlock. A thief who starts the computer must still guess the passphrase before the operating system loads.
- **Use measured boot where available.** With Secure Boot on, the TPM only releases the BitLocker key if the boot software is unchanged. On Linux, you can bind a LUKS key to the TPM with `systemd-cryptenroll`, and combine it with a PIN. A changed boot chain then prompts for the recovery key instead of silently unlocking.
- **Enable DMA protection.** Turn on "Kernel DMA Protection" (Windows) or IOMMU protection (Linux, `intel_iommu=on` or `amd_iommu=on`), and be careful with Thunderbolt and USB4 ports and docks that you do not control.
- **Disable features you do not use** in firmware: network boot, legacy boot, and unused ports.

### 12. Protect against someone who has had physical access

- Treat an unattended computer as potentially modified ("evil maid"): a person with a few minutes can install a hardware keylogger or tamper with the boot process.
- Never leave your computer unattended in a hotel room, an office, or a shared space if the threat is a determined person with access. If you must, power it off, and consider tamper-evident seals on screws and ports, with photographs taken before you leave.
- Have the computer repaired only by a service you trust, and ideally remove the drive or sign out and erase it first.
- Do not plug in USB devices, cables, or chargers that you did not choose. Use a data-blocking adapter for charging.
- Use a privacy screen filter in public.
- After any period of doubtful custody, check the boot configuration, and if you are not confident, reinstall the operating system from verified media.

### 13. Separate sensitive work

- Use a separate user account, a separate computer, or at minimum a virtual machine for sensitive activity, so that a compromise of your everyday account does not expose it.
- Keep sensitive files in an encrypted container or encrypted folder (for example VeraCrypt, an encrypted disk image, or Cryptomator) that stays closed when you are not using it. Even if the machine is unlocked, a closed container stays encrypted.
- Use a hardware security key for login and for accounts accessed from the machine.
- Check for unfamiliar software, startup items, device-management profiles, remote-access tools, browser extensions, and certificate authorities. Remove what you do not recognize ([chapter 23](23-if-compromised.md)).

## High-risk steps (levels 4 and 5)

These steps add friction. Adopt them only if your threat model needs them, and get advice from a specialist or helpline ([further reading](further-reading.md)), because mistakes can create a false sense of security.

### 14. Use a dedicated, minimal computer for sensitive work

- Use a separate, clean computer used only for the sensitive role. Do not sign in to personal accounts on it, and do not use it for casual browsing.
- Install the operating system from verified media, with full-disk encryption from the start, a long passphrase, and the minimal set of programs required.
- Consider a security-focused operating system: a hardened Linux distribution, or Qubes OS, which isolates activities in separate virtual machines. For amnesic sessions that leave no trace on the computer, Tails runs from a USB stick. Each has a learning curve and compatibility costs.
- Buy hardware carefully. Use a reputable retailer, check for signs of tampering, and reinstall the OS immediately instead of trusting a pre-installed image. Prefer hardware that receives firmware updates and supports Secure Boot customization.
- Keep the computer's role narrow, updates current, and the list of installed software short.

### 15. Reduce the attack surface further

- Use a long unique passphrase for disk encryption that differs from the login password, and avoid biometrics for the disk.
- Where practical, boot from verified firmware and operating system images, with Secure Boot keys you manage yourself. This is advanced and not required for most people.
- Keep encryption keys off the machine: recovery keys and backup keys in a separate safe location.
- Minimize network exposure: turn off services, use a host firewall with default deny, and consider separating networks for sensitive devices ([chapter 13](13-home-and-devices.md)).
- Use isolated virtual machines for opening untrusted documents, and a separate one for browsing.
- Do not rely on antivirus as a defense against targeted attacks. Rely on updates, isolation, and minimal software.

### 16. Plan for loss, seizure, and wiping

- Assume that a device that leaves your sight may be examined ([chapter 19](19-device-seizure.md)). Carry only what you need, and keep recovery keys elsewhere.
- Learn how to power off the computer quickly, and keep it powered off when you cross a border or leave it unattended.
- Understand how to securely retire a computer: for encrypted drives, erasing the encryption key (cryptographic erase) combined with a factory reset is fast and reliable. For unencrypted drives, a normal delete does not remove data, and overwriting is unreliable on solid-state drives; the dependable answers are encryption from the start and physical destruction at the end.
- Do not wipe, delete, or destroy data you are legally required to keep, or after you know that you are the subject of an investigation or dispute. Speak to a lawyer first.

## Selling, recycling, or giving away

- Back up what you need, then sign out of all accounts, remove the device from your cloud accounts, and deauthorize licenses.
- Use the built-in reset with encryption enabled ("Reset this PC" with data removal on Windows; "Erase All Content and Settings" or Erase Assistant on macOS; for Linux, erase the LUKS header or overwrite the key slots, then reinstall).
- For drives that held sensitive data and were not encrypted, destroy them physically.

## Work and school devices

- Assume an employer or school device is monitored, and that the administrator can read files, see browsing, install software, and wipe the device.
- Do not use it for personal accounts, medical research, or job searches.
- Use your own device for private activity, and do not install work management software on it unless required.
- Check the acceptable-use policy to learn what is monitored.

## What this does not fix

- **A computer that is on and unlocked.** Disk encryption does not protect against malware, a stolen session, or someone who sits down at your unlocked computer.
- **Sleep and hibernate states.** Keys can remain in memory, and some attacks (cold-boot and DMA) can recover them. Shut down when it matters.
- **Compelled disclosure.** If the law lets an authority require your passphrase, encryption does not stop that ([chapter 19](19-device-seizure.md)).
- **Weak passphrases.** A short or guessable one lets an attacker brute-force an encrypted disk.
- **Hardware implants and compromised firmware.** A skilled adversary with physical access, or a tampered supply chain, may defeat software protections. Higher threat levels reduce but do not eliminate this risk.
- **Keyloggers.** Hardware or software keyloggers capture the passphrase when you type it.
- **Telemetry and managed devices.** The vendor still receives some data, and a managed device remains under someone else's control.

## Checklist

**Baseline**

- [ ] OS, firmware, browser, and software update automatically; the OS is still supported.
- [ ] Full-disk encryption is on, and the recovery key is stored safely and away from the computer.
- [ ] A strong, unique login passphrase; the screen locks quickly.
- [ ] Daily use under a standard account.
- [ ] Firewall, Secure Boot, and built-in malware protection are on.
- [ ] Remote access and file sharing are off unless needed.
- [ ] Software comes only from official sources; unused programs and extensions removed.
- [ ] An encrypted backup, with a copy that is disconnected.
- [ ] Telemetry and privacy settings reviewed; the webcam covered or controlled.

**Elevated**

- [ ] Firmware password set; boot from external media disabled; pre-boot PIN or passphrase required.
- [ ] DMA protection is on; ports and docks are controlled.
- [ ] Computer is never left unattended in doubtful places; tamper-evident measures where needed.
- [ ] Sensitive files are in closed encrypted containers or a separate account or machine.
- [ ] Hardware key for sign-in where supported.

**High risk**

- [ ] A dedicated, minimal computer or isolated environment for sensitive work.
- [ ] Hardware bought and installed carefully; OS installed from verified media.
- [ ] Separate disk passphrase; recovery keys stored apart.
- [ ] A plan for loss, seizure, and secure retirement of the machine, agreed with a lawyer or helpline where needed.

---

Previous: [Phones](09-phones.md) | [Home](../README.md) | Next: [Files, cloud, and backups](11-files-cloud-backups.md)
