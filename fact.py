def abc():
    for i in range(1, 101):
        j = str(i)
        if(not(i % 5) and not(i % 3)):
            print(j + " - FizzBuzz")
        elif(not(i % 3)):
            print(j + " - Fizz")
        elif(not(i % 5)):
            print(j + " - Buzz")
        else:
            print(j + " - Null")


abc()
