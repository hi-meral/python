import functools

def square(x):
    return x*x


hello = map(square,[1,2,3])


print(list(hello))

