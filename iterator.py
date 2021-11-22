class MyIterator:

    def __init__(self, value) -> None:
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        current = self.value
        self.value += 2
        return current


myiter = MyIterator(1)


# print(myiter)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


print("_______")

# FOLLOWING IS A CUSTOM GENERATOR AND ALSO CAN BE CALLED USING NEXT()


def custome_generator_fun(start, end):
    current = start
    while True:
        if current < end:
            yield current
            current += 1
        else:
            raise StopIteration


custome_generator = custome_generator_fun(1, 5)
print(next(custome_generator))
print(next(custome_generator))
print(next(custome_generator))

print("_______")


# FOLLOWING IS JUST A REGULAR GENERATOR

gt2 = (x*x for x in range(1, 5))

print(next(gt2))
print(next(gt2))
print(next(gt2))
