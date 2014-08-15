'''
Unique Paths 

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

https://oj.leetcode.com/problems/unique-paths/

-------------------------------------------------------

Unique Paths II 

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

https://oj.leetcode.com/problems/unique-paths-ii/
'''


class Solution:
    # @return an integer
    # Obs: BFS or DFS would work, then count the number
    # Recursive: details please be aware
    def uniquePaths(self, m, n):
        return self.countPath(m,n,1,1)
        
    def countPath(self, m, n, i, j):    
        if (i == m and j != n):
            return self.countPath(m,n,i,j+1)
        elif (i != m and j == n):
            return self.countPath(m,n,i+1,j)
        elif (i == m and j == n):
            return 1
        else:
            return self.countPath(m,n,i+1,j)+self.countPath(m,n,i,j+1)

    # DFS then
    def uniquePaths_1(self,m,n):
        explore_stack = [(1,1)]
        count = 0
        while len(explore_stack) != 0:
            node = explore_stack.pop()
            if node[0] < m and node[1] < n:
                explore_stack.append((node[0]+1,node[1]))
                explore_stack.append((node[0],node[1]+1))
            elif node[0] == m and node[1] == n:
                count += 1
            elif node[0] == m and node[1] < n:
                explore_stack.append((node[0],node[1]+1))
            elif node[0] < m and node[1] == n:
                explore_stack.append((node[0]+1,node[1]))

        return count

    # Try DP
    # up(m,n) = up(m-1,n)+up(m-2,n)
    # up[i][j]: number of unique paths i & j distance from end node
    def uniquePaths_DP(self,m,n):
        up = []
        up.append([1 for i in range(n)])
        for i in range(1,m):
            up.append([1])
    
        for i in range(1,m):
            for j in range(1,n):
                up[i].append(up[i-1][j]+up[i][j-1])
        
        return up[m-1][n-1]

    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    # Observations: 
    # 1. add a check 
    # 2. check ability 
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        if m == 0: return 0
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1: return 0
        if obstacleGrid[m-1][n-1] == 1: return 0

        up = [[]]
        for i in range(n):
            if obstacleGrid[-1][n-i-1] == 1:
                up[0].extend([0 for j in range(i,n)]) 
                break
            else:
                up[0].append(1)

        for i in range(1,m):
            if obstacleGrid[m-i-1][-1] == 1:
                for j in range(i,m):
                    up.append([0])
                break
            else:
                up.append([1])

        for i in range(1,m):
            for j in range(1,n):
                up[i].append(up[i-1][j]+up[i][j-1])
                if obstacleGrid[m-i-1][n-j-1]:
                    up[i][j] = 0
        
        return up[m-1][n-1]

    def uniquePathsWithObstacles(self, obstaclesGrid):
    
        
if __name__ == "__main__":
    s = Solution()
    #print s.uniquePaths(10,12)
    #print s.uniquePaths_1(3,12)
    #print s.uniquePaths_DP(10,12)
    print s.uniquePathsWithObstacles([[0,0],[1,0]])
    print s.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])
