class Dunder(object):
    def __init__(self) -> None:
        super().__init__()
        self._bar = 10
        self.__baz = 20


du = Dunder()

print(du._bar)

#print(du.__baz)  # error
print(du._Dunder__baz)

print("for more check mangling.py file")
