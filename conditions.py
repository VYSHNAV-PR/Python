#if,elif ,else
# a=10
# if a>1:
#     print("Positive number")
# elif a==2:
#     print("Two")
# else:
#     print("Ngative number")

# #nested if
# a=20
# b=5
# if a>10:
#     if b<10:
#         print(a,"is greater than 10 and ",b,"is less than 10")
    
#nested if with and,or not
#AND
# x=15
# y=4
# if x>10 and y<5:
#     print(x,"grater than 10 and",y,"less than 5")

#OR
# x=20
# y=4
# if x>10 or y>5:
#     print(x,"grater than 10 and",y,"less than 5")

#NOT
# x=15
# y=4
# if not(x<10):
#     print(x,"greater than 10")

#ternary operator
# a=int(input("Enter the number:"))
# result="greater than 5" if a>5 else"less than 5"    
# print(result)

#pass
# x=-10
# if x>0:
#     pass
# else:
#     print(x,"is negative number")

#for loop with break
# a=int(input("Enter limit:"))
# for i in range(1,a):
#     if i==3:
#         break
#     print(i)

#for loop with continue
# a=int(input("Enter limit:"))
# for i in range(1,a):
#     if i==3:
#         continue
#     print(i)

#while loop
# a=1
# while a<=5:
#     print(a)
#     a+=1

#nested for loop
# for i in range(4):
#     for j in range(2):
#         print(f"i={i},j={j}")

#list comprehension
# even=[x for x in range(1,11) if x%2==0]
# odd=[x for x in range(1,11) if x%2!=0]
# print("ODD:",odd)
# print("EVEN:",even)

#square of even and odd using list comprehension
even=[x**2 for x in range(1,11) if x%2==0]
odd=[x**2 for x in range(1,11) if x%2!=0]
print("ODD:",odd)
print("EVEN:",even)