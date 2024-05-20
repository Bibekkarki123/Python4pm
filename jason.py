
# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y['age'])


# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)



# import json

# print(json.loads('{"name": "John", "age": 30}'))
# print(json.dumps({"name": "John", "age": 30}))



# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


# import json

# data = {
#     'name':'ram',
#     'age': 20,
#     'address':'kathmandu'
# }
# json_data = json.dumps(data)
# print(json_data)

# json_data1 = json.loads(json_data)
# print(json_data1)