# Call ConnectHandler function from netmiko to establish ssh connections
from netmiko import ConnectHandler

connection = {
    "device_type": "cisco_ios",
    "host": "192.168.43.12",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco",
}

# Estabkish SSH connection to Dictionary attributes
ssh_connect = ConnectHandler(**connection)

if ssh_connect:  # Check if ssh successful
    print("Success!")

output = ssh_connect.send_command("show version")
print(output)
