
n=int(input("Enter the rows:"))
#right angle traingle pattern
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")

#reversed right angle traingle
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")

#full pyramid triangle
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")
#     print()
#reversed full pyramid traingle
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")
#     print()

#diamond shape
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")
#     print()

#squre
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#hollow right angled triangle
# for i in range(1,n+1):
#     for j in range(1,i+1):
#        if j==1 or i==n or i==j:
#            print("*",end=" ")
#        else:
#            print(" ",end=" ")
#     print("")

#hollow reverse right angled triangle
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#        if j==1 or i==n or i==j:
#            print("*",end=" ")
#        else:
#            print(" ",end=" ")
#     print("")

#hollow full pyramid triangle
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#        if k==1 or k==2*i-1 or i==n:
#            print("*",end=" ")
#        else:
#            print(" ",end=" ")
#     print()

#hollow reversed pyramid triangle
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#        if k==1 or k==2*i-1 or i==n:
#            print("*",end=" ")
#        else:
#            print(" ",end=" ")
#     print()

#hollow diamond shape
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#        if k==1 or k==2*i-1:
#            print("*",end=" ")
#        else:
#            print(" ",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#        if k==1 or k==2*i-1:
#            print("*",end=" ")
#        else:
#            print(" ",end=" ")
#     print()


#reverse hill and normal hill
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")
#     print()
# for i in range(2,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print("*",end=" ")
#     print()

#left pascal triangle
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")
# for i in range(n-1,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")
#right pascal triangle
# for i in range(1, n + 1):
#     print("  " * (n - i) ,end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print()
# for i in range(n-1,0,-1):
#     print("  " * (n - i) ,end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print()