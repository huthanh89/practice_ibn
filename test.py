from ncclient import manager
import xml.dom.minidom

#m = manager.connect(host='10.29.1.110', port=830, username='cisco',password='cisco', device_params={'name': 'csr'})

HOST = 'ios-xe-mgmt.cisco.com'
PORT = 8181
USER = 'root'
PASS = 'D_Vay!_10&'

netconf_connection = manager.connect(host=HOST,
    port=PORT,
    username=USER,
    password=PASS,
    hostkey_verify=False)


#config = netconf_connection.get_config("running")

print(netconf_connection)

#print(xml.dom.minidom.parseString(config.xml).toprettyxml())

#for c in m.server_capabilities:
#    print(c)