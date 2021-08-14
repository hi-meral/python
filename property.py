class Person():

    def __init__(self, age):
        self.setAge(age)

    def getAge(self):
        print("age is returned")
        return self.age

    def setAge(self, value):
        if value < 0:
            raise ValueError("Age can not be less that zero")
        self.age = value
        print("Age is defined ")

    def setAge(self, value):
        if value < 0:
            raise ValueError("not posiible")
        print("Age is defined:", value)
        self.age = value

    def delAge(self):
        print("object deleted")
        del self.age

    age1 = property(getAge, setAge, delAge)


p = Person(-30)

print(p.age1)
