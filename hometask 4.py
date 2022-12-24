phonebook = {}

name = input('Enter a name:')

number = input('Enter a number:')


if phonebook.get(name):
    print(f'{name} already exists. You need to delete a record and add again if you want to change it')
else:
    phonebook[name] = number




while True:
    user_input = input('Enter a command:')
    split_input = user_input.split()

    command = split_input[0]
    if command == 'stats':
        print(len(phonebook))
    elif command == 'add':
        name=input('Enter a name:')
        if name in phonebook.keys():
            print("Fault. There is such name in a phonebook.")
            
        else:
            print("There is no such name in a phonebook. Continue.")
        name=input('Enter a name:')
        number=input('Enter a number:')
        phonebook[name]=number
        print('New contact was added')
    elif command == 'delete':
            key = input('Enter some name: ')
            if phonebook.get(key):
                del phonebook[key]
                print("Record was deleted")
            else:
                print('Such record never existed')
    elif command == 'list':
        list = (phonebook.items())
        print(list)
    elif command == 'show':
        print(phonebook)
        name=input('Enter a name:')
        print(phonebook[name])
    elif command == 'end':
        break
