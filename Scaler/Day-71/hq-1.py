from CreateLLfromL import *
import sys
sys.setrecursionlimit(10**6)


class Solution:

    def middle(self, A):

        S = A
        F = A

        while F.next is not None and F.next.next is not None:

            S = S.next
            F = F.next.next

        return S

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

    def sortList(self, A):

        if A is None or A.next is None:
            return A

        M = self.middle(A)

        A1 = M.next
        M.next = None

        t1 = self.sortList(A)
        t2 = self.sortList(A1)

        return self.mergeTwoLists(t1, t2)


X = Solution()

NLL = ListNode([13, 5, 10, 78, 99, 1])
R = X.sortList(NLL)

showLL(R)
