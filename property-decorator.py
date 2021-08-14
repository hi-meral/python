class cel():
    def __init__(self, temp=0):
        self._temp = temp

    @property
    def temprature(self):
        print("get the tempratrure:")
        return self._temp

    @temprature.setter
    def temprature(self, value):
        if (value < -273):
            raise ValueError("Temperature below -273 is not possible")
        print("setting new value", value)
        self._temp = value

    @temprature.deleter
    def temprature(self):
        print("del  temp value:", self._temp)
        del self._temp


c = cel(-275)
print(c.temprature)  # call get metho @property
c.temprature = -22  # call set method  @temprature.setter
print(c.temprature)  # call get method @property and john goets to value in def
del c.temprature  # call del method @temprature.deleter
