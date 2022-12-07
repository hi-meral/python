class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.hold = []
        self.HS = {}
        self.capacity = capacity

    # @return an integer

    def get(self, key):

        return self.HS.get(key, -1)

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):

        if len(self.hold) == self.capacity:
            x = self.hold.pop(0)
            del self.HS[x]
        elif self.HS.has_key(x):
            self.hold.remove(x)

        self.HS[key] = value
        self.hold.append(key)
