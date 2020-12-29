# def user_data():
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     job = input("Enter your Job title: ")
#     print("Your name is:", name, "and you are", age, "and you work as", job)
#
#
# def financial_data():
#     salary = int(input("Enter your salary per month: "))
#     print("You earn", salary * 12, "per year")

# def router(model, ip):
#     print("Router Model: ", model, "and Routr IP is:", ip)
#
#
# router("1900", "192.168.1.1")
# def calc(arg1, arg2):
#     add = arg1 + arg2
#     sub = arg1 - arg2
#     mult = arg1 * arg2
#     div = arg1 / arg2
#
#     print("Add:", add)
#     print("Sub:", sub)
#     print("Multi:", mult)
#     print("Div:", div)

def router():
    print("You entered Router Function")


def switch():
    print("You entered Switch Function")


while True:
    device_type = input("Enter your device type or any keyword to exit: ")

    if device_type == "Router":
        router()
    elif device_type == "Switch":
        switch()
    else:
        break
