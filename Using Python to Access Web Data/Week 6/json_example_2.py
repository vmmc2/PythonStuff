# JSON Parsing Example 2
import json 

s = '''[
    {
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    },
    {
        "id" : "009",
        "x" : "7",
        "name" : "Chuck"
    }
]
'''

info = json.loads(s)
print("Length of the list:", len(info))
print(" ")

for element in info:
    print("Name:", element["name"])
    print("Id:", element["id"])
    print("Attribute:", element["x"])
    print(" ")

