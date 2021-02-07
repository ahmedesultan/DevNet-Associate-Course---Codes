# # # One Line Comment
# # # number1 = 10
# # # number2 = 20
# # # number3 = 30
# # # print(number3)
# # #
# # # names = ["ahmed", "ali"]
# # #
# # # sunrise = True
# # #
# # # course = "devnet"
# #
# # # names = ("ahmed", "mohammed", "ebrahim", "ahmed")
# #
# # # employees = {"ahmed": 31, "mohammed": 22, "ali": 20}
# #
# # devices = {
# #     "Sw1": "192.168.10.10",
# #     "Sw2": "192.168.10.20",
# #     "Sw3": "192.168.10.30",
# # }
# # print(devices["Sw3"])
#
# device_type = input("Enter your device type 'cisco' or 'juniper': ")
#
# if device_type == "cisco":
#     print("You choosed cisco")
#     print("You choosed cisco")
#     print("You choosed cisco")
#     print("You choosed cisco")
#     print("You choosed cisco")
#     print("You choosed cisco")
#     print("You choosed cisco")
#     print("You choosed cisco")
#     print("You choosed cisco")
#     print("You choosed cisco")
#
# elif device_type == "juniper":
#     print("You choosed juniper")
#     print("You choosed juniper")
#     print("You choosed juniper")
#     print("You choosed juniper")
#     print("You choosed juniper")
#     print("You choosed juniper")
#     print("You choosed juniper")
#     print("You choosed juniper")
#     print("You choosed juniper")
#     print("You choosed juniper")
#     print("You choosed juniper")
#     print("You choosed juniper")
#     print("You choosed juniper")
#
# else:
#     print("You choosed wrong device !")
#
# number1 = int(input("Enter your first number: "))
# number2 = int(input("Enter your second number: "))
#
# print("Addition = ", number1 + number2)
# print("Sub = ", number1 - number2)
# print("Multi = ", number1 * number2)
# print("Div = ", number1 / number2)
# print("Sum", number1 % number2)

# name = ["ahmed", "ali"]
# print(name[0])
# print(name[1])
#


# for i in range(100000):
#     print("Hello:", i)
#     i += 1

# name = input("Enter your name: ")
#
# if name == "ahmed":
#     print("Welcome", name)
#
# # elif name == "mohammed":
# #     print("Welocme", name)
#
# else:
#     print("Welcome", name)
#
# number = input("Please, Enter your phone number starting with country code:")
#
# if number.startswith("00966"):
#     print("You Entered Saudi Number")
# else:
#     print("You Entered Unkown number!")

# ip = input("Enter your IP Address: ")
#
# if ip.startswith("10"):
#     print("You Entered Class 'A' IP")
# elif ip.startswith("172"):
#     print("You Entered Class 'B' IP")
# elif ip.startswith("192"):
#     print("You Entered Class 'C' IP")
# else:
#     print("Unkown IP Address!")

# ips = ["192.168.1.1", "10.10.10.10", "172.16.1.1","1.1.1.1"]
#
# for i in ips:
#     print(i)

while True:

    ip = input("Enter your IP Address or type 'any keyword' to end script: ")

    if ip.startswith("10"):
        print("You Entered Class 'A' IP")

    elif ip.startswith("172"):
        print("You Entered Class 'B' IP")

    elif ip.startswith("192"):
        print("You Entered Class 'C' IP")

    else:
        break

    print("")
