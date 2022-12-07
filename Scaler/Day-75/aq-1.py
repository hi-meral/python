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
    def solve(self, A):

        q = Queue()
        C = 1

        q.enqueue("11")
        q.enqueue("22")

        while C < A:

            ele = q.dequeue()
            C += 1

            first_half = ele[:len(ele)//2]
            second_half = ele[len(ele)//2:]

            newele = first_half + "11" + second_half
            q.enqueue(newele)

            newele = first_half + "22" + second_half
            q.enqueue(newele)

        return int(q.front())