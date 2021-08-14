class AgeDescriptor:

    def __init__(self):
        self.age = {}

    def __get__(self, instance, owner):
        return self.age

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Name must be a string")
        elif(value < 0 or value > 120):
            raise TypeError("Name must be a genuin")
        else:
            self.age = value

    def __delele__(self, instance):
        del self.age


class Person:
    age = AgeDescriptor()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{0} is {1} years old".format(self.name, self.age)


p = Person("Meral", 10)

print(str(p))


p1 = Person("Ankit", 20)

print(str(p1))
