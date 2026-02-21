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


#encapsulation
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name #public attribute
#         self.__salary=salary #private attribute
#     def employee_display(self):
#         print(f"Name:{self.name} Salary:{self.__salary}")
#     def update_employee(self,new_salary):
#         self.__salary=new_salary
# emp=Employee("Vyshnav",25000)
# emp.employee_display()
# # print(emp.name)
# # print(emp.__salary)
# emp.update_employee(30000)
# emp.employee_display()

#inheritance-single inheritance
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print(f"{self.name} makes a sound")
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} says wooof!")
# dog=Dog("Lab")
# dog.speak()

#multiple-inheritance
# class Engine:
#     def start_engine(self):
#         print("Engine started")
# class Wheels:
#     def rotate(self):
#         print("Wheels rotating")
# class Car(Engine,Wheels):
#     def __init__(self,name):
#         self.name=name
#     def drive(self):
#         print(f"{self.name} is going for a drive...")
# car=Car("Porsche")
# car.start_engine()
# car.rotate()
# car.drive()

#multilevel inheritance
# class Grandfather:
#     def sing(self):
#         print("Grandfather is singing")
# class Parent(Grandfather):
#     def dance(self):
#         print("Parent is dancing")
# class Son(Parent):
#     def play(self):
#         print("Son is playing")
# son=Son()
# son.sing()
# son.dance()
# son.play()

#heirarchial inheritance
# class Animal:
#     def speak(self):
#      print("Animal speaks.")
# class Dog(Animal):
#     def speak(self):
#       print("Dog barks.")
# class Cat(Animal):
#     def speak(self):
#       print("Cat meows.")
# dog = Dog()
# cat = Cat()
# dog.speak() # Dog barks.
# cat.speak() # Cat meows

#Hybrid inheritance
# class A:
#    def method_a(self):
#       print("Method from class A")
# class B(A):
#    def method_b(self):
#     print("Method from class B")
# class C(A):
#    def method_c(self):
#     print("Method from class C")
# class D(B, C):
#    def method_d(self):
#     print("Method from class D")
# d = D()
# d.method_a() # Inherited from B's parent A
# d.method_b() # Inherited from B
# d.method_c() # Inherited from C
# d.method_d() # Defined in D
#polymorphism
# class Animal:
#     def speak(self):
#         return "Animal makes sound"
# class Cat:
#     def speak(self):
#         return "MEOW.."
# class Dog:
#     def speak(self):
#         return "WOOF.."
# def animal_sound(animal:Animal):
#     return animal.speak()
# cat=Cat()
# dog=Dog()
# print(animal_sound(cat))
# print(animal_sound(dog))

#duck typing in polymorphism
# class Tiger:
#     def speak(self):
#         print("Grrr..")
# class Lion:
#     def speak(self):
#         print("Lion Roars")
# class Human:
#     def speak(self):
#         print("OOYY..")
# def make_sound(obj):
#     obj.speak()
# for creature in [Tiger(),Lion(),Human()]:
#     make_sound(creature)

#abstraction
# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def area(self):
#         return self.width * self.height
# rectangle=Rectangle(10,5)
# print(f"Area of Reactangle:",rectangle.area())
        
#destructor
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(F"{self.name} has been created..")
#     def __del__(self):
#         print(f"{self.name} has been destroyed..")
# person=Person("Vyshnav",24)
# del person

#decorators
# def aaa(func):
#     def wrap(*args,**kwargs):
#         print(f"Before")
#         res=func(*args,**kwargs)
#         print(res)
#         print(f"After")
#     return wrap
# @aaa
# def add(a,b):
#     return a+b
# add(10,20)
# @aaa
# def substract(a,b):
#     return a-b
# substract(20,10)

#decorator @classmethod
# class Company:
#     company_name="ABC solutions"
#     @classmethod
#     def change_company(cls,new_name):
#         cls.company_name=new_name
# Company.change_company("XYZ infotech")
# print(f"Chmaged Company:",Company.company_name)

#static method
# class Operations:
#     @staticmethod
#     def add(a,b):
#         return a+b
# op=Operations()
# print(op.add(100,200))         