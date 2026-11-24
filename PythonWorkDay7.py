#DAY 07
demo_dict = {"person 01": {"name": "Ali",
                           "age": 24,
                           "City": ["Karachi", "Lahore", "Islamabad"]
                           },
                           "person 02": {"name": "Khan",
                                         "age": 43,
                                         "City": ["Quetta", "Multan", "Faisalabad"]
                                         }
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
print(demo_dict)
print(list(demo_dict["person 01"].values())[2])
second_dict = (list(demo_dict["person 01"].values())[0])
print(second_dict)
demo_dict.pop()
print(demo_dict)
demo_dict.clear()
print(demo_dict)
dict = demo_dict.copy()
print(dict)
x = (34, 45, 545)
y = ("Ali", "Khan", "Junaid")
dict = demo_dict.fromkeys(x,y)
print(dict)