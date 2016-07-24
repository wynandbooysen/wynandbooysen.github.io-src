Title: Hosting Multiple WordPress Sites On Your VPS
Date: 2015-12-07 20:00
Author: Wynand Booysen
Category: Linux
Tags: vps, ubuntu, wordpress
Slug: hosting-multiple-wordpress-sites-on-your-vps
Status: published

The cost of running multiple WordPress sites on shared hosting
eventually starts adding up, or you might just want to move to a VPS
(Virtual Private Server) to have dedicated resources and a more
responsive site.

The truth is you can easily get a cheap VPS for the same price as a
WordPress site running on a shared host.

So what's the difference between shared hosting and a VPS?  Shared
hosting as the name implies means your resources, mainly CPU and RAM are
shared amongst several sites - which is why sites will be less
responsive. A VPS has an assigned or guaranteed amount of CPU and RAM
allocated to your VPS.

[DigitalOcean](https://www.digitalocean.com/?refcode=ae32c4293b17)
offers a one-click installer for WordPress VPS for only $10 a month to
run a single site - expensive but easy to get started and the site will
be capable of handling a lot of visitors.  You can however run WordPress
on the $5 a month VPS provided that you setup the server and install
WordPress yourself.

Setting up a server from scratch is an interesting learning opportunity
and can be loads of fun, but can also be a time consuming process.

If you want to quickly get up and running on a VPS the easiest solution
is to use the ServerPilot control panel from
[ServerPilot.io](https://www.serverpilot.io/?refcode=27e9d31b3beb)

ServerPilot's control panel allows you to connect to and manage your
VPS, which at the time of writing has to be a freshly installed Ubuntu
14.04 server.  The agent that gets pushed to the server will install and
configure NGINX, Apache, PHP and MySQL and allow you to deploy '*apps*'
which can be WordPress sites or other PHP sites from the GUI.

Creating a WordPress site is as easy as filling out a form with the
'*app*' name, domain name, checking the PHP version and WordPress tick
boxes and selecting the server after which you'll be prompted to set
your WordPress site admin name and password just like any other hosted
WordPress site.

You can manage multiple servers and apps on ServerPilot's free account
without any restrictions.  The paid options add extras like server
monitoring for a monthly fee.

Make use of this link when signing up for [Digital Ocean and you'll
receive $10 credit that will allow you to run their $5
instance](https://www.digitalocean.com/?refcode=ae32c4293b17), **FREE**
for two months for you to try out their services.  Also use this link
to [ServerPilot](https://www.serverpilot.io/?refcode=27e9d31b3beb) to get
started on the **FREE **tier.

Happy hosting!