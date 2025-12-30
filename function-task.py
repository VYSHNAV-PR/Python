#1. Write a function that takes a number as input and returns whether the number is even or odd.
# a=int(input("Enter the Number:"))
# def evenorodd(a):
#     if a%2==0:
#         return print(a,"is Even")
#     else:
#         return print(a,"is Odd")
# evenorodd(a)
#2. Write a function that takes three numbers as input and returns the largest number among them.
# a=int(input("Enter the Number1:"))
# b=int(input("Enter the Number2:"))
# c=int(input("Enter the Number3:"))
# def largest(a,b,c):
#     if a>b and a>c:
#         return print(a,"is largest")
#     elif b>c and b>a:
#         return print(b,"is largest")
#     else:
#         return print(c,"is largest")
# largest(a,b,c)
#3. Write a function that takes a list of numbers as input and returns the sum of all elements in the list.
# number=list(map(int,input("Enter the numbers").split()))
# def sum(number):
#     total=0
#     for n in number:
#         total+=n
#     return total
# add=sum(number)
# print(f"Sum of all numbers:",add)

#4. Write a function that takes a list of numbers as input and returns a new list containing only even numbers.
# num=list(map(int,input("Enter the numbers").split()))
# print(" OG List:",num)
# def even(num):
#     even=[]
#     for n in num:
#         if n%2==0:
#             even.append(n)
#     return even
# print("Even numbers list:",even(num))

#5. Write a function that takes a string as input and returns the length of the string.
# string=input("Enter the string:")
# def length(string):
#    count=0
#    for i in string:
#       count+=1
#    return count
# print(f"Length of the String {string}:",length(string))

#6. Write a function that takes a string as input and returns the string in uppercase.
# string1=input("Enter the string:")
# def upper(text):
#     return text.upper()
# print("Uppercase:",upper(string1))
#7. Write a function that takes a number as input and returns whether the ``number is positive, negative, or zero.
# nn=int(input("Enter the number:"))
# def check(num):
#     if num>0:
#         return "Positive"  
#     elif num<0:
#         return "Negative"  
#     else:
#         return "Zero"   
# print(check(nn))
#8.Write a function that takes a number as input and returns True if the number
# is a multiple of both 3 and 5, otherwise returns False .
# div=int(input("Enter the number:"))
# def check_number(num1):
#     if num1%3==0 and num1%5==0:
#         return True
#     else:
#         return False
# print(check_number(div))
#9. Write a function that takes a list of numbers as input and returns the maximum value in the list
# num2=list(map(int,input("Enter the numbers:").split()))
# def max(number):
#     max_number=number[0]
#     for n in number:
#         if n >max_number:
#             max_number=n
#     return max_number
# print(f"Maximum Value:{max(num2)}")
#10. Write a function that takes marks as input and returns the grade according to the following rules:
# A for marks ≥ 90
# B for marks ≥ 75
# C for marks ≥ 60
# Fail for marks below 60
# grades=int(input("Enter the Mark:"))
# def grade(n1):
#     if n1>=90:
#         return "A grade"
#     elif n1>=75:
#         return "B grade"
#     elif n1>=60:
#         return "C grade"
#     else:
#         return "Failed"
# print(grade(grades))
#11. Write a function that takes a price as input and returns the discounted price after applying a 10% discount
price=float(input("Enter the price:"))
def discount(prices):
    dis=prices*10/100
    final=prices-dis
    return final
print("Discounted Price:",discount(price))
#12.Write a function that takes a list of numbers as input and returns the count of even and odd numbers.
num3=list(map(int,input("Enter the numbers:").split()))
def count(num3):
    even_count=0
    odd_count=0
    for i in num3:
        if i%2==0:
          even_count+=1
        else:
           odd_count+=1
    return even_count,odd_count
even,odd=count(num3)
print("Even Count:",even)
print("Odd Count:",odd)
#13.Write a function that takes a temperature in Celsius as input and returns the temperature in Fahrenheit.
temp=int(input("Enter the temperature in Celsius:"))
def celsius_to_fahrenheit(celsius):
    farenheit=(celsius*9/5)+32
    return farenheit
print("Temperature in Farenheit:",celsius_to_fahrenheit(temp),"°F")

