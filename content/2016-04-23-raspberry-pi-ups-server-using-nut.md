Title: Raspberry Pi - UPS server using NUT
Date: 2016-04-23 16:10
Author: Wynand Booysen
Category: Linux
Tags: headless, Linux, RaspberryPi, Raspbian
Slug: raspberry-pi-ups-server-using-nut
Status: published

So today we will setup a NUT (Network UPS Tools) server on a Raspberry
Pi to turn our USB attached UPS into a networked UPS.

I'm using a Raspberry Pi model B+ that was lying around, running the
minimal image - Raspbian Jessie Lite.

So we start off by connecting to the Raspberry Pi over SSH (default
credentials username:**pi** and password:**raspberry**) and setting an
static IP which will be used later when we configure the NUT-server and
our NUT-clients.

This has changed since Jessie and now gets done in /etc/dhcpcd.conf
which we open for editing using:

```bash
sudo nano /etc/dhcpcd.conf
```

and at the bottom of the file we add *interface* **eth0** for the
onboard NIC and it's static values:

```bash
interface eth0
static ip_address=x.x.x.x

static routers=y.y.y.y
static domain_name_servers=8.8.8.8 8.8.4.4
```

*static ip\_address* is the IP address to be used for the Raspberry Pi,
*static routers* is the network's default Gateway IP and *static
domain\_name\_servers* are the IP addresses of your DNS servers and save
(CTRL+X, then Y)

Quick reboot (`sudo reboot` ) and SSH back in on the new IP address, and now we can
begin configuring NUT.  Start by updating and upgrading the system
using:

```bash
sudo apt-get update && sudo apt-get upgrade
```

Followed by installing the NUT-server and NUT-client:

```bash
sudo apt-get install nut-client nut-server
```

Ensure that *usbutils* is installed so we can use *lsusb* to get some
info from the UPS:

```bash
sudo apt-get install usbutils
```

and connect the UPS via USB if not already connected.  Run *lsusb* which
will return a list of the connected USB devices - usually device number
004 should be the UPS on a freshly installed Raspbian system, in my case
my Eaton UPS is being identified as a MGE UPS with vendor ID 0463:

```bash
pi@raspberrypi:~ $ lsusb
Bus 001 Device 004: ID 0463:ffff MGE UPS Systems UPS
Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp. SMSC9512/9514 Fast Ethernet Adapter
Bus 001 Device 002: ID 0424:9514 Standard Microsystems Corp. 
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

So first file we edit will be */etc/nut/ups.conf* to configure our UPS
using Nano again:

```bash
sudo nano /etc/nut/ups.conf
```

and right at the bottom we add our UPS with a *\[friendly\_name\],
driver, port* and *desc:*

```bash
[eaton]
        driver = usbhid-ups
        port = auto
        desc = "Eaton UPS"
```

and save (CTRL+X, then Y) then we test the UPS driver by running:

```bash
sudo upsdrvctl start
```

which will return something similar depending on your UPS model and if
not a quick reboot usually does the trick to get the UPS to play along:

```bash
Network UPS Tools - UPS driver controller 2.7.2
Network UPS Tools - Generic HID driver 0.38 (2.7.2)
USB communication driver 0.32
Using subdriver: MGE HID 1.33
```

Key lines here are the last two stating it's communicating via USB
driver and loading the sub-driver for the UPS model.

The next step is to configure **upsmon** and **upsd** of which the later
communicates with the UPS driver configured while **upsmon** monitors
and communicates shutdown procedures to **upsd**.  NUT allows multiple
instances of **upsmon** to run on different machines while communicating
with the same physical UPS.

So for **upsd** to be accessible via the network we edit `*/etc/nut/upsd.conf*`

`sudo nano /etc/nut/upsd.conf` and uncomment the LISTEN directive for
the localhost IP (127.0.0.1) and add another LISTEN directive for the
static IP (x.x.x.x) that we set before starting the installation of NUT:

```bash
#
LISTEN 127.0.0.1 3493
LISTEN x.x.x.x 3493

#
```

We will need to add some users to manage access to **upsd** by editing
the **upsd** users config file `sudo nano /etc/nut/upsd.users` and adding the following:

```bash
[admin]
        password = youradmpass
        actions = SET
        instcmds = ALL

#
# --- Configuring for a user who can execute tests only
#
[testuser]
        password  = testuserpass  
        instcmds  = test.battery.start
        instcmds  = test.battery.stop

#
# --- Configuring for upsmon
#
# To add a user for your upsmon, use this example:
#
[upsmon_local]
        password  = local_pass
        upsmon master
[upsmon_remote]
        password  = remote_pass
        upsmon slave
```

then we edit `sudo nano /etc/nut/upsmon.conf`  and add the UPS to be monitored and user
credentials for **upsd** in the MONITOR section (CTRL+W to use the FIND
in Nano) as:

```bash
MONITOR friendly_name@localhost 1 upsmon_local local_pass master
```

and finally edit `sudo nano /etc/nut/nut.conf`  and set the value for MODE equal to
'netserver' without any spaces before and after the = sign:

```bash
# IMPORTANT NOTE:
#  This file is intended to be sourced by shell scripts.
#  You MUST NOT use spaces around the equal sign!

MODE=netserver
```

We are now ready to start the NUT-server and local NUT-client on the
Raspberry Pi:

```bash
sudo systemctl status nut-server.service
sudo systemctl status nut-client.service
```

reboot the Raspberry Pi and confirm that the services has started
automatically:

```bash
pi@raspberrypi:~ $ ps -ef | grep ups
nut        522     1  0 17:31 ?        00:00:34 /lib/nut/usbhid-ups -a eaton
nut        524     1  0 17:31 ?        00:00:00 /lib/nut/upsd
root       526     1  0 17:31 ?        00:00:00 /lib/nut/upsmon
nut        527   526  0 17:31 ?        00:00:00 /lib/nut/upsmon
pi         688   574  0 18:52 pts/1    00:00:00 grep --color=auto ups
```

and upsc *friendly\_name* should return values from the UPS:

```bash
pi@raspberrypi:~ $ upsc eaton
Init SSL without certificate database
battery.charge: 100
battery.runtime: 3953
battery.type: PbAc
device.mfr: EATON
device.model: 5E 1100i
device.type: ups
driver.name: usbhid-ups
driver.parameter.pollfreq: 30
driver.parameter.pollinterval: 2
driver.parameter.port: auto
driver.version: 2.7.2
driver.version.data: MGE HID 1.33
driver.version.internal: 0.38
input.voltage: 231.0
outlet.1.status: on
outlet.desc: Main Outlet
outlet.id: 1
outlet.switchable: no
output.frequency: 49.9
output.frequency.nominal: 50
output.voltage: 232.0
output.voltage.nominal: 230
ups.beeper.status: enabled
ups.delay.shutdown: 20
ups.firmware: 01.04.0018
ups.load: 5
ups.mfr: EATON
ups.model: 5E 1100i
ups.power.nominal: 1100
ups.productid: ffff
ups.start.battery: yes
ups.status: OL CHRG
ups.timer.shutdown: -1
ups.vendorid: 0463
```

Now you can continue adding NUT-clients on your network, and on the
clients set nut.conf MODE=netclient and upsmon.conf to:

```bash
MONITOR friendly_name@x.x.x.x 1 upsmon_remote remote_pass slave
```

Congratulations, your NUT server is now officially running!
