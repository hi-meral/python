class CreateTree:
    def __init__(self):
        pass

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

    def below(self, A, K):

        if A == None:
            return 0

        if K == 0:
            return 1

        return self.below(A.left, K-1) + self.below(A.right, K-1)

    def getTree7(self, T):

        A = TreeNode(T[0])

        AA = TreeNode(T[1])
        AB = TreeNode(T[2])

        AAA = TreeNode(T[3])
        AAB = TreeNode(T[4])

        ABA = TreeNode(T[5])
        ABB = TreeNode(T[6])

        #ABAB = TreeNode(T[7])

        #AABA = TreeNode(T[8])

        A.left = AA
        A.right = AB

        AA.left = AAA
        AA.right = AAB

        AB.left = ABA
        AB.right = ABB

        #AAB.left = AABA
        #AAA.left = ABAB

        return A

    def getTree9(self, T):

        A = TreeNode(T[0])

        AA = TreeNode(T[1])
        AB = TreeNode(T[2])

        AAA = TreeNode(T[3])
        AAB = TreeNode(T[4])

        ABA = TreeNode(T[5])
        ABB = TreeNode(T[6])

        ABAB = TreeNode(T[7])

        AABA = TreeNode(T[8])

        A.left = AA
        A.right = AB

        AA.left = AAA
        AA.right = AAB

        AB.right = ABA
        AB.right = ABB

        AAB.left = AABA
        AAA.left = ABAB

        return A

    def getBSTree(self):

        A = TreeNode(10)

        AA = TreeNode(5)
        AB = TreeNode(15)

        AAA = TreeNode(3)
        AAB = TreeNode(8)

        ABA = TreeNode(12)
        ABB = TreeNode(17)

        A.left = AA
        A.right = AB

        AA.left = AAA
        AA.right = AAB

        AB.left = ABA
        #AB.right = ABB

        return A

    def getCustTree1(self):

        # 5 1 -1 2 -1 -1

        A = TreeNode(5)

        AL = TreeNode(1)
        #AR = TreeNode(15)

        ALL = TreeNode(2)

        A.left = AL
        #A.right = AB

        AL.left = ALL

        return A

    def getTree(self):

        one = TreeNode(1)

        two_1 = TreeNode(2)
        two_2 = TreeNode(3)

        three_1 = TreeNode(4)
        three_2 = TreeNode(5)
        three_3 = TreeNode(6)
        three_4 = TreeNode(7)

        four_1 = TreeNode(8)
        four_2 = TreeNode(9)
        four_3 = TreeNode(10)
        four_4 = TreeNode(11)
        four_5 = TreeNode(12)
        four_6 = TreeNode(13)
        four_7 = TreeNode(14)
        four_8 = TreeNode(15)

        ###################

        one.left = two_1
        one.right = two_2

        ###################

        two_1.left = three_1
        two_1.right = three_2

        two_2.left = three_3
        two_2.right = three_4

        ###################

        three_1.left = four_1
        three_1.right = four_2

        three_2.left = four_3
        three_2.right = four_4

        three_3.left = four_5
        three_3.right = four_6

        three_4.left = four_7
        three_4.right = four_8

        ###################

        return one

    def getTree3(self, T):

        A = TreeNode(T[0])

        AA = TreeNode(T[1])
        AB = TreeNode(T[2])

        A.left = AA
        A.right = AB

        return A

    def getTreeLeft1(self):

        A = TreeNode(3)

        AA = TreeNode(0)
        BB = TreeNode(1)

        AA.left = TreeNode(1)

        A.left = AA
        A.right = BB

        BBB = TreeNode(1)
        BB.right = BBB

        BBB.right = TreeNode(1)

        return A


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class showLL:
    def __init__(self, LL):

        while LL is not None:
            print(LL.val)
            LL = LL.next
