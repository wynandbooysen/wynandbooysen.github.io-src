Title: Windows 10: Installing software using PackageManagement (OneGet)
Date: 2015-12-22 04:00
Author: Wynand Booysen
Category: Windows
Slug: windows-10-installing-software-using-packagemanagement-oneget
Status: published

The best feature to be included with Windows 10 has to be the
command-line based installer, at least for those of us in a SysAdmin
and/or DevOps role.

For those of you that have worked on Linux before and have used Yum and
Apt-Get, this is Microsoft's attempt to provide a similar experience for
the Windows platform.

It's been over a year since this was introduced in the Preview versions
of Windows 10 so its still fairly new.  I found it wasn't as easy to get
it going as a lot of articles and tutorials still reference the OneGet
commands and since its been renamed to PackageManagement there has been
some minor changes.

To use PackageManagement (OneGet) on Windows 10 make sure you set the
PowerShell execution policy to 'RemoteSigned' otherwise it will fail
silently
([bug](https://github.com/OneGet/oneget/issues/97#issuecomment-139331418))

```powershell
Set-ExecutionPolicy RemoteSigned
```

Add the Chocolatey plugin and repository using this one-liner to get
access to 3rd party applications from the Chocolatey repository, the

```powershell
-Force
```
flag performs a bootstrap that takes care of both:

```powershell
Get-PackageProvider Chocolatey -Force | Out-Null
```

That's it, we are ready to install some applications, using the ```-Force``` flag is similar
to ```-y```  used with
Yum and Apt-Get which assumes Yes when prompted:

-   VLC Media Player:

```powershell
Install-Package vlc -Force | Out-Null
```

-   Skype:

```powershell
Install-Package skype -Force | Out-Null
```

-   7zip:

```powershell
Install-Package 7zip -Force | Out-Null
```

-   Atom:

```powershell
Install-Package atom -Force | Out-Null
```

Or you can search for your favorite applications using this command:

```powershell
Find-Package <application> -Force
```

There isn't a lot of applications available and some of those in the
Chocolatey repository simply do not work.

Hopefully we will see software companies (like Adobe, VMWare and Oracle
) providing official repositories going forward, to ease the deployment
and provisioning of systems in the future using the command-line.
