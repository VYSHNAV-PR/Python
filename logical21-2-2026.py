# # Read number
# num = int(input("Enter a number: "))

# temp = num
# sum_fact = 0
# while temp > 0:
#     digit = temp % 10        # get last digit
#     temp = temp // 10        # remove last digit

#     # calculate factorial manually
#     fact = 1
#     i = 1
#     while i <= digit:
#         fact = fact * i
#         i += 1

#     sum_fact += fact

# # check strong number
# if sum_fact == num:
#     print("Strong Number")
# else:
#     print("Not a Strong Number")

rows=int(input("Enter rows:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

