import datetime
from data.load_data import load_application
from data.store_data import store_application
from utils import get_phone_number
def submit_application():
    application_df=load_application()
    print("\n--Enter Values--\n")
    
    name=input("Enter Name: ")
    while(name==""):
        print("Name Can't be empty")
        name=input("Enter Name: ")

    # To ensure Date is imported in right format
    while True:
        dob = input("Enter DOB (DD-MM-YYYY): ")

        try:
            dob = datetime.datetime.strptime(dob, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Invalid Date Format")

    gender=input("Enter Gender (M or F):").upper()
    while(len(gender)!=1 or  (gender!="M" and gender!="F")):
        print("Invalid Gender")
        gender=input("Enter Gender (M or F):").upper()

    while True:
        try:
            class_grade=int(input("Enter Grade (1-12): "))
            if class_grade in range(1,13):
              break
            print("Invalid Grade")  
        except ValueError:
            print("Invalid Grade")

    phone=get_phone_number()
    new_application = {
        'application_no':  application_df['application_no'].max() + 1,
        "name":name,
        "dob": dob,
        "gender":gender,
        "class_grade":class_grade,
        "phone":phone,
        "status":"Pending"
    }
    
    application_df.loc[len(application_df)] = new_application
    print("\nApplication Submitted Successfully\n")
    print(f"Check Application Status using the application no: {new_application['application_no']}")

    # Function to save updated application.csv
    if(store_application(application_df)):
        print("\nChanges Saved Successfully\n")
    else:
        print("\nFailed to Save Changes\n")