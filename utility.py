def find_max(list1):
    number = list1[0]

    for e in list1:
        if(e > number):
            number = e

    return number
