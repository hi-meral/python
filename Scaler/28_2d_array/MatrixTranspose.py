class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A):

        Z = []

        for j in range(len(A[0])):

            rowsum = []

            for i in range(len(A)):

                #A[i][j] = A[i][j] - B[i][j]
                rowsum.append(A[i][j])

            Z.append(rowsum)

        return Z


s = Solution()


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

B = [[9, 8, 7],    [6, 5, 4],  [3, 2, 1]]

C = [[1, 2, 3, 4], [5, 6, 7, 8],
     [9, 2, 3, 4], [11, 13, 14, 15]]

D = [
    [24, 63, 39, 81, 84, 30],
    [21, 64, 95, 6, 88, 73],
    [33, 6, 63, 96, 86, 66],
    [62, 88, 23, 52, 94, 77],
    [81, 58, 74, 18, 16, 25],
    [26, 40, 88, 64, 72, 23],
    [45, 44, 86, 92, 50, 26],
    [64, 34, 83, 26, 29, 68],
    [43, 42, 7, 17, 45, 52],
    [94, 25, 62, 19, 95, 77]
]

E = [[1, 2], [1, 2], [1, 2]]

print(s.solve(E))
