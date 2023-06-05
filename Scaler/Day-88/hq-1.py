
class Solution:

    def set_of_count(self, off_left, off_right, s):

        for c in s:

            if c == '(':
                off_left += 1

            if c == ')':
                if off_left > 0:
                    off_left -= 1
                else:
                    off_right += 1

        return (off_left, off_right)

    def rec(self, idx, s, curr_s, off_left, off_right, res_set, balance):

        N = len(s)
        if idx == N:
            if off_left == 0 and off_right == 0:
                res_set.add(curr_s)
                return res_set

        elif balance >= 0:
            if s[idx] == '(' and off_left > 0:
                res_set = self.rec(idx+1, s, curr_s, off_left-1,
                                   off_right, res_set, balance)
            if s[idx] == ')' and off_right > 0:
                res_set = self.rec(idx+1, s, curr_s, off_left,
                                   off_right-1, res_set, balance)

            diff = 0

            if s[idx] == '(':
                diff = 1
            if s[idx] == ')':
                diff = -1

            res_set = self.rec(
                idx+1, s, curr_s + s[idx], off_left, off_right, res_set, balance + diff)

            return res_set

    def removeInvalidParentheses(self, s):

        off_left, off_right = self.set_of_count(0, 0, s)
        res_set = set()
        self.rec(0, s, "", off_left, off_right, res_set, 0)
        res = []
        for val in res_set:
            res.append(val)
        return res

    def solve(self, A):
        ans = self.removeInvalidParentheses(A)
        return ans


S = Solution()
A = "()())()"
A = "(a)())()"
R = S.solve(A)
print(R)
