from principal.class_details import view_class_details
from principal.student_details import view_details
from principal.application_handling import view_applications
def Principal_options():
    print("\n---Principal Options----\n")
    print("1. View Class Details")
    print("2. View Student Details")
    print("3. View Applications")
    print("4. Exit ")
    while True:
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
            break
        else:
            print("Invalid Choice")