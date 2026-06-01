from data.load_data import load_timetable,load_subjects
from data.store_data import store_timetable
from utils import input_class_id
import ast
import pandas as pd
from utils import input_class_teacher_id
def create_or_edit_timetable():
    
    timetable_df=load_timetable()

    class_id=input_class_id()
    teacher_id=input_class_teacher_id(class_id)
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

    tt_string = str(tt_dict)

    # Update existing row
    if not tt_row.empty:

        timetable_df.loc[
            timetable_df['class_id'] == class_id,
            'timetable'
        ] = tt_string

    # Add new row
    else:

        new_row = {
            'class_id': class_id,
            'timetable': tt_string
        }

        timetable_df = pd.concat(
            [timetable_df, pd.DataFrame([new_row])],
            ignore_index=True
        )
        

    if(store_timetable(timetable_df)):
        print("\nChanges Saved Successfully\n")
    else:
        print("\nFailed to Save Changes\n")

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

