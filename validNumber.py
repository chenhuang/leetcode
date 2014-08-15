#! /usr/bin/env python

'''
Valid Number 

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

https://oj.leetcode.com/problems/valid-number/
'''

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        isValid = True 
        try:
            float(s)
        except:
            return False
        return True
        
