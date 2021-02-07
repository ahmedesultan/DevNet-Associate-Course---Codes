# Call ConnectHandler function from netmiko to establish ssh connections
from netmiko import ConnectHandler

cisco_switches = ["192.168.43.10", "192.168.43.11", "192.168.43.12", "192.168.43.13"]

for ip in cisco_switches:
    ssh_info = {
        "device_type": "cisco_ios",
        "host": ip.strip(),
        "username": "admin",
        "password": "cisco",
        "secret": "cisco"
    }
    net_connect = ConnectHandler(**ssh_info)
    output = net_connect.send_command("show runn | i hostname")
    print(output)
