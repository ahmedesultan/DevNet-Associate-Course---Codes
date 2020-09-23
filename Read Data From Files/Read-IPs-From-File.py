""" First create "ip-list.txt" file and fill it with your IPs
and place it in the same folder as the .py file"""

file = open("ip-list.txt", "r")
ips = file.readlines()
for ip in ips:
    print("IP Address is: ", ip.strip())
file.close()


