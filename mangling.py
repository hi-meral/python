class Student:
    def __init__(self, name) -> None:
        self.__name = name
        pass

    def _protectedclass(self):
        print("protected")

    def __privateclass(self):
        print("private")

    def publicclass(self):
        self.__privateclass()


class Newboy(Student):

    def __init__(self, name) -> None:
        super().__init__(name)
        super()._protectedclass()
        # super().__privateclass()  ## error


s = Student("Meral")
n = Newboy("Tom")

print(s._Student__name)
print(n._Student__name)
