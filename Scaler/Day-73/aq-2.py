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

    def is_empty(self):
        return 1 if self.get_length() == 0 else 0


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        pass

        s = Stack()

        for a in A:

            if not s.is_empty() and s.peek() == a:
                s.pop()
            else:
                s.insert(a)

        ans_str = ""

        while not s.is_empty():

            ans_str = s.pop() + ans_str

        return ans_str


X = Solution()

A = "tabccbta"
R = X.solve(A)

print(R)
