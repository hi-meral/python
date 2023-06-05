##from CreateTreefromDict import *
import sys
sys.setrecursionlimit(10**6)
# Definition for a  binary tree node


class TreeNode:

    def __init__(self):
        self.isEnd = 0
        self.hm = {}


class Solution:

    def insertTrie(self, root, data):

        t = root
        l = len(data)

        for x in range(l):

            ch_x = data[x]
            if t.hm.__contains__(ch_x):
                t.hm[ch_x][0] += 1
                t = t.hm[ch_x][1]
            else:
                nn = TreeNode()
                t.hm[ch_x] = [1, nn]
                t = nn

        t.isEnd = 1

    def searchTrie(self, root, data):
        t = root
        l = len(data)

        for x in range(l):

            ch_x = data[x]
            if t.hm.__contains__(ch_x):
                ret = t.hm[ch_x][0]
                t = t.hm[ch_x][1]
            else:
                return 0

        return ret

    # @param A : root node of tree
    # @return a list of integers

    def solve(self, A, B):

        trie = TreeNode()
        ans = []
        t = trie
        N = len(A)
        for i in range(N):
            if A[i] == 0:
                self.insertTrie(trie, B[i])
            elif A[i] == 1:
                ans.append(self.searchTrie(trie, B[i]))

        return ans


# Tr = CreateTree()
# Tx = Tr.getBSTree()

A = ["hat", "cat", "rat"]
B = ["cat", "ball"]

A = [0, 0, 1, 1]
B = ["hack", "hacker", "hac", "hak"]


A = [0, 1]
B = ["abcde", "abc"]

S = Solution()
R = S.solve(A, B)

print(R)
