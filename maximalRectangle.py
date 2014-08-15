#! /usr/bin/python

'''

Maximal Rectangle 

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

https://oj.leetcode.com/problems/maximal-rectangle/
'''

# DP problem, most solutions used the answer from largetst rectagnle in histogram, but i decided to use DP only

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        left_right = []
        m = len(matrix)
        n = len(matrix[0])
        max_area = 0
        for i in range(m):
            left_right.append([])
            for j in range(n):
                left_right[i].append([0,0])
                if matrix[i][j] == 1:
                    left_right[i][j] = [1,1]
                    if j > 0:
                        left_right[i][j][0] = max(left_right[i][j-1][0]+1,1)
                    if i > 0:
                        left_right[i][j][1] = max(left_right[i-1][j][1]+1,1)
                    
                    left_val = left_right[i][j][0]
                    right_val = left_right[i][j][1]
                    print left_val, right_val
                    if left_right[i-left_val+1][j-right_val+1] == [1,1]:
                        max_area = max(left_val * right_val,max_area)
        for i in left_right:
            print i

        return max_area


if __name__ == "__main__":
    s = Solution()
    matrix = [
[0,0,0,0],
[0,1,1,0],
[0,1,1,0],
[1,1,1,1],
[1,1,1,1]
]
    print s.maximalRectangle(matrix)

                    
        
