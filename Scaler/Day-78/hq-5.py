class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def isSymmetric(self, A):

        if A == None:
            return

        return self.isTwoSymmetric(A, A)

    def isTwoSymmetric(self, X, Y):

        if X is None or Y is None:
            return int(X == Y)

        if X.val != Y.val:
            return 0

        return self.isTwoSymmetric(X.right, Y.left) and self.isTwoSymmetric(X.left, Y.right)