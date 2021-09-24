

class CustomError(Exception):
    pass


try :
    global x
    #raise CustomError("Not possible")
    x = 10
except Exception as err:
    print(err)
else:
    print(x)

    