class Solution:
    # @param A : tuple of integers
    # @return an integer
    def monkey_door(self, A):

        door = [False] * (A+1)

        for i in range(1, A+1):

            for j in range(i, A+1):

                if j % i == 0:

                    door[j] = not door[j]

        c = 0

        for x in door:

            if x:
                c += 1

        return c


S = Solution()
R = S.monkey_door(100)

print(R)
