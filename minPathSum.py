#! /usr/bin/env python

'''
Minimum Path Sum 

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

https://oj.leetcode.com/problems/minimum-path-sum/
'''

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    # Obs: Dijkstra's algorithm, DP in essence.
    def minPathSum(self, grid):
        # distance matrix d[i][j] = min distance from [0][0] to [i][j]
        if len(grid) == 0:
            return 0
        
        m = len(grid[0]) # column number
        n = len(grid)   # row number

        d = [[0]]

        # for 1st row's elems
        for j in range(1,m):
            d[0].append(grid[0][j-1]+d[0][j-1])

        # for 1st column's elems
        for j in range(1,n):
            d.append([grid[j-1][0]+d[j-1][0]])

        # for each row and column [i][j]
        for i in range(1,n):
            for j in range(1,m):
                d[i].append(min(d[i][j-1]+grid[i][j-1],d[i-1][j]+grid[i-1][j]))
        print d
        
        return d[n-1][m-1]


if __name__ == "__main__":
    s = Solution()
    #grid = [[1,2,3,4],[5,6,7,8],[7,8,9,10]]
    #grid = [[2,3,4,2,2,5,5,6,6,3],[7,5,6,4,1,7,8,1,7,7],[4,0,4,5,4,2,7,8,9,3],[7,3,8,3,5,0,9,1,8,7],[4,5,4,0,9,5,8,0,8,5],[7,4,7,3,0,1,7,9,0,8],[5,9,1,5,3,7,6,4,8,6]]
    grid = [[1]]
    grid = [[1,2],[1,1]]
    print s.minPathSum(grid)
        
