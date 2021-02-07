""" Send configuration to device using Netmiko """

# Call Connect Handler function from Netmiko Library

from netmiko import ConnectHandler

connection = {
    "device_type": "cisco_ios",
    "host": "192.168.43.10",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco"
}
ssh_connect = ConnectHandler(**connection)  # Establish SSH session  with HOST

if ssh_connect:  # Check if the connection established !
    print("Connection Succeeded !\n")

output = ssh_connect.send_config_set("hostname SWx")
print(output)
