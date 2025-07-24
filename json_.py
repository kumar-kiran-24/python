import json


x={
    "name":"kiran",
    "age":20,
    "department":"ise"
}
#using the  json data
y=json.dumps(x)
print(y)

#convert the json data into python dictionary
z=json.loads(y)
print(z["name"])

#convert python to json

a = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

b=json.dumps(a)
print(b)
