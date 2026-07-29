# for i in range(1,6):
#     print("*")

# for i in range(3):
    # print(i,end=" ")

# num=[10,20,30]
# for i in range(len(num)):
#     print(num[i])



# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()    
    

for i in range(1,6):
    for z in range(5,i-1,-1):
        print(" ",end="")    
    print("*" * (2*i-1),end="")
    # for j in range(1,i+1):
    print()   