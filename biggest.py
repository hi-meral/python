max = 0
while True:

    x = (input("Insert : "))

    if (x.isdigit()):

        x = int(x)
        if(x > max):
            max = x
    else:

        print(f"Biggest number is {max}")
        break
