import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler

# Define parameters for establishing ssh connection with netmiko
connection = {
    "device_type": "cisco_ios",
    "host": "192.168.43.10",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco"
}
# Establish SSH session  with HOST
ssh_connect = ConnectHandler(**connection)

# Check if the connection established successfully!
if ssh_connect:
    print("\nSSH Connection Established Successfully to host:", connection["host"], "\n")

# Load data from YAML file into python dictionary
config = yaml.safe_load(open("config.yml"))

# Load Jinja2 template
env = Environment(loader=FileSystemLoader("./"), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('config.j2')

# Render template using data and print the output
output = (template.render(config))

# Send configuration to the device via netmiko connection
result = ssh_connect.send_config_set(output, cmd_verify=False)

# Print the configuration to terminal
print(result)
