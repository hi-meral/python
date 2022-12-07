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

    def precedence(self, x):

        if x == "(" or x == ")":
            return 0
        elif x == "^":
            return 1
        elif x == "*" or x == "/":
            return 2
        elif x == "+" or x == "-":
            return 3

    def is_operator(self, x):

        if x in ['^', '/', '*', '+', '-', '(', ')']:
            return True

    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A):

        postfix = ""
        s = Stack()

        for a in A:

            if self.is_operator(a):

                while not s.is_empty() and s.peek() != "(" and (a == ")" or self.precedence(s.peek()) <= self.precedence(a)):

                    p = s.pop()

                    if p == "(":
                        s.pop()
                        break

                    postfix += p
                else:
                    if a == ")":
                        s.pop()
                    else:
                        s.insert(a)

            else:
                postfix += a

        while not s.is_empty():
            postfix += s.pop()

        return postfix


X = Solution()

A = "x^y/(a*z)+b"
A = "a+b*(c^d-e)^(f+g*h)-i"
A = "l-(l*q/s)/q*(u-p)"

R = X.solve(A)

print(R)
