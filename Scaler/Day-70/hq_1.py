from CreateLLfromL import *

NLL = ListNode([1, 2])


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):

        H = A
        C = 0

        if B == 0:
            return H

        while A is not None:
            C += 1
            A = A.next

        if C == 1:
            return None

        if B >= C:
            H = H.next
            return H

        C1 = 1
        A = H

        while C1 < (C-B):
            C1 += 1
            A = A.next

        if A.next.next is not None:
            A.next = A.next.next
        else:
            A.next = None

        return H


X = Solution()

R = X.removeNthFromEnd(NLL, 2)

showLL(R)
