#! /usr/bin/env python

'''
Wildcard Matching

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:


https://oj.leetcode.com/problems/wildcard-matching/
'''

# This one is similar with regex match
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        prev_p = ""
        new_p = ""
        for i in range(len(p)):
            if prev_p == "":
                prev_p = p[i]
                new_p += p[i]
            else:
                if prev_p == "*" and p[i] == "*":
                    continue
                else:
                    prev_p = p[i]
                    new_p += p[i]
        
        print new_p
        return self.isMatchRec(s,new_p,0,0)
    
    def isMatchRec(self,s,p,ss,pp):
        if ss == len(s) and pp == len(p):
            return True
        result = False

        if ss < len(s) and pp < len(p):
            if s[ss] == p[pp] or p[pp] == '?':
                result = result or self.isMatchRec(s,p,ss+1,pp+1)

            if p[pp] == '*':
                for i in (range(ss,len(s)+1)):
                    result = result or self.isMatchRec(s,p,i,pp+1)
                    if result == True: break

        return result

if __name__ == "__main__":
    s = Solution()
    print s.isMatch("aa","a")
    print s.isMatch("aa","aa")
    print s.isMatch("aaa","aa")
    print s.isMatch("aa","*")
    print s.isMatch("aa","a*")
    print s.isMatch("aa","?*")
    print s.isMatch("aab","c*a*b")
    print s.isMatch("aabbbabbbbbabbaabbbbbabbaababaabaaaaabbaaaabbbaaabbb","****b***a**ba**a***a")
