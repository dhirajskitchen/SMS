from data.load_data import load_students, load_timetable
import ast

def view_timetable(id: int):

    students_df = load_students()
    timetable_df = load_timetable()

    student = students_df[
        students_df['student_id'] == id
    ].iloc[0]

    tt_row = timetable_df[
        timetable_df['class_id'] == student['class_id']
    ]

    if tt_row.empty:
        print("No timetable found")
        return

    tt_dict = tt_row.iloc[0]['timetable']

    # Convert string to dictionary
    tt_dict = ast.literal_eval(tt_dict)

    printTimetable(tt_dict)


def printTimetable(tt_dict: dict):
    print(" " * 32+"---" + "CLASS TIMETABLE"+"---")
    
    tt_format = {
        'Monday': ['A', 'B', 'C', 'D', 'E'],
        'Tuesday': ['B', 'C', 'D', 'E', 'A'],
        'Wednesday': ['C', 'D', 'E', 'A', 'B'],
        'Thursday': ['D', 'E', 'A', 'B', 'C'],
        'Friday': ['E', 'A', 'B', 'C', 'D']
    }
    
    print(f"\n{'Day':<12} | {'Period 1':<15} | {'Period 2':<15} | {'Period 3':<15} | {'Period 4':<15} | {'Period 5':<15}")
    print(f"{'':12} | {'(09:00-10:00)':<15} | {'(10:00-11:00)':<15} | {'(11:00-12:00)':<15} | {'(12:00-01:00)':<15} | {'(01:00-02:00)':<15}")
    print("-" * 100)
    

    for day in tt_format:
        row = f"{day:<12} | "
        for slot in tt_format[day]:
            subject = str(tt_dict.get(slot, "N/A"))
            row += f"{subject:<15} | "
        print(row)
    
    print("-" * 100)