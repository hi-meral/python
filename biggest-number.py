max = 0
dict1 = {}
dict2 = {}


def get_key(val):
    dict2 = {}
    for value in dict1:
        if val == int(dict1[value]):
            dict2[value] = int(dict1[value])
            print(f"Biggest number is {val}")

    for win in dict2:
        print(f"{win} hit {dict2[win]} marks")


while True:

    s = (input("Student : "))

    if(s == "end"):
        get_key(max)
        break

    x = (input("Marks : "))

    dict1[s] = x

    if (s != "end" and x.isdigit()):
        x = int(x)
        if(x > max):
            max = x
    else:
        get_key(max)
        break
