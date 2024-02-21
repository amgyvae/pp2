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
