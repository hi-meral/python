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


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, A):
        MinL = 0
        MaxL = 0
        HM = {}
        Q = Queue()

        Q.enqueue((A, 0))

        while Q.size():

            CR = Q.dequeue()

            T = CR[0]
            L = CR[1]

            MinL = min(MinL, L)
            MaxL = max(MaxL, L)

            if L not in HM:
                HM[L] = []

            HM[L].append(T.val)

            if T.left is not None:
                Q.enqueue((T.left, L-1))
            if T.right is not None:
                Q.enqueue((T.right, L+1))

        ans = []

        for i in range(MinL, MaxL+1):
            ans.append(HM[i][-1])

        return ans


Tr = CreateTree()
#Tx = Tr.getTree([1, 2, 3, 4, 5, 6, 7, 8, 9])
Tx = Tr.getTree([6, 3, 7, 2, 5, 8, 9])
S = Solution()

R = S.solve(Tx)
# R = T.inorderTraversal(T)

print(R)
