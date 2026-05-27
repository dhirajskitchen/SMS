from applicant.submit_application import submit_application
from applicant.check_status import check_status

def Applicant_options():
    while True:
        print("\n---Applicant Options----\n")
        print("1. Submit application")
        print("2. Check Status")
        print("3. Exit")
        try:
            ch=int(input("Enter Choice number: "))
        except:
            ch=-1

        if ch==1:
            submit_application()
        elif ch==2:
            check_status()
        elif ch==3:
            break
        else:
            print("Invalid Choice")
