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
   
                    

if __name__ == "__main__":
    s = Solution()
    print s.isMatch("ba","bc*d*a")

