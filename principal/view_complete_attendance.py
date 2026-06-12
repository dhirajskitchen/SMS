from data.load_data import load_students,load_attendance,load_classes
from utils import input_date
def view_complete_attendance():
    date=input_date()
    students_df=load_students()
    attendance_df=load_attendance()
    classes_df=load_classes()
    attendance_df=attendance_df[attendance_df['date']==date].sort_values('class_id')
    if len(attendance_df)==0:
        print("\n No attendance data found for the date\n")
        return None
    student_lookup = students_df.set_index('student_id')['name'].to_dict()
    class_lookup = (
        classes_df
        .set_index('class_id')[['class_grade', 'section']]
        .to_dict('index')
    )

    print(f"{'Name':<25} {'Class':<10} {'Status':<10}")
    print("-" * 50)

    for _, row in attendance_df.iterrows():
        class_info = class_lookup.get(row['class_id'])

        if class_info:
            class_name = f"{class_info['class_grade']}-{class_info['section']}"
        else:
            class_name = "Unknown"

        print(
            f"{student_lookup.get(row['student_id'], 'Unknown'):<25} "
            f"{class_name:<10} "
            f"{row['status']:<10}"
    )