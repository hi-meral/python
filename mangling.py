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

    def callName(self):
        print(self.__name)

class Newboy(Student):

    def __init__(self, name) -> None:
        super().__init__(name)
        super()._protectedclass()
        # super().__privateclass()  ## error


s = Student("Meral")
n = Newboy("Tom")

#print(s.__name) # error
s.callName()  # works

s.__name = "Hero"  # no error and no change as well

s.callName()  # works

print(s._Student__name) # bad practice
print(n._Student__name) # very bad practice

##print(n._Newboy__name)  # error