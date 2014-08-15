#! /usr/bin/env python

'''
Set Matrix Zeroes 

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = 'a'
                
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'a':
                    for k in range(n):
                        if matrix[i][k] != 'a':
                            matrix[i][k] = 0
                    for k in range(m):
                        if matrix[k][j] != 'a':
                            matrix[k][j] = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
        return matrix

if __name__ == "__main__":
    s = Solution()
    print s.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])
