class Person:

    def __init__(self, height, color, talk):
        self.height = height
        self.color = color
        self.talk = talk

    def talk1(self):
        print(f"He speaks {self.talk}")


p1 = Person(5.11, "brown", "sweet")

p1.talk1()
