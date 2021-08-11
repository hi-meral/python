num = 9

for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

print("########")

for i in range(1,num+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()