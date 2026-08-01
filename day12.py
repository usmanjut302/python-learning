#  Object Oriented Programming OOP,Classes and objects

# class Student:
#     pass
# s1=Student()

# s1.name="usman"
# s1.age=24
# print(s1.name)
# print(s1.age)


# Practice 1

# class Mobile:
#     pass
# mob=Mobile()
# mob.brand="samsung"
# mob.price=90000
# print(mob.brand)
# print(mob.price)


# __init__() constructor 

# class Mobile:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
# mob=Mobile("samsung",200000)
# print(mob.brand)        
# print(mob.price)        


# Practice 2

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# s1=Student("usman",24)
# print(s1.name)
# print(s1.age)

# Methods inside a class
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def intro(self):
#         print("my name is ",self.name)
#         print("my age is ",self.age)
# s1=Student("usman",24)
# s1.intro()  
# 
# 
# Practice 3
# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

#     def show(self):
#         print("the car brand is :",self.brand)
#         print("the car model is :",self.model)
# car1=Car("toyota",2002)
# car2=Car("honda",2022)
# car1.show()        
# car2.show()        
    

# Topic: Class variable vs instance variable
# class Student():
#     school="cadet College"  #this is class variable#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=Student("Usman",24)    #this is instance variable             
# s2=Student("ali",25)
# s2.school="punjab college"
# print(s1.name)
# print(s1.age)
# print(s1.school)
# print(s2.name)
# print(s2.age)
# print(s2.school)


# Practice 4

# class Employee:
#     company="google"
#     def __init__(self,name):
#         self.name=name

# e1=Employee("usman")
# e2=Employee("jutt")

# print(e1.name)
# print(e1.company)

# print(e2.name)
# print(e2.company)

# Challenge question

class Laptop:
    brand="HP"
    def __init__(self,model,price):
        self.model=model
        self.price=price
l1=Laptop("elitebook",85000)        
l2=Laptop("pavilion",65000) 
l2.brand="dell"
print(l1.model)       
print(l1.brand)       
print(l1.price)

print(l2.model)       
print(l2.brand)       
print(l2.price)       
    