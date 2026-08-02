#  Decorator
#  like gift wrapping : gift is your function, wrapper is your decorator

# eg.
# def greet():
#     print("hello")
# now decorate it 

# def decorator(func):
#     def wrapper():
#         print("before function")
#         func()
#         print("after function")
#     return wrapper
# @decorator
# def greet():
#     print("hello")  
# greet()      



def decorator(func):
    def wrapper():
        print("Program Started")
        func()
    return wrapper
@decorator
def learn():
    print("Learning Python ")  
learn()     
