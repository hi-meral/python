class Solution:

    def numSetBits(self, A):

        bstr = ""
        while A > 0:
            bstr += str(A % 2)
            A = A//2

        return bstr

    def fill32bit(self, bstr):

        bstr += "0"*(32-len(bstr))

        return bstr

    def convert2decimal(self, bstr32):

        N = len(bstr32)
        summ = 0
        for i in range(N-1, -1, -1):
            summ += int(bstr32[i]) << N-1-i

        return summ

    def reverse(self, A):
        bstr = self.numSetBits(A)
        bstr32 = self.fill32bit(bstr)
        dec = self.convert2decimal(bstr32)
        return dec


s = Solution()
print(s.reverse(3))
