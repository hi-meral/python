class PropertyDemo(object):

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    @property
    def username(self):
        return self.name
    
    @username.setter
    def username(self,value):
        if(len(value) > 5):
            raise ValueError("Should be 5 character long")
 
        self.name = value

    @username.deleter
    def username(self):
        del self.name


pd = PropertyDemo("Meral",30)


print(pd.username)

pd.username = "Vishwa"

print(pd.username)