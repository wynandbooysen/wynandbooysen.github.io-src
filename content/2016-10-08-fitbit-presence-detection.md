Title: FitBit Presence Detection
Date: 2016-10-08 18:00
Modified: 2016-10-08 18:00
Category: Python
Tags: fitbit, Bluetooth
Slug: fitbit-presence-detection
Authors: Wynand Booysen
Summary: FitBit Presence Detection

Show with the launch of the FitBit Alta and the new FitBit Flex 2 the prices of the FitBit Flex was bound to go down.  So I picked up a FitBit Flex for just R800.  So why did I get one?

Well I try and keep fit and tracking your activity helps you stay motivated.  But mainly I wanted to check the sleep monitoring function and have another Bluetooth device to be possilbly used for presence detection.

So the FitBit Flex uses a Nordic Semiconductor nRF8001 chip - which is for Bluetooth 4.0 LE connectivity.

It also comes with a USB dongle that uses Texas Instruments CC2540F128 Bluetooth LE SoC to sync the Flex's data via a computer instead of the phone app.

So since the Flex is a Bluetooth device it should have unique hardware address (MAC)?

Galileo is a Python utility by Benoit Allard that allows communication with the Bluetooth based FitBit devices and sync to FitBit website.

Using Galileo you can scan for FitBit devices to sync their data.  It will list all devices along with their MAC addresses.

Simple bash script and we can grep for the specific unit's MAC address and execute something when the device is present.
