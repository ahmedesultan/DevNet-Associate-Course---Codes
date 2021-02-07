""" create "commands.txt" file and fill it with your commands
and place it in the same folder as the .py file"""

file = open('commands.txt', 'w')
file.write("show running-config\nshow version\nshow clock")
print("Done Writing !")
file.close()



