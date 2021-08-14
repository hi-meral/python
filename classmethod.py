from datetime import datetime as dt


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def by_birthdate(cls, name, birthdate):
        dt2 = dt.strptime(birthdate, "%Y/%m/%d")
        dt1 = dt.today() - dt2
        age1 = round(dt1.days/365)
        return cls(name, age1)


p = Person("Meral", 40)


a = p.by_birthdate("Ankit", "1986/11/16")

print(a.age)
