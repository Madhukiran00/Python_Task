from datetime import datetime,timedelta

# hours=int(input("Enter hours: "))
# minutes=(input("Enter minutes: "))


cur_time=int(datetime.now().strftime("%H,%M,%S"))   

print(datetime.(cur_time) + timedelta(hour=2))
  
    