# Lamda Function
# nameless function

# def square(x):
#     return x*x
# print(square(5))

# square = lambda x:x*x
# print(square(6))


# Map() :applies  a func to every item in an iterable 

# num=[1,2,3,4,5,6,7]
# result=list(map(lambda x:x*2,num))
# print (result)

# filter() :keeps only the item that satisfy a condition

# num =[1,2,4,5,6,7]
# even=list(filter(lambda x:x%2==0,num))
# print(even)

# reduce(): repeatdly combine values into a single result
# 1st import it
# from functools import reduce
# num=[1,4,5,7,9,6]
# total = reduce(lambda x , y:x+y,num)
# print(total)


# Question /
# 1 Lambda 
square =lambda x:x*2
print(square(10))

# 2 map()
num=[2,4,6]
mul=list(map(lambda x:x*3,num))
print(mul)

# 3 filter()
num=[5,10,15,20]
greater=list(filter(lambda x:x>10,num))
print(greater)

