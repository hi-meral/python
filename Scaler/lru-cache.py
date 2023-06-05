class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.hold = []
        self.HS = {}
        self.capacity = capacity

    # @return an integer

    def get(self, key):

        print(self.HS.get(key, -1))

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):

        if self.HS.get(key, -1) >= 0:
            self.hold.remove(key)

        elif len(self.hold) == self.capacity:
            x = self.hold.pop(0)
            del self.HS[x]

        self.HS[key] = value
        self.hold.append(key)


LRU = LRUCache(7)
LRU.set(2, 1)
LRU.set(1, 10)
LRU.set(8, 13)
LRU.get(12)
LRU.set(2, 8)
LRU.get(11)
LRU.get(7)
LRU.set(14, 7)
LRU.set(12, 9)
LRU.set(7, 10)
LRU.get(11)
LRU.set(9, 3)
LRU.set(14, 15)
LRU.get(15)
LRU.get(9)
LRU.set(4, 13)
LRU.get(3)
LRU.set(13, 7)
LRU.get(2)
LRU.set(5, 9)
LRU.get(6)
LRU.get(13)
LRU.set(4, 5)
LRU.set(3, 2)
LRU.set(4, 12)
LRU.get(13)
LRU.get(7)
LRU.set(9, 7)
LRU.get(3)
LRU.get(6)
LRU.get(2)
LRU.set(8, 4)
LRU.set(8, 9)
LRU.set(1, 4)
LRU.set(2, 9)
LRU.set(8, 8)
LRU.get(13)
LRU.get(3)
LRU.get(13)
LRU.get(6)
LRU.set(3, 8)
LRU.get(14)
LRU.get(4)
LRU.set(5, 6)
LRU.set(10, 15)
LRU.get(12)
LRU.set(13, 5)
LRU.set(10, 9)
LRU.set(3, 12)
LRU.set(14, 15)
LRU.get(4)
LRU.set(10, 5)
LRU.get(5)
LRU.get(15)
LRU.set(7, 6)
LRU.get(1)
LRU.set(5, 12)
LRU.set(1, 6)
LRU.set(11, 8)
