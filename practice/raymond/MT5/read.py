import json as j

x = open("get_info.json")
data = j.load(x)
print(data)