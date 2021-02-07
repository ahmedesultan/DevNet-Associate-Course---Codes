from dnacentersdk import api

# Create a DNA Center API connection object
# It uses DNA Center sandbox URL, username and password

DNAC = api.DNACenterAPI(username="devnetuser", password="Cisco123!", base_url="https://sandboxdnac2.cisco.com")

# Find all devices
DEVICES = DNAC.devices.get_device_list()

# Print select information about the retrieved devices
print('\n{0:25}{1:1}{2:45}{3:1}{4:15}'.format("Device Name", "|", "Device Type", "|", "Up Time", "|"))
print('-' * 95)

for DEVICE in DEVICES.response:
    print('{0:25}{1:1}{2:45}{3:1}{4:15}'.format(DEVICE.hostname, "|", DEVICE.type, "|", DEVICE.upTime))
    print('-' * 95)

print("\n\n")

# Get the health of all clients on Thursday, August 22, 2019 8:41:29 PM GMT
CLIENTS = DNAC.clients.get_overall_client_health(timestamp="1566506489000")

# Print select information about the retrieved client health statistics
print('{0:25}{1:1}{2:45}{3:1}{4:15}'.format("Client Category", "|", "Number of Clients", "|", "Clients Score", "|"))
print('-' * 95)

for CLIENT in CLIENTS.response:
    for score in CLIENT.scoreDetail:
        print('{0:25}{1:1}{2:45}{3:1}{4:15}'.format(score.scoreCategory.value, "|", score.clientCount, "|",
                                                    score.scoreValue))
        print('-' * 95)
