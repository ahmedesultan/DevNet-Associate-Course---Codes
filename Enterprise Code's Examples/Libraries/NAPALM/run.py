import napalm

driver = napalm.get_network_driver('ios')
device = driver(hostname="192.168.43.10", username='admin', password='cisco')
device.open()

users = device.get_users()
print(users)

interfaces = device.get_interfaces()
print(interfaces)
