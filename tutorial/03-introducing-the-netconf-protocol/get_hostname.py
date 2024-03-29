
# import the ncclient library
from ncclient import manager
import sys
import xml.dom.minidom
import pprint

# the variables below assume the user is leveraging the
# DEVNET Sandbox CSR1000v Lab 
#
# use the IP address or hostname of your CSR1000V device
HOST = 'ios-xe-mgmt.cisco.com'
# use the NETCONF port for your IOS-XE device
PORT = 10000
# use the user credentials for your IOS-XE device
USER = 'root'
PASS = 'D_Vay!_10&'


# create a main() method
def main():
    """
    Main method that retrieves the hostname from config via NETCONF.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:

        # XML filter to issue with the get operation
        # IOS-XE pre-16.2     YANG model called urn:ios
        # IOS-XE 16.2 - 16.4  YANG model called http://cisco.com/ns/yang/ned/ios
        # IOS-XE 16.5+        YANG model called http://cisco.com/ns/yang/Cisco-IOS-XE-native
        hostname_filter = '''
                          <filter>
                              <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                                  <hostname></hostname>
                              </native>
                          </filter>
                          '''                             
        result = m.get_config('running')
        xml_doc = xml.dom.minidom.parseString(result.xml)
        pprint.pprint(result.xml)


if __name__ == '__main__':
    sys.exit(main())
