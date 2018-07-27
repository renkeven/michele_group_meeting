import numpy as np
import pandas as pd

#Load Schedule
#See Usage on Initial Group Scheduler jupyter notebook:

def load_schedule(sdate,topic,presenter):
    schedule = pd.DataFrame({'Date':sdate,'Topic':topic, 'Speaker':presenter})
    
    return schedule

def update_schedule(schedule):    
    New_Schedule = schedule[schedule['Date'] >= pd.Timestamp(pd.datetime.now().date())].append(schedule[schedule['Date'] < pd.Timestamp(pd.datetime.now().date())])
    New_Schedule = New_Schedule.reset_index(drop=True)
       
    New_Start_Date = New_Schedule['Date'][0]
    Schedule_Days = pd.date_range(New_Start_Date, periods=len(schedule), freq='W-Thu')
    
    New_Schedule['Date'] = Schedule_Days
    
    return New_Schedule

def Offset_Schedule(schedule,date,weeks_num):
    #Date Offset by 1 week at start_date
    Insert_Index = schedule[schedule['Date'] >= date].index[0]
    Offset = schedule.iloc[Insert_Index:,schedule.columns.get_loc('Date')] + pd.DateOffset(weeks=weeks_num)
    schedule.iloc[Insert_Index:,schedule.columns.get_loc('Date')] = Offset
    
    return schedule