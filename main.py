import json
from datetime import datetime
FILE_NAME_JSON = 'medications_dict.json'


def create_new_file_json(file_name):
    with open(file_name, "w") as write_file:
        json.dump({}, write_file, indent=4)
    return print(f'create new file {file_name}')


def load_json():
    try:
        med_dict = json.load(open(FILE_NAME_JSON))
        return med_dict
    except FileNotFoundError:
        print('file not found')
        create_new_file_json(FILE_NAME_JSON)
        return load_json()


medications_dict = load_json()


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
        return print_to_json(self.name, 'added')

    def del_medications(self: str):
        try:
            del medications_dict[self]
            return print_to_json(self, 'removed')
        except KeyError:
            print('Not find medication\n Choice medication in list\n')
            create_user_list()

    def find_medication(self: str):
        try:
            return print(medications_dict[self])
        except KeyError:
            print('Not find medication\n Choice medication in list\n')
            create_user_list()


def input_ex_date():
    try:
        date_entry = input('Enter expiration date (i.e. 2021.3.2)\n>>>')
        year, month, day = map(int, date_entry.split('.'))
        date_dt = datetime(year, month, day)
        date = date_dt.strftime("%m.%d.%Y")
        return date
    except ValueError:
        print('date entered incorrectly')
        return input_ex_date()


def input_medication():
    name = input('Enter name\n>>>')
    date = input_ex_date()
    number = int(input('Enter number of drugs\n>>>'))
    m1 = Medications(name.title(), date, number)
    return m1


def print_to_json(name, operation, m_dict=medications_dict):
    with open(FILE_NAME_JSON, "w") as write_file:
        json.dump(m_dict, write_file, indent=4)
    return print(f'{name} {operation} \n {FILE_NAME_JSON} - safe')


def create_user_list():
    user_list = []
    temp_list = list(medications_dict.keys())
    for i in temp_list:
        user_list.append(i)
    return print(sorted(user_list))


def list_exp():
    user_list_exp = []
    try:
        for i in medications_dict:
            i_exp = medications_dict[i]['expiration_date']
            year, month, day = map(int, i_exp.split('.'))
            i_exp_dt = datetime(day, month, year)
            if (i_exp_dt - datetime.now()).days <= 7:
                user_list_exp.append([i, i_exp])
        return user_list_exp
    except TypeError:
        print('List is empty')
        return user_list_exp


def msg_exp():
    if len(list_exp()) > 0:
        return print('The following drugs have expired:\n', list_exp())
    else:
        return print('No expired drugs')


def msg_command_list():
    return print("""\nEnter the command:
        * list - to view a list of medications.
        * exp - to view a list of following drugs have expired.
        * find - find a medication by name.
        * add  - add medication.
        * del  - removal of medications.
        * edit - change medications.
        * help - for help.
        * exit - for exit.
        """)


def command_user():
    while True:
        command = input('\nEnter the command:\n>>> ')
        if command.lower() == 'list':
            create_user_list()
        elif command.lower() == 'exp':
            msg_exp()
        elif command.lower() == 'find':
            find_name = input('Enter name medication\n>>>')
            Medications.find_medication(find_name.title())
        elif command.lower() == 'add':
            input_medication().add_medications()
        elif command.lower() == 'del':
            del_name = input('Enter name medication for delete\n>>>')
            Medications.del_medications(del_name)
        elif command.lower() == 'edit':
            input_medication().add_medications()
        elif command.lower() == 'help':
            msg_command_list()
        elif command.lower() == 'exit':
            break
        else:
            print("Unknown  command")


def start():
    print("Welcome to the first aid kit.\n")
    msg_exp()
    msg_command_list()
    command_user()


if __name__ == '__main__':
    start()
