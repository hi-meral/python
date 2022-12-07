from collections import deque


class Stack(object):

    def __init__(self) -> None:
        self.container = deque()

    def insert(self, value):
        self.container.append(value)

    def peek(self):
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
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):

        ans = B
        s = Stack()

        for i in range(A):
            z = C[i]

            if z > 0:
                s.insert(C[i])
            else:
                s.pop()

        if not s.is_empty():
            ans = s.peek()

        return ans


X = Solution()

A = 10
B = 23
C = [86, 63, 60, 0, 47, 0, 99, 9, 0, 0]

R = X.solve(A, B, C)

print(R)
