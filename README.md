# Modem Patcher

Band 77 patcher for the OnePlus 9 and 9 Pro.

# What and why?

OnePlus has band 77 disabled on the OnePlus 9 and 9 Pro. The original way to enable band 77 used QPST. QPST only seems to work on OxygenOS, and requires Windows. If you don't use OOS, or don't use Windows, this script can patch the modem file with the necessary changes.

# Requirements

1. OnePlus 9 or 9 Pro (tested on 9 Pro on Android 13 with lineageOS)
2. Unlocked bootloader
3. Python 3
4. Android platform-tools (adb and fastboot)

# How to use

- First, we need to dump our modem file. Boot into bootloader (`adb reboot bootloader`), and run `fastboot getvar current-slot`. Take note of this.
- If not rooted, temporarily boot TWRP (`fastboot boot TWRP.img` in bootloader). Commands are the same in TWRP, or not. We need to find what partition the modem is on.
- Run `adb shell` (`su` after if not using TWRP), then run `ls -lath /dev/block`. Find the modem for your current slot, and take note of it.
- Run these commands in order (replace sde9 with the partition if it's different): 
  - [TIP] You may need to change `/tmp` to `/storage/emulated/0` if you're having issues.
```
dd if=/dev/block/sde9 of=/tmp/modem.bin bs=2048
exit
adb pull /tmp/modem.bin
adb pull /tmp/modem.bin modem.bin.bak
```

- We can now patch the modem.bin with the script. Run `git clone https://github.com/itsnebulalol/modempatcher`
- To go into the directory, run `cd modempatcher`
- Now, we can run `python3 main.py -p /path/to/modem.bin`
  - [TIP] Add -l or -L for Android 11, and maybe Android 12. Neither are tested.
- Boot into bootloader, and `fastboot flash --slot=all modem modem.bin`

# Having issues?

This script may not be perfect, and may not work on every device. Before, we pulled the modem image a second time so we have a backup. You can run `fastboot flash --slot=all modem modem.bin.bak` in bootloader to flash the backup.

Lost the backup? Add the `-u` flag to the script to unpatch the modem.bin, and you can flash it again.

# Credits

- [rmendez011](https://forum.xda-developers.com/m/rmendez011.6576671/) for the [original guide](https://forum.xda-developers.com/t/updated-4-4-23-how-to-enable-n77-n78-5g-c-band-with-5g-uw-icon-on-le2115-le2125-oneplus-9-9-pro-5g-running-oxygen-os-11-13-f-21-verizon.4429489/) with QPST
