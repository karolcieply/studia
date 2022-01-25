from datetime import datetime

year = input("Enter year: ")
week = input("Enter week: ")

data = datetime.fromisocalendar(int(year), int(week), 1)
print(data.strftime("%A %b %d %H:%M:%S %Y"))
