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
print "Trying to login to root shell"
remote_connection.send("start shell user root\n")
time.sleep(0.5)

print "Passing the password"
remote_connection.send("snt123\n")
time.sleep(1)

print "Logged in as root"

for n in range(1,51):
#      print "Iteration number -" + str(n)
      remote_connection.send("ifconfig ge-0/0/1 down")
      print "Interface ge-0/0/1 is taken down"
      time.sleep(0.1)

      remote_connection.send("ifconfig ge-0/0/1 up")
      print "Interface ge-0/0/1 is brought up"
      time.sleep(0.1)

ssh_client.close()
