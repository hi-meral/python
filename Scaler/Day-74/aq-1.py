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

    def get_length(self):
        return len(self.container)

    def printstack(self):
        print(self.container)

    def is_empty(self):
        return 1 if self.get_length() == 0 else 0


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):

        N = len(A)
        R = [-1] * N

        S = Stack()

        if A[0] is not None:
            S.insert(A[0])

        for i in range(1, N):

            while not S.is_empty() and S.top() >= A[i]:
                S.pop()

            if not S.is_empty():
                R[i] = S.top()

            S.insert(A[i])

        return R


A = [4, 5, 2, 10, 8]
A = [0, 4, 3, 2, 1]
A = [34, 35, 27, 42, 5, 28, 39, 20, 28]
X = Solution()


R = X.prevSmaller(A)

print(R)
