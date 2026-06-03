from data.load_data import load_students,load_teachers,load_application,load_classes
import datetime

def input_date():
    while True:
        try:
            date_str = input("Enter Date (DD-MM-YYYY): ")
            date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
            # Check if date is not in future
            if date_obj > datetime.date.today():
                print("Cannot mark attendance for future dates")
                continue
            return date_obj
        except ValueError:
            print("Invalid Date Format")

def input_student_id():
    students_df=load_students()
    while True:
        try:
            id=int(input("Enter ID: "))
            if id in students_df['student_id'].values:
                return id
            print("Invalid ID")
        except:
            print("Invalid ID")

def input_teacher_id():
    teachers_df=load_teachers()
    while True:
        try:
            id=int(input("Enter Teacher ID: "))
            if id in teachers_df['teacher_id'].values:
                return id
            print("Invalid ID")
        except:
            print("Invalid ID")

def input_application_no():
    applications_df=load_application()
    while True:
        try:
            applications_no=int(input("Enter Application No: "))
            if applications_no in applications_df['application_no'].values:
                return applications_no
            print("Invalid Application No")
        except:
            print("Invalid Application No")

def input_class_id():
    class_df=load_classes()
    while True:
        try:
            class_id=int(input("Enter Class ID: "))
            if class_id in class_df['class_id'].values:
                return class_id
            print("Invalid ID")
        except ValueError:
            print("Invalid ID")

def input_class_teacher_id(class_id:int):
    teachers_df=load_teachers()
    classes_df=load_classes()
    while True:
        try:
            id=int(input("Enter Teacher ID: "))
            if id==classes_df[classes_df['class_id']==class_id].iloc[0]['class_teacher_id']:
                return id
            elif id in teachers_df['teacher_id'].values:
                print("Your not the class teacher for this class")
                continue
            print("Invalid ID")
        except:
            print("Invalid ID")

def get_phone_number():
    while True:
        phone = input("Enter a 10-digit phone number: ").strip()

        if phone.isdigit() and len(phone) == 10:
            return phone

        print("Invalid phone number. Please enter exactly 10 digits.")