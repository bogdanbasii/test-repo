# Task 1
import json


try:
    with open('json_phonebook.json', 'r') as file:
        data = file.read()
        phonebook = json.loads(data)
except FileNotFoundError:
    # if file does not exist
    phonebook = {}

while True:
    user_input = input('Enter a command:')
    split_input = user_input.split()
    command = split_input[0]


    if command == 'stats':
        print(len(phonebook))


    elif command == 'add':
        name = input('Enter a name:')
        if not name in phonebook.keys():
            number = input('Enter a number:')
            phonebook[name] = number
            with open('json_phonebook.json', 'w+') as file:
                content = json.dumps(phonebook)
                file.write(content)
            print('New contact was added')
    

    elif command == 'del':
        key = input('Enter some name: ')
        if phonebook.get(key):
            del phonebook[key]
            with open('json_phonebook.json', 'w') as file:
                data = json.dumps(phonebook)
                file.write(data)
            print("Record was deleted")
        else:
            print('Such record never existed')



    elif command == 'list':
        list = (phonebook.items())
        print(list)


    elif command == 'show':
        print(phonebook)
        name = input('Enter a name:')
        if name not in phonebook.keys():
            print("Fault. There is no such name in a phonebook.")
        else:
            print(phonebook[name])


    elif command == 'end':
        break



# Task 2

def log_message(func):

    def wrap(*args, **kwargs):
        print(time.ctime())
        return_value = func(*args, **kwargs)
        fname = func.__name__
        print(fname)
        f = open('log1.txt', "w+")
        f.write(time.ctime() +os.linesep)
        f.write(fname)
        f.close()
        return return_value

    return wrap

@log_message
def my_func():
    print('This is my func')
my_func()



# Task 3

import os

import time
class MyException(Exception):
    def __init__(self, message):
        with open('log2.txt', 'w') as f:
            f.write(time.ctime() + os.linesep)
            f.write(str(message))
    pass
if True:
    raise MyException('Custom exception is occured')
