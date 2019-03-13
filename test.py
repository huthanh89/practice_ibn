# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Library for NETCONF clients. Offer API to query the device.

from ncclient import manager
from pprint import pprint
import xmltodict

# -----------------------------------------------------------------------------
# Application
# -----------------------------------------------------------------------------

HOST_ADDRESS = "ios-xe-mgmt.cisco.com"
NETCONF_PORT = 10000
USERNAME = "root"
PASSWORD = "D_Vay!_10&"

# SSH into device.

with manager.connect(host=HOST_ADDRESS, 
    port=NETCONF_PORT, 
    username=USERNAME,
    password=PASSWORD, 
    hostkey_verify=False, 
    allow_agent=False, 
    look_for_keys=False) as deviceManager:

    pprint(deviceManager)
    pprint(deviceManager.connected)
    pprint(deviceManager.session_id)

    xmlResult = deviceManager.get_config(source='running').data_xml

    print(deviceManager.data_xml)

    # Write result into xml file.

    with open("%s.xml" % HOST_ADDRESS, 'w') as f:
        f.write(xmlResult)