from datetime import datetime



date_entry = input('Enter expiration date (i.e. 2021,3,2)\n>>>')
year, month, day = map(int, date_entry.split(','))
date_dt = datetime(year, month, day)
date = date_dt.strftime("%m.%d.%Y")
print(type(date), date)
