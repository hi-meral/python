import threading
import time

from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


food_order_queue = Queue()

total = 3


def place_orders(todayorder):
    order_placed = 0
    while order_placed < total:
        order = input("Receiving order ...  : ")
        print("Placing order for:", order)
        food_order_queue.enqueue(order)
        todayorder -= 1
        order_placed += 1
        time.sleep(2)
    print(f"Total order taken {order_placed}. Now order closed")


def serve_orders():
    time.sleep(10)
    order_serverd = 0
    while order_serverd < total:
        order = food_order_queue.dequeue()
        time.sleep(7)
        if(order != None):
            print("Now serving: ", order)
            order_serverd += 1

    print(f"Total order served {order_serverd}. Now restaurant closed")


if __name__ == '__main__':
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    t1 = threading.Thread(target=place_orders, args=(total,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
