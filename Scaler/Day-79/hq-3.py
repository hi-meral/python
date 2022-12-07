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


sys.setrecursionlimit(10**6)


class Solution:

    ans = 0
    # @param A : root node of tree
    # @return an integer

    def t2Sum(self, A, B):

        S = set()
        self.inOrder(A, B, S)
        return self.ans

    def inOrder(self, A, B, S):

        if A == None:
            return

        H = self.inOrder(A.left, B, S)
        X = B - A.val
        if X in S:
            self.ans = 1

        S.add(A.val)
        H = self.inOrder(A.right, B, S)


Tr = CreateTree()
#Tx = Tr.getTree([12, 5, 15, 3, 6, 13, 16])
#Tx = Tr.getTree([10, 5, 15, 1, 8, 7])
Tx = Tr.getTree7([5, 3, 7, 1, 4, 6, 8])
S = Solution()


A = [1, 6, 2, 3]
B = [6, 1, 3, 2]

R = S.t2Sum(Tx, 16)
#R1 = Tx.inorderTraversal(R)

print(R)
