from data.load_data import load_timetable,load_subjects
from utils import input_class_id
import ast
def create_or_edit_timetable():
    timetable_df=load_timetable()

    class_id=input_class_id()

    tt_row = timetable_df[
        timetable_df['class_id'] == class_id
    ]

    if tt_row.empty:
        tt_dict={'A':None,'B':None,'C':None,'D':None,'E':None}
    else:
        tt_dict = tt_row.iloc[0]['timetable']
        # Convert string to dictionary
        tt_dict = ast.literal_eval(tt_dict)

    for slot in tt_dict:
        print(f"Current Subject in slot {slot} - {tt_dict[slot]}")
        subject=get_subject(slot)
        if subject==None:
            continue
        tt_dict[slot]=subject

    # Function to commit changes to timatable.csv

def get_subject(slot):
    subjects_df=load_subjects()
    while True:
        subject=input(f"Enter Subject for the slot {slot}: ")
        if subject=='':
            return None
        
        if subject in subjects_df['subject_name'].values:
            return subject
        
        print("Invalid Subject")
    return None

