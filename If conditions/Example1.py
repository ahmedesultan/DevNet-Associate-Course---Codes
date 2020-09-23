
# Ask user to input some value
user_input = input("Enter your device vendor name: ")

if user_input.upper() == "cisco":
    print("You choosed", user_input)
elif user_input == "juniper":
    print("You choosed", user_input)
elif user_input == "huwawi":
    print("You choosed", user_input)

else:
    print("Your input is not supported, please enter a valid vendor name")