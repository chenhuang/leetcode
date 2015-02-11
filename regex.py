class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    # matched[i][j]: if matched until s[i] and p[j]
    # matched[i][j] = matched[i-1][j] if p[j] == *
    # or matched[i-1][j-1] if p[j] == s[i] 
    # or p[j] == '.'
    # 
    # return matched[m][n]: m:len(s), n:len(p)
    # Initialization:
    #   matched[0][0] = 1
    #   matched[i][0] = 1 if p[0] == *
    # Loop:
    #   i = 0 to m:
    #       j = 0 to n:
    # 
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                    if i == 2 and j == 5:
                        print dp[i][j]
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        print dp
        return dp[len(s)][len(p)]

    # @return a boolean
    def isMatch_(self, s, p):
        # transition matrix: 
        matched = [[False for i in range(len(p) + 1)] for j in range(len(s)+1)]
        matched[0][0] = True

        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                matched[0][i] = matched[0][max(i-2,0)]
        
        for i in range(1,len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '.':
                    matched[i][j] = matched[i-1][j-1]
                elif p[j-1] == '*':
                    matched[i][j] = matched[i][j-1] or matched[i][j-2] or (matched[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                else:
                    matched[i][j] = matched[i-1][j-1] and s[i-1] == p[j-1]
                
        '''
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    if j-2 > 0 and p[j-2] == '*':
                        matched[i][j] = matched[i-1][j-1] or matched[i-1][max(j-2,0)]
                    else:
                        matched[i][j] = matched[i-1][j-1]
                elif p[j-1] == '*':
                    if s[i-1] == s[max(i-2,0)] or p[max(j-2,0)] == '.': 
                        matched[i][j] = matched[i][j-1] or matched[i][j-2] or matched[i-1][j-1] or matched[i-1][j]
        '''
        
        #def foo(x): print x
        #map(foo, matched)

        return matched[len(s)][len(p)]
   

if __name__ == "__main__":
    s = Solution()
    #print s.isMatch_("ba","bc*d*a")
    print s.isMatch_("bbbba", ".*a*a")
    print s.isMatch_("bbb", ".*")
    #print s.isMatch_("aa","a")

