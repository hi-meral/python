class Solution:

    def getFreq(self, A, B):

        freq = {}

        for i in range(B):

            freq[A[i]] = freq.get(A[i], 0) + 1

        return freq

    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def dNums(self, A, B):

        ans = []
        freq = self.getFreq(A, B)
        ans.append(len(freq))

        N = len(A)
        i = 1
        j = B

        while j < N:

            freq[A[i-1]] -= 1

            if freq[A[i-1]] == 0:
                freq.pop(A[i-1])

            freq[A[j]] = freq.get(A[j], 0) + 1

            ans.append(len(freq))

            i += 1
            j += 1

        return ans


A = [1, 1, 2, 2]
B = 1

# A = [4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1,
#    9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8]
#B = -3
s = Solution()
x = s.dNums(A, B)

print(x)
