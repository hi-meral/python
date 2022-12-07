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

    def is_match(self, ch1, ch2):

        match_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        return match_dict[ch1] == ch2

        # @param A : string
        # @return an integer
    def solve(self, A):

        s = Stack()

        starting_braces = ['(', '{', '[']
        ending_braces = [')', '}', ']']

        for i in A:
            if i in starting_braces:
                s.insert(i)

            if i in ending_braces:
                if s.is_empty():
                    return 0
                if not self.is_match(i, s.pop()):
                    return 0

        return s.is_empty()


X = Solution()

A = ["4", "13", "5", "/", "+"]
R = X.evalRPN(A)

print(R)
