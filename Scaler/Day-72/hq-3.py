#from CreateLLfromL import *

#NLL = ListNode([1, 1])

class showLL:
    def __init__(self, LL):

        while LL is not None:
            print(LL.random.val)
            LL = LL.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None


L1 = ListNode(1)
L2 = ListNode(2)
L3 = ListNode(3)
L4 = ListNode(4)
L5 = ListNode(5)

L1.next = L2
L1.random = L5

L2.next = L3
L2.random = L2

L3.next = L4
L3.random = L1

L4.next = L5
L4.random = L3

L5.random = L3


def clonelist(A):

    if A is None:
        return None

    h1 = A
    t1 = A
    while t1 is not None:

        t2 = ListNode(t1.val)
        t2.next = t1.next
        t1.next = t2

        t1 = t2.next

    t1 = h1
    h2 = h1.next

    while t1 is not None:

        t1.next.random = t1.random.next

        t1 = t1.next.next

    t1 = h1
    t2 = h2

    while t2.next is not None:

        t1.next = t2.next

        if t1.next is not None:
            t1 = t1.next

        t2.next = t1.next

        if t2.next is not None:
            t2 = t2.next

    return h2

# X = Solution()

# R = X.lPalin(NLL)

# print(R)


ans = clonelist(L1)

showLL(ans)
