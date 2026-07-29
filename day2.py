# 1  print no.s form 1 to 20
# i=0
# while i<20:
#     i=i+1
#     print(i)

# 2 print even no.s
# i=2
# while i<50:
#     print(i)
#     i+=2

# 3 print odd no.s 
# i=1
# while i<50:
#     print(i)
#     i+=2


# 4 multiplication table
# i=1
# n = int(input("enter a no."))
# for i in range (1,11):
#     print(f"{n}x{i}={n*i}")

# # 5 factorial 

# # n= int(input("enter a no. "))
# # fact=1
# # for i in range(1,n+1):
# #     fact = fact*i
# # print(f"the factorial= {fact}")    

# 6 no. of + ,- and zero values
# negative=0
# positive=0
# zero=0
# for i in range(0,10):
#     n=int(input("enter no. :"))
#     if n>0:
#         positive+=1
#     elif n<0:
#         negative+=1
#     else:
#         zero+=1
# print("the positive no. is :", positive)            
# print("the negative no. is :",negative)            
# print("the zer0 no. is :",zero)
# 
# 
# 7 larest and smallest no.

# for i in range(0,10):
#     n=int(input("enter the no.s :"))            
#     if i==0:
#         largest=n
#         smallest=n
#     if n >largest:
#         largest=n
#     elif n <smallest:
#         smallest=n
# print("the largest no. is :", largest)
# print(f"the smallest no. is :{smallest}")


# 8 nd largest ann 2nd smallest no.
for i in range(0,10):
    n = int (input("enter a no."))
    if i==0:
        largest=n
        second_largest=n
        smallest=n
        second_smallest=n

    if n>largest:
        second_largest=largest
        largest=n

    elif n<smallest:
        second_smallest=smallest
        smallest=n

    elif n>second_largest and n<largest:
        second_largest=n

    elif n<second_smallest and n>smallest:
        second_smallest=n

        

print(f"the 2nd smallest no. is {second_smallest}")
print(f"the 2nd largest no. is {second_largest}")
print("the largest no. is :", largest)
print(f"the smallest no. is :{smallest}")
            