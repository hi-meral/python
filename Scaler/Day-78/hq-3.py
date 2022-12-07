class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        HM = {}

        for a in range(len(A)):
            HM[A[a]] = a

        S1 = 0
        E1 = len(A)-1

        S2 = 0
        E2 = len(B)-1

        return self.Tree(A, S1, E1, B, S2, E2, HM)

    def Tree(self, A, S1, E1, B, S2, E2, HM):

        if S1 > E1 and S2 > E2:
            return None

        root = TreeNode(B[E2])

        ind = HM[B[E2]]

        X = ind - S1

        root.left = self.Tree(A, S1, ind-1, B, S2, S2+X-1, HM)
        root.right = self.Tree(A, ind+1, E1, B, S2+X, E2-1, HM)

        return root