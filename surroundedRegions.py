#! /usr/bin/python

'''
Surrounded Regions 

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

https://oj.leetcode.com/problems/surrounded-regions/
'''

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        m = len(board)
        n = len(board[0])

        left,right,top,bottom = 0, n-1, 0, m-1

        stack = []
        for i in range(m):
            if board[i][left] == 'O':
                stack.append((i,left))
            if board[i][right] == 'O':
                stack.append((i,right))

        for j in range(n):
            if board[top][j] == 'O':
                stack.append((top,j))
            if board[bottom][j] == 'O':
                stack.append((bottom,j))

        while len(stack)>0:
            (i,j) = stack.pop()
            board[i] = board[i][:j]+'Y'+board[i][j+1:] 
            next_nodes = self.find_next(board,i,j)
            if len(next_nodes) > 0:
                stack.extend(next_nodes)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i] = board[i][:j]+'X'+board[i][j+1:] 
                if board[i][j] == 'Y':
                    board[i] = board[i][:j]+'O'+board[i][j+1:] 
#        return board
                
                
    def find_next(self, board,i,j):
        m = len(board)
        n = len(board[0])

        output = []
        if i > 0 and board[i-1][j] == 'O':
            output.append((i-1,j))
        if i+1 < m and board[i+1][j] == 'O':
            output.append((i+1,j))
        if j > 0 and board[i][j-1] == 'O':
            output.append((i,j-1))
        if j+1 < n and board[i][j+1] == 'O':
            output.append((i,j+1))

        return output
            
if __name__ == "__main__":
    s = Solution()
    board = ["XOXOXO","OXOXOX","XOXOXO","OXOXOX"]

    print s.solve(board)

