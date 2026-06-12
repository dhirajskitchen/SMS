from data.load_data import load_marks,load_subjects

def view_marks(id:int):
    marks_df=load_marks()
    subjects_df=load_subjects()
    student_marks = marks_df[marks_df['student_id'] == id]
    print("\n---Student Marks---\n")
    for index, row in student_marks.iterrows():
        print("Subject: ", subjects_df[
                                            subjects_df['subject_id'] == row['subject_id']
                                        ].iloc[0][
                                            'subject_name'])
        print("Marks:", row['marks_obtained'])
