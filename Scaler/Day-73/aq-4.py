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
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        sl = Stack()
        sr = Stack()

        for i in range(len(A)):

            x = A[i]
            sl.insert(x)

        while not sl.is_empty():

            x = sl.pop()

            if not sr.is_empty():
                y = sr.pop()
                while y < x and not sr.is_empty():
                    sl.insert(y)
                    y = sr.pop()
                else:
                    if y > x:
                        sr.insert(y)
                        sr.insert(x)
                    else:
                        sr.insert(x)
                        sr.insert(y)
            else:
                sr.insert(x)

        ans = []

        while not sr.is_empty():
            z = sr.pop()
            ans.append(z)

        return ans


X = Solution()

A = [5, 17, 11]
R = X.solve(A)

print(R)
