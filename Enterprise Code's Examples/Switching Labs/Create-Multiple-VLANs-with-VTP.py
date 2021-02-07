import getpass
import telnetlib

HOST = "192.168.43.10"
user = input("Welcome to Telnet. Enter your credentials: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"vtp domain cisco \n")

for i in range(1, 101):
    tn.write(b"Vlan " + str(i).encode('ascii') + b" \n")
    tn.write(b"name Vlan" + str(i).encode('ascii') + b" \n")

tn.write(b"end \n")
tn.write(b"exit \n")

print(tn.read_all().decode('ascii'))
