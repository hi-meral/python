def deco1(func) :
    def inner(*args) :
        #print('The positional arguments are', args)
        #print('The keyword arguments are', kwargs)
        list1 = args[:]
        print(list1[0]+1)
        #args[0] = 700
        return func(*args)

    return inner

@deco1
def hello1(x):
    return x;

x= 589;
print(hello1(x))