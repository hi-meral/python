# Python program to execute
# main directly
print("Always executed this {}".format(__name__))

if __name__ == "__main__":
    print("Executed when invoked directly")
else:
    print("Executed when imported")
