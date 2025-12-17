# 1. Given a list of numbers, write a program to find the sum of all numbers, the
# sum of even numbers, and the sum of odd numbers using list
# comprehension.
numbers=[1,2,3,4,5,6]
sum=0
allnumbers=[num for num in numbers]
for n in allnumbers:
    sum+=n
# Sum of even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
even_sum = 0
for num in even_numbers:
    even_sum += num

# Sum of odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]
odd_sum = 0
for num in odd_numbers:
    odd_sum += num

print("Sum of all numbers:", sum)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

#2.Given a list of numbers, create a new list that contains only numbers greater than 10 and divisible by 3 using list comprehension.
numbers = [3, 6, 9, 12, 15, 18, 20, 22, 24, 30]
a=[num for num in numbers if num>10 and num%3==0]
print(a)
#3.Given a list of numbers, create a new list containing only even numbers greater than 10 using list comprehension.
number = [3, 6, 9, 12, 15, 18, 20, 22, 24, 30]
evenn=[n for n in number if n%2==0 and n>10]
print(evenn)
#4.Given a list of strings, create a new list containing the length of each string using list comprehension.
strings = ["apple", "banana", "cherry", "kiwi"]
length=[len(s) for s in strings]
print("Length of each string:",length)
#5.Given a list of numbers, create a new list where:even numbers are replaced with "even" odd numbers are replaced with "odd"
numm = [1, 2, 3, 4, 5, 6]
replace=["even" if n%2==0 else "odd"  for n in numm ]
print(replace)
