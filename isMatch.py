#! /usr/bin/env python

'''
Regular Expression Matching 

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
'''

class Solution:
    # @return a boolean
    # DFS should be able to do it
    def isMatch(self, s, p):
        print s,p
        return self.dfs(s,p,0,0)

    # Needs pruning
    def dfs(self,s,p,ss,pp):
        if pp == len(p):return ss == len(s)
        #print s,p,ss,pp
        if pp+1 < len(p) and p[pp+1] == '*':
            if p[pp] == '.':
                return (ss+1 < len(s) and self.dfs(s,p,ss+1,pp)) or self.dfs(s,p,ss,pp+2) or self.dfs(s,p,ss+1,pp+2)
            else:
                if ss < len(s) and s[ss] == p[pp]:
                    return self.dfs(s,p,ss+1,pp) or self.dfs(s,p,ss+1,pp+2)
                else:
                    return self.dfs(s,p,ss,pp+2)
        else:
            if ss < len(s) and (p[pp] == s[ss] or p[pp] == '.'):
                return self.dfs(s,p,ss+1,pp+1)
            else:
                return False


if __name__ == "__main__":
    s = Solution()
    print s.isMatch("abc","abc")
    print s.isMatch("aa","a")
    print s.isMatch("aaa","aa")
    print s.isMatch("aa","a*")
    print s.isMatch("aa",".*")
    print s.isMatch("ab",".*")
    print s.isMatch("aab","c*a*b")
    print s.isMatch("ab", ".*c")
    print s.isMatch("aaa", "a*a")
    print s.isMatch("a", "ab*")
    print s.isMatch("bbab", "b*a*")
    print s.isMatch("aab", "c*a*b")
    print s.isMatch("baccbbcbcacacbbc", "c*.*b*c*ba*b*b*.a*")
