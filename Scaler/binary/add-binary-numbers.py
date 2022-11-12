import string


class Solution:

    def reverse(self, str1):
        str2 = ""
        N = len(str1)
        for i in range(N-1, -1, -1):
            str2 += str1[i]

        return str2

    # @param A : tuple of integers
    # @return an integer

    def addBinary(self, A, B):

        i = len(A)-1
        j = len(B) - 1
        carry = 0
        ans = ""

        while i >= 0 or j >= 0 or carry:

            sum = 0

            if(i >= 0):
                sum += int(A[i])
                i -= 1

            if(j >= 0):
                sum += int(B[j])
                j -= 1

            sum += carry

            bit = sum % 2

            carry = sum//2

            ans += str(bit)

        return self.reverse(ans)


s = Solution()
print(s.singleNumber("0011", "0101"))
