from CreateTreefromDict import *

from collections import deque


class Stack(object):

    def __init__(self) -> None:
        self.container = deque()

    def insert(self, value):
        self.container.append(value)

    def top(self):
        return self.container[-1]

    def pop(self):
        return self.container.pop()

    def size(self):
        return len(self.container)

    def is_empty(self):
        return True if self.size() == 0 else False

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):

        if A == None:
            return

        ans = []
        curr = A
        S = Stack()

        while S.size() or curr is not None:

            while curr is not None:
                S.insert(curr)
                curr = curr.left

            curr = S.pop()
            ans.append(curr.val)

            curr = curr.right

        return ans


Tr = CreateTree()
T = Tr.getTree([1, 2, 3, 4, 5, 6, 7, 8, 9])
S = Solution()

R = S.levelOrder(T)
# R = T.inorderTraversal(T)

print(R)
