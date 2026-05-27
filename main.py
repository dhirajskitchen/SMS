from student.student_main import Student_options
from parent.parent_main import Parent_options
from teacher.teacher_main import Teacher_options
from principal.principal_main import Principal_options
from applicant.applicant_main import Applicant_options

def homePage():
    while True:
        print("\n---School Management System---\n")
        print("Pick User Type:")
        print("1. Student")
        print("2. Teacher")
        print("3. Principal")
        print("4. Applicant")
        print("5. Parents")
        print("6. Exit")
        try:
            ch=int(input("Enter Choice number: "))
        except:
            ch=-1
        if ch==1:
            Student_options()
        elif ch==2:
            Teacher_options()
        elif ch==3:
            Principal_options()
        elif ch==4:
            Applicant_options()
        elif ch==5:
            Parent_options()
        elif ch==6:
            break
        else:
            print("Invalid choice")

homePage()