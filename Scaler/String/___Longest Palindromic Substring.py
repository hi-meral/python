class Solution:

    long_palindrom = ""
    long_palindrom_length = 0

    def isPalindrome(self, A, N, p1, p2):

        while (p1 >= 0 and p2 <= N-1 and A[p1] == A[p2]):

            p1 -= 1
            p2 += 1

        if (p2-p1-1) > self.long_palindrom_length:

            self.long_palindrom = ""
            self.long_palindrom_length = p2-p1-1
            for i in range(p1+1, p2):
                self.long_palindrom += A[i]

        # @param A : string
        # @return a strings

    def longestPalindrome(self, A):

        N = len(A)
        for i in range(N):

            self.isPalindrome(A, N, i, i)

            if i < N-1:
                self.isPalindrome(A, N, i, i+1)

        return self.long_palindrom


A = "a"
s = Solution()

print(s.longestPalindrome(A))
