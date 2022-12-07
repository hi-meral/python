from CreateTreefromDict import *


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):

        S = float('-inf')
        E = float('inf')
        ans = self.checkRange(A, S, E)
        return ans

    def checkRange(self, R, S, E):

        if R is None:
            return 1

        if S <= R.val <= E:
            L = self.checkRange(R.left, S, R.val-1)
            R = self.checkRange(R.right, R.val+1, E)
        else:
            return 0

        return L and R


Tr = CreateTree()
Tx = Tr.getTree([12, 5, 15, 3, 6, 13, 16])
#Tx = Tr.getTree([6, 3, 7, 2, 5, 8, 9])
S = Solution()


A = [1, 6, 2, 3]
B = [6, 1, 3, 2]

R = S.isValidBST(Tx)
# R = T.inorderTraversal(T)

print(R)
