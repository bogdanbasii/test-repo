import re

phonebook = {}

name = input('Enter a name:')

number = input('Enter a number:')


ukrphones = ''.join(re.findall(r"^(?:(?:\+380|380|0)\d{9})$", number))

if number == ukrphones:
    print(f"It is a Ukrainian number:{number}")
    phonebook[name] = number
else:
    phonebook.clear()
    print("It is not a Ukrainian number")



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

            ukrphones = ''.join(re.findall(r"^(?:(?:\+380|380|0)\d{9})$", number))

            if number == ukrphones:
                print(f"It is a Ukrainian number:{number}")
                phonebook[name] = number

                print('New contact was added')
            else:
                print("It is not a Ukrainian number")
        else:
            name in phonebook.keys()
            print("Fault. There is such name in a phonebook.")


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
        name = input('Enter a name:')
        if name not in phonebook.keys():
            print("Fault. There is no such name in a phonebook.")
        else:
            print(phonebook[name])

    elif command == 'end':
        break


#Task 2


file = input("Enter file name: ")
with open(file, "r") as f:
    content = f.read()
    print(content)

    content_new = re.sub(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+\S', '*@*', content)

print(content_new)

