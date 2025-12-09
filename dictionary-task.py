#1.Create a dictionary with keys "name" and "age" and values "Nik" and 20 .
dicttt={
    "name":"Nik",
    "age":20
}
print(dicttt)
#2.Access the value of key "name" from {"name": "Nik", "age": 20} .
print(dicttt["name"])
#3.Add a new key "city" with value "Delhi" to {"name": "Nik", "age": 20} .
new=dicttt.update({"city":"Delhi"})
print(dicttt)
#4.Update the value of "age" to 25 in {"name": "Nik", "age": 20} .
a={"name": "Nik", "age": 20}
n=a["age"]=25
print(a)
#5.Delete the key "age" from {"name": "Nik", "age": 20} .
b={"name": "Nik", "age": 20}
remove=b.pop("age")
print(b)
#6. Check if the key "email" exists in {"name": "Nik", "age": 20}.
c={"name": "Nik", "age": 20}
print("email" in c)
#7. Get all keys from {"name": "Nik", "age": 20} using a dictionary method.
d={"name": "Nik", "age": 20}
print(d.keys())
#8. Get all values from {"name": "Nik", "age": 20} using a dictionary method.d={"name": "Nik", "age": 20}
d={"name": "Nik", "age": 20}
print(d.values())
#9.Convert the dictionary {"a": 1, "b": 2} into a list of (key, value) pairs.
my_dict={"a": 1, "b": 2} 
list_pair=list(my_dict.items())
print(list_pair)
#10.Create a dictionary from two lists: (use zip method) 
key = ["name", "age"]
value = ["Nik", 20]
my_dict = dict(zip(key, value))
print(my_dict)
#11. Count how many keys are in {"a": 1, "b": 2, "c": 3} .
x = {"a": 1, "b": 2, "c": 3}
key_count=len(x.keys())
print(key_count)
#12. Merge two dictionaries {"a": 1} and {"b": 2} into one. 
d1={"a": 1}
d2= {"b": 2}
d1.update(d2)
print(d1)
#13.Clear all elements from {"a": 1, "b": 2} using a dictionary method.
merged={"a": 1, "b": 2}
merged.clear()
print(merged)
#14.Copy the dictionary {"x": 10, "y": 20} using a dictionary method.
coppy={"x": 10, "y": 20}
copied=coppy.copy()
print(copied)
#15.Get the value of key "salary" safely from {"name": "Nik", "age": 20} without getting an error.
details={"name": "Nik", "age": 20}
print(details.get("salary"))
#16.From {"a": 1, "b": 2, "c": 3} , remove the last inserted item using a dictionary method
detail={"a": 1, "b": 2, "c": 3}
last_item=detail.popitem()
print(last_item)
print(detail)
#17.Given student = {"name": "Rahul", "marks": {"math": 90, "science": 85}} ,access only the "science" marks.
student = {"name": "Rahul", "marks": {"math": 90, "science": 85}} 
access=student["marks"]["science"]
print("Mark Obtained for Science:",access)
#18. From the above student dictionary, update "math" marks to 95 .
change=student["marks"]["math"]=95
print("Mark Obtained for Math:",change)
#19.Add a new subject "english": 88 inside the "marks" dictionary
add=student["marks"]["english"]=88
print(student)
#20. Delete the subject "science" from inside "marks" .
deleting=student["marks"].pop("science")
print(student)