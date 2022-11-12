class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):

        summ = 0

        for i in range(len(A)):

            summ = summ ^ A[i]

        return summ


s = Solution()
print(3 ^ 5)
print(s.singleNumber([1, 2, 2, 3, 1, 5]))
