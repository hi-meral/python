from collections import deque


class Queue:

    def __init__(self) -> None:
        self.container = deque()

    def add(self, value):
        self.container.append(value)

    def popleft(self):
        if self.empty():
            return
        return self.container.popleft()

    def porright(self):
        if self.empty():
            return

        return self.container.pop()

    def top(self):

        if self.empty():
            return

        return self.container[0]

    def tail(self):

        if self.empty():
            return
        return self.container[-1]

    def size(self):
        return len(self.container)

    def empty(self):
        return self.size() == 0


class Solution:

    def solve(self, A, B):

        N = len(A)
        C = []
        q = Queue()

        for i in range(B):

            while not q.empty() and A[i] > q.top():
                q.porright()

            q.add(A[i])

        C.append(q.top())

        for i in range(B, N):

            ele = A[i-B]

            if q.top() == ele:
                q.popleft()

            while not q.empty() and A[i] > q.top():
                q.popleft()

            q.add(A[i])

            C.append(q.top())

        return C


A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3
X = [3, 3, 5, 5, 6, 7]

A = [1, 2, 3, 4, 2, 7, 1, 3, 6]
B = 6
X = [7, 7, 7, 7]

S = Solution()
X = S.solve(A, B)

print(X)
