from data.load_data import load_students,load_classes
from utils import input_student_id

def view_details():
    id=input_student_id()
    df=load_students()

    classes_df=load_classes()
    student_details = df[df['student_id'] == id].iloc[0]
    student_class=classes_df[classes_df['class_id']==student_details['class_id']].iloc[0]
    
    print("\n---Student Details---\n")
    print("Student ID: ",student_details['student_id'])
    print("Name: ",student_details['name'])
    print("DOB: ",student_details['dob'])
    print("Gender: ",student_details['gender'])
    print("Class and Section: ",student_class['class_grade'],student_class['section'])
    print("Attendance Percentage: ",student_details['attendance_percentage'])
    print("Parent Phone ",student_details['phone'])
    print("Fee status: ",student_details['fee_status'])