import telnetlib

# Declare variables to store user credentials
host_ip = input("Enter your devcice IP: ")
username = input("Enter Telnet Username: ")
user_password = input("Enter your Telnet Password: ")

# Establish Telnet Connection
connection = telnetlib.Telnet(host=host_ip)

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
print("Success Connection to:",host_ip)
print("")

# Iterate through user command's input
while True:
    command = input("Please enter your command: ")
    connection.write(command.encode("ascii") + b"\n")

    output = connection.read_until(b"#")
    print(output.decode("ascii"))

    # Exit if user enters "exit"
    if command == "exit" or command == "Exit":
        break
