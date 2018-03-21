import json
import yaml


a_list = [100, {'key1':'yaml', 'key2':'json'}, 'class1_exercise6']


with open("my_yaml.yml", "w") as f:
    f.write(yaml.dump(a_list))


with open("my_json.json", "w") as f:
    json.dump(a_list, f)

