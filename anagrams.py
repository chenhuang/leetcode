#! /usr/bin/env python

'''

Anagrams 

Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.

https://oj.leetcode.com/problems/anagrams/
'''

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        sign_hash = {}
        for i in range(len(strs)):
            signature = self.getSign(strs[i])
            if signature not in sign_hash.keys():
                sign_hash[signature] = []

            sign_hash[signature].append(strs[i])
        
        output = []
        for key in sign_hash.keys():
            output.append(sign_hash[key])
        return output


    def getSign(self, str_):
        char_count = [0 for i in range(26)]
        for i in str_:
            if ord(i)-ord('a') >=0 and ord(i)-ord('a')<26:
                char_count[ord(i)-ord('a')] += 1
        output = ""
        for i in range(26):
            if char_count[i] > 0:
                output+=str(char_count[i])
                output+='c'
                output+=str(i)

        return output

if __name__ == "__main__":
    s = Solution()
    print s.anagrams(["abc","c ab"," adbc","ab cd","z","z"])
