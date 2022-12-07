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
    def solve(self, A, B):

        N = len(A)
        dq = Dequeue()
        C = 0

        for i in range(B):

            while dq.size() and dq.rear() < A[i]:
                dq.dequeueright()

            dq.enqueue(A[i])

        C += dq.front()

        for i in range(B, N):

            if dq.front() == A[i-B]:
                dq.dequeue()

            while dq.size() and dq.rear() < A[i]:
                dq.dequeueright()

            dq.enqueue(A[i])

            C += dq.front()

        dq = Dequeue()

        for i in range(B):

            while dq.size() and dq.rear() > A[i]:
                dq.dequeueright()

            dq.enqueue(A[i])

        C += dq.front()

        for i in range(B, N):

            if dq.front() == A[i-B]:
                dq.dequeue()

            while dq.size() and dq.rear() > A[i]:
                dq.dequeueright()

            dq.enqueue(A[i])

            C += dq.front()

        return C % 1000000007


S = Solution()

A = [2, 5, -1, 7, -3, -1, -2]
B = 4

A = [2, -1, 3]
B = 2

R = S.solve(A, B)

print(R)
