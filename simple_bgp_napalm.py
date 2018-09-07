#!/usr/bin/python

import json
from napalm import get_network_driver
from getpass import getpass
from datetime import datetime


print "Connecting to Juniper devices"
jnpr_device = raw_input("Enter the Juniper Device IP Address:")
username = raw_input("Username:")
password = getpass("Password:")			   

junos_driver = get_network_driver("junos")
vsrx_in_snt = junos_driver(hostname=jnpr_device, username=username, password=password)
vsrx_in_snt.open()
junos_bgp_neighbors = vsrx_in_snt.get_bgp_neighbors()
print (vsrx_in_snt.get_bgp_neighbors())
#print(json.dumps(junos_bgp_neighbors,indent=4)
#vsrx_in_snt.close()
