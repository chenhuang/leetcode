#! /usr/bin/env python

'''
N-Queens 
'''

# Observations:
# DFS with contraint propagation:
# Use recursion to implement DFS.
# Constraint: no two queens are attacking each other 

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        board = []
        # Build board:
        for i in range(n):
            row = ""
            for j in range(n):
                row+="."
            board.append(row)

        # Solve the problem recursively
        self.output = []
        self.solveNQueensRec(board)
        return self.output

    def solveNQueensRec(self, board):    
        if self.findEmptyRow(board) == -1:
            print board
            self.output.append(board)
            return 
        
        row = self.findEmptyRow(board)
        for i in range(len(board)):
            new_board = list(board)
            new_board[row] = new_board[row][:i]+'Q'+new_board[row][i+1:]
            if self.isValid(new_board):
                self.solveNQueensRec(new_board)

    def isValid(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 'Q':
                    for k in range(j+1,len(board)):
                        # Check Row
                        if board[i][k] == 'Q':
                            return False
                    for k in range(i+1,len(board)):
                        # Check Column
                        if board[k][j] == 'Q':
                            return False
                    # Check diagnal
                    for k in range(1,len(board)):
                        if max(i+k,j+k) < len(board):
                            if board[i+k][j+k] == 'Q':
                                return False
                        if i-k > 0 and j+k < len(board):
                            if board[i-k][j+k] == 'Q':
                                return False
                        if i+k < len(board) and j-k > 0:
                            if board[i+k][j-k] == 'Q':
                                return False
                        if min(i-k,j-k) > 0:
                            if board[i-k][j-k] == 'Q':
                                return False
                    break
        return True

    def findEmptyRow(self, board):
        for i in range(len(board)):
            count = 0
            for j in range(len(board)):
                if board[i][j] == "Q":
                    count += 1
            if count == 0:
                return i
        return -1
       
# Optimal solution: 
# http://zhedahht.blog.163.com/blog/static/2541117420114331616329/

    def solveNQueens_1(self, n):
        columnIndex = []
        for i in range(n):
            columnIndex.append(i)

        output = []
        self.permutation(columnIndex,0,output)
#        print output
#        print len(output)
    
    # generate n permutations for input list n
    def permutation(self, columnIndex, start, output):
        if start == len(columnIndex):
            #output.append(columnIndex)
            # Add check valid code here
            if self.isValid(columnIndex):
                output.append(columnIndex)
        else:
            a = columnIndex[start]
            for i in range(start, len(columnIndex)):
                b = columnIndex[i]
                columnIndex[i] = a
                columnIndex[start] = b
                
                self.permutation(columnIndex, start+1, output)

                columnIndex[i] = b
                columnIndex[start] = a
        
    def isValid(self, per_list):
        for i in range(len(per_list)):
            for j in range(i+1,len(per_list)):
                if i-j == per_list[i]-per_list[j] or j-i == per_list[i]-per_list[j]:
                    return False

        return True

if __name__ == "__main__":
    s = Solution()
    s.solveNQueens_1(9)
        
