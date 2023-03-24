x = input("Enter a symbol:")

print(x)

for item in x:
    if item.isdigit():
        if int(item) % 2 == 0:
            print(f"{item} is even")
        else:
            print(f"{item} is odd")
    elif item.isupper():
        print(f"{item} is a capital letter")
    elif item.islower():
        print(f"{item} is a lowercase letter")
    else:
        print(f"{item} is a symbol")




import time

while True:
   print("I love Python")
   time.sleep(4.2)
