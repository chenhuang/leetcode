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
        matched = []
        # corner case
        if len(p) == 0:
            if len(s) == 0: return True
            return False
            
        # initialization
        for i in range(len(s)):
            matched.append([])
            if i == 0:
                if p[0] == s[0] or p[0] == '.' or p[0] == '*':
                    matched[0].append(True)
                else:
                    return False
            else:
                if p[0] == '*':
                    matched[i].append(True)
                else:
                    matched[i].append(False)
        
        # build transition matrix
        for i in range(1,len(s)):
            for j in range(1, min(i+1,len(p))):
                matched[i].append(False)
                if p[j] == '*' or p[j] == '.' or p[j] == s[i]:
                    matched[i][j] = matched[i-1][j-1] 

        # return the result
        return matched[len(s)-1][len(p)-1]    

if __name__ == "__main__":
    s = Solution()
    print s.isMatch("aa","a")
