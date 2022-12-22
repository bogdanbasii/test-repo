name = input('Enter a name:')

number = input('Enter a number:')


phonebook = {name:number}

while True:
    user_input = input('Enter a command:')
    split_input = user_input.split()

    command = split_input[0]

    if command == 'stats':
        print(len(phonebook))
    elif command == 'add':
         for i in range(1):
             name=input('Enter a name:')
             number=input('Enter a number:')
             phonebook[name]=number
             print('New contact was added')
    elif command == 'del':
        print(phonebook)
        del phonebook[input('Enter a name to delete: ')]
        print('Contact was deleted')
    elif command == 'list':
        list = (phonebook.items())
        print(list)
    elif command == 'show':
        name=input('Enter a name:')
        print(phonebook[name])
    elif command == 'end':
        break      