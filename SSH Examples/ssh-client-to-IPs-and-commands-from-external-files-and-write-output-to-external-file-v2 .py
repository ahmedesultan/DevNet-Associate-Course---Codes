# Import ConnectHandler function from netmiko library to initiate ssh connections
# Import date and time functionality from datetime library
from datetime import datetime

from netmiko import ConnectHandler

"""First of all, create a text file with name "commands.txt" and put some
commands.txt inside and create another text file with name "devices.txt" and
put devices.txt ips inside."""

# Open commands.txt file and read each command
with open('commands.txt') as f:
    commands_list = f.readlines()

# Open devices.txt file and read each device ip
with open('devices.txt') as f:
    devices_list = f.readlines()

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

    # Establish SSH connection to devices.txt
    net_connect = ConnectHandler(**ios_device)

    # Loop through each command in "commands.txt" file
    for command in commands_list:
        output = net_connect.send_command(command.strip())
        print(output)

        # This section for exporting "output" to external file
        # create file with ip and date of the current time
        file = open('Host {} - {}-config.txt'.format(ios_device['host'], datetime.now().date()), 'w')
        file.write("-------------------------\n")
        file.write("Host {}".format(ios_device['host']))
        file.write("\n")
        file.write(output)
        file.close()
