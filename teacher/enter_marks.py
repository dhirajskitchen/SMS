from data.load_data import load_students,load_classes,load_marks,load_subjects
from utils import input_teacher_id

def Mark_student(id:int,teacher_id:int,marks_df):
    student_df=load_students()
    classes_df=load_classes()
    subject_df=load_subjects()
    student=student_df[student_df['student_id']==id].iloc[0]

    subject_ids=classes_df[classes_df['class_id']==student['class_id']].iloc[0]['subject_ids']
    subject_ids = list(map(int, subject_ids.split(',')))

    student_marks=marks_df[marks_df['student_id']==id]

    for subject_id in subject_ids:
        if subject_id not in student_marks['subject_id'].values:
            new_row = {
                'mark_id':  marks_df['mark_id'].max() + 1,
                'student_id': id,
                'subject_id': subject_id,
                'teacher_id': teacher_id,
                'marks_obtained': None,
                'total_marks': 100
            }
            marks_df.loc[len(marks_df)] = new_row
    
    for subject_id in subject_ids:
        subject=subject_df[subject_df['subject_id']==subject_id].iloc[0]['subject_name']
        while True:
            try:
                mark=int(input(f"Enter Marks for {student_df[student_df['student_id']==id].iloc[0]['name']} ({id}) in {subject}"))
                if mark in range(0,101):
                    break
                print("Invalid Mark")
            except ValueError:
                print("Invalid Mark")
        
        marks_df.loc[
            (marks_df['student_id'] == id) &
            (marks_df['subject_id'] == subject_id),
            'marks_obtained'
        ] = mark

    return marks_df

def Mark_class():
    teacher_id=input_teacher_id()
    student_df=load_students()
    classes_df=load_classes()
    marks_df=load_marks()
    while True:
        try:
            class_id=int(input("Enter Class ID: "))
            if class_id in classes_df['class_id'].values:
                break
            print("Invalid ID")
        except:
            print("Invalid ID")

    students=student_df[student_df['class_id']==class_id]
    for index, student in students.iterrows():
        marks_df=Mark_student(student['student_id'],teacher_id,marks_df)

    # function to commit changes to csv
