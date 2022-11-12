class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A):

        N = len(A)

        M = len(A[0])

        Z = [[0 for _ in range(N)] for _ in range(2 * N-1)]

        for j in range(M):

            x, y = 0, j
            while (x < N and y >= 0):

                Z[j][x] = A[x][y]
                #print(A[x][y], end=" ")

                x += 1
                y -= 1

        for i in range(1, N):

            x, y = i, M-1

            while (x < N and y >= 0):

                Z[N-1+i][x-i] = A[x][y]
                #print(A[x][y], end=" ")

                x += 1
                y -= 1

        return Z


s = Solution()


A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

C = [[1, 2, 3, 4], [4, 5, 6, 7], [1, 2, 2, 1], [1, 9, 5, 2]]
print(s.solve(C))
