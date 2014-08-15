#! /usr/bin/env python

'''
Sudoku Solver 

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


A sudoku puzzle...

...and its solution numbers marked in red.

https://oj.leetcode.com/problems/sudoku-solver/
'''

# Observations:
# 1. The navie solution is to iterate all possible combinations, which is uncomputable. 
# 2. A different approach is to do DFS on the solution space. 
# 3. This will turn the problem into a search problem: 
# 4. each step will have a bunch of branches to choose: from number 1-9. 
# 5. The selection of numbers are based on contraints: row, column and square
# 6. Summary: search problem with contraints.

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        stack = []
        stack.append(board)

        while len(stack) > 0:
            board = stack.pop()
            (i,j) = self.findEmptyCell(board)
            if i != -1 and j != -1:
                candidates = self.validOptionsAll(board,i,j)
                if candidates:
                    for k in candidates:
                        new_board = list(board)
                        #new_board[i] = new_board[i][:j]+str(k)+new_board[i][j+1:]
                        new_board[i] = ''.join(new_board[i][0:j])+str(k)+''.join(new_board[i][j+1:])
                        stack.append(new_board)
            else:
                return board
                    

    def findEmptyCell(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return (i,j)

        return (-1,-1)
        
    # Given the board, determine valid number options for board[i,j]:
    def validOptionsAll(self, board, i, j):
        # Validate row:
        row = []
        for k in board[i]:
            row.append(k)

        row_candidate_list = self.validOptions(row)
        
        column = []
        for k in range(9):
            column.append(board[k][j])
        
        column_candidate_list = self.validOptions(column)

        square = []

        for k in range((i/3)*3,(i/3)*3+3):
            for l in range((j/3)*3,(j/3)*3+3):
                square.append(board[k][l])

        square_candidate_list = self.validOptions(square)

        candidate_list = [] 
        for i in row_candidate_list:
            if i in column_candidate_list and i in square_candidate_list:
                candidate_list.append(i)

        if len(candidate_list) > 0:
            return candidate_list
        else:
            return None
        
    # Return valid options given the list
    def validOptions(self, input_list):
        count = []
        for i in range(9):
            count.append(0)

        for j in input_list:
            if j != '.':
                count[int(j)-1] += 1
        
        output_list = []
        for i in range(9):
            if count[i] < 1:
                output_list.append(i+1)

        return output_list

    # Recursively solve sudoku, so called in-place algorithms
    def solveSudokuRec(self, board):
        (i,j) = self.findEmptyCell(board)
        if i == -1 and j == -1:
            return 
        candidates = self.validOptionsAll(board,i,j)
        if candidates:
            for k in candidates:
                new_board = list(board)
                new_board[i] =  ''.join(board[i][0:j])+str(k)+''.join(board[i][j+1:])
                self.solveSudokuRec(new_board)


if __name__ == "__main__":

    s = Solution()
    s.solveSudoku([".....7..9",".4..812..","...9...1.","..53...72","293....5.",".....53..","8...23...","7...5..4.","531.7...."])
    s.solveSudokuRec([".....7..9",".4..812..","...9...1.","..53...72","293....5.",".....53..","8...23...","7...5..4.","531.7...."])



