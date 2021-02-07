""" Get All switches 'hostname' with Netmkio """

from netmiko import ConnectHandler
from netmiko.ssh_exception import AuthenticationException  # SSH Authentication error Exception
from netmiko.ssh_exception import NetMikoTimeoutException  # Device Unreachable Exception
from netmiko.ssh_exception import SSHException  # SSH is not enabled Exception

# Define all switches IPs in a List
cisco_switches = ["192.168.43.10", "192.168.43.11", "192.168.43.12", "192.168.43.13"]

for ip in cisco_switches:
    try:
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

    # Raise this Exception if SSH Username or Password is wrong
    except AuthenticationException:
        print("Authentication Failure:", ssh_info["host"])

    # Raise this Exception if Device is down or the link is down
    except NetMikoTimeoutException:
        print("Timeout to device:", ssh_info["host"], ", Check the host IP and Make sure it's Up and Running")

    # Raise this Exception if SSH is not enabled
    except SSHException:
        print("SSH Issue, Are you sure SSH is enabled?", ssh_info["host"])

    # Raise this Exception for anything else
    except Exception as unkown_error:
        print("Some other error:"), unkown_error
