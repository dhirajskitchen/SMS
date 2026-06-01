from data.load_data import load_classes,load_teachers,load_subjects
from utils import input_class_id

def view_class_details():
    class_df=load_classes()
    teachers_df=load_teachers()
    class_id=input_class_id()
    
    class_details=class_df[class_df['class_id']==class_id].iloc[0]
    print("\n--Class Deatails--\n")
    print("Class id: ",class_details['class_id'])
    print("Class Grade: ",class_details['class_grade'])
    print("Section: ",class_details['section'])
    print("Subjects: ",get_subjects(class_details['subject_ids']))
    print("Class Teacher ID: ",class_details['class_teacher_id'])
    print("Class Teacher: ",teachers_df[teachers_df['teacher_id']==class_details['class_teacher_id']].iloc[0]['name'])
    print("Class Strength: ",class_details['strength'])
    
def get_subjects(subject_ids):
    subjects_df=load_subjects()
    subject_ids = list(
        map(int, subject_ids.split(','))
    )

    subjects = subjects_df[
        subjects_df['subject_id'].isin(subject_ids)
    ]['subject_name'].tolist()

    return subjects



