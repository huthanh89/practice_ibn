#
# Get configured interfaces using Netconf
#

from ncclient import manager
import sys
import xml.dom.minidom
import os
from xml.dom.minidom import parse, parseString

# the variables below assume the user is leveraging the
# network programmability lab and accessing csr1000v
# use the IP address or hostname of your CSR1000V device
HOST = 'ios-xe-mgmt.cisco.com'
# use the NETCONF port for your CSR1000V device
PORT = 10000
# use the user credentials for your CSR1000V device
USER = 'root'
PASS = 'D_Vay!_10&'
# XML file to open
FILE = 'get_interfaces.xml'

# create a main() method
def get_configured_interfaces(xml_filter):
    with manager.connect(host=HOST, port=PORT, username=USER,
                        password=PASS, hostkey_verify=False,
                        device_params={'name': 'default'},
                        allow_agent=False, look_for_keys=False) as m:
                        
        return(m.get_config('running', xml_filter))


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, FILE));

dom = parse(f)  # parse an open file

interfaces = get_configured_interfaces(dom.toxml())
interfaces = xml.dom.minidom.parseString(interfaces.xml)
interfaces = interfaces.getElementsByTagName("interfaces")
print(interfaces[0].toprettyxml())
