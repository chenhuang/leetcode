#! /usr/bin/python

'''
Longest Palindromic Substring 

Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

https://oj.leetcode.com/problems/longest-palindromic-substring/
'''

class Solution:
    # @return a string
    # DP O(n^2)
    # The problem is I wanted to write efficient code with efficient algorithm, however, I was not able to express my logic clearly, and then using efficient data sctructure/code will worse the problem. I have the idea, the idea is good, but first I need to write logically sound code.
    def longestPalindrome(self, s):
        s_length = [0 for i in range(len(s))]
        max_length = 0
        output = ""

        # length from 1 to len(s)
        for length in range(0, len(s)):
            for i in range(0,len(s)-length):
                if s[i] == s[i+length] and s_length[i+1] == length-1:
                    s_length[i] = length
                    if s_length[i] > max_length:
                        max_length = s_length[i]
                        output = ''.join(s[i:i+length])
            print s_length

        return output

    # P[(i,j)]:
    # if s[i] = s[j] and P[(i+1,j-1)] == s[i:j+1]
    # p[(i,j)] = p[(i,j)]
    def longestPalindrome(self, s):
        
    

if __name__ == "__main__":
    s = Solution()
    print s.longestPalindrome("abba")
                        
                   
            
        

