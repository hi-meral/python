class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):

        #Z = [[0]*A]*A
        N = A
        Z = [[0]*N]

        for i in range(N-1):
            Z.append([0]*N)

        T = 0
        B = N-1
        L = 0
        R = N-1
        num = 1
        direction = 1

        while T <= B and L <= R:

            if direction == 1:

                for i in range(L, R+1):

                    Z[T][i] = num
                    num += 1

                T += 1
                direction = 2

            if direction == 2:

                for i in range(T, B+1):

                    Z[i][R] = num

                    num += 1

                R -= 1
                direction = 3

            if direction == 3:

                for i in range(R, L-1, -1):

                    Z[B][i] = num
                    num += 1

                B -= 1
                direction = 4

            if direction == 4:

                for i in range(B, T-1, -1):

                    Z[i][L] = num

                    num += 1

                L += 1
                direction = 1

        return Z


s = Solution()


print(s.solve(5))
