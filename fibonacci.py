

def fabboci_number():
    nth = int(input("Print up to : "))
    a, b , cc = 0,1,0
    while cc < nth:
        print(a)
        a,b = b , a + b
        cc += 1
    

fabboci_number()