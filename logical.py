num=int(input("Enter the limit:"))
for i in range(1,num):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

# a=int(input("Enter a number:"))
# b=["one","two","three","four","five","six","seven","eight","nine"]
# if 1<=a<=9:
#     print(b[a-1])
# else:
#     print("Greater than 9")