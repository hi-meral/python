class Solution:
    # @param A : tuple of integers
    # @return an integer
    def sword(self, A):

        person = [True] * (A)

        for x in range(A):

            person[x] = x

        sword = 0

        while True:

            if sword == len(person)-1:
                sword = -1

            person.pop(sword+1)
            sword = sword+1

            if sword == len(person):
                sword = 0

            if len(person) == 1:
                break

        return person[0]+1


S = Solution()
R = S.sword(100)

print(R)
