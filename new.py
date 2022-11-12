from CreateLLfromL import *


NLL = ListNode([1, 2, 3, 4, 5, 6])


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):

        if A.next is None:
            return None

        if A.next.next is None:
            A = A.next
            return A

        S = A
        F = A

        while F.next.next is not None and F.next.next.next is not None:
            S = S.next
            F = F.next.next

        S.next = S.next.next

        return A


X = Solution()


ans = X.solve(NLL)

showLL(ans)
