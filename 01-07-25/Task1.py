from datetime import datetime 

#now()
print(datetime.now())
print(datetime.now().date())

# strptime()

print(datetime.strptime("2025-07-01","%Y-%m-%d"))

print(datetime.strptime("01-07-2025","%d-%m-%Y"))

print(datetime.strptime("jul-04-2025","%b-%d-%Y"))

print(datetime.strptime("july 05 25","%B %d %y"))

print(datetime.strptime("jun-06-2022",'%b-%d-%Y'))

print(datetime.strptime("jun-06-2022 02:15:23", '%b-%d-%Y %H:%M:%S'))

# strftime()

cur_datetime=datetime.now()

print(cur_datetime.strftime("%Y-%m-%d"))

print(cur_datetime.strftime("%d-%m-%y"))

print(cur_datetime.strftime("%d-%m-%Y"))

print(cur_datetime.strftime("%H-%M-%S"))

print(cur_datetime.strftime("%d"))



#Replace()

dt=datetime(2025,6,1)
print(dt)

print(dt.replace(year=2003))

print(dt.replace(month=12))

print(dt.replace(day=16))



# Weekday()
print(datetime.now())

print(datetime.now().weekday())

print(datetime(2024,9,6).weekday())

# timedelta

from datetime import datetime, timedelta

print(datetime(2025,7,1) + timedelta(days=10))

print(datetime(2025,4,12) + timedelta(days=5))

print(datetime.now()+timedelta(hours=5))


# isoformat

print(datetime.now().isoformat())

