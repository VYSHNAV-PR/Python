# # ATM Cash Withdrawal System

# balance = 10000  # Initial ATM balance

# while True:
#     print("\n--- ATM MENU ---")
#     print("1. Check ATM Balance")
#     print("2. Withdraw Cash")
#     print("3. Exit")

#     choice = input("Enter your choice (1-3): ")

#     if choice == "1":
#         print(f"ATM Balance: ₹{balance}")

#     elif choice == "2":
#         amount = int(input("Enter amount to withdraw: ₹"))

#         if amount <= 0:
#             print("Invalid amount. Please enter a positive value.")

#         elif amount % 100 != 0:
#             print("Withdrawal amount must be a multiple of 100.")

#         elif amount > balance:
#             print("Insufficient balance.")

#         else:
#             balance -= amount
#             print(f"Please collect your cash: ₹{amount}")
#             print(f"Remaining Balance: ₹{balance}")

#     elif choice == "3":
#         print("Thank you for using the ATM. Goodbye!")
#         break

#     else:
#         print("Invalid choice. Please select a valid option (1-3).")

# 2 question
rows=int(input("Enter rows:"))
for i in range(rows,0,-1):
    print(" "*(rows-i)+"*"*i)
for i in range(2,rows+1):
    print(" "*(rows-i)+"*"*i)   

# 3 question
n=int(input("Enter numbers:"))
count=0
while n>0:
    n=n//10
    count+=1
print("Number of digits in a number:",count)