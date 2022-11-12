class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        binarray = []

        while A > 0:
            d = A % 2
            A = A//2
            binarray.append(d)

        ans = 0
        N = len(binarray)
        for i in range(N):

            if binarray[i] == 1:
                ans += 5 ** (i+1)

        return ans


s = Solution()
print(s.solve(3))
