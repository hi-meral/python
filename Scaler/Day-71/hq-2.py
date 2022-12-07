from CreateLLfromL import *


NLL = ListNode([1, 2, 22, 56])

# Definition for singly-linked list.


class ListNode1:
    def __init__(self, x):
        self.val = x
        self.next = None


L1 = ListNode1(1)
L2 = ListNode1(2)
L3 = ListNode1(3)
L4 = ListNode1(4)
L5 = ListNode1(5)

L1.next = L2
L2.next = L3
L3.next = L4
L4.next = L5
L5.next = L3


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):

        if A.val < B.val:
            H = A
            t = A
            A = A.next
        else:
            H = B
            t = B
            B = B.next

        while A is not None and B is not None:

            if A.val < B.val:
                t.next = A
                t = A
                A = A.next
            else:
                t.next = B
                t = B
                B = B.next

        if A is not None:
            t.next = A
        if B is not None:
            t.next = B

        return H


X = Solution()

NLL2 = ListNode([9, 10, 11, 99])
ans = X.mergeTwoLists(NLL, NLL2)

showLL(ans)
