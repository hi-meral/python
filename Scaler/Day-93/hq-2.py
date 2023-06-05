import sys

sys.setrecursionlimit(10**6)


class Solution:

    HM = {}
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer

    def solve(self, A, B, C):

        R = 0
        N = len(B)

        R = self.getSatisfaction(B, C, N-1, 6)

        # for a in A:

        #     R += self.getSatisfaction(B, C, N-1, a)

        return R

    def getSatisfaction(self, B, C, i, a):

        if i < 0:
            return 0

        t = (i, a)
        if t not in self.HM:

            x = self.getSatisfaction(B, C, i-1, a)

            if B[i] <= a:

                if x > 0:
                    x = min(x, self.getSatisfaction(B, C, i, a - B[i]) + C[i])
                else:
                    x = self.getSatisfaction(B, C, i, a - B[i]) + C[i]

            self.HM[t] = x

        return self.HM[t]


S = Solution()
A = [2, 4, 6]
B = [2, 1, 3]
C = [2, 5, 3]

R = S.solve(A, B, C)

print(R)
