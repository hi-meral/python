x = 5

# simple variable


def pass_by_value(x):
    print("x={x} ,  id= {y}".format(x=x, y=id(x)))
    x = 100
    print("x={x} ,  id= {y}".format(x=x, y=id(x)))


pass_by_value(x)
print(x)

###############################


x = [5]

#  list or tuple


def pass_by_ref(x):
    print("x={x} ,  id= {y}".format(x=x, y=id(x)))
    x[0] = 100
    print("x={x} ,  id= {y}".format(x=x, y=id(x)))


pass_by_ref(x)
print(x[0])
