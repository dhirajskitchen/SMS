from student.student_details import view_details,edit_details
from student.view_marks import view_marks
from student.view_timetable import view_timetable
from utils import input_student_id

def Student_options():
    id=input_student_id()
    
    while True:
        print("\n---Student Options----\n")
        print("1. View Details")
        print("2. Edit Details")
        print("3. View Marks")
        print("4. View Timetable")
        print("5. View Attendance Details")
        print("6. Exit")
        try:
            ch=int(input("Enter Choice number: "))
        except:
            ch=-1

        if ch==1:
            view_details(id)
        elif ch==2:
            edit_details(id)
        elif ch==3:
            view_marks(id)
        elif ch==4:
            view_timetable(id)
        elif ch==6:
            break
        else:
            print("Invalid Choice")
