#creating a class
# class Bike:
#     def __init__(self,brand,color,year): #initialise the attributes of the object
#         self.brand=brand
#         self.color=color
#         self.year=year
#     def display_info(self):
#         print(f"Brand:{self.brand}\nColor:{self.color}\nYear:{self.year}")

# bike1=Bike("Honda","Black",2020)
# bike1.display_info()
# print(f"\n")
# bike2=Bike("Royal Enfield","Mat Green",2018)
# bike2.display_info()
# print(type(bike1))

#Accessing attributes
# print(F"Brand:{bike1.brand}")
# bike1.brand="KTM" #changing the brand name of the bike
# bike1.display_info()

# class Dog:
#     def __init__(self,breed,age):
#         self.breed=breed
#         self.age=age
#     def bark(self):
#         print(f"Breed:{self.breed}\nAge:{self.age}")
# dog1=Dog("German Sheppard",10)
# dog1.bark()
# print("\n")
# #Accessing attributes
# print(F"Breed:{dog1.breed}\n")
# dog1.breed="Golden Retriever"
# dog1.age=8
# dog1.bark()

#student mark
# class Student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def display_grade(self):
#         if self.mark>=80:
#              return "A grade"
#         elif self.mark>=70:
#              return "B grade"
#         elif self.mark>=60:
#              return "C grade"
#         elif self.mark>=50:
#              return "D grade"
#         else:
#             return "Failed!!"
       
# student1=Student("Vyshnav",85)
# print(f"Name:{student1.name}\nMark:{student1.mark}\nGrade:{student1.display_grade()}")

#__str__ method
# class Book:
#     def __init__(self,bookname,author):
#         self.bookname=bookname
#         self.author=author
#     def __str__(self):
#         return f"{self.bookname} written by {self.author}"
# book1=Book("Macbeth","Shakespear")
# print(book1)
        
#instnace and class variables
# class Employee:
#     company="IBM" #class variable
#     def __init__(self,name,position):
#         self.name=name  #intsance variable
#         self.position=position
# emp1=Employee("Vyshnav","Developer")
# emp2=Employee("Hari","Developer")
# print(emp1.company)
# print(emp2.company)

# print(emp1.name)
# print(emp2.name)    

#inner class object
# class Employee:
#     class Company:
#         def __init__(self,cname,location):
#             self.cname=cname
#             self.location=location
#     def __init__(self,name,salary,cname,location):
#         self.name=name
#         self.salary=salary
#         self.company=Employee.Company(cname,location)
#     def employee_details(self):
#         print(f"Name:{self.name}\nSalary:{self.salary}\nCompany:{self.company.cname}\nLocation:{self.company.location}")
# emp1=Employee("Vyshnav",25000,"XYZ Comp","Kochi")
# emp1.employee_details()

#Composition-Tightly coupled
# class Company:
#         def __init__(self,cname,location):
#             self.cname=cname
#             self.location=location
# class Employee:
#       def __init__(self,name,salary,cname,location):
#             self.name=name
#             self.salary=salary
#             self.company=Company(cname,location)
#       def display_employee(self):
#             print(f"Name:{self.name}\nSalary:{self.salary}\nCompany:{self.company.cname}\nLocation:{self.company.location}")
      
# emp1=Employee("Vyshnav",25000,"XYZ Comp","Kochi")
# emp1.display_employee()
   
# Loosely coupled      
# class Company:
#         def __init__(self,cname,location):
#             self.cname=cname
#             self.location=location
# class Employee:
#       def __init__(self,name,salary,company):
#             self.name=name
#             self.salary=salary
#             self.company=company
#       def display_employee(self):
#             print(f"Name:{self.name}\nSalary:{self.salary}\nCompany:{self.company.cname}\nLocation:{self.company.location}")

# c1=Company("XYZ Comp","Kochi")
# emp1=Employee("Vyshnav",25000,c1)
# emp1.display_employee() 

# del emp1
# try:
#     print(emp1.company.cname)
# except Exception as e:
#       print('Error',e)

#inner class to loosely coupled
# class Company:
#     def __init__(self, cname, location):
#         self.cname = cname
#         self.location = location


# class Employee:
#     def __init__(self, name, salary, company):
#         self.name = name
#         self.salary = salary
#         self.company = company

#     def employee_details(self):
#         print(
#             f"Name: {self.name}\n"
#             f"Salary: {self.salary}\n"
#             f"Company: {self.company.cname}\n"
#             f"Location: {self.company.location}"
#         )

# c1 = Company("XYZ Comp", "Kochi")
# emp1 = Employee("Vyshnav", 25000, c1)
# emp1.employee_details()


        