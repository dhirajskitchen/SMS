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

    tt_format = {
        'Monday': ['A', 'B', 'C', 'D', 'E'],
        'Tuesday': ['B', 'C', 'D', 'E', 'A'],
        'Wednesday': ['C', 'D', 'E', 'A', 'B'],
        'Thursday': ['D', 'E', 'A', 'B', 'C'],
        'Friday': ['E', 'A', 'B', 'C', 'D']
    }

    for day in tt_format:

        print(day, end=" ")

        for slot in tt_format[day]:
            print(tt_dict[slot], end=" ")

        print()