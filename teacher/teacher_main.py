from teacher.class_details import view_class_details
from teacher.student_details import view_details
from teacher.enter_marks import Mark_class
from teacher.timetable_operations import create_or_edit_timetable
def Teacher_options():
    while True:
        print("\n---Teacher Options----\n")
        print("1. View Class Details")
        print("2. View Student Details")
        print("3. Enter Marks")
        print("5. Edit or Create Timetable")
        print("6. Exit ")
        try:
            ch=int(input("Enter Choice number: "))
        except:
            ch=-1

        if ch==1:
            view_class_details()
        elif ch==2:
            view_details()
        elif ch==3:
            Mark_class()
        elif ch==5:
            create_or_edit_timetable()
        elif ch==6:
            break
        else:
            print("Invalid Choice")