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
        print self.generateParenthesisRec_2(0,0,n,"")
        #self.generateParenthesisRec_1(0,0,n,"")
        return self.output

    def generateParenthesisRec_1(self,left_num,right_num,total_num,string):
        if left_num == total_num and right_num == total_num:
            self.output.append(string)
        else:
            if left_num < total_num:
                self.generateParenthesisRec_1(left_num+1,right_num,total_num,string+"(")
            if right_num < left_num:
                self.generateParenthesisRec_1(left_num,right_num+1,total_num,string+")")

    def generateParenthesisRec(self,left_num,right_num,total_num,string):
        if left_num == total_num and right_num == total_num:
            self.output.append(string)
        else:
            for i in range(left_num+1, total_num+1):
                lefts = ''
                for j in range(i-left_num):
                    lefts += '('
                self.generateParenthesisRec(i, right_num, total_num, string+lefts)
            for i in range(right_num+1, left_num+1):
                rights = ''
                for j in range(i-right_num):
                    rights += ')'
                self.generateParenthesisRec(left_num,i,total_num,string+rights)
    
    def generateParenthesisRec_2(self, left_num, right_num, total_num, string):
        output = []
        if left_num == total_num and right_num == total_num:
            output.append(string)
        else:
            if left_num < total_num:
                output.extend(self.generateParenthesisRec_2(left_num+1,right_num,total_num, string+"("))
            if left_num > right_num:
                output.extend(self.generateParenthesisRec_2(left_num,right_num+1,total_num,string+")"))

        return output

if __name__ == "__main__":
    s = Solution()
    print s.generateParenthesis(3)
            
