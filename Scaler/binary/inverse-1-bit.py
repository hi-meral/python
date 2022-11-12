from tkinter.messagebox import RETRY


class Solution:
    def solve(self, x, i):
        return x ^ (1 << i-1)


x = 5
i = 1
s = Solution()
print(s.solve(x, i))
