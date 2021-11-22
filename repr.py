x = 10

print(repr(x))


class Person:
    name = 'Adam'

    def __repr__(self):
        return repr(self.name)

    def __str__(self) -> str:
        return 'Hello'

print(repr(Person()))

p = Person()
print(repr(p))

print(p)        # call __str__



#######

import datetime 
today = datetime.datetime.now() 
  
# Prints readable format for date-time object 
print (str(today) )
  
# prints the official format of date-time object 
print (repr(today)      )


