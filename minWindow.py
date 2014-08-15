#! /usr/bin/env python

'''
Minimum Window Substring 

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

https://oj.leetcode.com/problems/minimum-window-substring/
'''

class Solution:
    # @return a string
    def minWindow(self, S, T):
        len_s = len(S)
        len_t = len(T)
        needToFind = []
        hasFound = []
        minWindowBegin,minWindowEnd = 0,0

        for i in range(256):
            needToFind.append(0)
            hasFound.append(0)

        for i in T:
            needToFind[ord(i)] += 1

        minWindowLen = len_s
        count = 0
        begin = 0
        end = 0

        for end in range(len_s):
            if needToFind[ord(S[end])] == 0:
                continue
            hasFound[ord(S[end])] += 1
            if hasFound[ord(S[end])] <= needToFind[ord(S[end])]:
                count += 1

            if count == len_t:
                while needToFind[ord(S[begin])] == 0 or hasFound[ord(S[begin])] > needToFind[ord(S[begin])]:
                    if hasFound[ord(S[begin])] > needToFind[ord(S[begin])]:
                        hasFound[ord(S[begin])] -= 1
                    begin += 1

                if end-begin+1 < minWindowLen:
                    minWindowBegin = begin
                    minWindowEnd = end
                    minWindowLen = end-begin+1


        return S[minWindowBegin:minWindowEnd+1]

if __name__ == "__main__":
    s = Solution()
    print s.minWindow("ADOBECODEBANC","ABC")
    




