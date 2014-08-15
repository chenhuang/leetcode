#! /usr/bin/env python

'''
Search a 2D Matrix 

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

https://oj.leetcode.com/problems/search-a-2d-matrix/
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        # determine row first
        i,j = 0, m-1
        while i <= j:
            mid = (i+j)/2
            if target > matrix[mid][0]:
                i = mid+1
            elif target < matrix[mid][0]:
                j = mid-1
            else:
                return True

        row = min(i,j)
        i,j = 0, n-1
        while i <= j:
            mid = (i+j)/2
            if target > matrix[row][mid]:
                i = mid+1
            elif target < matrix[row][mid]:
                j = mid-1
            else:
                return True

        return False

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]]
    print s.searchMatrix(matrix,12)
            

