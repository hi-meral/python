class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class Solution:

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

    def reverseList(self):

        prev = None
        node = self.head
        count = 0

        while node != None:

            next = node.next
            node.next = prev
            prev = node
            node = next

            count += 1

        return prev

    def print_ll(self):

        temp = self.head
        ans = []
        while temp != None:
            ans.append(str(temp.value))
            temp = temp.next

        print("-".join(ans))


S = Solution()
S.insert_node(1, 100)
S.insert_node(2, 200)
S.insert_node(3, 300)
S.insert_node(4, 300)
S.insert_node(5, 500)
S.insert_node(6, 600)
S.insert_node(7, 800)
S.insert_node(8, 800)


#S.head = S.reverseList()
S.deleteDuplicates(S.head)
S.print_ll()

#X = S.solve(S.head)
# print(X)
