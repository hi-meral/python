from CreateTreefromDict import *
import math

import sys
sys.setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


sys.setrecursionlimit(10**6)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):

        return self.createNode(A, 0, len(A)-1)

    def createNode(self, A, S, E):

        if S > E:
            return None

        X = (E+S)//2

        root = TreeNode(A[X])
        root.left = self.createNode(A, S, X-1)
        root.right = self.createNode(A, X+1, E)

        return root


Tr = CreateTree()
#Tx = Tr.getTree([12, 5, 15, 3, 6, 13, 16])
#Tx = Tr.getTree([10, 5, 15, 1, 8, 7])
Tx = Tr.getTree2([10, 5, 15, 1, 8, 7])
S = Solution()


A = [1, 6, 2, 3]
B = [6, 1, 3, 2]

R = S.sortedArrayToBST([1, 4, 8])
R1 = Tx.inorderTraversal(R)

print(R1)
