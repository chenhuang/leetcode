#! /usr/bin/env python

'''
Sort Colors 

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

https://oj.leetcode.com/problems/sort-colors/
'''

# Observations:
# Two pointers: i = 0, j = len(A)-1
# if A[i] == 2, swap A[i] with A[j] and j--
# if A[i] == 0, i++

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        i,j = 0,len(A)-1
        
        while i < j:
            if A[i] == 0:
                i += 1
            if A[i] == 1 or A[i] == 2:
                tmp = A[j]
                A[j] = A[i]
                A[i] = tmp
                j -= 1

        j = len(A)-1
        while i < j:
            if A[i] == 1:
                i += 1
            elif A[i] == 2:
                tmp = A[j]
                A[j] = A[i]
                A[i] = tmp
                j -= 1
            else:
                i+=1

        return A

if __name__ == "__main__":
    s = Solution()
    print s.sortColors([1,2,0,1,2,0,0,1,1,2])
                
            


