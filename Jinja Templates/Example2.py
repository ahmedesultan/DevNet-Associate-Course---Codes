"""Sending configuration generated with Jinja Template to cisco devices and export configuration in
external text file"""

from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler

# SSH connection parameters needed to establish ssh remote connection
connection = {
    "device_type": "cisco_ios",
    "host": "192.168.43.14",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco"
}
# Establish SSH session  with HOST
ssh_connect = ConnectHandler(**connection)

# Check if the connection established successfully!
if ssh_connect:
    print("SSH Connection Established Successfully!")

# Tell python to load all external files from the current directory
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("configure-interfaces-template.j2")

# Define which configuration you would like to use Jinja for
interface_dict = {
    "name": "G1/0",
    "description": "Server Port",
    "vlan": "10",
}

# Combine between dictionary attributes with Jinja templates variables
output = template.render(interface=interface_dict)
# print(output)

# Write result configuration to external file and take those configuration and send it back to the device
with open('Host {}-config.txt'.format(connection['host']), "w") as f:
    commands_list = f.write(output)
    print("Done Writing configuration to external file!")
    print("\nStart sending configuration to", connection["host"])
    ssh_connect.send_config_set(output, cmd_verify=False)
    ssh_connect.save_config()
    print("Finish sending configuration to", connection["host"])
