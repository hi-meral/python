# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        path = self.getPath(A, B)

        s = []
        self.checkDistance(path[0], C, s)
        ans = len(s)-1

        if ans >= 0:
            return ans

        for i in range(1, len(path)):
            s = []
            self.checkDistance(path[i], C, s)
            ans = len(s)-1

            if ans >= 0:
                return ans + i

        return -1

    def getPath(self, A, d):

        path = []

        self.checkNode(A, d, path)

        return path

    def checkNode(self, A, d, path):

        if A == None:
            return False

        if A.val == d:
            path.append(A)
            return True

        if self.checkNode(A.left, d, path) or self.checkNode(A.right, d, path):
            path.append(A)
            return True

        return False
        
    def checkDistance(self, A, d, s):

        if A == None:
            return False

        if A.val == d:
            s.append(1)
            return True

        g1 = self.checkDistance(A.left, d, s)
        g2 = self.checkDistance(A.right, d, s)

        if(g1 or g2):
            s.append(1)
            return True

        return False
