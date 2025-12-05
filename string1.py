# str="hello, world!"
# print(str[1:10])
# print(str[-6:])
# print(str[0:13:2])
# print(str[::-1])

# s="Hello world!"
# new_s=s.replace("world","python")
# print(new_s)

#concatenation
# s1="hello"
# s2="python"
# result=s1+","+s2+"!"
# print(result)
# print(s1.upper())

# words=['python','is','awesome']
# res=" ".join(words)
# print(res)

#format string
# name="vyshnav"
# age=24
# format_string="My name is %s, and iam %d years old." %(name,age)
# print(format_string)

# name="vyshnav"
# age=24
# format_string="My name is {}, and iam {} years old." .format(name,age)
# print(format_string)


# format_string="My name is {n}, and iam {a} years old." .format(n="vyshnav",a=24)
# print(format_string)

# name="vyshnav"
# age=24
# print(f"My name is {name}, and iam {age} years old.")

#escape character
print('hello,"world!"')

#string methods
s="hello,world!"
print(len(s))
#strip()
print(s.strip())
#split
print(s.split(","))
#find
print(s.find("world"))
#count
print(s.count("hello"))
#startwith and endwith
print(s.startswith("hello"))
print(s.endswith("world!"))

