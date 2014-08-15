#! /usr/bin/python

'''
Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

https://oj.leetcode.com/problems/valid-parentheses/
'''

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        isMatch = {'(':')','{':'}','[':']'}

        for i in range(len(s)):
            if s[i] in ['(','{','[']:
                stack.append(s[i])
            if s[i] in [')','}',']']:
                if len(stack) == 0: return False
                a = stack.pop()
                if s[i] != isMatch[a]:
                    return False

        if len(stack) != 0:
            return False
        return True
                    
                
