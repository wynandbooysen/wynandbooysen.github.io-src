Title: Using Ansible To Manage Mikrotik Devices
Date: 2017-01-07 10:57
Modified: 2017-01-07 10:57
Category: Mikrotik
Tags: script, router, firewall, ansible
Slug: using-ansible-to-manage-mikrotik-devices
Authors: Wynand Booysen
Summary: Using Ansible To Manage Mikrotik Devices

Mikrotik devices are very capable devices with lots of features for a reasonable price - the problem? Managing several devices and keeping your base configurations up-to-date and consistent.

Mikrotik devices have an application programming interface (API) that can be used for management, but you'll need to roll your own solution.  But they can also be accessed and managed via SSH.

Mikrotik does also provide software named The Dude which does network monitoring as well as some remote management, but in order to establish and maintain an consistent base line one really needs a configuration management tool.

So in order to use a configuration tool for Mikrotik devices, it has to be agentless and able to manage them over SSH - and easy to use.

So I picked Ansible since it met the criteria the best.  You need a server that can SSH into your Mikrotik devices which serves as the control server, and Ansible Playbooks which contain the tasks to be performed against the managed nodes and a list of hosts that need to be managed.  The Playbooks are written in YAML.  It works, but it's not perfect and here is why.

Mikrotik's RouterOS is based on the Linux kernel, but it is a minimal purpose built OS.  It doesn't have Python installed - which is what Ansible uses to manage the nodes.  It does check for Python on the node after connecting by default, but you have the option to override this in your Playbook and execute RAW commands directly against the node

It doesn't properly support pseudo terminals (PTY) which means the connection stays open/active and Ansible will appear to be hanging.

In previous versions of Ansible a PTY was only used when the command needed to be executed as root. An if statement prevented the code from always using it. Since Ansible v2+ a PTY is always used unless specifically disabled in the ansible.cfg by uncommenting a line.  This however is only disables it for Paramiko connections, which is a little bit slower, but not OpenSSH connections.  Paramiko also throws 'No handlers could be found for logger 'paramiko.transport'' when it encounters an error due to logging not being configured, but you can just use -vvvv when executing the Playbook to debug the errors.

These few quirks aside, Ansible does make it easier to manage Mikrotik devices.