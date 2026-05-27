from utils import input_application_no
from data.load_data import load_application

def check_status():
    application_no=input_application_no()
    application_df=load_application()

    print("Application Status: ",application_df[application_df['application_no']==application_no].iloc[0]['status'])
