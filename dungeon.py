class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        if len(dungeon) == 0:
            return 0
        r_num = len(dungeon)
        c_num = len(dungeon[0])        
        dp = [[0 for i in range(c_num)] for i in range(r_num)]
        dp[r_num-1][c_num-1] = max(1, -dungeon[r_num-1][c_num-1]+1)
        
        for i in reversed(range(r_num-1)):
            if dungeon[i][c_num-1] >= dp[i+1][c_num-1]:
                dp[i][c_num-1] = 1
            else:
                dp[i][c_num-1] = dp[i+1][c_num-1] - dungeon[i][c_num-1]
        
        for i in reversed(range(c_num-1)):
            if dungeon[r_num-1][i] >= dp[r_num-1][i+1]:
                dp[r_num-1][i] = 1
            else:
                dp[r_num-1][i] = dp[r_num-1][i+1] - dungeon[r_num-1][i]
        
        for i in reversed(range(len(dungeon)-1)):
            for j in reversed(range(len(dungeon[0])-1)):
                if dungeon[i][j] >= min(dp[i+1][j],dp[i][j+1]):
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i+1][j],dp[i][j+1]) - dungeon[i][j]
                    
        return dp[0][0]

if __name__ == "__main__":
    s = Solution()
    print s.calculateMinimumHP([[0,0]])

