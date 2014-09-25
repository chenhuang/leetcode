#! /usr/bin/python

import os
import re
import sys

class Solution:
    def findMedian(self,A,B):
        len_a= len(A)
        len_b= len(B)

        return self.findKth(A,B,(len_a+len_b)/2)

    def findKth(self,A,B,k):
        len_a = len(A)
        len_b = len(B)
        if len_a == 0:
            return B[0-k]
        if len_b == 0:
            return A[0-k]

        if k == 1:
            return max(A[-1],B[-1])

        mid = k/2
        A_mid = A[0-mid]
        B_mid = B[0-mid]

        if A_mid < B_mid:
            return self.findKth(A,B[:0-mid],k/2)
        elif A_mid > B_mid:
            return self.findKth(A[:0-mid],B,k/2)

if __name__ == "__main__":
    s = Solution()
    print s.findKth([1,3,5,7],[2,4,6],2)

