
    
    
from datetime import datetime, timedelta

print("⏰..Set Alaram..⏰")
hour=int(input("Enter Hours u want to sleep: "))
minute=int(input("Enter Minutes u want to sleep: "))
cur_time = datetime.now() 
new_time = cur_time + timedelta(hours=hour,minutes=minute)

print("You have only {0} hours {1} minutes ".format(hour,minute))
print("You wake up at :", new_time.strftime("%H:%M:%S"))
