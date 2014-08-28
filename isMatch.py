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
    def isMatch_1(self, s, p):
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

    def isMatch_2(self,string,pattern):
        stack = []
        for i in pattern:
            if len(stack) > 0:
                if i == "*" and stack[-1] == i:
                    continue
            stack.append(i)
        pattern = "".join(stack)

        return self.isMatch_rec(string,pattern)
        

    def isMatch_rec(self,string,pattern):
        result = False
        if len(pattern) == 0 and len(string) == 0:
            result = True
        elif len(pattern) > 0 and len(string) > 0:
            if pattern[0] == "*":
                for i in range(len(string)+1):
                    if self.isMatch_rec(string[i:], pattern[1:]):
                        result = True
            elif pattern[0] == "?":
                if self.isMatch_rec(string[1:],pattern[1:]):
                    result = True
            else:
                if pattern[0] == string[0]:
                    if self.isMatch_rec(string[1:],pattern[1:]):
                        result = True
        return result

    def isMatch(self, s, p):
        s_cur = 0;
        p_cur= 0;
        match = 0;
        star = -1;
        while s_cur<len(s):
            if p_cur< len(p) and (s[s_cur]==p[p_cur] or p[p_cur]=='?'):
                s_cur = s_cur + 1
                p_cur = p_cur + 1
            elif p_cur<len(p) and p[p_cur]=='*':
                match = s_cur
                star = p_cur
                p_cur = p_cur+1
            elif (star!=-1):
                p_cur = star+1
                match = match+1
                s_cur = match
            else:
                return False
        while p_cur<len(p) and p[p_cur]=='*':
            p_cur = p_cur+1
             
        if p_cur==len(p):
            return True
        else:
            return False

''' 
The recursion version is easy to understand, a better solution is to use dynamic programming, here we use M[i][j] to represent that S[i:] and T[j:] match. 

M[i][j] <- (s[i] == t[j] && s[i] != '*') and M[i+1][j+1] or s[i] == '*' and M[i+1][j] || M[i][j+1]

M[i][n] = s[i] == '*' and M[i+1][n]
M[m][j] = t[j] == '*' and M[m][j+1]
'''

def isMatch_DP(self, string, pattern):
    m = len(string)
    n = len(pattern)

    M = []
    for i in range(m):
        M.append([False for j in range(n)])
   
    # Initialize M
    for i in reversed(range(m)):
        M[i][n-1] = pattern[n-1] == '*'
    for i in reversed(range(n)):
        M[m-1][i] = (pattern[i] == '*' or pattern[i] == '?') and M[m-1][i+1]


if __name__ == "__main__":
    s = Solution()
    print s.isMatch("abc","abc")
    print s.isMatch("ab","aa")
    print s.isMatch("a","*")
    print s.isMatch("aa","a*")
    print s.isMatch("aa","?*")
    print s.isMatch("aabbbabbbbbabbaabbbbbabbaababaabaaaaabbaaaabbbaaabbb","****b***a**ba**a***a")
    print s.isMatch("aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba","*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*")
    #print s.isMatch("ab", ".*c")
    #print s.isMatch("aaa", "a*a")
    #print s.isMatch("a", "ab*")
    #print s.isMatch("bbab", "b*a*")
    #print s.isMatch("aab", "c*a*b")
    #print s.isMatch("baccbbcbcacacbbc", "c*.*b*c*ba*b*b*.a*")
