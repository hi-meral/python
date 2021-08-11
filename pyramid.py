
num = int(input("Number : "))

#num = 4

for i in range(1,num+1):
    for j in range(0, num-i):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()
