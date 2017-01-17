Title: Setting Up Ubiquiti AP at Home with Dockerized Controller
Date: 2017-01-17 17:59
Modified: 2017-01-17 17:59
Category: Docker
Tags: ubiquiti, docker, access point
Slug: setting-up-ubiquiti-ap-at-home-with-dockerized-controller
Authors: Wynand Booysen
Summary: Setting Up Ubiquiti AP at Home with Dockerized Controller

I got to the point where the all-in-one solutions provided by consumer grade router/modem/firewall/Wifi devices were just not cutting it anymore.

My HTPC is wired for Internet access, which seems to stay connected without any issue.  However my phones/tablets/laptops would randomly drop of the Wifi and not be able to reconnect to it or shows it's connected to Wifi but has no Internet access.

The only way to resolve the Wifi issue is to restart the DLink 'router'

So I made up my mind to separate these functions, at least the router/firewall from the Wifi.

Currently I'm borrowing a spare Ubiquiti to test with before committing to buying a unit for myself.

Ubiquiti provides software based Unifi Controller that is used to configure and manage the AccessPoints (APs).  Instead of spinning up a VM or installing it directly on one of my machines I just opted to run the docker container published by LinuxServer.io on docker hub (linuxserver/unifi)

```bash
docker run -d -h unifi --name=unifi   -v /path/to/storage/for/configs/unifi:/config   -e PGID=<gid> -e PUID=<uid>    -p 8080:8080   -p 8081:8081   -p 8443:8443   -p 8843:8843   -p 8880:8880   linuxserver/unifi
```

Update the path to the directory to be used for the volume where the config file will be persisted on the docker host, and provide the GID and UID of the user that is the owner of the path specified

This will boot up and become accessible after a few seconds on https://ip:8443

This doesn't run the latest version but is recent enough for my purposes as this is only a temp solution.

First issue since I'm borrowing a unit, it has been configured before and has been sitting in a cupboard for a while.  So first step is to reset it back to factory settings by using the reset switch on the unit and a trusty paper clip - hold during boot until it flashes orange.

Second issue due to the age, the firmware might be too old to communicate with version 5 of the Unifi Controller software - I will cover upgrading the AP via SSH using the Controllers bundled firmware.

Once reset and booted up again, check your DHCP server for the lease or scan the network for the AP.  I've tried using the Ubiquiti Device Discovery Tool (Chrome Extension) but had no success in finding the device on the network.  So I got my IP from my DHCP server.

Armed with the IP of the AP, we SSH into the AP.  Default user name and password are both ubnt

```bash
ssh ubnt@YOUR.AP.IP.ADDRESS
```

Once logged in the console will display the model and version number.  From here we will issue the upgrade command as follow:

```bash
upgrade http://YOUR.CONTROLLER.IP.ADDRESS:8080/dl/firmware/BZ2/3.7.28.5442/firmware.
bin
```
Replace BZ2 with your model as required and the firmware version, which in my case is 3.7.28.5442 with the appropriate version found under:

```bash
/usr/lib/unifi/dl/firmware/MODEL/
```

inside the docker image, which can be accessed while it is running by executing:

```bash
docker exec -it unifi /bin/bash
```

and navigating to the bundled firmware directory as listed above.

After updating however it was still failing to detect the AP from the controller, because the AP tries to register by looking for http://unifi:8080/inform on the local network.  So you can either set an ALIAS for the Unifi Controller in DNS, pass option 43 in your DHCP scope or manually update the address on the AP while logged in via SSH by issuing:

```bash
mca-cli
```

to enter CLI, then:

```bash
set-inform http://ip-of-controller:8080/inform
```

after which it should appear in the Unifi Controller with the option to adopt it, and then issue the set-inform command again to complete the handshake after which the status will be provisioning followed by connected.

In a later post I'll review setting up the actual AP from the Unifi Controller, assigning an SSID as well as other options offered.