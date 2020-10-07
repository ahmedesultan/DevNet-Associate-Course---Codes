from nornir import InitNornir
from nornir_netmiko import netmiko_send_config, netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir("config.yml")

# send only one command to hosts
# result = nr.run(netmiko_send_command, command_string="sh ip int brief")

# send command from file 'commands' to hosts
result = nr.run(netmiko_send_config, config_file="commands")
print_result(result)
