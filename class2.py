class Mamman():
    def walk(self):
        print("it can walk")


class Cat(Mamman):
    def mewing(self):
        print("it can mew")


class Dog(Mamman):
    def bark(self):
        print("it can bark well")


cat1 = Cat()
cat1.walk()
cat1.mewing()
