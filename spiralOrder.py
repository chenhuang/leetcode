#! /usr/bin/env python

'''
Spiral Matrix 

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''

# Observations:
# 1. Given this example: the sequence is: row(1), column(-1), row(-1), column(1),row(2)
# 2. The thickness of peel increase by 1 each time. 
# 3. Need to avoid duplicated visit for corner elements: 1,2,3, then 6, 9, then 8, 7, then 4, then 5: navie approach is by using hashing, alternative approach?
# 4. Can be solved either with a D&C or iterative approach, try iterative approach first. 

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        interval = 0
        m = len(matrix)
        if m == 0: 
            return []
        if m > 0:  
            n = len(matrix[0])
        if n == 0:
            return []

        output = []
        while interval <= min(m-1-interval, n-1-interval):
            # top row
            output.extend(matrix[interval][interval:n-interval])
            # bottom column
            for j in range(interval+1,m-1-interval):
                output.append(matrix[j][n-1-interval])
            # bottom row
            if interval < m-1-interval:
                bottom_row = matrix[m-1-interval][interval:n-interval]
                bottom_row.reverse()
                output.extend(bottom_row)
            # top column
            if interval+1 < m-1-interval-1:
                top_column = []
                for j in range(m-1-interval-1,interval,-1):
                    top_column.append(matrix[j][interval])
                output.extend(top_column)
            interval += 1
        return output

    def spiralOrder_1(self, matrix):
        m = len(matrix)
        if m == 0: return []
        n = len(matrix[0])
        if n == 0: return []
    
        left, right, top, bottom = 0, n-1, 0, m-1
        output = []
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                output.append(matrix[top][i])
            for i in range(top+1,bottom):
                output.append(matrix[i][right])
            for i in range(right,left-1,-1):       
                if top < bottom:
                    output.append(matrix[bottom][i])
            for i in range(bottom-1,top,-1):
                if left < right:
                    output.append(matrix[i][left])
            left, right, top, bottom = left+1, right-1,top+1,bottom-1

        return output
                
            

if __name__ == "__main__":
    s = Solution()
    print s.spiralOrder_1([[ 1], [2], [3 ]])

