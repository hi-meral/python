from abc import ABC, abstractmethod

class AbstractClass(ABC):
    
    @abstractmethod
    def do_something(self):
        print("From Main class")        # doesn't call automatically
    
    
class B(AbstractClass):
    def do_something(self):             # without declaring it throws error
        super().do_something()         # have to call implicitelly 
        print("From sub class")


b = B()
b.do_something()
