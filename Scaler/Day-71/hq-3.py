from CreateLLfromL import *
import sys
sys.setrecursionlimit(10**6)


class ListNode1:
    def __init__(self, x):
        self.val = x
        self.next = None


L1 = ListNode1(1)
L2 = ListNode1(2)
L3 = ListNode1(3)
L4 = ListNode1(4)
L5 = ListNode1(5)

L8 = ListNode1(8)
L9 = ListNode1(9)


L1.next = L2
L2.next = L3
L3.next = L4
L4.next = L5

L8.next = L9
L9.next = L3

'''
Definition for singly-linked list
class ListNode:
   def __init__(self, val):
      self.val = val
      self.next = None
'''


class Solution:
    def getIntersectionNode(self, A, B):

        if A is None:
            return None

        if B is None:
            return None

        h1 = A
        h2 = B

        while A.next is not None:

            A = A.next

        M = A
        A.next = B

        s = h1
        s1 = h1
        f = h1

        while s is not None and f is not None and f.next is not None:

            s = s.next
            f = f.next.next

            if s == f:
                break

        if f is None or f.next is None:
            return None

        s2 = s

        while s1 != s2:

            s1 = s1.next
            s2 = s2.next

        M.next = None
        return s1


X = Solution()

R = X.getIntersectionNode(L1, L8)

showLL(R)
