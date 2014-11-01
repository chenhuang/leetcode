#! /usr/bin/env python

'''
Word Search

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
For example,
Given board =
[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

https://oj.leetcode.com/problems/word-search/
'''

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    # Typical DFS problem:
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0][0])):
                if self.dfs(board,i,j,word):
                    return True
        return False
    

    def dfs(self, board, i,j, word):
        stack = []
        if board[i][0][j] == word[0]:
            stack.append((i,j,0,[(i,j)]))

        while len(stack) > 0:
            i,j,loc,path = stack.pop()
            #print i,j,prefix,path,board[i][0][j]

            if loc == len(word)-1 and board[i][0][j] == word[loc]:
                return True
            elif board[i][0][j] == word[loc]:
                if i+1 < len(board) and (i+1,j) not in path:
                    path.append((i+1,j))
                    stack.append((i+1,j,loc+1,list(path)))
                    path.pop()
                if j+1 < len(board[0][0]) and (i,j+1) not in path:
                    path.append((i,j+1))
                    stack.append((i,j+1,loc+1,list(path)))
                    path.pop()

                if i-1 >= 0 and (i-1,j) not in path:
                    path.append((i-1,j))
                    stack.append((i-1,j,loc+1,list(path)))
                    path.pop()

                if j-1 >= 0 and (i,j-1) not in path:
                    path.append((i,j-1))
                    stack.append((i,j-1,loc+1,list(path)))
                    path.pop()

        return False

    def word_search(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0][0])):
                if self.word_search_rec(board,word,(i,j)):
                    return True

        return False
        
    def word_search_rec(self, board, word, pos):
        result = False
        if len(word) == 0:
            return True
        else:
            (x,y) = pos
            if word[0] == board[x][0][y]:
                old_line = board[x][0]
                board[x][0] = board[x][0][:y]+'0'+board[x][0][y+1:]
                if x+1 >= 0 and x+1 < len(board):
                    result = self.word_search_rec(board, word[1:], (x+1,y)) or result
                if x-1 >= 0 and result == False:
                    result = self.word_search_rec(board, word[1:], (x-1,y)) or result
                if y-1 >= 0 and result == False:
                    result = self.word_search_rec(board, word[1:], (x,y-1)) or result
                if y+1 >= 0 and y+1 < len(board[0][0]) and result == False:
                    result = self.word_search_rec(board, word[1:], (x,y+1)) or result
                board[x][0] = old_line

            return result

if __name__ == "__main__":
    s = Solution()
    board = [["ABCE"],["SFCS"],["ADEE"]]
    print s.exist(board, "ABCCED")
    print s.exist(board, "SFCS")
    print s.exist(board, "ABCB")
    print s.word_search(board, "ABCCED")
    print s.word_search(board, "SFCS")
    print s.word_search(board, "ABCB")

            
            
        

