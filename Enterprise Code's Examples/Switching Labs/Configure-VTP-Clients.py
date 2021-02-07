import getpass
import telnetlib

user = input("Enter your name: ")
password = getpass.getpass()

for i in range(10, 14):
    HOST = "192.168.43." + str(i)
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"conf t\n")
    tn.write(b"vtp mode client \n")
    tn.write(b"end \n")
    tn.write(b"wr \n")
    tn.write(b"exit \n")

    print(tn.read_all().decode('ascii'))
