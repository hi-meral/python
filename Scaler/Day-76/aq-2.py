from collections import deque


class Dequeue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.append(val)

    def enqueueleft(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            return

        return self.buffer.popleft()

    def dequeueright(self):
        if len(self.buffer) == 0:
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def front(self):
        return self.buffer[0]

    def rear(self):
        return self.buffer[-1]

    def size(self):
        return len(self.buffer)


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):

        N = len(A)
        dq = Dequeue()
        C = []

        for i in range(B):

            while dq.size() and dq.rear() < A[i]:
                dq.dequeueright()

            dq.enqueue(A[i])

        C.append(dq.front())

        for i in range(B, N):

            if dq.front() == A[i-B]:
                dq.dequeue()

            while dq.size() and dq.rear() < A[i]:
                dq.dequeueright()

            dq.enqueue(A[i])

            C.append(dq.front())

        return C


X = Solution()

A = [1, 2, 3, 4, 2, 7, 1, 3, 6]
B = 6

R = X.slidingMaximum(A, B)

print(R)
