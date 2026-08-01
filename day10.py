# try and except 
try :
    age=int(input("enter the age :"))
    print(age)
except:
    print("invalid age")  

# catching a specific exception
      
try :
    age=int(input("enter the age :"))
    print(age)
except ValueError:
    print("invalid age")


# else  

try :
    age=int(input("enter the age :"))
    print(age)
except ValueError:
    print("invalid age")
else:
    print("double age",age*age)   


# finally 
# 
try :
    age=int(input("enter the age :"))
    print(age)
except ValueError:
    print("invalid age")
finally:
    print("program end")         


# Multiple exceptions 

try:
    n=int(input("enter a no."))
    result=10/n
    print(result)
except ValueError:
    print("no only plz") 
except ZeroDivisionError:
    print("cant be divided by zero ")       


# Challenge 
try:
    a=int(input("enter the 1st no. :"))
    b=int(input("enter the 2nd no. :"))
    result=a/b
    print(result)
except ValueError:
    print("No.s Only plz")
except ZeroDivisionError:
    print("Can not divide zero")  
# # else:
finally:
    print("progrem completed ")         


age = int(input("ente rthe age :"))
if age<18:
    raise ValueError("age must be greater then 18")
print("eligible to vote") 


# Question

password=input("enter the password :")
try:
    if len(password)<8:
        raise ValueError("password must contain 8 digits")
    else:
        print("password accepted")
except ValueError as e:
    print("Enter the password correct")
finally:
    print("program end")    