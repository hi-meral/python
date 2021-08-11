class Pizza():

    you = 40

    def __init__(self, ingredients) -> None:
        self.ingredients = ingredients

    @classmethod
    def margrita(cls):
        self.you = 42 # error
        return cls(['cheese'])

    @staticmethod
    def welcome(name):
        return f'Hello, {name} welcome to pizza zone'


p = Pizza(['bit'])

Q = p.margrita()  # new object
