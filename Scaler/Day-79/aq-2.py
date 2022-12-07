from CreateTreefromDict import *


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

        ans = self.checkRange(A)
        return ans[1]

    def checkRange(self, R):

        if R.left is None and R.right is None:
            return [1, 1, R.val, R.val]

        t = 1
        X = [1, 0, 0, 0]
        if R.left is not None:
            X = self.checkRange(R.left)

            if X[3] > R.val:
                X[0] = 0

        Y = [1, 0, 0, 0]
        if R.right is not None:
            Y = self.checkRange(R.right)

            if Y[2] < R.val:
                Y[0] = 0

        Z1 = X[0] and Y[0]

        if X[0] == 1 and Y[0] == 1:
            Z2 = 1 + X[1] + Y[1]
        elif X[0] == 0:
            Z2 = Y[1]
        elif Y[0] == 0:
            Z2 = X[1]

        if R.left is not None and R.right is not None:
            Z3 = min(X[2], Y[2])
        elif R.left is not None:
            Z3 = X[2]
        elif R.right is not None:
            Z3 = Y[2]

        if R.left is not None and R.right is not None:
            Z4 = max(X[3], Y[3])
        elif R.left is not None:
            Z4 = X[3]
        elif R.right is not None:
            Z4 = Y[3]

        return [Z1, Z2, Z3, Z4]


Tr = CreateTree()
#Tx = Tr.getTree([12, 5, 15, 3, 6, 13, 16])
#Tx = Tr.getTree([10, 5, 15, 1, 8, 7])
Tx = Tr.getTree([5, 3, 8, 1, 4, 7, 9])
S = Solution()


A = [1, 6, 2, 3]
B = [6, 1, 3, 2]

R = S.solve(Tx)
# R = T.inorderTraversal(T)

print(R)
