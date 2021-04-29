import json
from datetime import datetime
import sys


medications_dict = json.load(open('medications_dict.json'))


class Medications:
    def __init__(self, name: str, expiration_date: str = '', number_of_medications=0):
        self.name = name
        self.expiration_date = expiration_date
        self.number_of_medications = number_of_medications

    def add_medications(self):
        x = {
            self.name: {
                'name': self.name,
                'expiration_date': self.expiration_date,
                'number_of_medications': self.number_of_medications
                }
            }
        medications_dict.update(x)
        return print_to_json()


def del_medications():
    m_del = input('Enter name medication for delete\n>>>')
    del medications_dict[m_del]
    print(f'{m_del} removed')
    return print_to_json()


def input_ex_date():
    date_entry = input('Enter expiration date (i.e. 2021.3.2)\n>>>')
    year, month, day = map(int, date_entry.split('.'))
    date_dt = datetime(year, month, day)
    date = date_dt.strftime("%m.%d.%Y")
    return date


def input_medication():
    name = input('Enter name\n>>>')
    # date = input('Enter expiration date (dd.mm.yyyy)\n>>>')
    date = input_ex_date()
    number = int(input('Enter number of drugs\n>>>'))
    m1 = Medications(name, date, number)
    return m1


def find_medication():
    name = input('Enter name medication\n>>>')
    return print(medications_dict[name])


def print_to_json():
    with open("medications_dict.json", "w") as write_file:
        json.dump(medications_dict, write_file, indent=4)
    return print('medications_dict.json - safe')


def create_user_list():
    user_list = []
    temp_list = list(medications_dict.keys())
    for i in temp_list:
        user_list.append(i)
    return print(sorted(user_list))


def menu():
    print("Welcome to the first aid kit.")
    print("""Enter the command:
    * list - to view a list of medications.
    * find - find a medication by name
    * add  - add medication
    * del  - removal of medications
    * edit - change medications 
    * exit - for exit """)

    while True:
        command = input('\nEnter the command:\n>>> ')
        if command == 'list':
            create_user_list()
        elif command == 'find':
            find_medication()
        elif command == 'add':
            input_medication().add_medications()
        elif command == 'del':
            del_medications()
        elif command == 'edit':
            input_medication().add_medications()
        elif command == 'exit':
            break
        else:
            print("Unknown  command")


menu()
