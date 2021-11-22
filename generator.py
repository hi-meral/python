gt2 = (x*x for x in range(1, 5))

print(next(gt2))
print(next(gt2))
print(next(gt2))
print(next(gt2))

# for g in gt2:
# print(g)


# FOLLOWING IS A CUSTOM GENERATOR

def custome_generator_fun(start, end):
    current = start
    while True:
        if current < end:
            yield current**2
            current += 1
        else:
            raise StopIteration


custome_generator = custome_generator_fun(1, 5)


print(next(custome_generator))
print(next(custome_generator))
print(next(custome_generator))
print(next(custome_generator))
