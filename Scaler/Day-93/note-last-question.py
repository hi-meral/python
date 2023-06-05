import sys

sys.setrecursionlimit(10**6)


class Solution:

    DP = []
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer

    def solve(self, A):

        N = len(A)

        S = sum(A)
        S1 = S//2

        for d in range(N):
            self.DP.append([-1] * (S1+1))

        R = self.recuFun(A, S1, N-1)

        for x in range(len(self.DP)):

            for y in range(len(self.DP[x])):

                print(self.DP[x][y], end=" ")

            print("")
        return R

    def recuFun(self, A, W, i):

        if i < 0:
            if W == 0:
                return 1
            else:
                return 0

        if self.DP[i][W] != -1:
            return self.DP[i][W]

        for q in range(0, W+1):
            a = self.recuFun(A, q, i-1)

            if q-A[i] >= 0:

                b = self.recuFun(A, int(q-A[i]), i-1)
            else:
                b = 0

            self.DP[i][q] = a or b

        return self.DP[i][W]


S = Solution()
A = [1, 3, 11]


R = S.solve(A)

print(R)
