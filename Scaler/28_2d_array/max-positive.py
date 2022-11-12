'''
Given an array of integers A, of size N.

Return the maximum size subarray of A having only non-negative elements. If there are more than one such subarray, return the one having the smallest starting index in A.

NOTE: It is guaranteed that an answer always exist'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ret = [[]]
        for i in A:
            if i < 0:
                ret.append([])
            else:
                ret[-1].append(i)
        mxlen = max([len(i) for i in ret])
        for i in ret:
            if len(i) == mxlen:
                return i


s = Solution()

print(s.solve([-1, 5, 6, -2, -1, 7, 8, 9]))
