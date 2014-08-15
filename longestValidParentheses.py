#! /usr/bin/python

'''
Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

https://oj.leetcode.com/problems/longest-valid-parentheses/
'''

class Solution:
    # @param s, a string
    # @return an integer
    # Observations: 
    # 1. a valid parentheses: ) matched with (
    def longestValidParentheses(self, s):
        longest, last, indices = 0, 0, []
        for i in range(len(s)):
            if s[i] == '(':
                indices.append(i)
            elif len(indices) == 0:
                last = i + 1
            else:
                index = indices.pop()
                if len(indices) == 0:
                    longest = max(longest, i - last + 1)
                else:
                    longest = max(longest, i - indices[-1])
        return longest

if __name__ == '__main__':
    s = Solution()
    print s.longestValidParentheses("()()")


