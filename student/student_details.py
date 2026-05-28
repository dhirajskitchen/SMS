from data.load_data import load_students,load_classes
import datetime
from data.store_data import store_students
def view_details(id:int):
    students_df=load_students()

    classes_df=load_classes()
    student_details = students_df[students_df['student_id'] == id].iloc[0]
    student_class=classes_df[classes_df['class_id']==student_details['class_id']].iloc[0]
    
    print("\n---Student Details---\n")
    print("Student ID: ",student_details['student_id'])
    print("Name: ",student_details['name'])
    print("DOB: ",student_details['dob'])
    print("Gender: ",student_details['gender'])
    print("Class and Section: ",student_class['class_grade'],student_class['section'])
    print("Attendance Percentage: ",student_details['attendance_percentage'])
    print("Fee status: ",student_details['fee_status'])

def edit_details(id:int):
    students_df=load_students()
    print("\n--Enter new Values--\n")
    
    new_Name=input("Enter new Name: ")

    # To ensure Date is imported in right format
    while True:
        dob = input("Enter DOB (DD-MM-YYYY): ")

        try:
            new_dob = datetime.datetime.strptime(
                dob,
                "%d-%m-%Y"
            ).strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Invalid Date Format")

    new_gender=input("Enter Gender (M or F):").upper()
    while(len(new_gender)!=1 or  (new_gender!="M" and new_gender!="F")):
        print("Invalid Gender")
        new_gender=input("Enter Gender (M or F):").upper()

    students_df.loc[students_df['student_id'] == id, [
    'name',
    'dob',
    'gender'
    ]] = [new_Name,new_dob,new_gender]

    if(store_students(students_df)):
        print("\nChanges Saved Successfully\n")
    else:
        print("\nFailed to Save Changes\n")
