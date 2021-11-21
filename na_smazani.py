from datetime import date,timedelta
from datetime import datetime
date_string = '2009-11-29 03:17 PM'
format = '%Y-%m-%d %I:%M %p'
my_dates = datetime.strptime(date_string, format)

# This prints '2009-11-29 03:17 AM'
print(my_dates.strftime(format))

# # 03/25/2020,07:00 PM
my_date = "03/25/2020" #date.today()
my_time = "07:00 PM" #datetime.min.time()
mydatetime_str = my_date +" " + my_time
print(mydatetime_str)
my_datetime = datetime.strptime(mydatetime_str, "%m/%d/%Y %I:%M %p")
new_datetime = my_datetime + timedelta(hours=12)
print(new_datetime.strftime("%m/%d/%Y %I:%M %p"))


