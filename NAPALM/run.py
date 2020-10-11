import napalm


driver = napalm.get_network_driver('ios')
device = driver(hostname="192.168.43.10", username='admin', password='cisco')
device.open()
print(device.get_config(retrieve="running"))
print(device.get_environment())
device.close()