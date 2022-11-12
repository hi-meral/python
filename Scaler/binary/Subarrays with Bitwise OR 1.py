class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an long
    def solve(self, A):
        last = 0
        ans = 0
        N = len(A)
        for i in range(N):
            if A[i] == 1:
                last = i+1
            print("-", last)
            ans += last
        return ans


A = [0, 1, 0, 0, 0]

s = Solution()
print(s.solve(A))
