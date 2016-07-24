Title: Install Oracle VirtualBox 5.0 On A Headless Ubuntu Server
Date: 2016-01-10 21:46
Author: Wynand Booysen
Category: Linux
Tags: headless, ubuntu, virtualbox
Slug: install-oracle-virtualbox-5-0-on-a-headless-ubuntu-server
Status: published

Today I'll be showing you how to install VirtualBox 5.0 on a headless
Ubuntu Server along with phpVirtualBox 5 to allow remote management
using a Web GUI.

Why use VirtualBox?

Simple.  It's free. It's a Type 2 hypervisor that basically runs on most
hardware, unlike most Type 1 hypervisors that are limited to certain
supported hardware.

VirtualBox is cross platform and runs on Mac/Linux/Windows, which means
you can use your existing machine - no dedicated server required.  But
in this instance I'll be using a spare HP MicroServer that I have laying
around.

**Preparing The Server**
------------------------

We start off with a basic Ubuntu Server installation - I'm using 14.04.3
LTS.

Ensure that it's updated by executing:

```bash
sudo apt-get update && sudo apt-get upgrade -y
```

Install the required prerequisites for VirtualBox to install
successfully:

```bash
sudo apt-get install build-essential dkms -y
```

**Installing Oracle VirtualBox**
--------------------------------

Append the Oracle VirtualBox repository to **/etc/apt/sources.list**:

```bash
deb http://download.virtualbox.org/virtualbox/debian trusty contrib
```

And add the VirtualBox repository's public key to your system:

```bash
wget -q http://download.virtualbox.org/virtualbox/debian/oracle_vbox.asc -O- | sudo apt-key add -
```

Run an update to pull in the repository:

```bash
sudo apt-get update
```

Then install VirtualBox 5.0:

```bash
sudo apt-get install virtualbox-5.0 -y
```

During the VirtualBox installation the '**vboxusers**' group is
created.  Add your user account to this group, which allow your user to
access USB devices from VirtualBox guests.  In this instance my user is
called '**vlab**':

```bash
sudo usermod -aG vboxusers vlab
```

Check if VirtualBox's module are loaded by running:

```bash
sudo /etc/init.d/vboxdrv status
```

Else run:

```bash
sudo /etc/init.d/vboxdrv setup
```

**Installing VirtualBox Extension Pack**
----------------------------------------

The VirtualBox Extension Pack enables additional support for USB 2.0 and
USB 3.0 devices, VirtualBox RDP and PXE boot for Intel cards.  Download
the extension package compatible with your version from
**http://download.virtualbox.org/virtualbox/** :

```bash
wget http://download.virtualbox.org/virtualbox/5.0.12/Oracle_VM_VirtualBox_Extension_Pack-5.0.12-104815.vbox-extpack
```

Install the pack using VBoxManage:

```bash
sudo VBoxManage extpack install Oracle_VM_VirtualBox_Extension_Pack-5.0.12-104815.vbox-extpack
```

**Installing phpVirtualBox**
----------------------------

phpVirtualBox is an open source PHP based AJAX web interface for
VirtualBox that mimics the desktop GUI allowing you to administrate it
via a web browser - links are on the
[virtualbox.org](https://www.virtualbox.org/) site under 'Hot Picks' or
you can go directly to
[phpVirtualBox's](http://sourceforge.net/projects/phpvirtualbox/) page.

To install it we need to download some prerequisites again, mainly
Apache, PHP and unzip:

```bash
sudo apt-get install apache2 php5 php5-mysql libapache2-mod-php5 php-soap unzip
```

Then we download the latest phpVirtualBox version from the official
site:

```bash
wget http://sourceforge.net/projects/phpvirtualbox/files/phpvirtualbox-5.0-5.zip
```

Unzip the files:

```bash
unzip phpvirtualbox-5.0-5.zip
```

Move the extracted files to Apache's root folder structure under
phpVirtualBox which will make it available via the browser under
http://&lt;YOUR\_IP\_ADDRESS&gt;/phpvirtualbox :

```bash
sudo mv phpvirtualbox-5.0-5 /var/www/html/phpvirtualbox
```

And grant full access to the folder:

```bash
sudo chmod 777 /var/www/html/phpvirtualbox
```

**Configuring phpVirtualBox**
-----------------------------

Configure a config file by copying the existing config.php-example:

```bash
sudo cp /var/www/html/phpvirtualbox/config.php-example /var/www/html/phpvirtualbox/config.php
```

Then edit the '**config.php**' file:

```bash
sudo nano /var/www/html/phpvirtualbox/config.php
```

and change the username/password to that of the user that will be
running VirtualBox (the user added to the '**vboxusers**' group earlier)
- in my exmple it will be vlab/vlab and save the changes:

```bash
[...]
var $username = 'vlab';
var $password = 'vlab';
[...]
```

In order for vboxweb-service start vboxwebsrv, the file
/etc/default/virtualbox must exist, create the file:

```bash
sudo nano /etc/default/virtualbox
```

and specify the setting for the user vboxweb will use (again I'm using
my account - **vlab**):

```bash
VBOXWEB_USER=vlab
```

And then start the service:

```bash
sudo /etc/init.d/vboxweb-service start
```

**Accessing phpVirtualBox**

You should now be able to browse over to
http://&lt;YOUR\_IP\_ADDRESS&gt;/phpvirtualbox and get the login prompt:

The default credentials are just **admin/admin**

From here you can manage your VM's exactly like you would with the
desktop application.

**Troubleshooting**
-------------------

If your console button appears to be greyed out confirm that the
extension pack was installed successfully using:

```bash
vboxmanage list extpacks
```

which should return '**Extension Packs:  1**' :

Also check if Remote Desktop is enabled on the Virtual Machine by clicking on
it, then selecting **Settings** -&gt; **Remote Display**

Your **Console** button should no be working
