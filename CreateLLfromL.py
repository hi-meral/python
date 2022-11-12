class ListNode:
    def __init__(self, A):

        self.val = A.pop(0)
        self.next = None

        if len(A) == 0:
            return

        self.next = ListNode(A)


class showLL:
    def __init__(self, LL):

        while LL is not None:
            print(LL.val)
            LL = LL.next
