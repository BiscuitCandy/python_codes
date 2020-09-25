import random
from functools import reduce

def Divisibility(n):
    def by(x):
        if n%x:
            return ("The given number is not divisible by "+ str(x))
        else:
            return ("The given number is divisible by "+ str(x))
    return by

def isPrime(x):
    for i in range(2, int(pow(x, 0.5))+1):
        if x%i == 0 :
            return ("The given nUmber is not prime")
        else:
            return ("The given number is prime")

def sumOfDigits(x):
    x = list(str(x))
    return sum(list(map(int, x)))

def productOfDigits(x):
    x = list(str(x))
    x = (list(map(int, x)))
    return reduce(lambda a,b: a*b , x,1)


n = random.randrange(20,9999)

DivisibleBy = Divisibility(n)

hints = {1 : ("Sum of digits of the number is " + str(sumOfDigits(n))),
         2 : ("product of digits of number is " + str(productOfDigits(n))),
         3 : (DivisibleBy(2)),
         4 : DivisibleBy(3),
         5 : DivisibleBy(5),
         6 : DivisibleBy(7),
         7 : isPrime(n),
         8 : ("Count of Zeros in the number is " + str(str(n).count('0')))
        }

choices = 3

print("-"*99)
print("Guess The Number".center(99, "-"))
print("-"*99)

while choices:
    print("Guess the "+str(len(str(n)))+"-digited number", sep= "")
    m = int(input())
    if m == n:
        print("You have Got it")
    else:
        if choices != 1:
            print("Try Again")
            print("Here is a hint to cheerUp")
            x = random.randint(1,9)
            print(hints.get(x, "Sorry a problem to get the hint"))
        else:
            print("Sorry, you lost all the chances")
    choices -= 1

print("Bye-Bye, Waiting for your next visit!")