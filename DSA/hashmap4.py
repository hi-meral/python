
from tkinter.tix import Tree


class HashMap():

    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        #print(h % self.MAX)
        return h % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        stored = False

        if not self.arr[h]:
            self.arr[h] = val

        else:

            for i in range(h+1, self.MAX):
                if not self.arr[i]:
                    self.arr[i] = val
                    stored = True
                    break
            if not stored:
                for i in range(h-1):
                    if not self.arr[i]:
                        self.arr[i] = val
                        stored = True
                        break

    def __delitem__(self, key):

        h = self.get_hash(key)
        del self.arr[h]


h = HashMap()

h["iarch 1"] = 200
h["march 6"] = 310
h["march 17"] = 360
# h["march 6"] = 299
# del h["march 17"]

print(h.arr)
