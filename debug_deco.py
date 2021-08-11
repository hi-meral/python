def debug_deco(func):
    def nested1(*args):
        print(f'calling function - {func.__name__}')
        print(f'with parameters - {args}')
        return func(*args)
    return nested1


@debug_deco
def addme(x, y):
    print(x+y)


@debug_deco
def multime(x, y):
    print(x*y)


addme(1, 3)
multime(2, 5)
