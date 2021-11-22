######### PASS BY VALUE ###########
# when any mutable object is passed in function it is called pass by value/assignment 

t1 = (1,2,3)


def passbyValue(t1):
    print(t1)

######### PASS BY REF ###########
#when any mutable object is passed in function it is called pass by ref 

list1 = [1,2,3]

def passByRef(l):
        print(l)
        l.extend([4,5])
        print(l)


passByRef(list1)    # mutable always pass by ref
print(list1)

##passByRef(list1[:])  # only in this case it will pass by value


## advance

list2 = list1

print(id(list1))
print(id(list2))

passByRef(list2)

print(list1)
print(list2)

print(id(list1))
print(id(list2))