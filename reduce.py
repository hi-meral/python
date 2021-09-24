import functools




final = functools.reduce(lambda a,b : a if a>b else b, [2,6,1,3,8,4,0,2])

print(final)