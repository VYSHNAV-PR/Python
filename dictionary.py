#creating dictionary 
# my_dict={
#     "name":"vyshnav",
#     "age":24,
#     "place":"Perintalmanna"
# }
# print(my_dict)

# another_dict=dict(name="hari",age=24,place="manarkad")
# print(another_dict)

#empty dictionary
# empty={}
# print(empty)

#accessing the dictionary
# my_dict={
#     "name":"vyshnav",
#     "age":24,
#     "place":"Perintalmanna"
# }
# print(my_dict["name"])
#accessing the dictionary using .get
# my_dict={
#     "name":"vyshnav",
#     "age":24,
#     "place":"Perintalmanna"
# }
# print(my_dict.get("name"))

#adding item to dictionary
add={"name":"vyshnav","age":24,"place":"pmna"}
new=add["name"]="hari"
city=add["city"]="kochi"
print(add)

#removing item from dictionary-pop()
# dd={"name":"vyshnav","age":24,"place":"pmna"}
# dd.pop("place")
# print(dd)
#popitem
# add1={"name":"vyshnav","age":24,"place":"pmna"}
# add1.popitem()
# print(add1)
#del 
# add1={"name":"vyshnav","age":24,"place":"pmna"}
# del add1["age"]
# print(add1)
#copy
# add1={"name":"vyshnav","age":24,"place":"pmna"}
# copyy=add1.copy()
# print(copyy)
#clear
# dd1={"name":"vyshnav","age":24,"place":"pmna"}
# dd1.clear()
# print(dd1)

#nested dictionary
my_dict={
    "person1":{"name":"vyshnav","age":24},
    "person2":{"name":"hari","age":24}
}
print(my_dict)
#accessing the nested dictionary
my_dict={
    "person1":{"name":"vyshnav","age":24},
    "person2":{"name":"hari","age":24}
}
print(my_dict["person1"]["name"])
print(my_dict["person2"]["name"])
#modify the nested dictionary
my_dict={
    "person1":{"name":"vyshnav","age":24},
    "person2":{"name":"hari","age":24}
}
add=my_dict["person1"]["place"]="pmna"
add1=my_dict["person2"]["place"]="mnrkd"
print(my_dict)

#dict methods-keys()
dict={"names":"vyshnav","age":24}
print(dict.keys())
#values()
dict={"names":"vyshnav","age":24}
print(dict.values())
#items()
dict={"names":"vyshnav","age":24}
print(dict.items())
#update
dict={"names":"vyshnav","age":24}
upd=dict.update({"age":25,"city":"kochi"})
print(dict)
#fromkeys
keys=["names","age"]
new_key=dict.fromkeys(keys,"unknown")
print(new_key)
#setdefault()
my_dict = {"name": "John", "age": 30}
city = my_dict.setdefault("city", "New York")
print(city)
print(my_dict)