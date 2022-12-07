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
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

        S = float('-inf')
        E = float('inf')
        return self.checkPrev(A, S, E)

    def checkPrev(self, A, S, E):

        a = A.pop(0)
        if S <= a <= E:

            if not len(A):
                return "YES"

            t = A[0]

            if t > a:
                return self.checkPrev(A, a+1, E)
            elif t < a:
                return self.checkPrev(A, S, a-1)
            else:
                return "NO"
        else:
            return "NO"


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
