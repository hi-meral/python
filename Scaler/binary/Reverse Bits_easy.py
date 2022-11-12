class Solution:
    # @param A : list of integers
    # @return a list of integers
    def reverse(self, A):

        N = 32
        res = 0

        for i in range(N-1, -1, -1):

            y = A & 1

            mul = y * (1 << i)

            res += mul

            A = A >> 1

        return res


#A = [1, 0, 1, 0]
A = 3
s = Solution()
print(s.reverse(A))
