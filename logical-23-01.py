#3 Write a program to reverse a given positive integer.
# number=1234
# rev_sum=0
# while number>0:
#     digit=number%10
#     rev_sum=rev_sum*10+digit
#     number=number//10
# print(f"Reversed Number:{rev_sum}")

# 2Pattern Printing – Butterfly Pattern
# row=int(input("Enter rows:"))
# for i in range(1,row+1):
#     print("*" * i + " " * (2 * (row - i)) + "*" * i)
# for i in range(row,0,-1):
#    print("*" * i + " " * (2 * (row - i)) + "*" * i)

#1Create a simple Bank Management System using your preferred programming language.
# def bank_management_system():
#     balance = 1000.00  # Initial balance
#     print("Welcome to the Simple Bank!")

#     while True:
#         print("\n--- Menu ---")
#         print("1. Check Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")
#         choice = input("Enter your choice (1-4): ")

#         if choice == '1':
#             print(f"Current Balance: ₹{balance}")

#         elif choice == '2':
#             try:
#                 amount = int(input("Enter amount to deposit: ₹"))
#                 if amount > 0:
#                     balance += amount
#                     print(f"Deposited ₹{amount}. New Balance: ₹{balance}")
#                 else:
#                     print("Invalid deposit amount. Please enter a positive value.")
#             except ValueError:
#                 print("Invalid input. Please enter a number.")

        # elif choice == '3':
        #     try:
        #         amount = int(input("Enter amount to withdraw: ₹"))
        #         if amount <= 0:
        #             print("Invalid withdrawal amount. Please enter a positive value.")
        #         elif amount > balance:
        #             print(f"Insufficient funds. Current Balance: ₹{balance}")
        #         else:
        #             balance -= amount
        #             print(f"Withdrew ₹{amount}. New Balance: ₹{balance}")
        #     except ValueError:
        #         print("Invalid input. Please enter a number.")

        # elif choice == '4':
        #     print("Thank you for using the Simple Bank. Goodbye!")
            # break  # Exit the while loop

        # else:
        #     print("Invalid choice. Please enter a number between 1 and 4.")

# Run the system
# bank_management_system()
