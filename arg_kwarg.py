
def callme(*a, **b):

    for x in a:
        print(x, end="\n")

    print(end="\n\n")

    for k, v in b.items():
        print(k, v, end="\n")


callme(9, 77, 40, firstname="meral", lastname="maradia")


# OR YOU CAN DO REVERSE


def revarg(x, y, z):
    print(x+y+z)


m = 5
n = 7


combo = [m, n, 9]

revarg(*combo)
