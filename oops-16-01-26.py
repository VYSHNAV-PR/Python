# class BankAccount:
#     def __init__(self,owner_name,balance):
#         self.owner_name=owner_name
#         self.__balance=balance #private attribute
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             print(f"Deposited Rs{amount}")
#         else:
#             print(f"invalid amount deposited")
#     def withdraw_amount(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount
#             print(f"Withdraw Rs{amount}")
#         else:
#             print(f"Insufficient Balance")
#     def get_balance(self):
#         return self.__balance
# account=BankAccount("Alice",1000)
# account.deposit(500) #500 deposited
# account.withdraw_amount(200) #withdraw 200 from account
# print(f"Final Balance:{account.get_balance()}")

# print(account.__balance)


class Customer:
    def __init__(self,name,income,credit_score):
        self.name=name
        self.income=income
        self.credit_score=credit_score
    def check_eligibility(self):
        if self.income>=25000 and self.credit_score>=650:
            print(f"{self.name} is Eligible for loan")
        else:
            print(f"{self.name} is not Eligible for loan")
names=input("Enter name:")
incomes=int(input("Enter income:"))
credit=int(input("Enter credit score:"))
customer=Customer(names,incomes,credit)
customer.check_eligibility()