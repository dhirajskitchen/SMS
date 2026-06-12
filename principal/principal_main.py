from principal.class_details import view_class_details
from principal.student_details import view_details
from principal.application_handling import view_applications
from principal.view_complete_attendance import view_complete_attendance
from principal.view_all_students import view_all_students
def Principal_options():
    while True:
        print("\n---Principal Options----\n")
        print("1. View Class Details")
        print("2. View Student Details")
        print("3. View Applications")
        print("4. View Complete Attendance ")
        print("5. View All Students")
        print("6. Exit")
        try:
            ch=int(input("Enter Choice number: "))
        except:
            ch=-1

        if ch==1:
            view_class_details()
        elif ch==2:
            view_details()
        elif ch==3:
            view_applications()
        elif ch==4:
            view_complete_attendance()
        elif ch==5:
           view_all_students()
        elif ch==6:
            break
        else:
            print("Invalid Choice")