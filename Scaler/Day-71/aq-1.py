from CreateLLfromL import *


NLL = ListNode([1, 2, 3, 4, 5, 6])

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
    # @return the head node in the linked list
    def detectCycle(self, A):

        S = A
        S1 = S
        F = A

        while S is not None and F is not None and F.next is not None:

            S = S.next
            F = F.next.next

            if S == F:
                break

        if F is None or F.next is None:
            return None

        S2 = S

        while S1 != S2:

            S1 = S1.next
            S2 = S2.next

        return S1


X = Solution()


ans = X.detectCycle(L1)

print(ans)
