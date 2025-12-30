#function
# def greet(name):
#     print(f"hello {name}")

# greet("vyshnav")

#sum
# def sum(a,b):
#     summ=a+b
#     print("Sum:",summ)

# sum(3,4)

#positional argument
# def display(name,age):
#     print(f"Hello iam {name} and iam {age} years old")

# display("Vyshnav",24)

#keyword
# def display(name,age):
#     print(f"Hello iam {name} and iam {age} years old")

# display(name="Vyshnav",age=24)

#default
# def display(name,age=25):
#     print(f"Hello iam {name} and iam {age} years old")

# display(name="Vyshnav")

#return statement
# def multiply(a,b):
#     return a*b
# res=multiply(12,12)
# print(res)

#docstring
# def add(a,b):
#     """line to add two numbers"""
#     return a+b
# sum=add(4,5)
# print(add.__doc__)

#lambda function
# add=lambda x,y:x+y
# print(add(20,12))

#lambda function using map(),filter() and reduce()
# num=[1,2,3,4]
# square=map(lambda x:x**2,num)
# print(list(square))
# sqaure=[x**2 for x in range(1,11)]
# print(sqaure)

#filter
# number=[1,2,3,4,5,6]
# even=list(filter(lambda x:x%2==0,number))
# even=[x for x in range(1,11) if x%2==0]
# print(even)

#reduce
# from functools import reduce
# sum=reduce(lambda x,y:x+y,number)
# count=0
# sum=[x+count for x in range(1,7)]
# print(sum)

#higher order function
# def calculate(a,b,operator):
#     return operator(a,b)
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# print(calculate(10,5,add))
# print(calculate(10,5,sub))
# print(calculate(10,5,mul))
# print(calculate(10,5,div))

#function scope
# x=12 #global scope
# def outer():
    # x=5 #enclosed scope
    # def inner():
        # x=2 #local scope
#         print(x)
#     inner()
# outer()
# print(x)

#arbitory argument
# def sum(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# res=sum(1,2,3,4,5,6,7)
# print(res)

#keyword argument
# def details(**kwargs):
#     for keys,value in kwargs.items():
#         print(f"{keys}:{value}")
# details(name="vyshnav",age=24,place="perintalmanna",gender="male",country="india")

def priority(a,*args,**kwargs):
    print("positional argument:",a)
    print("arbitory argument:",args)
    print("keyword argument:",kwargs)
a=priority(1,2,3,name="vyshu",age=24)
