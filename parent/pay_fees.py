from data.load_data import load_students

def pay_fees(id:int):
    students_df=load_students()
    status=students_df[students_df['student_id']==id].iloc[0]['fee_status']
    if status=='Paid':
        print("Fee already Paid")
        return
    
    print("--Fee Options--")
    print("1. Pay Now")
    print("2. Pay Later")
    while True:
        try:
            ch=int(input("Enter Choice: "))
        except ValueError:
            ch=-1
        
        if ch==1:
            print("Fees Paid")
            students_df.loc[
                students_df['student_id']==id,
                'fee_status'
            ]='Paid' 
            break
        elif ch==2:
            break
        else:
            print("Invalid Choice")
    
    # commit changes in students_df