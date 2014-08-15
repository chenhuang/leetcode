#! /usr/bin/env python

'''
Longest Substring Without Repeating Characters 

Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        char_index = []
        for i in range(ord('z')-ord('A')+1):
            char_index.append(0)

        cur_len = 0
        for i in range(len(s)):
            if char_index[ord(s[i])-ord('A')] == 0:
                char_index[ord(s[i])-ord('A')] = 1
                cur_len += 1
            else:
                char_index = [0 for j in range(ord('z')-ord('A')+1)]
                max_len = max(max_len,cur_len)
                cur_len = 1
                char_index[ord(s[i])-ord('A')] = 1

        return max_len
        
if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLongestSubstring("bbb")
