from CreateLLfromL import *

NLL = ListNode([1, 1])


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

    def reverseList(self, X):

        rh = None

        if X is None:

            return None

        while X is not None:

            t = X
            X = X.next
            t.next = None
            t.next = rh
            rh = t

        return rh

        # @param A : head node of linked list
        # @return an integer
    def lPalin(self, A):

        M = self.middle(A)

        B = M.next
        M.next = None

        C = self.reverseList(B)

        while C is not None:

            if A.val != C.val:
                return 0

            A = A.next
            C = C.next

        return 1


X = Solution()

R = X.lPalin(NLL)

print(R)
