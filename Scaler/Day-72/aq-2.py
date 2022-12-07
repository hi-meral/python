from CreateLLfromL import *

NLL = ListNode([1])


# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:

    def middle(self, A):

        s = A
        f = A

        while f.next is not None and f.next.next is not None:

            s = s.next
            f = f.next.next

        return s

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

    def sortList(self, A):

        if A is None:
            return None

        if A.next is None:
            return A

        M = self.middle(A)

        B = M.next
        M.next = None

        t1 = self.sortList(A)
        t2 = self.sortList(B)

        t3 = self.mergeTwoLists(t1, t2)
        return t3


X = Solution()

R = X.sortList(NLL)

showLL(R)
