# NORMAL GENERATORS ARE LIKE

g = (x*2/3 for x in range(10))

print(g)

print(next(g))
print(next(g))
print(next(g))


print('\n\n\n\n')


## CUSTOM GENERATORS ARE LIKE, USING YIELD ###

def revString(str):

    l = len(str)
    for i in range(l-1,-1,-1):
        yield str[i]

x = revString("Maradia")

print(x)

print(next(x))
print(next(x))
print(next(x))
print(next(x))



