class Solution:

    dp = {}

    def solve(self, A):

        N = len(A)
        M = len(A[0])
        self.dp = {}
        R = self.saveQ(0, 0, A, N, M)
        return R

    def saveQ(self, i, j, A, N, M):

        if i >= N or j >= M:
            return float('inf')

        if i == N-1 and j == M-1:

            return 1 - A[i][j]

        t = (i, j)
        if t not in self.dp:

            a = self.saveQ(i+1, j, A, N, M)
            b = self.saveQ(i, j+1, A, N, M)

            self.dp[t] = min(a, b) - A[i][j]

        return self.dp[t]


S = Solution()
A = [[-3, 2, 4, -7],
     [-6, 5, -4, 6],
     [-15, -8, 3, -4],
     [7, 4, -2, -7]]
R = S.solve(A)

print(R)
