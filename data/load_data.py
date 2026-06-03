import pandas as pd
import os

# LOAD STUDENTS TABLE
def load_students():
    # print(os.getcwd())
    df=pd.read_csv("./data/students.csv")
    df["phone"] = df["phone"].astype(str)
    return df

# LOAD SUBJECTS TABLE
def load_subjects():
    return pd.read_csv("./data/subjects.csv")

# LOAD TEACHERS TABLE
def load_teachers():
    return pd.read_csv("./data/teachers.csv")

# LOAD CLASSES TABLE
def load_classes():
    return pd.read_csv("./data/classes.csv")

# LOAD MARKS TABLE
def load_marks():
    return pd.read_csv("./data/marks.csv")

# LOAD TIMETABLE TABLE
def load_timetable():
    return pd.read_csv("./data/timetable.csv")

# LOAD APPLICATION TABLE
def load_application():
    return pd.read_csv("./data/application.csv")

# LOAD ATTENDANCE TABLE
def load_attendance():
    return pd.read_csv("./data/attendance.csv")