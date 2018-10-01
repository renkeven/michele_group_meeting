import numpy as np
import pandas as pd

#Load Schedule
#See Usage on Initial Group Scheduler jupyter notebook:

def load_schedule(sdate,topic,presenter):
    schedule = pd.DataFrame({'Date':sdate,'Topic':topic, 'Speaker':presenter})
    
    return schedule

def update_schedule(schedule):
    
    Period_Dictionary = {0:'W-Mon', 1:'W-Tue', 2:'W-Wed', 3:'W-Thu', 4:'W-Fri'}
    Current_Day = schedule['Date'].dt.dayofweek[0]

    Start_Schedule_Date = schedule.iloc[0,schedule.columns.get_loc('Date')]
    
    
    
    if Start_Schedule_Date > pd.Timestamp(pd.datetime.now().date()):        
        return schedule
    
    else:
        End_Schedule_Date = schedule.iloc[-1,schedule.columns.get_loc('Date')]
        Start_Today_Periods = len(schedule[schedule['Date'] < pd.Timestamp(pd.datetime.now().date())])
    
        New_Schedule = schedule[schedule['Date'] >= pd.Timestamp(pd.datetime.now().date())].append(schedule[schedule['Date'] < pd.Timestamp(pd.datetime.now().date())])
        New_Schedule = New_Schedule.reset_index(drop=True)
    
        New_Dates = pd.date_range(End_Schedule_Date + pd.DateOffset(days=1), periods = Start_Today_Periods, freq=Period_Dictionary[Current_Day])
        New_Schedule.iloc[-Start_Today_Periods:, New_Schedule.columns.get_loc('Date')] = New_Dates
    
        return New_Schedule

"""
REDUNDANT
def update_schedule(schedule):    
    New_Schedule = schedule[schedule['Date'] >= pd.Timestamp(pd.datetime.now().date())].append(schedule[schedule['Date'] < pd.Timestamp(pd.datetime.now().date())])
    New_Schedule = New_Schedule.reset_index(drop=True)
       
    New_Start_Date = New_Schedule['Date'][0]
    Schedule_Days = pd.date_range(New_Start_Date, periods=len(schedule), freq='W-Thu')
    
    New_Schedule['Date'] = Schedule_Days
    
    return New_Schedule
"""

def Offset_Schedule(schedule,date,weeks_num):
    #Date Offset by 1 week at start_date
    
    if (schedule['Date'] == date).any() == True:
    
        Insert_Index = schedule[schedule['Date'] >= date].index[0]
        Offset = schedule.iloc[Insert_Index:,schedule.columns.get_loc('Date')] + pd.DateOffset(weeks=weeks_num)
        schedule.iloc[Insert_Index:,schedule.columns.get_loc('Date')] = Offset
    
    else:
        print 'Date not present in dataframe'
    
    return schedule

def DoW_Schedule(schedule,proposed_day):
    #Change Meeting Start Dates
    #0 = Monday, 4 = Friday
    
    current_day = schedule['Date'].dt.dayofweek[0]
    Offset = schedule['Date'] + pd.DateOffset(days=(proposed_day - current_day))        
    
    schedule['Date'] = Offset
    
    return schedule