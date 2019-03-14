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

# ssh -p 10000 root@ios-xe-mgmt.cisco.com
# putty.exe -ssh root@ios-xe-mgmt.cisco.com:10000 -pw "D_Vay!_10&"

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


    # -----------------------------------------------------------------------------
    # Get Device Status
    # -----------------------------------------------------------------------------

    print("Device Connected:")
    print(deviceManager.connected)

    print("Session ID: ") 
    print(deviceManager.session_id)

    # -----------------------------------------------------------------------------
    # Get Capabilities
    # -----------------------------------------------------------------------------

    #for c in deviceManager.server_capabilities:
    #    print(c)

    # -----------------------------------------------------------------------------
    # Get xml from source and print to output.
    # -----------------------------------------------------------------------------

    #xmlResult = deviceManager.get_config(source='running').data_xml
    
    #with open("%s.xml" % HOST_ADDRESS, 'w') as f:
    #    f.write(xmlResult)