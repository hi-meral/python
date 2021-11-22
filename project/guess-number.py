import random

random_number = random.randint(1,10)

guess = 0

while guess!=random_number:
    guess = int(input("Insert number from 1 to 10 : "))
    if(guess<random_number):
        print("too less")
    elif(guess>random_number):
        print("too high")

print("Congrats, You won")

