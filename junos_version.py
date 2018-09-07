#!/usr/bin/python

import getpass
import sys
import telnetlib

HOST = "10.19.11.81"
user = raw_input("Enter the username:")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login:")
tn.write(user+"\n")
if password:
	tn.read_until("Password:")
	tn.write(password+"\n")

tn.write("show version|no-more\n")
#tn.write("show system uptime|no-more\n")
tn.write("exit\n")
print tn.read_all()
















