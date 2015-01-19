class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit1(self, prices):
        # write your code here
        # p[0][n] = profit from 0 to n
        # = max(p[0][i]+p[i][n])
        max_total = 0

        for i in range(len(prices)):
            if i == 3:
                print str(i)+"\t"+str(self.maxProfitOnce(prices, 0, i+1))+"\t"+str(self.maxProfitOnce(prices, i, len(prices)))
            max_total = max(max_total, self.maxProfitOnce(prices, 0, i+1) + self.maxProfitOnce(prices, i, len(prices)))
        
        return max_total

    def maxProfitOnce(self,prices,i,j):
        max_so_far = 0
        min_idx = i

        for k in range(i, j):
            if prices[min_idx] > prices[k]:
                min_idx = k
            max_so_far = max(prices[k]-prices[min_idx], max_so_far)
            if j == 4:
                print k, max_so_far

        return max_so_far

    def maxProfit(self, prices):
        max_total = 0
        max_so_far = 0
        min_idx = 0
        max_idx = len(prices) - 1
        
        p = [[],[]]
        p[0] = [0 for i in range(len(prices))]
        p[1] = [0 for i in range(len(prices))]
        
        for i in range(len(prices)):
            if prices[min_idx] > prices[i]: 
                min_idx = i
            max_so_far = max(max_so_far, prices[i]-prices[min_idx])
            p[0][i] = max_so_far

        max_so_far = 0
        
        for i in list(reversed(range(len(prices)))):
            if prices[max_idx] < prices[i]:
                max_idx = i
            max_so_far = max(max_so_far, prices[max_idx]-prices[i])
            p[1][i] = max_so_far
            
        for i in range(len(prices)):
            max_total = max(max_total, p[0][i]+p[1][i])
    
        return max_total

if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([2,1,2,0,1])

