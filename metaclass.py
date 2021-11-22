## Backgroud

## All class are made from type() metaclass - check this line o/p --> print(type(Hello))

integer1 = 10

class Hello:
    
    x = 5

    def enjoy(self):
        print (Hello.__name__)

print(type(integer1))
print(type(Hello))

h = Hello()
h.enjoy()

## So class can be created by type() as following

def enjoy1(self):
    print ('Here is the class - '+Hello1.__name__)

## The following will create the same class as above
Hello1 = type('Hello1', (), {'x':5, 'enjoy1':enjoy1})

print(type(Hello1))

h = Hello1()
h.enjoy1()

## Now we can create a custom MetaClass that can be a Creator of a normal class


class Meta(type):
    
    def __new__(self,classname, bases, attributes):

        ## WE CAN DO OTHER STUFF HERE WHATEVER WE WANT

        ## lest say I want to remove some attribute while creating a class from this meta class

        a = {}
        for name, val in attributes.items():
            
            # so if any attribute is color will be ignored
            if name != "color":
                a[name] = val

        return type(classname, bases, a)

# now creating a class from this metaclass by providing it as a metaclass parameter

class Dog(metaclass=Meta):

        color = 'brown'
        height = 2.4

        def bark():
            print("He will bark as Bhow Bhow")


d = Dog()

print(d.height)
#print(d.color)  ##error



