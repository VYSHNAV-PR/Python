# 1. Write a program to check whether a number is positive, negative, or zero
# a=int(input("Enter the number:"))
# if a>0:
#     print(a,"is a positive number")
# elif a<0:
#     print(a,"is a negative number")
# else:
#     print(a,"is neither negative or positive")
# 2. Check if a number is even or odd.
# check=int(input("Enter the number:"))
# if check%2==0:
#     print(check,"is an even number")
# else:
#     print(check,"is a odd number")
# 3. Given a number, check if it is greater than 100.
# greater=int(input("Enter the number:"))
# if greater>100:
#     print(greater,"is greater than 100")
# else:
#     print(greater,"is not greater than 100")
#4. Check whether a person is eligible to vote (age ≥ 18)
# age=int(input("Enter the age:"))
# if age>=18:
#     print("You are eligible for voting")
# else:
#     print("Not eligible to vote")
#5. Given two numbers, print the greater number.
# num1=int(input("Enter the 1st number:"))
# num2=int(input("Enter the 2nd number:"))
# if num1>num2:
#     print(num1,"is greater")
# else:
#     print(num2,"is greater")
#6.Given three numbers, print the largest number.
# num1=int(input("Enter the 1st number:"))
# num2=int(input("Enter the 2nd number:"))
# num3=int(input("Enter the 3rd number:"))
# if num1>num2 and num1>num3:
#     print(num1,"is the largest number")
# elif num2>num1 and num2>num3:
#     print(num2,"is the largest number")
# else:
#      print(num3,"is the largest number")
#7.Check whether a year is a leap year.
# year=int(input("Enter the year:"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print(year,"is a leap year")
# else:
#     print(year,"not a leap year")
#8.Given a mark, print:# "Pass" if marks ≥ 40 # "Fail" otherwise
# mark=int(input("Enter the mark:"))
# if mark>=40:
#     print(mark,"You are Passed!")
# else:
#     print(mark,"Failed")
# 9.Given a mark, print grades:# A → ≥ 90 # B → ≥ 75 # C → ≥ 60 # Fail → below 60
# mark2=int(input("Enter the mark:"))
# if mark2>=90:
#     print("A grade")
# elif mark2>=75:
#     print("B garde")
# elif mark2>=60:
#     print("C garde")
# else:
#     print("Failed!")
#  10.Check if a character is a vowel or consonant.
# v=input("Enter a character:")
# if v=='a'or v=='e' or v=='i' or v=='o' or v=='u'or v=='A'or v=='E' or v=='I' or v=='O' or v=='U':
#     print(v,"is vowel")
# else:
#     print(v,"is consonant")
# 11.Print numbers from 1 to 10 but stop when number is 6
# for i in range(1,11):
#     if i==6:
#         break
#     print(i)
# 12.Print numbers from 1 to 10 but skip number 5.
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)
# 13.Use pass inside an if block and explain why it doesn’t cause an error.
# a=5
# if a>0:
#     pass
# else:
#     print(a,"is negative")
# 14.Print all even numbers between 1 and 20 .
# for i in range(1,21):
#     if i%2==0:
#         print(i)
# 15.Find the sum of numbers from 1 to 10
# sum=0
# for i in range(1,11):
#     sum+=i
# print("Sum:",sum)
# 16.Check whether a given number is a multiple of both 3 and 5.
# multiple=int(input("Enter the number:"))
# if multiple%3==0 and multiple%5==0:
#     print(multiple,"is a multiple of 3 and 5")
# else:
#     print(multiple,"is not a  multiple of 3 and 5")
# 17. Print "Hello" 5 times using a loop
# for i in range(5):
#     print("Hello")
# 18. Given a list [1,2,3,4,5] , print only numbers greater than 3.
l=[1,2,3,4,5]
new_l=[]
for n in l:
    if n>3:
        new_l.append(n)
print(new_l)


