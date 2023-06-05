# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
class Solution:
    # @param A : root node of tree
    # @return an integer

    ans = float('-inf')

    def solve(self, A):

        self.maxPath(A)

        return self.ans-1

    def maxPath(self, A):

        if A == None:
            return 0

        L = self.maxPath(A.left)
        R = self.maxPath(A.right)

        P = 1 + max(L, 0) + max(R, 0)
        self.ans = max(self.ans, P)

        return 1 + max(L, R, 0)
