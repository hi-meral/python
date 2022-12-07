class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        HM = {}

        for b in range(len(B)):
            HM[B[b]] = b

        S1 = 0
        E1 = len(A)-1

        S2 = 0
        E2 = len(B)-1

        return self.Tree(A, S1, E1, B, S2, E2, HM)

    def Tree(self, A, S1, E1, B, S2, E2, HM):

        if S1 > E1 and S2 > E2:
            return None

        root = TreeNode(A[S1])

        ind = HM[A[S1]]

        X = ind - S2

        root.left = self.Tree(A, S1+1, S1+X, B, S2, ind-1, HM)
        root.right = self.Tree(A, S1+X+1, E1, B, ind+1, E2, HM)

        return root