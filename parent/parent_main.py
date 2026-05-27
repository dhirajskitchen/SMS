from parent.student_details import view_details
from parent.view_marks import view_marks
from parent.pay_fees import pay_fees
from utils import input_student_id

def Parent_options():
    id=input_student_id()
    print("\n---Parent Options----\n")
    print("1. View Student Details")
    print("2. View Student Marks")
    print("4. Exit")
    while True:
        try:
            ch=int(input("Enter Choice number: "))
        except:
            ch=-1

        if ch==1:
            view_details(id)
        elif ch==2:
            view_marks(id)
        elif ch==3:
            pay_fees(id)
        elif ch==4:
            break
        else:
            print("Invalid Choice")
