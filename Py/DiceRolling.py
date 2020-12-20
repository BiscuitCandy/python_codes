import random

x = True

while x:
    print("the number rolled is", end = " ")
    print(random.randrange(1,7))
    y = input("Wanna Try Again")
    if y.lower() in ["yes", "y"]:
        x = True
    else:
        x = False