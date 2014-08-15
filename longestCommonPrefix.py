#! /usr/bin/python

'''
Longest Common Prefix 

Write a function to find the longest common prefix string amongst an array of strings.

https://oj.leetcode.com/problems/longest-common-prefix/
'''

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ""
        common_prefix = strs[0]

        for i in range(1,len(strs)):
            j = 0
            while j < min(len(common_prefix),len(strs[j])) and strs[i][j] == common_prefix[j]:
                j+=1
            common_prefix = common_prefix[:j]

        return common_prefix
            

