#!/usr/bin/python

import json
from napalm import get_network_driver
from getpass import getpass
from datetime import datetime

print "Connecting to Juniper devices"
jnpr_device = ["10.19.11.81",
               "10.19.11.82",
			   "10.19.11.83"]

username = raw_input("Username:")
password = getpass("Password:")			   

for ip_addr in jnpr_device:		   
#with jnpr_device as ip_addr:
    junos_driver = get_network_driver("junos")
    vsrx_in_snt = junos_driver(hostname=ip,
	                           username=username,
							   password=password)
    vsrx_in_snt.open()
	
    if vsrx_in_snt.is_alive()["is Alive"]:
        print str(datetime.now()) + " Getting bgp neighbors information from {}" .format(ip_addr)
        print(json.dumps(vsrx_in_snt.get_bgp_neighbors(), indent=4)
        print "=" *80
else:
# Code the ping module here  
        print "ALERT: Device {} is unreachable, please check the availability" .format(ip_addr)
