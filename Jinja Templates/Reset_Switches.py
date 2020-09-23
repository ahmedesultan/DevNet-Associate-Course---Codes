"""Sending interfaces configuration generated with Jinja Template to cisco devices to reset interfaces"""

from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
import pyfiglet

# Prints Banner with tool name
banner = pyfiglet.figlet_format("Reset", font="doom")
print(banner)


# Define list of switches ips
cisco_switches = ["192.168.43.10", "192.168.43.11", "192.168.43.12", "192.168.43.13"]

for switch in cisco_switches:
    # SSH connection parameters needed to establish ssh remote connection
    connection = {
        "device_type": "cisco_ios",
        "host": switch.strip(),
        "username": "admin",
        "password": "cisco",
        "secret": "cisco"
    }
    # Establish SSH session  with HOST
    ssh_connect = ConnectHandler(**connection)

    # Check if the connection established successfully!
    if ssh_connect:
        print("\nSSH Connection Established Successfully to host:", connection["host"])

    # Tell python to load all external files from the current directory
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("reset-interfaces-template.j2")

    interfaces = ["G1/0", "G1/1", "G1/2", "G1/3"]

    # Define which configuration you would like to use Jinja for
    for interface in interfaces:
        interface_dict = {
            "name": interface.strip(),
        }

        # Combine between dictionary attributes with Jinja templates variables
        output = template.render(interface=interface_dict)
        ssh_connect.send_config_set(output, cmd_verify=False)
        ssh_connect.save_config()
    print("Finish sending configuration to", connection["host"])
    print("-----------------------------------------------------\n")
