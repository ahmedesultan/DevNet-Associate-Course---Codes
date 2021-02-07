""" Python Script to check if Telnet is enabled on a given IP from 'IPs.txt' file """

# Import telnet library
import telnetlib

with open('IPs.txt') as f:
    devices_list = f.readlines()

for device in devices_list:
    connection = telnetlib.Telnet(host=device.strip())

    if connection:
        print("Telnet is Enabled ✔")
    else:
        print("Telnet is Disabled ✘")
