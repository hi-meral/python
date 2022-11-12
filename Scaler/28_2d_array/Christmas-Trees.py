'''
You are given an array A consisting of heights of Christmas trees and an array B of the same size consisting of the cost of each of the trees (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)), and you are supposed to choose 3 trees (let's say, indices p, q, and r), such that Ap < Aq < Ar, where p < q < r.
The cost of these trees is Bp + Bq + Br.

You are to choose 3 trees such that their total cost is minimum. Return that cost.

If it is not possible to choose 3 such trees return -1.'''


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

        flag = 0
        ans = 0

        for i in range(1, len(A)-1):

            minn = 0
            f = 0
            anss = B[i]
            for j in range(i-1, -1, -1):
                if(A[j] < A[i]):
                    if f == 0:
                        f = 1
                        minn = B[j]
                    else:
                        minn = min(minn, B[j])

            if(f == 0):
                continue

            anss += minn

            minn = 0
            f = 0

            for j in range(i+1, len(A)):
                if(A[j] > A[i]):
                    if f == 0:
                        f = 1
                        minn = B[j]
                    else:
                        minn = min(minn, B[j])

            if(f == 0):
                continue

            anss += minn

            if flag == 0:
                ans = anss
            else:
                ans = min(ans, anss)

            flag = 1

        if(flag == 1):
            return ans
        else:
            return -1


s = Solution()

A = [1, 6, 4, 2, 6, 9]
B = [2, 5, 7, 3, 2, 7]

print(s.solve(A, B))
