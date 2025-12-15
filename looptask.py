a=int(input("Enter first number:"))
op=input("Enter the operator:")
b=int(input("Enter the second number:"))
if op=="+":
    sum=a+b
    print("Addition:",sum)
elif op=="-":
     diff=a-b
     print("Difference:",diff)
elif op=="*":
     mul=a*b
     print("Multiply:",mul)
elif op=="/":
     res=a/b if not b==0 else "Division by zero not allowed" 
     print("Division:",res)  
else:
     print("Select one Operator") 