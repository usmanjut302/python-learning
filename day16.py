# iterator : is a obj that let you go thrugh itmes one at a time 

# num=[10,20,30,40,50]
# it =iter(num)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# ----------------------------
# Generator : special function that use yield instead of return

# def count():
#     yield 1
#     yield 2222
#     yield 3
# g=count()

# print(next(g))
# print(next(g))
# print(next(g))
# ----------------------------------
# Generator with a Loop

# def number(n):
#     for i in range (1,n+1):
#         yield i
# for num in number(7):
#     print (num)        

# question    # 
# number=[5,10,15]
# it=iter(number)
# print(next(it))
# print(next(it))


# Question
def number(n):

    for i in range(1,n+1):
        yield i
for num in number(5):
    print(num)        
