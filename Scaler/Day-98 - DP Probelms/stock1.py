
class Solution:

    def stock1(self, A):

        N = len(A)
        minPrice = A[0]
        ans = 0

        for i in range(1, N):

            profit = A[i] - minPrice
            ans = max(ans, profit)
            minPrice = min(minPrice, A[i])

        return max(0, ans)


S = Solution()
A = [7, 1, 5, 3, 6, 4]
R = S.stock1(A)

print(R)
