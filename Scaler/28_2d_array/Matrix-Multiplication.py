class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):

        M = len(A)
        N = len(A[0])
        P = len(B[0])

        C = []

        for i in range(0, M):
            C.append([0] * P)

        for i in range(0, M):
            for j in range(0, P):
                for k in range(0, N):
                    C[i][j] += A[i][k] * B[k][j]

        return C
