class A:
    def __init__(self) -> None:
        pass

    def _parentmethod(self):
        print("parent method called")


class B(A):

    def __init__(self) -> None:
        super().__init__()

    def parentmethod(self):
        print("child method called")


a = A()
a._parentmethod()

b = B()
b.parentmethod()
