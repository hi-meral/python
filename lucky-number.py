lucky_number = 1103
counter = 0
while True:
    x = int(input("Try your luck : "))

    if (x == lucky_number):
        print("You won!!")
        break
    else:
        counter += 1

    if(counter == 3):
        print("you are done, Try again")
        break
