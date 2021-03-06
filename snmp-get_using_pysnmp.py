#!/usr/bin/python

from pysnmp.hlapi import *

errorIndication, errorStatus, errorindex, varBinds = next(
     getCmd(SnmpEngine(), 
	 CommunityData('public'),
	 UdpTransportTarget('10.19.11.81', 161),
	 ContextData(),
	 ObjectType(ObjectIdentity('SNMPv2-MIB', 'ifIndex', 510))
)
if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' %(errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

else:
    for varBind in varBinds:
	    print('=.join([x.prettyPrint() for x in varBind]))
