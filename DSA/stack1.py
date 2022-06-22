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
        return True if self.get_length() == 0 else False


def reverse_string(str):
    s = Stack()
    for i in str:
        s.insert(i)

    while not s.is_empty():
        print(s.pop(), end="")
