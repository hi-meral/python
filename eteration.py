
#x = int(input("Num of rows"))

x = 3
for i in range(1,x):
    m = i+1
    for ii in range(1,m):
        print("*", end = " ")

print()
print('##############')


for row in range(6):
    for col in range(7):
        if(row == 0 and col%3!=0):
            print('*', end="")
        elif(row==1 and col%3==0):
            print("*",end="")
        elif(row>1 and (row - col) == 2):
            print("*",end="")
        elif(row>1 and (row + col) == 8):
                print("*",end="")
        else:
            print(end=" ")
    print()