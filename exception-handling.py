import sys

try:

    with open("operateme.log") as f:
        pass

    x = 1/1

    # generate the error implicitally
    #raise NameError("Hello")
except FileNotFoundError as err:
    print("FileNotFoundError : " + err)
except NameError as err:
    print("NameError" + err)
except Exception as err:
    print("Oops! ", sys.exc_info()[0], "occured.")

else:
    print("congrats no error")
finally:
    print("ho liya, nikal lo")
