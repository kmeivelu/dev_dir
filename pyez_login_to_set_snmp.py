#!/usr/bin/python

from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from pprint import pprint

#import sys

#hostname = input("Enter the Juniper Device IP Address:")
hostname = raw_input ("Enter the Juniper Device IP Address:")
username = raw_input("Username:")
password = getpass("Password:")

device = {"host": hostname, "user": username, "passwd": password}

#with Device(**device) as jnpr_device:
#    pprint(jnpr_device.facts)

jnpr_device = Device(**device)
jnpr_device.open()

cfg = Config(jnpr_device)
print "Setting hostname using set notation"
#cfg.load("set snmp community public authorization read-write", format="set", merge=True)

print "Setting SNMP configuration usinf XML"
cfg.load(path="/root/load_snmp_config.xml", format="xml", merge=True)

print "Current config differences"
print cfg.diff()

#print "Performing rollback"
#cfg.rollback(0)

print "Performing commit"
cfg.commit()

jnpr_device.close()

