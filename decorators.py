

def my_deco1(fun):
    def new_fun(x, y):
        return (fun(x*2, y))
    return new_fun


@my_deco1
def fun1(x, y):
    return x


print(fun1(10, 10))
