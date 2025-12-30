#without recursion function
# n =int(input("Enter the number:"))
# def factorial(num):
#     result=1
#     if num<0:
#         return "Cannot find factorial for negative number"
#     for i in range(1,num+1):
#         result*=i
#     return result
# print("Factorial of",n,":",factorial(n))

#recursive function
# def fact(n):
#     if n<0:
#         return f"{n} have no factorial" 
#     elif n==0 or n==1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))

#tail recursive function
# def tail_fact(n,a=1):#a is accumulator
#     if n<0:
#         return f"{n} have no factorial" 
#     elif n==0 or n==1:
#         return a
#     else:
#         return tail_fact(n-1,a*n)
# print(tail_fact(5))

#fibonacci using recursion
# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# num=int(input("Enter the number:"))
# print(f"fibonacci:",fibonacci(num))

#sum of all element in list
def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0]+sum_list(lst[1:])
print(sum_list([1,2,3,4,5]))