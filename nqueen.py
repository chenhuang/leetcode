#! /usr/bin/python

class Solution:
    def nqueen(self, board, n):
        result = []
        len_board = len(board)

        if self.isValid(board):
            if len_board == n:
                result+=[board]
            else:
                for i in range(n):
                    new_board = board+[[len_board,i]]
                    sub_solution = self.nqueen(new_board,n)
                    result.extend(sub_solution)

        return result

    def isValid(self,board):
        # check for column:
        for i in range(len(board)):
            for j in range(i+1, len(board)):
                if board[i][1] == board[j][1]:
                    return False
                if board[i][0]-board[j][0] == board[i][1]-board[j][1]:
                    return False
                if board[i][0]-board[j][0] == board[j][1]-board[i][1]:
                    return False

        return True

    def print_board(self,board,n):
        for i in board:
            row = []
            for j in range(n):
                if i[1] == j:
                    row.append('Q')
                else:
                    row.append('0')
            print row
                
                    

if __name__ == "__main__":
    s = Solution()
    results = s.nqueen([],8)
    print "Number of solutions: " + str(len(results))

    for i in results:
        s.print_board(i,8)
        print ""
        
        
