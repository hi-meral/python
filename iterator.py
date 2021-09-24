class MyIterator:

    def __init__(self,value) -> None:
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        current = self.value
        self.value += 2
        return current

myiter = MyIterator(1)


##print(myiter)

##print(next(myiter))
##print(next(myiter))


def iterfunction(start,end):
    current = start
    while True:
        if current < end:
            yield current
            current += 1
        else:
            raise StopIteration

it = iterfunction(1,5)


print(next(it))
print(next(it))
print(next(it))
print(next(it))


