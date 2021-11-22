class Point:
    def __init__(self, x=0, y=0):

        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x},{self.y}"

    def __add__(self, other):

        a = self.x + other.x
        b = self.y + other.y

        return Point(a, b)

    # same way we can override

    # p1.__lt__(p2)
    # p1.__le__(p2)
    # p1.__eq__(p2)
    # p1.__ne__(p2)
    # p1.__gt__(p2)
    # p1.__ge__(p2)


p1 = Point(2, 4)
p2 = Point(1, 2)

p3 = p1+p2

print(p3)
