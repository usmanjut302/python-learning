# Module 

import math
print(math.sqrt(25))

# 2. Importing the Module
# import the whole module : 

import math
print(math.pi)
print(math.factorial(4))

#  import only what you need :

from math import sqrt
print(sqrt(64))

# give nickname to module 

import math as m
print(m.pi)

# Program 1

import math as m
print(m.sqrt(144))
print(m.factorial(6))
print(m.pi)
print(m.ceil(8.1))
print(m.floor(8.9))


# The random Module
#1. random integer
import random
print(random.randint(1,10))

# 2. random choice
import random
fruits=["apple","orange","banana","mango"]
print(random.choice(fruits))


# 3. Shuffle a list
import random
numbers = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(numbers)
print(numbers)


# practice question

import random as r
print(r.randint(1,100))
color=["blue","green","yellow","purple","red"]
print(r.choice(color))
r.shuffle(color)
print(color)

# Challenge question

import random as r
computer = r.randint(1,10)
guess=int(input("Enter a guess no :"))
print("the computer no. is ",computer)       
if guess==computer:
    print("you win ")
else:
    print("try again") 


# creating you own module

# step 1: create a file mymodule.py
 
# step2 

import mymodule
mymodule.greet("usman")
result=mymodule.add(20,24)
print(result)

# another way

from mymodule import greet,add
greet("jutt")
print(add(20,10))


# Practice questions

import mymodule as mm
print(mm.add(30,20))
print(mm.subtract(33,20))
print(mm.divide(30,60))
print(mm.multiply(12,20))

