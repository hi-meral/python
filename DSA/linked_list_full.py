class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.down = None


col00 = ListNode(3)
col01 = ListNode(7)
col02 = ListNode(7)
col03 = ListNode(8)

col00.down, col01.down, col02.down = col01, col02, col03

col10 = ListNode(4)
col11 = ListNode(11)

col10.down = col11

col20 = ListNode(20)
col21 = ListNode(22)

col20.down = col21

col30 = ListNode(20)
col31 = ListNode(20)
col32 = ListNode(28)
col33 = ListNode(39)

col30.down, col31.down, col32.down = col31, col32, col33

col40 = ListNode(30)
col41 = ListNode(31)
col42 = ListNode(39)

col40.down, col41.down = col41, col42

col00.right, col10.right, col20.right, col30.right = col10, col20, col30, col40


class Solution:

    def merge2List2(self, X, Y):

        if X.val < Y.val:
            H = X
            t = H
            X = X.right
        else:
            H = Y
            t = Y
            Y = Y.down

        while X != None and Y != None:

            if X.val < Y.val:
                t.right = X
                t = t.right
                X = X.right
            else:
                t.right = Y
                t = t.right
                Y = Y.down

        while X != None:
            t.right = X
            t = t.right
            X = X.right

        while Y != None:
            t.right = Y
            t = t.right
            Y = Y.down

        return H

    def flatter(self, A):

        flat = A
        col = A.right
        temp = A.down
        while temp != None:
            flat.right = temp
            flat = flat.right
            temp = temp.down

        flat = A

        while col != None:

            hold_right = col.right
            flat = self.merge2List2(flat, col)

            col = hold_right

        ret = flat

        while flat != None:
            flat.down = None
            flat = flat.right

        return ret

    def isPalindrom(self, A):

        if A == None:
            return 0

        temp = A
        length = 0

        while temp != None:
            length += 1
            temp = temp.next

        M = self.middleNode(A)

        X = A
        Y = M.next
        M.next = None

        X = self.reverseList(X)

        lp = self.checkPalindrom(X, Y, not (length & 1))

        return lp == length

    def longestPalindromList(self, A):

        if A is None:
            return 0

        if A.next is None:
            return 1

        left = A
        right = A.next

        temp_left = left
        temp_right = right

        ans = float('-inf')

        while temp_right.next != None:

            ans = max(ans, self.checkPalindrom(temp_left, temp_right))
            ans = max(ans, self.checkPalindrom(temp_left, temp_right, True))

            x = temp_right.next
            temp_right.next = temp_left
            temp_left = temp_right
            temp_right = x

        return ans

    def checkPalindrom(self, X, Y, even=False):

        t_ans = 1

        if not even:
            Y = Y.next
        else:
            t_ans = 0

        while X != None and Y != None and X.value == Y.value:
            t_ans += 2
            X = X.next
            Y = Y.next

        return t_ans

    def sortList(self, A):

        if A is None or A.next is None:
            return A

        M = self.middleNode(A)

        B = M.next
        M.next = None

        self.print_ll(A)
        self.print_ll(B)

        H1 = self.sortList(A)
        H2 = self.sortList(B)
        return self.merge2List(H1, H2)

    def merge2List(self, A, B):

        if A.value < B.value:
            H = A
            t = A
            A = A.next
        else:
            H = B
            t = B
            B = B.next

        while A != None and B != None:

            if A.value < B.value:
                t.next = A
                A = A.next
                t = t.next
            else:
                t.next = B
                B = B.next
                t = t.next

        if A != None:
            t.next = A

        if B != None:
            t.next = B

        return H

    def middleNode(self, A):

        S = A
        F = A

        while F != None and F.next != None and F.next.next != None:

            S = S.next
            F = F.next.next

        return S

    def getIntersectionNode(self, A, B):

        H = A

        while H.next != None:
            H = H.next

        H1 = H

        H.next = B

        slow = A
        fast = A
        a_pointer = A

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                another_pointer = slow
                break

        if fast.next == None or fast.next.next == None:
            return None

        while a_pointer != another_pointer:
            a_pointer = a_pointer.next
            another_pointer = another_pointer.next

        # return a_pointer

        H1.next = None

        return a_pointer

    def deleteDuplicates(self, A):

        temp = A

        while temp is not None:

            if temp.next and temp.value == temp.next.value:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return A

    def solve(self, A, B, C):

        if A == None:
            return None

        count = 1
        temp = A
        while count < B-1:

            temp = temp.next
            count += 1

        prev = None

        hold = A if B == 1 else temp.next
        node = A if B == 1 else temp.next
        count = 0 if B == 1 else count

        while count < C:

            next = node.next
            node.next = prev
            prev = node
            node = next

            count += 1

        hold.next = node

        if B == 1:
            A = prev
        else:
            temp.next = prev

        return A

    def __init__(self) -> None:

        self.head = None
        self.size = 0

    def insert_node(self, position, value):

        if position >= 1 and position <= self.size+1:

            temp = Node(value)

            if position == 1:

                temp.next = self.head
                self.head = temp
                self.size += 1
            else:

                c = 1
                previous = self.head

                while c < position - 1:

                    previous = previous.next

                    c += 1

                temp.next = previous.next
                previous.next = temp
                self.size += 1

    def delete_node(self, position):

        if position == 1:
            self.head = self.head.next
            self.size -= 1
        elif position <= self.size:

            c = 1
            previous = self.head

            while c < position-1:

                previous = previous.next
                c += 1

            previous.next = previous.next.next
            self.size -= 1

    def reversePart(self, A, B):

        prev = None
        node = A
        count = 0
        while node != None and count < B:

            next = node.next
            node.next = prev
            prev = node
            node = next

            count += 1

        A.next = node
        return prev

    def reverseList(self, E):

        prev = None
        node = E
        count = 0

        while node != None:

            next = node.next
            node.next = prev
            prev = node
            node = next

            count += 1

        return prev

    def print_ll(self, node):

        temp = node
        ans = []
        while temp != None:
            ans.append(str(temp.val))
            temp = temp.next

        print("-".join(ans))

    def print_down(self, node):

        temp = node
        ans = []
        while temp != None:
            ans.append(str(temp.val))
            temp = temp.down

        print("-".join(ans))

    def print_right(self, node):

        temp = node
        ans = []
        while temp != None:
            ans.append(str(temp.val))
            temp = temp.right

        print("-".join(ans))


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(4)
node6 = Node(3)
node7 = Node(2)
node8 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
#node7.next = node8

node11 = Node(111)
node22 = Node(222)
node33 = Node(333)

node11.next = node22
node22.next = node33
node33.next = node5


S = Solution()
X = S.flatter(col00)

# print(X)
S.print_right(X)
S.print_down(X)
