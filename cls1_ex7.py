import yaml
import json
from pprint import pprint as pp

with open("my_json.json", "r") as json_data:
    j_data = json.load(json_data)
    pp(j_data)

with open("my_yaml.yml", "r") as yaml_data:
    y_data = yaml.load(yaml_data)
    print(y_data)

