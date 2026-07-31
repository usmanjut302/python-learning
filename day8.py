# student mangment system

# Step 1





students = []
def add_student():
    name=input("enter name of student :")
    age=int(input("enter age of student :"))
    course=input("enter course name :")
    dicts={
        "name":name,
        "age":age,
        "course":course,
    }   
    students.append(dicts)
    



    # Step 2 

def display_student():
    for student in students:
        print("Name:",student["name"])
        print("Age:",student["age"])
        print("Course:",student["course"]) 


    # step3
def search_student():
    search = input("enter the students name:")
    found=False
    for student in students:
        if search==student["name"]:
            print("Name:",student["name"])
            print("Age:",student["age"])
            print("Course:",student["course"])
            found=True
            break
    if not found:
            print("student not found")    
            
# print("now delete the students")
def delete_student():
    search = input("enter the students name:")
    found=False
    for student in students:
        if search==student["name"]:
            students.remove(student)
            print("the student is deleted successfully ")  
            found=True
            break
    if not found:
        print("student is not present")    



while True:
    print("===== Student Management =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
   
    choice=int(input("enter a no."))
    
    if choice == 1:
        add_student()


    elif choice == 2:
        display_student()
        

    elif choice == 3:
        search_student()
        
    elif choice == 4:

        delete_student()
    elif choice == 5:
        print("Goodbye!")
        break   