#!/usr/bin/python

import getpass
import sys
import telnetlib

for n in range(1, 4):
  ip_address = "10.19.11.8" + str(n)
  user = raw_input("Enter the username:")
  password = getpass.getpass()

  tn = telnetlib.Telnet(ip_address)

  tn.read_until("login:")
  tn.write(user+"\n")
  if password:
	  tn.read_until("Password:")
	  tn.write(password+"\n")

  tn.write("show version\n")
  tn.write("show system uptime\n")
  tn.write("exit\n")
  print tn.read_all()
#  print ip_address 
