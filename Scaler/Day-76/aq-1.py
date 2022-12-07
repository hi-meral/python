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
    # @param A : string
    # @return a strings
    def solve(self, A):

        N = len(A)
        dq = Dequeue()
        B = ""
        HS = {}

        for i in range(N):

            HS[A[i]] = HS.get(A[i], 0) + 1

            dq.enqueue(A[i])

            while dq.size() and HS[dq.front()] > 1:
                dq.dequeue()

            B += dq.front() if dq.size() else "#"

        return B
