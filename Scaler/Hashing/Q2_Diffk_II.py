class Solution:

    def getFreq(self, A):

        freq = {}

        for i in range(len(A)):

            freq[A[i]] = freq.get(A[i], 0) + 1

        return freq

    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):

        N = len(A)

        freq = self.getFreq(A)

        for i in range(N):

            x = A[i]
            y = A[i] - B

            if x == y and freq[y] > 1:
                return 1
            elif x != y and y in freq:
                return 1

        return 0


A = [8, 9, 1, -2, 4, 5, 11, -6, 7, 5]
B = 11


# A = [4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1,
#    9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8]
#B = -3
s = Solution()
x = s.diffPossible(A, B)

print(x)
