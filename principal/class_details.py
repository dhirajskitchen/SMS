from data.load_data import load_classes,load_teachers

def view_class_details():
    class_df=load_classes()
    teachers_df=load_teachers()
    while True:
        try:
            class_id=int(input("Enter Class ID: "))
            if class_id in class_df['class_id'].values:
                break
            print("Invalid ID")
        except ValueError:
            print("Invalid ID")
    
    class_details=class_df[class_df['class_id']==class_id].iloc[0]
    print("\n--Class Deatails--\n")
    print("Class id: ",class_details['class_id'])
    print("Class Grade: ",class_details['class_grade'])
    print("Section: ",class_details['section'])
    print("Subjects: ",class_details['subjects'])
    print("Class Teacher ID: ",class_details['class_teacher_id'])
    print("Class Teacher: ",teachers_df[teachers_df['teacher_id']==class_details['class_teacher_id']].iloc[0]['name'])



