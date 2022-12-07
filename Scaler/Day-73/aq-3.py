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

    def evalRPN(self, A):

        s = Stack()

        sign_ = ['+', '-', '*', '/']

        for a in A:

            if a in sign_:

                B = s.pop()
                A = s.pop()

                if a in "+":
                    s.insert(A+B)
                if a in "-":
                    s.insert(A-B)
                if a in "*":
                    s.insert(A*B)
                if a in "/":
                    s.insert(A//B)
            else:
                a = int(a)

                s.insert(a)

        return s.pop()


X = Solution()

A = ["4", "13", "5", "/", "+"]
R = X.evalRPN(A)

print(R)
