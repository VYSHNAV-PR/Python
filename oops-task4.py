# class Order:
#     def __init__(self,order_id,product_name,status):
#         self.order_id=order_id
#         self.product_name=product_name
#         self.status=status
#     def display_orders(self):
#         print(f"{self.order_id} - {self.product_name} - {self.status}")
# orders=[]
# for i in range(2):
#     print(f"Enter Order {i+1}:")
#     order_id=int(input("Enter Order ID:"))
#     product_name=input("Enter Product Name:")
#     status=input("Enter Status:")
#     print("\n")
#     order=Order(order_id,product_name,status)
#     orders.append(order)
#  #update status with order_id
# update_id=int(input("Enter the Order ID to update:"))
# new_status=input("Enter the new status:")
# for order in orders:
#     if order.order_id==update_id:
#         order.status=new_status
#         break
# #Updated Orders:
# print(f"Updated Order:")
# for order in orders:
#     order.display_orders()


#2
class Employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
    def apply_bonus(self,percentage):
        self.salary+=self.salary*(percentage/100)
    def display_info(self):
        print(f"Name:{self.name} | Position:{self.position} | Salary:{self.salary}")
employees=[]
for i in range(2):
    print(f"Enter the details of Employee {i+1}:")
    name=input("Enter the Name:")
    position=input("Enter Position:")
    salary=float(input("Enter Salary:"))
    emp=Employee(name,position,salary)
    bonus=float(input("Enter Bonus%:"))
    print("\n")
    emp.apply_bonus(bonus)
    employees.append(emp)
#display details of employees
print(f"-----Employee Details-----")
for emp in employees:
    emp.display_info()        