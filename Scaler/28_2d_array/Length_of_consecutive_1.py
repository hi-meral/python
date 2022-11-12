class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):

        ans = float('-inf')
        N = len(A)
        C = 0

        for i in range(N):

            if A[i] == "1":
                C += 1

        if C == N:
            return C

        for i in range(N):

            if A[i] == "1":
                continue

            L, R = 0, 0

            for x in range(i-1, -1, -1):

                if A[x] == "1":
                    L += 1
                else:
                    break

            for y in range(i+1, N):

                if A[y] == "1":
                    R += 1
                else:
                    break

            if L+R == C:

                ones = L+R

            else:

                ones = L+R+1

            ans = max(ans, ones)

        return ans


s = Solution()


print(s.solve("1110111"))
