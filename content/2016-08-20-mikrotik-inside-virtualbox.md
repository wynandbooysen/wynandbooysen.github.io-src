Title: Mikrotik Inside VirtualBox
Date: 2016-08-20 11:00
Modified: 2016-08-20 11:00
Category: Mikrotik
Tags: router, firewall
Slug: mikrotik-inside-virtualbox
Authors: Wynand Booysen
Summary: Mikrotik Inside VirtualBox

We'll have a look at setting up a virtual Mikrotik using VirtualBox.  This handy for testing scripts/configurations as well as testing backups from prodcution devices - by restoring them onto the virtual Mikrotik.

Head on over to <http://www.mikrotik.com/download> and download the VDI image.

After downloading the file simply copy and paste it into the same directory, which depending on the host OS will append the word copy to it in one fashion or another.  The reason for this is that we will use the 'copy' as the hard drive of the virtual Mikrotik allowing for a simple delete and replace with yet another copy whenever we need to do a hard 'reset' on the device.

Then on VirtualBox, create a new virtual machine.  For the sake of simplicity I'll name mine Mikrotik.

Select Type as Linux and for Version Other Linux (64bit) and click Continue.

For RAM I drop it to 128MB which is still somewhat excessive and click Continue.

Now select 'Do not add a virtual hard disk' - we will add the 'copy' of the downloaded VDI after creating the virtual machine.  Click on Create

Ignore the prompt about the machine not having a hard drive.  Once created manually add the exisitng hard drive and change the network adapter to bridged mode so that it will receive an IP on your network and allow you to connect using WinBox/SSH/WebFig.

It should take a few seconds for the virtual Mikrotik to boot, afterwhich you can log into the Mikrotik using the default admin user with no password.

Issue the command ```/ip address print``` to get the IP of the virtual Mikrotik.

Now you can log into the virtual Mikrotik just like any other Mikrotik device.
