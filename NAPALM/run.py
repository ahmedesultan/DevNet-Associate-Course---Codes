import napalm
import json

driver = napalm.get_network_driver('ios')
device = driver(hostname="192.168.43.10", username='admin', password='cisco')
device.open()

running = device.get_config(retrieve="running")
environment = device.get_environment()
interfaces = device.get_interfaces()

print(json.dumps(running))


device.close()
