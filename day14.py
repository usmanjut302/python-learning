# Polymorphism
# same method is used for different objects 

# class Animal:
#     def sound(self):
#         print("animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("cat meow")
# d1=Dog()
# d1.sound()

# c1=Cat()
# c1.sound()

# ------------
# Duck Typing
# # ------------

# class Dog:
#     def sound(self):
#         print("dog barks")
# class Cat:
#     def sound(self):
#         print("cat meow")
# def make_sound(animal):
#     animal.sound()        
# d1=Dog()
# make_sound(d1)

# c1=Cat()
# make_sound(c1)



# Practice Q

# class Bird:
#     def move(self):
#         print("birds fly")
# class Fish:
#     def move(self):
#         print("fish swims")
# def action(obj):
#     obj.move()

# b=Bird()
# f=Fish()

# action(b)
# action(f)


# practice 2

# class Teacher:
#     def teach(self):
#         print("teacher is teaching")
# class Doctor:
#     def teach(self):
#         print("doctor explaining health")
# def start(person):
#     person.teach()

# t=Teacher()
# d=Doctor()

# start(t)
# start(d)
# --------------------------------------------
# Operator Overloading

# class Number:
#     def __init__(self,value):
#         self.value=value

#     def __add__(self, other):
#         return self.value +other.value

# n1=Number(10)
# n2=Number(20)

# print(n1+n2)


# practice

# class Box:
#     def __init__(self,weight):
#         self.weight=weight
#     def __add__(self, other):
#         return self.weight + other.weight

# w1=Box(22)
# w2=Box(32)

# print(w1+w2)

# ----------------------------
# Final practice of day14

class Student:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self, other):
        return self.marks + other.marks
s1=Student(80)
s2=Student(90)
print(s1+s2)        
        