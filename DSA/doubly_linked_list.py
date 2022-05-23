class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList():

    def __init__(self):
        self.head = None

    def printme(self):
        if self.head == None:
            print("Linked List is empty")

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + ' - '
            itr = itr.next

        print(llstr)

    def insert_at_begining(self, data):
        self.head = Node(data, self.head, None)

    def insert_at_end(self, data):

        itr = self.head

        if(itr == None):
            self.head = Node(data, None, self.head)
        else:
            while itr.next:
                itr = itr.next

            itr.next = Node(data, None, itr)

    def insert_in_between(self, index, data):

        if index < 0 or index > self.get_count():
            raise Exception('Invaid Index')

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head

        while itr:

            if count == index - 1:

                node = Node(data, itr.next, itr)
                itr.next = node

            itr = itr.next
            count += 1

    def create_from_list(self, data_list):

        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def get_count(self):
        counter = 0

        itr = self.head

        while itr:
            itr = itr.next
            counter += 1

        return counter

    def remove_element(self, index):

        if index < 0 or index >= self.get_count():
            raise Exception('Invaid Index')

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0

        while itr:

            if (count == index - 1):
                itr.next = itr.next.next
                itr.next.prev = itr
                break

            itr = itr.next

            count += 1

    def insert_after_value(self, data_after, data_to_insert):

        itr = self.head

        while itr:

            if (itr.data == data_after):
                node = Node(data_to_insert, itr.next, itr)
                itr.next = node
                break

            itr = itr.next

    def remove_by_value(self, data):

        if self.head == None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head

        while itr.next:

            if (itr.next.data == data):
                itr.next = itr.next.next
                itr.next.prev = itr
                break

            itr = itr.next

    def print_forward(self):
        itr = self.head
        llstr = ""

        if(self.head == None):
            print("Linked list is empty")
        else:
            while itr:
                llstr = llstr + itr.data + ' -> '
                itr = itr.next

        print(llstr)

    def print_backward(self):
        itr = self.head
        llstr = ""

        if(self.head == None):
            print("Linked list is empty")
            return
        else:
            while itr.next:
                #llstr = llstr + itr.data + ' - '
                itr = itr.next

        while itr:
            llstr = llstr + itr.data + ' <- '
            itr = itr.prev

        print(llstr)


if __name__ == '__main__':

    ll = LinkedList()
    ll.create_from_list(["banana", "mango", "grapes", "orange"])

    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.printme()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.printme()
    # ll.remove_by_value("figs")
    # ll.printme()
    # ll.remove_by_value("banana")
    # ll.remove_by_value("mango")
    # ll.remove_by_value("apple")
    # ll.remove_by_value("grapes")
    # ll.printme()

    ll.print_forward()
    ll.print_backward()
