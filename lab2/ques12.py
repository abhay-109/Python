# 12. Create a dictionary to store student names as keys and their scores in three subjects as
# values (in a list). Write functions to:
# a. Display the average marks of each student
# b. Find the topper
# c. Update the marks of a student
dict={}

def avg(s_name):
    val=dict[s_name]
    avg=sum(val)/3
    print(f'the average : {avg}')


def update_marks(name):
    if name in dict:
        print(f"Enter new marks for {name}:")
        new_marks = []
        for i in range(3):
            mark = int(input(f"Subject {i + 1}: "))
            new_marks.append(mark)
        dict[name] = new_marks
        print(f"Marks updated for {name}.")
    else:
        print(f"Student '{name}' not found.")


while True:
    while True:
        student_name=input('Enter the name of studen : ')
        marks=[]
        for i in range(3):
            marks.append(int(input(f'enter the marks of subject {i} : ')))
        dict[student_name]=marks
        ch=input('enter the y for continue adding students name : ')
        if ch!='y':
      
            break  
    avg(student_name)
    up=input('enter do you want to updata the student marks : ')
    if up:
        update_marks()

    end=input('do you want end the program enter y :')
    if end!='y':
        break


