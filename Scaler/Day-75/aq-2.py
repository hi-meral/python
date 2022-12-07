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
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A, B):

        q = Queue()
        C = 0
        N = len(A)

        for i in range(N):
            q.enqueue(A[i])

        while q.size() > 0:

            ele = q.dequeue()
            C += 1

            if ele == B[0]:
                B.pop(0)
            else:
                q.enqueue(ele)

        return C