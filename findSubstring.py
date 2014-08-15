#! /usr/bin/env python

'''
Substring with Concatenation of All Words 

You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

https://oj.leetcode.com/problems/substring-with-concatenation-of-all-words/
'''

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        if len(L) == 0: return None

        subs_len = len(L)*len(L[0])
        output = []

        for i in range(0,len(S)-subs_len):
            #print S,L,i
            if self.isSubstring(S,L,i):
                output.append(i)
        return output

    def isSubstring(self,S,L,start):
        subs_len = len(L)*len(L[0])
        sub_len = len(L[0])
        index_flag = [0 for i in range(len(L))]

        for i in range(start,start+subs_len-sub_len+1,sub_len):
            string = S[i:i+sub_len]
            #print string
            for j in range(len(L)):
                #print string, L[j]
                if L[j] == string:
                    index_flag[j] += 1
                    break

        #print index_flag
        for i in index_flag:
            if i != 1:
                return False
        return True
                

if __name__ == "__main__":
    s = Solution()
    print s.findSubstring("barfoothefoobarman", ["foo", "bar"])
