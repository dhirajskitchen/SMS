from data.load_data import load_attendance, load_students

def view_attendance(student_id: int):

    attendance_df = load_attendance()
    students_df = load_students()
    
    student = students_df[students_df['student_id'] == student_id].iloc[0]
    student_attendance = attendance_df[attendance_df['student_id'] == student_id]
    
    print("\n---Attendance Details---\n")
    print(f"Student Name: {student['name']}")
    print(f"Student ID: {student['student_id']}")
    print(f"Current Attendance Percentage: {student['attendance_percentage']}%")
    
    if student_attendance.empty:
        print("\nNo attendance records found\n")
        return
    
    print("\n---Attendance Records (Last 5 Days)---\n")
    print(f"{'Date':<15} {'Status':<15}")
    print("-" * 30)
    
    # Show only last 5 days of attendance
    student_attendance_recent = student_attendance.tail(5)
    
    for index, record in student_attendance_recent.iterrows():
        date = record['date']
        status = record['status']
        print(f"{date:<15} {status:<15}")

    present_count = len(student_attendance[student_attendance['status'] == 'Present'])
    absent_count = len(student_attendance[student_attendance['status'] == 'Absent'])
    total_days = len(student_attendance)
    
    print("\n---Summary---\n")
    print(f"Total Days Marked: {total_days}")
    print(f"Present: {present_count}")
    print(f"Absent: {absent_count}")
    print()
