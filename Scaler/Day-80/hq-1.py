class Solution:

    def solve(self, A, B):

        iolist = self.inOrder(A, set())
        C = self.inOrderCommon(B, iolist, 0)

        return C % (10**9 + 7)

    def inOrder(self, A, iolist):

        if A == None:
            return iolist

        iolist = self.inOrder(A.left, iolist)

        iolist.add(A.val)

        iolist = self.inOrder(A.right, iolist)

        return iolist

    def inOrderCommon(self, A, iolist, C):

        if A == None:
            return 0

        if A.val in iolist:
            C = A.val
        else:
            C = 0

        return C + self.inOrderCommon(A.left, iolist, C) + self.inOrderCommon(A.right, iolist, C)
