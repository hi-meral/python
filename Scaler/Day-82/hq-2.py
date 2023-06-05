# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):

        if A == None:
            return []

        Q = []
        ans = []

        Q.append(A)
        ans.append(A.val)

        while len(Q) > 0:

            t = Q.pop(0)

            if t.left != None:
                Q.append(t.left)
                ans.append(t.left.val)
            else:
                ans.append(-1)

            if t.right != None:
                Q.append(t.right)
                ans.append(t.right.val)
            else:
                ans.append(-1)

        return ans
