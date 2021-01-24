from meraki_sdk.meraki_sdk_client import MerakiSdkClient

# Cisco DevNet Sandbox Meraki API Key
X_CISCO_MERAKI_API_KEY = "59fb53d96b56dd9cf05e9848450f29d3da18f8d5"

# Establish a new client connection to the meraki REST API
MERAKI = MerakiSdkClient(X_CISCO_MERAKI_API_KEY)

# Get a list of all the organizations for the Cisco DevNet Account
ORGS = MERAKI.organizations.get_organizations()

for ORG in ORGS:
    print("\nOrg ID: {} and Org Name: {} \n".format(ORG['id'], ORG['name']))

PARAMS = {}

# Demo Organization "DevNet Organization"
PARAMS["organization_id"] = "549236"

# Get a list of all the networks for the Cisco DevNet organization
NETS = MERAKI.networks.get_organization_networks(PARAMS)

print("\n===================================================")
print("List of Networks in '549236' organization")
print("===================================================")

for NET in NETS:
    print("Network ID: {}, Name: {}, Tags: {}".
          format(NET['id'], NET['name'], str(NET['tags'])))

# Get a list of all devices that are part of the "DevNet Sandbox ALWAYS ON" Network
DEVICES = MERAKI.devices.get_network_devices("L_646829496481105433")

print("\n===================================================")
print("List of devices in 'L_646829496481105433' Network")
print("===================================================")

for DEVICE in DEVICES:
    print("Device Model: {}, Serial: {}, MAC:{}, Firmware:{}".
          format(DEVICE['model'], DEVICE['serial'], DEVICE['mac'], DEVICE['firmware']))
