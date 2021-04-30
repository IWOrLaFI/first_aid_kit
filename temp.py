import json
from datetime import datetime
import sys

medications_dict = json.load(open('medications_dict.json'))
user_list = []


def create_user_list():
    user_list = []
    temp_list = list(medications_dict.keys())
    for i in temp_list:
        user_list.append(i)
    return print(sorted(user_list))

    year, month, day = map(int, date_entry.split('.'))
    date_dt = datetime(year, month, day)
    date = date_dt.strftime("%m.%d.%Y")


for i in medications_dict:
    temp_list = list(medications_dict[i]['expiration_date'])
    i_exp = medications_dict[i]['expiration_date']
    year, month, day = map(int, i_exp.split('.'))
    i_exp_dt = datetime(day, month, year)
    if (i_exp_dt - datetime.now()).days <= 7:
        user_list.append([i, i_exp])
print(user_list)

