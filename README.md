# ESP32_Micropython
Micropython Projects for ESP32

## Installation

### Drivers

Install the serial VCP driver.

https://wiki.keyestudio.com/How_to_Install_the_Driver_of_CP2102_on_MAC_System

(Use a local copy stored at sejf/data/Install/macOS_VCP_Driver)

### Thonny

### Flash MicroPython to ESP32

Tools > Manage Plugins > Esptool

Tools > Options > Install or Upgrade MicroPython (esptool)
- Target Port: Use cu.SLAB_USBtoUART (VCP Driver) and select erase all flash
- MicroPython family: ESP32
- Variant: Expressif ESP32/WROOM
- Version: use the latest one

![install](/pictures/install_micropython.png)

```
Downloading from https://micropython.org/resources/firmware/ESP32_GENERIC-20231005-v1.21.0.bin
Writing to /var/folders/m2/32401s8s4m1238n920c20rxh0000gp/T/tmpithlnrfw/ESP32_GENERIC-20231005-v1.21.0.bin
100%/Applications/Thonny.app/Contents/Frameworks/Python.framework/Versions/3.10/bin/python3.10 -u -m esptool --port /dev/cu.SLAB_USBtoUART --chip esp32 --baud 115200 write_flash --flash_mode keep --flash_size keep --erase-all 0x1000 /var/folders/m2/32401s8s4m1238n920c20rxh0000gp/T/tmpithlnrfw/ESP32_GENERIC-20231005-v1.21.0.bin
esptool.py v4.6.2
Serial port /dev/cu.SLAB_USBtoUART
Connecting....
Chip is ESP32-D0WD (revision v1.0)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: 10:52:1c:74:b8:10
Uploading stub...
Running stub...
Stub running...
Configuring flash size...
Erasing flash (this may take a while)...
Chip erase completed successfully in 14.3s
Compressed 1661872 bytes to 1104578...
Writing at 0x00001000... (1 %)
Writing at 0x00010999... (2 %)
...
Writing at 0x0018dfb7... (98 %)
Writing at 0x00193d01... (100 %)
Wrote 1661872 bytes (1104578 compressed) at 0x00001000 in 97.5 seconds (effective 136.3 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
Done!
```

### Known Issues & Fixes

The issue with uploading the micropython to the chip *"Failed to connect to ESP32: Invalid head of packet"*

Solution - press the BOOT button and keep it presssed while the micropathon is being uploaded to the chip.

https://github.com/espressif/arduino-esp32/issues/1253#issuecomment-380096908

*Hello,
I fixed it by pressing "Load" button before switch the ESP32 on. The Rx/Tx leds stop to blink, so the serial port was no more use by the ESP. I tried to launch a connection, and it works.*


## Python Console

As the port use `/dev/cu.usbserial-0001` to interact with the python console.
