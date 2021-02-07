vendors = ["cisco", "juniper", "huwawi", "arista"]

# Ask user to input some value and check if its in "vendors" list
user_input = input("Please enter your vendor name: ")

if user_input in vendors:
    print("True")
else:
    print("False!")



