demo_dict = {"name": "Ali",
             "age": 24,
             "City": "Lahore"
             }
print(demo_dict)
print(type(demo_dict))
demo_dict["City"] = "Karachi"
print(demo_dict)
print(demo_dict["name"])
print(list(demo_dict.keys())[1])
print(list(demo_dict.get())[2])
print(list(demo_dict.values())[2])
print(list(demo_dict.items())[0])
