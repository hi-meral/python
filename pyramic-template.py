
num = 10

for i in range(1,num+1) :
    for j in range(i,num):
        print(end=" ")

    for j in range(0,i):
        print("*",end="")

    for j in range(1,i):
        print("*",end="")

    print()

for ii in range(1,num+1) :

    for j in range(0,ii):
        print(end=" ")

    for j in range(num-ii,1,-1):
        print("*",end="")

    for j in range(num-(ii-1),1,-1):
        print("*",end="")

    print()