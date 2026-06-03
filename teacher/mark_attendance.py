from data.load_data import load_students, load_classes, load_attendance
from data.store_data import store_attendance, store_students
from utils import input_class_id, input_date,input_class_teacher_id
import datetime

def mark_attendance():
    """Teacher marks attendance for a class on a specific date"""
    attendance_df = load_attendance()
    students_df = load_students()
    
    class_id = input_class_id()
    input_class_teacher_id(class_id)
    date_obj = input_date()

    # Get all students in the class
    class_students = students_df[students_df['class_id'] == class_id]
    
    if class_students.empty:
        print("No students found in this class")
        return
    
    # Mark attendance for each student
    for index, student in class_students.iterrows():
        student_id = student['student_id']
        student_name = student['name']
        
        while True:
            status = input(f"Mark attendance for {student_name} ({student_id}) - (P)resent or (A)bsent: ").upper()
            if status in ['P', 'A']:
                break
            print("Invalid input. Please enter P or A")
        
        # Convert P/A to Present/Absent
        attendance_status = "Present" if status == "P" else "Absent"
        
        # Check if attendance already exists for this student on this date
        existing = attendance_df[
            (attendance_df['student_id'] == student_id) & 
            (attendance_df['class_id'] == class_id) & 
            (attendance_df['date'] == date_obj)
        ]
        
        if not existing.empty:
            # Update existing attendance
            attendance_df.loc[
                (attendance_df['student_id'] == student_id) & 
                (attendance_df['class_id'] == class_id) & 
                (attendance_df['date'] == date_obj),
                'status'
            ] = attendance_status
        else:
            # Add new attendance record
            new_id = attendance_df['attendance_id'].max() + 1
            new_row = {
                'attendance_id': new_id,
                'student_id': student_id,
                'class_id': class_id,
                'date': str(date_obj),
                'status': attendance_status
            }
            attendance_df.loc[len(attendance_df)] = new_row
    
    # Calculate and update attendance percentage for all students in the class
    update_attendance_percentage(class_id, attendance_df, students_df)
    
    # Save changes
    if store_attendance(attendance_df):
        print("\nAttendance marked successfully\n")
    else:
        print("\nFailed to save attendance\n")


def update_attendance_percentage(class_id, attendance_df, students_df):
    """Calculate and update attendance percentage for all students in a class"""
    class_students = students_df[students_df['class_id'] == class_id]
    
    for index, student in class_students.iterrows():
        student_id = student['student_id']
        
        # Get all attendance records for this student
        student_attendance = attendance_df[attendance_df['student_id'] == student_id]
        
        if len(student_attendance) == 0:
            percentage = 0
        else:
            # Count present days
            present_count = len(student_attendance[student_attendance['status'] == 'Present'])
            total_days = len(student_attendance)
            percentage = (present_count / total_days) * 100
        
        # Update student's attendance percentage
        students_df.loc[students_df['student_id'] == student_id, 'attendance_percentage'] = round(percentage, 2)
    
    # Save updated student records
    if not store_students(students_df):
        print("Warning: Failed to update attendance percentage in student records")
