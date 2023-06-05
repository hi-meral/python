##from CreateTreefromDict import *
import sys
sys.setrecursionlimit(10**6)
# Definition for a  binary tree node


# https://www.scaler.com/academy/mentee-dashboard/class/46462/homework/problems/5832?navref=cl_tt_nv

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
                t = t.hm[ch_x]
            else:
                nn = TreeNode()
                t.hm[ch_x] = nn
                t = nn

        t.isEnd = 1

    def searchTrie(self, root, data):
        t = root
        l = len(data)
        flag = 0
        for x in range(l):

            ch_x = data[x]
            if t.hm.__contains__(ch_x):
                t = t.hm[ch_x]
            else:

                if flag > 0:
                    return "0"

                if x == l-1:
                    flag += 1
                else:
                    for dd in t.hm:
                        if t.hm[dd].hm.__contains__(data[x+1]):
                            t = t.hm[dd]
                            flag += 1
                            break

        if flag == 1:
            return "1"
        else:
            return "0"

    # @param A : root node of tree
    # @return a list of integers

    def solve(self, A, B):

        trie = TreeNode()
        ans = ""
        t = trie
        N = len(A)
        for i in range(N):
            self.insertTrie(t, A[i])

        Q = len(B)
        for j in range(Q):
            ans = ans + self.searchTrie(trie, B[j])

        return ans


# Tr = CreateTree()
# Tx = Tr.getBSTree()

A = ["data", "circle", "cricket"]
B = ["date", "circel", "crikket", "data", "circl"]


S = Solution()
R = S.solve(A, B)

print(R)
