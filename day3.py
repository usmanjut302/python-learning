# revision 
# for i in range(5):
#     print (i)

# for i in range(2,11,2):
#     print(i)

# i=5
# while i>0:
#     print(i)
#     i-=1

# part2

# for i in range(1,21):
#     print(i)
#     i+=1

# 2.
# for i in range(1,51):
#     if (i%2==0):
#         print(i)

# 3.
# i=1
# n = int(input("enter a no."))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")

# total=0
# for i in range(0,5):
#     n=int(input("enter the numbers:"))
#     total=total+n
# print(total)

# 5.

# for i in range(0,10):
#     n= int(input("enter the numbers:"))
#     if i==0:
#         largest= n
#     if n>largest:
#         largest=n

# print(f"the largest no.:{largest}")

    # else:
    #     print("the largest no. is",largest)
# print(f"the largest no. :{largest}")            

# second_largest=0
# for i in range(0,10):
#     n=int (input("enter a no.:"))
#     if i==0:
#         largest=n
#         second_largest=n
#     if n>largest:
#         second_largest=largest
#         largest=n
#     elif n>second_largest and n!=largest:
#         second_largest=n
# print(f"the largest no. is :{largest}")            
# print(f"the 2nd largest no. is :{second_largest}")   
# 
num=[]
for i in range(0,5):
    n = int(input ("enter a no."))
    num.append(n)
print(num)    

for i in range(4,-1,-1):

    print(num[i])