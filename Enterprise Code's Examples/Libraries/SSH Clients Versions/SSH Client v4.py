from netmiko import ConnectHandler

"""SSH Client to Send Configuration Command to Devices"""

# Open devices.txt file and read each device ip
with open('devices.txt') as d:
    devices_list = d.readlines()
    # print(devices_list)

# Loop through each device in "devices.txt" file
for devices in devices_list:
    ios_device = {
        'device_type': 'cisco_ios',
        'host': devices.strip(),
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco'
    }

    print("\n-------------------------------------")
    print("Connecting to device:", devices.strip())
    print("---------------------------------------")

    # Establish SSH connection to devices.txt
    net_connect = ConnectHandler(**ios_device)

    # Push command "hostname Swx" in Configuration mode for every device
    output = net_connect.send_config_set("hostname SWx")
    print(output)
