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
add=lambda x,y:x+y
print(add(20,12))

#lambda function using map(),filter() and reduce()
# num=[1,2,3,4]
# square=map(lambda x:x**2,num)
# print(list(square))
# sqaure=[x**2 for x in range(1,11)]
# print(sqaure)

#filter
number=[1,2,3,4,5,6]
# even=list(filter(lambda x:x%2==0,number))
# even=[x for x in range(1,11) if x%2==0]
# print(even)

#reduce
from functools import reduce
# sum=reduce(lambda x,y:x+y,number)
count=0
sum=[x+count for x in range(1,7)]
print(sum)