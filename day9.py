# File Handling
# Practice 1
file = open("notes.txt","w")
file.write(" I am Learning Python")
file.close()

# # Practice 2

file = open("notes.txt", "r")
data=file.read()
print(data)
file.close()

# another way to write code

with open("notes.txt", "r") as file:
    data=file.read()
    print(data)


with open("notes.txt", "a") as file:
    file.write("note saved successfully \n")

with open("notes.txt","r") as file:
    data=file.read()
    print(data)

# Practice 4 count lines

with open("notes.txt", "r") as file:
    lines=file.readlines()
    # print(len(lines))
    count=1
    for line in lines:
        print(count,".",end="")
        print(line)
        count+=1
        



# bonus challenge

word=input("enter a word: ")
with open("notes.txt","r") as file:
    data=file.read()
    if word in data:
        print( "word found")
    else:
        print("word not found")    







