class Solution:
    # @param A : root node of tree
    # @return an integer

    def maxDepth(self, A):

        return self.maxPath(A)

    def maxPath(self, A):

        if A == None:
            return 0

        L = self.maxPath(A.left)
        R = self.maxPath(A.right)

        return 1 + max(L, R, 0)