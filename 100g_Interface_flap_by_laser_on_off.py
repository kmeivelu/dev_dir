#!/usr/bin/python
import time
import paramiko
import getpass

ip_address = raw_input("Enter the IP Address of the router:")
username = raw_input("Username:")
password = getpass.getpass("Password:")

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username, password=password)

print "Successful connection to ", ip_address

remote_connection = ssh_client.invoke_shell()
print "Trying to login to PFE shell"
remote_connection.send("start shell pfe network fpc1\n")
time.sleep(0.5)

#print "Passing the password"
#remote_connection.send("snt123\n")
#time.sleep(1)

print "Logged in to the Line card"

for n in range(1,51):
#      print "Iteration number -" + str(n)
      remote_connection.send("test qsfp 12 laser off")
      print "et-1/1/5 - Laser turned off"
      time.sleep(1)

      remote_connection.send("test qsfp 12 laser on")
      print "et-1/1/5 - Laser turned back on "
      time.sleep(1)

ssh_client.close()