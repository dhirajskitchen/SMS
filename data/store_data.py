def store_students(df):
    try:
        df.to_csv("./data/students.csv", index=False)
        return True
    except:
        return False

def store_application(df):
    try:
        df.to_csv("./data/application.csv", index=False)
        return True
    except:
        return False

def store_classes(df):
    try:
        df.to_csv("./data/classes.csv", index=False)
        return True
    except:
        return False

def store_subjects(df):
    try:
        df.to_csv("./data/subjects.csv", index=False)
        return True
    except:
        return False

def store_marks(df):
    try:
        df.to_csv("./data/marks.csv", index=False)
        return True
    except:
        return False

def store_teachers(df):
    try:
        df.to_csv("./data/teachers.csv", index=False)
        return True
    except:
        return False

def store_timetable(df):
    try:
        df.to_csv("./data/timetable.csv", index=False)
        return True
    except:
        return False

def store_attendance(df):
    try:
        df.to_csv("./data/attendance.csv", index=False)
        return True
    except:
        return False