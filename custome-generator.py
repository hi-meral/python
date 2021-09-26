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



