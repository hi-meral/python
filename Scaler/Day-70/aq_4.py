# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):

        H = A
        CN = 1
        RH = None
        while H is not None and CN <= C:

            if CN <= B-1:

                if CN == B-1:
                    TH = H

                H = H.next

            if CN >= B and CN <= C:

                if CN == B:
                    LH = H

                t = H
                H = H.next
                t.next = RH
                RH = t

            CN += 1

        LH.next = H

        if B > 1:
            TH.next = RH
            return A
        else:
            return RH
