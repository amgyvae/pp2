#1st task
from datetime import datetime, timedelta

current_date = datetime.now()

five_days_ago = current_date - timedelta(days=5)

print("Current Date:", current_date)
print("Five Days Ago:", five_days_ago)

#2nd task
from datetime import datetime, timedelta

current_date = datetime.now()

yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", current_date)
print("Tomorrow:", tomorrow)

#3rd task
from datetime import datetime

current_datetime = datetime.now()

current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Original Datetime:", current_datetime)
print("Datetime without Microseconds:", current_datetime_without_microseconds)

#4th task
from datetime import datetime

date1 = datetime(2024, 2, 14, 10, 0, 0)
date2 = datetime(2024, 2, 21, 9, 30, 0)

difference_seconds = (date2 - date1).total_seconds()

print("Difference between the two dates in seconds:", difference_seconds)
