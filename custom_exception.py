class InvalidLevelError(Exception):
    def __init__(self, message):
        self.message = message


level = -1


try:
    if(level < 0):
        raise InvalidLevelError("{} is an invalide level ".format(level))
except InvalidLevelError as e:
    print(e.message)



################################

print("\n\nExample 2 \n\n\n")
class CustomError(Exception):
    pass

try :
    global x
    raise CustomError("Not possible")
    x = 10
except Exception as err:
    print(err)
else:
    print(x)

####################

ImportError


# IndexError
# Raised when the index of a sequence is out of range.

# KeyError
# Raised when a key is not found in a dictionary.

# KeyboardInterrupt
# Raised when the user hits the interrupt key (Ctrl+c or delete).

# MemoryError
# Raised when an operation runs out of memory.

# NameError
# Raised when a variable is not found in local or global scope.

# SyntaxError
# Raised by parser when syntax error is encountered.

# IndentationError
# Raised when there is incorrect indentation.

# TabError
# Raised when indentation consists of inconsistent tabs and spaces.

# ValueError
# Raised when a function gets an argument of the correct type but improper value.

# ZeroDivisionError
# Raised when the second operand of division or modulo operation is zero.

