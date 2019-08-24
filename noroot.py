#!/usr/bin/python
import os
def upgrade():
 os.system("apt update && apt upgrade")
def install():
 os.system("apt install -y ruby unstable-repo metasploit")

