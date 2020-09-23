from jinja2 import Template

# Example 1
name = input("Enter your name: ")
tm = Template("Hello {{name}} ")
msg = tm.render(name=name)
print(msg)

# Example 2
name = "ahmed"
age = 31
tm = Template("My name is {{name}} and I am {{age}} ")
msg = tm.render(name=name, age=age)
print(msg)
