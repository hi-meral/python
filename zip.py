l = ['a', 'b', 'c', 'f', 'r', 'u']
d = [5, 6, 7]
n = dict(zip(l, d))
print(n)
n = list(zip(l, d))
print(n)

n = tuple(zip(l, d))
print(n)

n = set(zip(l, d))
print(n)

n = frozenset(zip(l, d))
print(n)


# unzipping
y, k = zip(*n)
print("unzip y:", y)
print("unzip k:", k)
