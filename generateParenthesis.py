#! /usr/bin/env python

'''
Generate Parentheses 

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"

https://oj.leetcode.com/problems/generate-parentheses/
'''

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.output = []
        self.generateParenthesisRec(0,0,n,"")
        return self.output

    def generateParenthesisRec(self,left_num,right_num,total_num,string):
        if left_num == total_num and right_num == total_num:
            self.output.append(string)
        else:
            if left_num < total_num:
                self.generateParenthesisRec(left_num+1,right_num,total_num,string+"(")
            if right_num < left_num:
                self.generateParenthesisRec(left_num,right_num+1,total_num,string+")")

if __name__ == "__main__":
    s = Solution()
    print s.generateParenthesis(3)
            
