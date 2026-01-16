#You are given an array of positive integers. Your task is to reverse the digits of each element in
# the array without the use of built-in functions and return a new array with these reversed
# numbers.(Use any language.)

# def reverse_array_elements(n):
#     reverse_array=[]
#     for num in n:
#         rev=0
#         while num>0:
#             digit=num%10
#             rev=rev*10+digit
#             num//=10
#         reverse_array.append(rev)
#     print(reverse_array)
# n=[12,23,54]
# reverse_array_elements(n)

#Write a program to print the Butterfly Pattern like given below:
# n=int(input("Enter the rows:"))
# for i in range(1, n + 1):
#     print("*" * i + " " * (2 * (n - i)) + "*" * i)
# for i in range(n,0,-1):
#     print("*" * i + " " * (2 * (n - i)) + "*" * i)

#Write a program bn3that takes a list of integers and a target sum. Return all unique pairs of
# numbers from the list that add up to the target.
def find_pair(num,target):
    pairs=[]
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==target:
                pair=(num[i],num[j]) 
                if pair not in pairs:
                   pairs.append(pair)  
    return pairs
nums = [2, 4, 3, 5, 6, -1]
targets = 5
res=find_pair(nums,targets)     
print(res)   

#A Happy Number is a number defined by the following process:
# 1. Starting with any positive integer,
# 2. Replace the number by the sum of the squares of its digits,
# 3. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly
# in a cycle that does not include 1.
# If it ends in 1, it is a Happy Number
def happy_number(n):
   visited = []
   while n != 1 and n not in visited:
       visited.append(n)
       sum_sq = 0

       while n > 0:
          digit = n % 10
          sum_sq += digit * digit
          n //= 10

       n = sum_sq

   if n == 1:
    return True
   else:
      return False
num=int(input("Enter number:"))
print(happy_number(num))
