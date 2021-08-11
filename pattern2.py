num = 20;
a= int(ord("A"))

for i in range(1,num+1) :
    for j in range(i,num):
        print(end=" ")
    
    for j in range(a+(i-1),a-1,-1):
        print(chr(j),end="")
        
    for j in range(a+1,a+i):
        print(chr(j),end="")
    
    print()