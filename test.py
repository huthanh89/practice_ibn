# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Library for NETCONF clients. Offer API to map XML to Python construct.

from ncclient import manager
from pprint import pprint

HOST = "ios-xe-mgmt.cisco.com"
PORT = 10000
USER = "root"
PASS = "D_Vay!_10&"

# SSH into device.

with manager.connect(host=HOST, port=PORT, username=USER, password=PASS, hostkey_verify=False, allow_agent=False, look_for_keys=False) as device:

    pprint(device)
    pprint(device.connected)
    pprint(device.session_id)

    xmlResult = device.get_config(source='running').data_xml

    print(device.data_xml)

    # Write result into xml file.

    with open("%s.xml" % HOST, 'w') as f:
        f.write(xmlResult)