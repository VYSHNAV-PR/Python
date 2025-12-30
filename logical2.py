#Write a program to check whether two numbers are equal without using comparison operators
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
if not a-b:
    print("Numbers are equal")
else:
    print("Numbers are not equal")
#Create a program to find the maximum and minimum of two numbers without using any loops or conditional statements.


num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
max=((num1+num2)+abs(num1-num2))//2
min=((num1+num2)-abs(num1-num2))//2
print(max,"is maximum")
print(min,"is minimum")