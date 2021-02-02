#! /usr/bin/env python
"""
Script showing how to create multiple vlans on Cisco IOS Switches by reading VLANS ID and Name from Excel File.
"""

import csv
from jinja2 import Template
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException  # Device Unreachable
from netmiko.ssh_exception import SSHException  # SSH is not enabled
from netmiko.ssh_exception import AuthenticationException  # SSH Authentication error
import pyfiglet

# Prints Banner with tool name
banner = pyfiglet.figlet_format("VLANs Creator", font="doom")
print(banner)

# Read Vlan Excel File
# source_file = "vlans-info.csv"

# Read VLAN Template File
vlans_template_file = "switch-vlans-template.j2"

# Asks user for Switch credentials
host_ip = input("Enter your device IP: ")
username = input("Enter device SSH Username: ")
user_password = input("Enter device SSH Password: ")
enable_secret = input("Enter device Enable Password: ")
source_file = input("Enter your Excel file name with .csv extension: ")

device = {
    "address": host_ip,
    "device_type": "cisco_ios",
    # "ssh_port": 22,
    "username": username,
    "password": user_password,
    "secret": enable_secret
}

# String that will hold final full configuration of all VLANS
vlans_configs = ""

# Open up the Jinja template file (as text) and then create a Jinja Template Object
with open(vlans_template_file) as f:
    vlans_template = Template(f.read(), keep_trailing_newline=True)

# Open up the CSV file containing the data
with open(source_file) as f:
    # Use DictReader to access data from CSV
    reader = csv.DictReader(f)
    # For each row in the CSV, generate an vlan configuration using the jinja template
    for row in reader:
        vlan_config = vlans_template.render(
            vlan=row["ID"],
            name=row["Name"],
        )

        # Append this vlan configuration to the full configuration
        vlans_configs += vlan_config

# Save the final configuraiton to a file
with open("vlans_configs.txt", "w") as f:
    f.write(vlans_configs)

# Use Netmiko to connect to the device and send the configuration
try:
    print("Try connecting to device:", device["address"])
    with ConnectHandler(ip=device["address"],
                        # port=device["ssh_port"],
                        username=device["username"],
                        password=device["password"],
                        device_type=device["device_type"],
                        secret=device["secret"]) as ch:
        print("Connection Successful, Creating VLANS in progress ... !")
        print("It will print out the result on the terminal and pushes it to your switch automatically")
        config_set = vlans_configs.split("\n")
        output = ch.send_config_set(config_set)
        print(output)

except (AuthenticationException):
    print("Authentication Failure:", device["address"])

except (NetMikoTimeoutException):
    print("Timeout to device:",
          device["address"], ", Check the host IP and Make sure it's Up and Running")


except(SSHException):
    print("SSH Issue, Are you sure SSH is enabled?", device["address"])


except Exception as unkown_error:
    print("Some other error:"), unkown_error
