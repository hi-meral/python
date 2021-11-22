class Pizza():

    def __init__(self, pizzaname) -> None:
        self.pizzaname = pizzaname

    @classmethod
    def fromIngredients(cls,ingredients=['cheese']):

        if(all( i in ingredients for i in ['cheese'] )):
            return cls('Margrita')
        elif (all (i in ingredients for i in ['paneer','capsicum'] )):
            return cls('Loaded')
        elif ( all (i in ingredients  for i in ['brocoly','olive'] )):
            return cls('Veggi')
        else:
            return cls('Mixed')

    def enjoy(self):
        print (f'Hello There, Enjoy the {self.pizzaname} Pizza ')


t = Pizza('Tufani')

t.enjoy()

m = Pizza.fromIngredients(['Cheese','Garlic'])

m.enjoy()

v = Pizza.fromIngredients(['brocoly','olive','Mashroom'])

v.enjoy()