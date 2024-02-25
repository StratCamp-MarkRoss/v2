print("Enter number")
num = input()
num= int(num)
if num > 0:
    print("Positive")
    if (num % 2) == 0:
        print("Even")
    else:
        print("Odd")
elif num < 0:
    print("Negative")
    if (num % 2) == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Zero") 
