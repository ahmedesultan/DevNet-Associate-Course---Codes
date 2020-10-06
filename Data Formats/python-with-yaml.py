import yaml

with open("Example1.yml") as f:
    result = yaml.load(f)
    print(result)