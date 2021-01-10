
# Telnet to Multiple IPS and Return Output of specific commands

import telnetlib

ips = ["192.168.43.10", "192.168.43.11", "192.168.43.12", "192.168.43.13"]

# Declare variables to store user credentials
username = input("Enter Telnet Username: ")
user_password = input("Enter your Telnet Password: ")

for ip in ips:
    # Establish Telnet Connection
    connection = telnetlib.Telnet(host=ip)

    # Asks user for Telnet Username
    connection.read_until(b"Username: ")
    connection.write(username.encode("ascii") + b"\n")

    # Asks user for Telnet Password
    connection.read_until(b"Password: ")
    connection.write(user_password.encode("ascii") + b"\n")

    # connection.read_until(b">")
    # connection.write("enable".encode("ascii") + b"\n")

    # Enable Full output from Device
    connection.read_until(b"#")
    connection.write(b"terminal length 0" + b"\n")

    connection.read_until(b"#")

    # Print Success Message if connection succeded
    print("Success Connection to:", ip)
    print("")

    commands = ["show clock", "show ip int br"]

    for command in commands:
        connection.write(command.encode("ascii") + b"\n")

        output = connection.read_until(b"#")
        print(output.decode("ascii"))
