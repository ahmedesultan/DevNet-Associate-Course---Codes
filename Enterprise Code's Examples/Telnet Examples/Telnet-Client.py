""" Python Script to Connect to Given Cisco Device via Telnet and Print out some output,
It takes all needed information from the user input into variables and run it directly in the code """

__author__ = "Ahmed Sultan"
__email__ = "asultan.sdn@gmail.com"

# Import telnet library to establish connection to telnet enabled devices.txt
import telnetlib

# Declare Variables to store credentials
# This is a new comment
host_ip = input("Enter your device IP: ")
username = input("Enter device Telnet Username: ")
user_password = input("Enter device Telnet Password: ")

connection = telnetlib.Telnet(host=host_ip)
connection.read_until(b"Username: ")
connection.write(username.encode('ascii') + b"\n")
connection.read_until(b"Password: ")
connection.write(user_password.encode('ascii') + b"\n")
connection.read_until(b"#")
connection.write(b"terminal length 0" + b"\n")
connection.read_until(b"#")

print("Success Connection!")

# Print Output
while True:
    command = input("Enter 'show' for showing configuration or 'health' for checking device health ")
    if "show" in command.lower():
        commands = ["show runn | i hostname",
                    "show ip int b",
                    "show ip route",
                    "show clock"]
    elif "health" in command.lower():
        commands = ["show arp",
                    "show version | i uptime",
                    "show inventory"]

        for cmd in commands:
            print("\n")
            print("*===========START OF OUTPUT=============*")
            connection.write(cmd.encode('ascii') + b"\n")
            output = connection.read_until(b"#")
            print(output.decode('ascii'))
            print("*===========END OF OUTPUT=============*")
            print(b"\n".decode('ascii'))
        print(b"\n".decode('ascii'))
