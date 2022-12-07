from collections import deque
from CreateTreefromDict import *

import sys
sys.setrecursionlimit(10**6)


def inOrder(A):

    if A == None:
        return

    inOrder(A.left)
    print(A.val, end="-")
    inOrder(A.right)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.append(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            return

        return self.buffer.popleft()

    def is_empty(self):
        return len(self.buffer) == 0

    def front(self):
        return self.buffer[0]

    def rear(self):
        return self.buffer[-1]

    def size(self):
        return len(self.buffer)

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None


class Solution:

    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        return self.getPath(A, B, C, 0)

    def getPath(self, A, B, C, ret):

        if A == None:
            return

        path = []

        if A.val == B:
            ret = 1
            self.checkNodeForPath(A, C, path)

        if A.val == C:
            ret = 1
            self.checkNodeForPath(A, B, path)

        if ret == 1:
            return path
        else:
            self.getPath(A.left, B, C, ret)
            self.getPath(A.right, B, C, ret)

    def checkNodeForPath(self, A, d, path):

        if A == None:
            return False

        if A.val == d:
            path.append(A)
            return True

        if self.checkNodeForPath(A.left, d, path) or self.checkNodeForPath(A.right, d, path):
            path.append(A)
            return True

        return False

    def below(self, A, K):

        if A == None:
            return 0

        if K == 0:
            return 1

        return self.below(A.left, K-1) + self.below(A.right, K-1)


Tr = CreateTree()
Tx = Tr.getTree()

S = Solution()

R = S.solve(Tx, 3)


print(R)
