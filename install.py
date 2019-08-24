#!/usr/bin/python

import sys
import os
import noroot
import root
import banner
from colours import *

os.system("clear")

print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█              Metasploit for termux Installer                 █
█                                                              █
└══════════════════════════════════════════════════════════════┘     \033[1;m""")

banner.heading()
if not os.geteuid() == 0:
 prRed("Your device is not rooted")
 prYellow("Continuing the old method for non root users")
 prCyan("This will need to download about 200mb and takes upto 600mb diskspace")
 noroot.upgrade()
 noroot.install()
else:
 root()

