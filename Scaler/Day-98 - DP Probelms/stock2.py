
class Solution:

    def stock2(self, A):

        N = len(A)
        minPriceLeft = A[0]
        maxPriceRight = A[N-1]

        leftprofit = [0]
        rightprofit = [0]

        for i in range(1, N):

            leftprofit.append(A[i] - minPriceLeft)
            minPriceLeft = min(minPriceLeft, A[i])

        for i in range(N-2, -1, -1):

            rightprofit.append(maxPriceRight-A[i])
            maxPriceRight = max(maxPriceRight, A[i])

        ans = 0
        for i in range(N-1):

            profit = leftprofit[i] + rightprofit[i+1]

            ans = max(ans, profit)

        ans = max(ans, leftprofit[N-1])

        return ans


S = Solution()
#A = [7, 1, 5, 3, 6, 4]
A = [3, 4, 8, 2, 6]
R = S.stock2(A)

print(R)
