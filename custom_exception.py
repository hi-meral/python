class InvalidLevelError(Exception):
    def __init__(self, message):
        self.message = message


level = -1


try:
    if(level < 0):
        raise InvalidLevelError("{} is an invalide level ".format(level))
except InvalidLevelError as e:
    print(e.message)
