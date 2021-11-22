def hello(a, b, c):
    print(a)
    print(b)
    print(c)

hello(10,20,30)
hello(10,b=20,c=30)
hello(10,c=20,b=30)
#hello(10,a=20,c=30) # error, coz a mutiple time
#hello(a=10,20,30) #error, keyword arg must be at last