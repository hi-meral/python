# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):

        ans = -1
        ans = self.addingParentSum(A, B, 0, ans)
        return 1 if ans == B else 0

    def addingParentSum(self, A, B, X, ans):

        X = A.val + X

        if A.left == None and A.right == None and X == B:
            ans = X

        if A.left == None and A.right == None:
            X = A.val
            return ans

        if A.left != None:
            ans = self.addingParentSum(A.left, B, X, ans)

        if A.right != None:
            ans = self.addingParentSum(A.right, B, X, ans)

        return ans
