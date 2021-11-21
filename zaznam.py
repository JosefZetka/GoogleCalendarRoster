from datetime import date,timedelta,datetime

class Zaznam():
    def __init__(self,mesic,den,smena):
        self.mesic = mesic
        self.den = den
        self.smena = smena
class Record():
    def __init__(self,Subject,StartDate,StartTime,EndDate,EndTime):
        self.Subject = Subject
        self.StartDate = StartDate
        self.StartTime = StartTime
        self.EndDate = EndDate
        self.EndTime = EndTime
"""
Subject
The name of the event, required.
Example: Final exam
Start Date
The first day of the event, required.
Example: 05/30/2020
Start Time
The time the event begins.
Example: 10:00 AM
End Date
The last day of the event.
Example: 05/30/2020
End Time
The time the event ends.
Example: 1:00 PM
All Day Event
Whether the event is an all-day event. Enter True if it's an all-day event, and False if it isn't.
Example: False
Description
Description or notes about the event.
Example: 50 multiple choice questions and two essay questions
Location
The location for the event.
Example: "Columbia, Schermerhorn 614"
"""

def casy(smena):
    zacatek = ''
    konec = ''
    r = []
    if smena == 'R' or smena =='Z':
        zacatek = '07:00 AM'
        konec = '07:00 PM'
    elif smena =='N':
        zacatek = '07:00 PM'
        konec = '07:00 AM'
    else:
        zacatek = '07:00 AM'
        konec = '07:00 PM'
    r = [zacatek,konec]
    return r

def switch_demo(argument):
    switcher = \
    {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print(switcher.get(argument,"NOTHING"))

def in_case(arg):
    switcher = {
        "I.22": "01",
        "II.22": "02",
        "III.22": "03",
        "IV.22": "04",
        "V.22": "05",
        "VI.22": "06",
        "VII.22": "07",
        "VIII.22": "08",
        "IX.22": "09",
        "X.22": "10",
        "XI.22": "11",
        "XII.22": "12"
    }
    #print(switcher.get(arg,"NOTHING"))
    return(switcher.get(arg,str(arg)))

def datetime_str_adding(startdate,starttime):
    try:
        mydatetime_str = startdate +" " + starttime
        my_datetime = datetime.strptime(mydatetime_str, "%m/%d/%Y %I:%M %p")
        new_datetime = my_datetime + timedelta(hours=12)
        v = str(new_datetime.strftime("%m/%d/%Y,%I:%M %p"))
    except:
        v= str("")
    return v

