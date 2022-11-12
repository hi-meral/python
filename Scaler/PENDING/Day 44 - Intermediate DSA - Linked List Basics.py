# Definition for singly-linked list.
from socket import TCP_NODELAY


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getSize(self, Node):

        c = 0
        tNode = Node
        while tNode != None:
            tNode = tNode.next
            c += 1

        return c

    def printll(self, Node):

        tNode = Node
        while tNode != None:
            print(tNode.val, end="-")
            tNode = tNode.next

    # @param A : list of list of integers
    # @return the head node in the linked list

    def solve(self, A):

        N = ListNode(None)
        c = self.getSize(N)

        for a in A:

            self.printll(N)
            print()
            if a[0] == 0:

                if c == 1 and N.val == None:
                    N = ListNode(a[1])
                else:

                    nn = ListNode(a[1])
                    nn.next = N

                    N = nn

            elif a[0] == 1:

                if c == 1 and N.val == None:
                    N = ListNode(a[1])
                else:
                    tNode = N
                    for i in range(c):

                        if i == c-1:
                            nn = ListNode(a[1])
                            tNode.next = nn
                            break

                        tNode = tNode.next

            elif a[0] == 2:

                if c == 1 and N.val == None:
                    if a[2] > 0:
                        continue
                    else:
                        N = ListNode(a[1])
                elif a[2] == 0:
                    nn = ListNode(a[1])
                    nn.next = N

                    N = nn
                else:
                    tNode = N
                    for i in range(c):

                        if i == a[2]-1:
                            nn = ListNode(a[1])
                            nn.next = tNode.next

                            tNode.next = nn
                            break

                        tNode = tNode.next

            elif a[0] == 3:

                if c == 1 and N.val == None:
                    continue
                elif a[1] == 0:
                    N = N.next
                else:
                    tNode = N
                    for i in range(c):

                        if i == a[1]-1:

                            tNode.next = tNode.next.next
                            break

                        tNode = tNode.next

        return N


s = Solution()
#x = s.solve([[0, 1, -1], [1, 2, -1], [2, 3, 1]])
x = s.solve(
    [[0, 1, -1],
     [1, 2, -1],
     [2, 3, 1],
     [0, 4, -1],
     [3, 1, -1],
     [3, 2, -1]]
)

while x != None:
    print(x.val, end=" - ")
    x = x.next
