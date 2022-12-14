x = input("Enter a symbol:")
if x.isdigit():
    if int(x)%2==0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
else:
        print(f"{x} is a word with len of {len(x)}")







