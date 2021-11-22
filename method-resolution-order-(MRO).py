# depth-first, last to first

class Zero(object):
    def __init__(self):

        print("zero")
        super().__init__()


class Minus(object):
    def __init__(self):

        print("Minus")
        super().__init__()


class First(Zero):
    def __init__(self):

        print("first")
        super().__init__()


class Second(Minus):
    def __init__(self):

        print("Second")
        super().__init__()


class Third(First, Second):
    def __init__(self):

        print("Third")
        super().__init__()


th = Third()
