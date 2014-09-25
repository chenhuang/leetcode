#! /use/bin/python

class Solution:
    def binarySearch(self, A,target):
        start, end = 0, len(A)
        while start+1 < end:
            mid = (start+end)/2

            if A[mid] > target:
                end = mid
            elif A[mid] == target:
                start = mid
            else:
                start = mid
            print start,end,mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end

        return -1

if __name__ == "__main__":
    s = Solution()
    print s.binarySearch([1,1,3,4,5,6],1)
