# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):

        Q = []

        root = TreeNode(A[0])
        Q.append(root)
        i = 1

        while len(Q) > 0:

            temp = Q.pop(0)

            if A[i] != -1:
                temp.left = TreeNode(A[i])
                Q.append(temp.left)

            if A[i+1] != -1:
                temp.right = TreeNode(A[i+1])
                Q.append(temp.right)

            i += 2

        return root
