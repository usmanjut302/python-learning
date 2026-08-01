# Inheritance

# class Animal:
#     def sound(self):
#         print("animal makes a sound")
# class Dog(Animal):
#     pass
# d1=Dog()
# d1.sound()

# Practice: Method Overriding
# 
# class Animal:
#     def sound(self):
#         print("animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("dog barks")
# d1=Dog()
# d1.sound()

# Practice 

# class Vehicle:
#     def start(self):
#         print("vehice started")
# class Bike(Vehicle):
#     def start(self):
#         print("bike started")
# b=Bike()  
# b.start()  
# 
# ------------------------------------------------------
# ------------------------------------------------------
#super() Keyword

class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self,name,age):
        super().__init__(name)                    
        self.age=age

    def show(self):
        print("the name of student is :",self.name)    
        print("the age of student is :",self.age)
s1=Student("usman",24)
s1.show()    


# Final Challenge

class Employee:
    def __init__(self,name):
        self.name=name

class Manager(Employee):
    def __init__(self,name,department):
        super().__init__(name)
        self.department=department 

    def display(self):
        print("the name of manager is :", self.name)       
        print("the department of manager is :", self.department)       
m1=Manager("usman","Dveloper")
m1.display()
