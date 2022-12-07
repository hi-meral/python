from CreateLLfromL import *

NLL = ListNode([1, 2, 3, 4, 5, 6, 7, 8])


class Solution:

    def reorderList(self, A):

        M = self.middle(A)

        B = M.next
        M.next = None

        B1 = self.reverseList(B)

        return self.mergetwo(A, B1)

    def middle(self, A):

        S = A
        F = A

        while F.next is not None and F.next.next is not None:

            S = S.next
            F = F.next.next

        return S

    def mergetwo(self, Ax, Bx):

        H = Ax
        RH = None

        while Ax is not None and Bx is not None:

            if RH is None:
                RH = Ax
            else:
                RH.next = Ax
                RH = RH.next

            Ax = Ax.next

            RH.next = Bx

            RH = RH.next

            Bx = Bx.next

        if RH is None:
            RH = Ax
        else:
            RH.next = Ax

        return H

    def reverseList(self, M):

        # showLL(M)

        if M is None:
            return None

        RL = None

        while M is not None:
            t = M
            M = M.next
            t.next = None
            t.next = RL
            RL = t

        return RL


X = Solution()

R = X.reorderList(NLL)

showLL(R)
