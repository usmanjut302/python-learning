# functions
# problem 1 : func take two no.s and return largest

# def larger(a,b):
    
#     if a>b:
#         return a
#     elif b>a:
#         return b
#     else:
#         return("the no. are equal") 

    
# a=int(input("enter the no. a:"))
# b=int(input("enter the no. b:"))
# print (larger(a,b))
        



# (Problem 2)

# Write a function that checks whether a number is even or odd.

# Hint: Think about which operator tells you the remainder after division by 2.

# def even_odd(n):
#     if n%2==0:
#         return "its even no."
#     else:
#         return "its odd no."
# n = int(input("enter a no. :"))
# print(even_odd(n))  
# print(even_odd(5))  
# 


# Problem 3

# Write a function that returns the sum of all numbers from 1 to n
# total=0
# def numbers(n):
#     total=0
#     for i in range(1,n+1):
#         total=total+i
#     return total
# n= int(input("enter a no."))
# print(numbers(n))   
# 
# 
# Next Challenge (Problem 4)

# Write a program that:

# Takes 5 numbers from the user.
# Stores them in a list using append().
# Prints the complete list.
# Finds the largest and smallest numbers without using max() or min(). 
# l=[]

# def lists():
#     for i in range(1,6):
#         n=int(input("enter the no."))
#         l.append(n)
#     return l

# print(lists())
# largest=l[0]
# smallest=l[0]
# for num in l:
#     if num>largest:
#         largest=num
#     elif num<smallest:
#         smallest=num
# print(f"the largest no. is {largest}")        
# print(f"the smallest no. is {smallest}")        


# problem 
# count the vowels
count=0
def counting():
    count=0
    for ch in n:
        if ch in  "aeiou":
            count=count+1
    return count 
n=input("enter A WORD: ")
print(counting())        

