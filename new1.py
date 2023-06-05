
def merge2List2(X, Y):

    if X.val < Y.val:
        H = X
        t = H
        X = X.down
    else:
        H = Y
        t = Y
        Y = Y.down

    while X != None and Y != None:

        if X.val < Y.val:
            t.down = X
            t = t.down
            X = X.down
        else:
            t.down = Y
            t = t.down
            Y = Y.down

    while X != None:
        t.down = X
        t = t.down
        X = X.down

    while Y != None:
        t.down = Y
        t = t.down
        Y = Y.down

    return H


def preMerge(A):

    if A.down == None:
        return A

    M = getDownMid(A)
    B = M.down
    M.down = None

    U1 = preMerge(A)
    U2 = preMerge(B)

    return merge2List2(U1, U2)


def getDownMid(A):

    S = A
    F = A

    while F.down != None and F.down.down != None:
        S = S.down
        F = F.down.down

    return S


def delinkDown(A):

    temp = A

    while temp != None:
        t_down = temp.down
        temp.down = None
        temp.right = t_down
        temp = temp.right


def flatten(A):

    toprow = A
    temp = toprow

    while toprow != None:

        right_hold = toprow.right

        while temp.down != None:
            temp = temp.down

        temp.down = right_hold
        temp = temp.down
        toprow.right = None
        toprow = right_hold

    H = preMerge(A)

    delinkDown(H)

    return H


def print_down(node):

    temp = node
    ans = []
    while temp != None:
        ans.append(str(temp.val))
        temp = temp.down

    print("-".join(ans))


def print_right(node):

    temp = node
    ans = []
    while temp != None:
        ans.append(str(temp.val))
        temp = temp.right

    print("-".join(ans))


class ListNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.down = None


# create the linked list
head = ListNode(12)
head.right = ListNode(5)
head.right.down = ListNode(4)
head.right.down.down = ListNode(2)
head.right.down.down.down = ListNode(5)

head.right.right = ListNode(3)
head.right.right.down = ListNode(4)
head.right.right.down.down = ListNode(20)

head.right.right.right = ListNode(7)
head.right.right.right.down = ListNode(11)
head.right.right.right.down.down = ListNode(22)
head.right.right.right.down.down.down = ListNode(30)
head.right.right.right.down.down.down.down = ListNode(31)

head.right.right.right.right = ListNode(7)
head.right.right.right.right.down = ListNode(20)
head.right.right.right.right.down.down = ListNode(20)
head.right.right.right.right.down.down.down = ListNode(28)
head.right.right.right.right.down.down.down.down = ListNode(39)

X = flatten(head)

print_right(X)
print_down(X)
