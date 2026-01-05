# a=10
# print(a #syntax error

# a="hi"
# print(a+2)   #type error   

# ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
# print(ages['Michael'])  #key error

# dict1={name:"vysh",age:24}
# print(dict1) #name error

# l1=[1,2,3]
# print(l1[3]) #index error

# n=int("vysh")
# print(n) #value error

# a=10
# b=0
# print(a/b) #zero division error

# file=open("simple.txt","r")
# print(file.read()) File not found error

# import mymodule #ModuleNotFoundError

#error handling methods
# a=int(input("enter number:"))
# b=int(input("enter another number:"))
# try:
#     div=a/b
#     print(div)
# except ZeroDivisionError:
#     print("Cannot divide by zero")

#else and finally
# try:
#     a=int(input("enter the number:"))
#     res=10/a
# except ZeroDivisionError:
#     print("Cant divide by zero")
# else:
#     print(f"result:{res}")
# finally:
#     print("result will be displayed...")

#raise exception
# n=-3
# if n<0:
#     raise ValueError("Avoid Negatives Be Positive...")

#custom exceptions
# class NegativeError(Exception):
#     pass
# def check(num):
#     if num<0:
#         raise NegativeError("Ngative numbers not allowed..")
# try:
#     check(-5)
# except NegativeError as e:
#     print(e)
    
