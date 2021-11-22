class Foo:

    cur_object = 0

    def __new__(cls, *args, **kwargs):
        cls.cur_object += 1

        # can check number of objects
        if(cls.cur_object == 2):
            raise ValueError("Only one instance allowed")

        # it calles always before init
        print("__new__")
        instance = super(Foo, cls).__new__(cls)
        #instance = object.__new__(cls)
        
        # init is only called if it returns instance
        return instance

        # return None          # in this case __init__ won't be called

    def __init__(self, a, b):
        print("__init__")
        self.a = a
        self.b = b

    def bar(self):
        print("bar")
        print(self.a+self.b)


i = Foo(1, 2)
i.bar()

# second instance creation will throw an error
#q = Foo(3, 4)
