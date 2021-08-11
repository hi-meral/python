__all__ = ['lifestyle', 'men']

men = 28
woman = 23


def lifestyle():
    return 'lifestyle'


print("Always executed this {}".format(__name__))
if __name__ == "__main__":
    print("Executed when invoked directly")
else:
    print("Executed when imported")
