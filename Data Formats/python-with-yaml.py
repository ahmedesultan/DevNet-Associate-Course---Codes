import yaml

with open("Example1.yml") as f:
    result = yaml.safe_load(f)
    print(result)
