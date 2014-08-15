'''
Spiral Matrix II 

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
https://oj.leetcode.com/problems/spiral-matrix-ii/
'''

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix =[[0 for j in range(n)] for i in range(n)]
        left,right,top,bottom=0,n,0,n
        
        m = 1
        while left <= right and top <= bottom:
            for i in range(left,right):
                matrix[top][i] = m
                m+=1
            for i in range(top+1,bottom):
                matrix[i][right-1]=m
                m+=1
            for i in reversed(range(left,right-1)):
                matrix[bottom-1][i]=m
                m+=1
            for i in reversed(range(top+1, bottom-1)):
                matrix[i][left] = m
                m+=1

            left, right, top, bottom = left+1, right-1, top+1, bottom-1

        return matrix

if __name__ == "__main__":
    s = Solution()
    m = s.generateMatrix(4)

    for i in m:
        print i
