from data.load_data import load_application,load_students,load_classes

def view_applications():
    applications_df=load_application()
    students_df=load_students()
    classes_df=load_classes()
    pending_applications=applications_df[applications_df['status']=='Pending']

    print("\n--Pending Application--\n")
    for index, application in pending_applications.iterrows():
        view_application(application)
        print("\n--Application Choices--\n")
        print("1. Accept")
        print("2. Reject")
        print("3. Skip")

        while True:
            try:
                ch=int(input("Enter choice for application: "))
            except:
                ch=-1
            if ch==1:
                applications_df,students_df,classes_df=accept_application(application,applications_df,students_df,classes_df)
                break
            elif ch==2:
                applications_df=reject_application(application,applications_df)
                break
            elif ch==3:
                break
            else:
                print("Invalid Choice")

    # Commit changes in application_df,classes_df and students_df
def view_application(application):
    print("Application No: ",application['application_no'])
    print("Name: ",application['name'])
    print("DOB: ",application['dob'])
    print("Gender: ",application['gender'])
    print("Class Grade: ",application['class_grade'])

def accept_application(application,applications_df,students_df,classes_df):
    applications_df.loc[
            applications_df['application_no']
            == application['application_no'],
            'status'
        ] = 'Accepted'
    
    selected_class = classes_df[
            classes_df['class_grade'] == application['class_grade']
        ].sort_values('strength').iloc[0]['class_id']

    classes_df.loc[
            classes_df['class_id'] == selected_class,
            'strength'
        ] += 1
    
    new_Student= {
        'student_id': students_df['student_id'].max() + 1,
        "name":application['name'],
        "dob": application['dob'],
        "gender":application['gender'],
        "class_id":selected_class,
        "attendance_percentage":0,
        "fee_status":"Not Paid"
    }
    students_df.loc[len(students_df)]=new_Student
    
    return (applications_df,students_df,classes_df)

def reject_application(application,applications_df):
    applications_df.loc[
        applications_df['application_no']
        == application['application_no'],
        'status'
    ] = 'Rejected'
    return applications_df