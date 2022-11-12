class Solution:
    def lszero(self, A):
        N = len(A)
        total = 0
        pf = [None] * N
        pfdict = {}

        for i in range(N):
            total += A[i]
            pf[i] = total

        ans = []
        ans_max = float('-inf')

        for p in range(N):

            if pf[p] in pfdict:

                if abs((pfdict[pf[p]]+1) - p) > ans_max:
                    ans = [(pfdict[pf[p]]+1), p]
                    ans_max = abs((pfdict[pf[p]]+1) - p)
            elif pf[p] == 0:

                if abs(0 - p) > ans_max:
                    ans = [0, p]
                    ans_max = abs(0 - p)
            else:
                pfdict[pf[p]] = p

        if len(ans) == 0:
            return []

        if ans[1] < N:
            ans[1] += 1

        return A[ans[0]:ans[1]]


G = [-19, 8, 2, -8, 19, 5, -2, -23]
s = Solution()
print(s.lszero(G))
