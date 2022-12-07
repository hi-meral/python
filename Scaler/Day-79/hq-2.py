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
    def solve(self, A, B, C):

        arr = self.inOrder(A, [])
        cnt = 0

        for a in arr:
            if B <= a <= C:
                cnt += 1
        return cnt

    def inOrder(self, A, ans):

        if A == None:
            return

        self.inOrder(A.left, ans)
        ans.append(A.val)
        self.inOrder(A.right, ans)

        return ans


Tr = CreateTree()
#Tx = Tr.getTree([12, 5, 15, 3, 6, 13, 16])
#Tx = Tr.getTree([10, 5, 15, 1, 8, 7])
Tx = Tr.getTree7([5, 3, 7, 1, 4, 6, 8])
S = Solution()


A = [1, 6, 2, 3]
B = [6, 1, 3, 2]

R = S.solve(Tx, 3, 7)
#R1 = Tx.inorderTraversal(R)

print(R)
