class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        if A == 1:
            return 1

        B = A
        L, R = 1, A
        while B >= 1:

            if B <= L:
                return -1

            if B*B == A:
                return B
            elif B*B > A:
                R = B
                B = int(R - (R-L)/2)
            elif B*B < A:
                L = B
                B = int(R - (R-B)/2)


s = Solution()

# print(s.solve(49))

for i in range(1, 101):
    print(i, " -", s.solve(i))
