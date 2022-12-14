x = input("Enter a symbol:")

list= list(x)

print(list)

for item in list:
    if item.isdigit():
        if int(item) % 2 == 0:
            print(f"{item} is even")
        else:
            print(f"{item} is odd")
    elif item.isupper():
        print(f"{item} is a capital letter")
    else:
        print(f"{item} is a lowercase letter")
else:
    print(f"{item} is a symbol")




import time
a = 0
while a < 10:
   print("I love Python")
   time.sleep(4.2)