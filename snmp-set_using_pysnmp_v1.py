from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    setCmd(SnmpEngine(),
           CommunityData('private'),
           UdpTransportTarget(('10.19.11.81', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('IF-MIB', 'ifAdminStatus', 510),2))
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))

