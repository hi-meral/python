class Deco1:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args):
        list1 = []
        list1 = args[1:]

        for i in list1:
            if(i == 0):
                return "Can't device by zero"
        
        else:
            return self.func(*args)

@Deco1
def div1(a,b,c):
    return a/b/c

print(div1(4,2,0))