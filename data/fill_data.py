import pandas as pd
import random
from datetime import datetime, timedelta

# -----------------------------
# SUBJECTS CSV
# -----------------------------

subjects = [
    [1, "Mathematics"],
    [2, "Science"],
    [3, "English"],
    [4, "Social Science"],
    [5, "Computer Science"]
]

subjects_df = pd.DataFrame(
    subjects,
    columns=["subject_id", "subject_name"]
)

subjects_df.to_csv(
    "./data/subjects.csv",
    index=False
)

# -----------------------------
# TEACHERS CSV
# -----------------------------

teachers = [
    [1, "Arun Kumar", 1],
    [2, "Priya Sharma", 2],
    [3, "Rahul Verma", 3],
    [4, "Sneha Iyer", 4],
    [5, "Vikram Rao", 5]
]

teachers_df = pd.DataFrame(
    teachers,
    columns=["teacher_id", "name", "subject_id"]
)

teachers_df.to_csv(
    "./data/teachers.csv",
    index=False
)

# -----------------------------
# CLASSES CSV
# -----------------------------

classes = [
    [1, 6, "A", "1,2,3,4,5", 1, 28],
    [2, 6, "B", "1,2,3,4,5", 2, 30],
    [3, 7, "A", "1,2,3,4,5", 3, 27],
    [4, 7, "B", "1,2,3,4,5", 4, 25]
]

classes_df = pd.DataFrame(
    classes,
    columns=[
        "class_id",
        "class_grade",
        "section",
        "subject_ids",
        "class_teacher_id",
        "strength"
    ]
)

classes_df.to_csv(
    "./data/classes.csv",
    index=False
)

# -----------------------------
# STUDENTS CSV
# -----------------------------

student_names = [
    "Aarav", "Vivaan", "Aditya", "Diya",
    "Ananya", "Ishaan", "Meera", "Rohan",
    "Kavin", "Nisha"
]

students = []

for i in range(1, 11):

    dob = (
        datetime(2010, 1, 1)
        + timedelta(days=random.randint(0, 1500))
    ).date()

    students.append([
        i,
        student_names[i - 1],
        dob,
        random.choice(["M", "F"]),
        random.randint(1, 4),
        round(random.uniform(75, 100), 2),
        random.choice(["Paid", "Pending"])
    ])

students_df = pd.DataFrame(
    students,
    columns=[
        "student_id",
        "name",
        "dob",
        "gender",
        "class_id",
        "attendance_percentage",
        "fee_status"
    ]
)

students_df.to_csv(
    "./data/students.csv",
    index=False
)

# -----------------------------
# MARKS CSV
# -----------------------------

marks = []
mark_id = 1

for student_id in range(1, 11):

    for subject_id in range(1, 6):

        marks.append([
            mark_id,
            student_id,
            subject_id,
            subject_id,
            random.randint(40, 100),
            100
        ])

        mark_id += 1

marks_df = pd.DataFrame(
    marks,
    columns=[
        "mark_id",
        "student_id",
        "subject_id",
        "teacher_id",
        "marks_obtained",
        "total_marks"
    ]
)

marks_df.to_csv(
    "./data/marks.csv",
    index=False
)

# -----------------------------
# APPLICATION CSV
# -----------------------------

applications = [
    [1, "Ritika", "2012-05-10", "F", 6, "Pending"],
    [2, "Harish", "2011-09-14", "M", 7, "Accepted"],
    [3, "Sanjana", "2012-11-22", "F", 6, "Rejected"]
]

applications_df = pd.DataFrame(
    applications,
    columns=[
        "application_no",
        "name",
        "dob",
        "gender",
        "class_grade",
        "status"
    ]
)

applications_df.to_csv(
    "./data/application.csv",
    index=False
)

# -----------------------------
# TIMETABLE CSV
# -----------------------------

timetable = [
    [1, "Monday", "09:00-10:00", 1],
    [1, "Monday", "10:00-11:00", 2],
    [1, "Monday", "11:00-12:00", 3],
    [2, "Tuesday", "09:00-10:00", 4],
    [2, "Tuesday", "10:00-11:00", 5]
]

timetable_df = pd.DataFrame(
    timetable,
    columns=[
        "class_id",
        "day",
        "time_slot",
        "subject_id"
    ]
)

timetable_df.to_csv(
    "./data/timetable.csv",
    index=False
)

print("Dummy CSV files generated successfully!")