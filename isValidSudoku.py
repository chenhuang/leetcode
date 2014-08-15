#! /usr/bin/env python

'''
Valid Sudoku 

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        isValid = True
        for i in range(9):
            # Check for row
            row = []
            for j in board[i]:
                row.append(j)
            isValid = isValid and self.validPart(row)
            # Check for column
            column = []
            for j in range(9):
                column.append(board[j][i])
            isValid = isValid and self.validPart(column)

        # Check for square
        for i in range(0,9,3):
            for j in range(0,9,3):
                square = []
                for k in range(i,i+3):      
                    for l in range(j,j+3):
                        square.append(board[k][l])
                isValid = isValid and self.validPart(square)

        return isValid

    def validPart(self, input):
        count = []
        for i in range(9):
            count.append(0)

        for i in input:
            if i != '.':
                count[int(i)-1]+=1

        for i in count:
            if i > 1:
                return False

        return True

if __name__ == "__main__":
    s = Solution()
    board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    print s.isValidSudoku(board)
