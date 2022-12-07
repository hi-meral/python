from CreateTreefromDict import *

from collections import deque


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
    # @return a list of integers
    def levelOrder(self, A):

        if A == None:
            return

        ans = []

        Q = Queue()
        Q.enqueue(A)

        while Q.size():

            x = Q.size()
            ta = []

            for i in range(x):
                curr = Q.dequeue()
                ta.append(curr.val)

                if curr.left is not None:
                    Q.enqueue(curr.left)

                if curr.right is not None:
                    Q.enqueue(curr.right)

            ans.append(ta)

        return ans


Tr = CreateTree()
T = Tr.getTree([1, 2, 3, 4, 5, 6, 7, 8, 9])
S = Solution()

R = S.levelOrder(T)
# R = T.inorderTraversal(T)

print(R)
