#! /usr/bin/python
'''
Best Time to Buy and Sell Stock 

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/

'''

'''
Best Time to Buy and Sell Stock II 

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

'''

'''
Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

'''


class Solution:
# @param prices, a list of integer
# @return an integer
# Buy and Sell I:
# Max profit with one transaction:
# Observation: 
# 1. Max profit == Max(A[j]-A[i])
# 2. Record the max A[j]-A[i] at each j. 
# 3. Keep record of the max until the end.
# 
  def maxProfit(self, prices):
    max_so_far = 0
    min_so_far = 0
    for p in prices:
      if p > min_so_far: 
        min_so_far = p
      if p - min_so_far > max_so_far:
        max_so_far = p-min_so_far
    return max_so_far

# Buy and Sell II:
# Max profit from endless transactions
# Observations:
# 1. The best strategy is to buy at the begining of each up trend and sell at the end of each up trend.  
# 2. That means for each up trend the profit should be calculated.

  def maxProfit_II(self,prices):
    i = prices[0]
    profit = 0
    for j in prices[1:]:
      if j > i:
        profit += j - i
    return profit

# Buy and Sell III:
# Max profit from at most two transactions:
# Observations: 
# 1. At most twice, so could be 0,1,or2.
# 2. One way is to conduct reduction to 1 transctions, then apply the same method on the rest of the histories. 
# 3. The above is a greedy apporach, d&c is able to apply on such examples. 
# 4. Does greedy approach works? the only concern would be may be the first picked transcation might cross the optimal solution. 
# 5. Overlap suggests that there are two solution that each one has one part in current solution. Suppose that is the case, and the two parts are A and B, and A < B, and A's right part is coverted by greedy solution C, that means A's left half is less that the left most of C, however, according to greedy definition, A shall be collected by C. Thus greedy works in this case. 
# 6. This is not right, greedy does not work, for example: 1,2,3,4,2,3,8,4,3,10: greedy would be [1,10], then 0, profit = 9, all transaction would be 3+6+7 = 16, two would be 7+7 = 14. So has to be a different approach. 
# One solution is to first find all solutions by greedy, then pick two that are not overlapped with each other. This is time consuming. 
# List all possible transactions, and pick two that does not overlap with each other and gain the maximum profit. 
# All possible transactions: O(n^2), find max profit: O(n^4). 
# D&C: find a divide point, then identify the max from left and right, find the max sum. 
# Divide point: O(n), within each side, O(n) to find the max: total O(N^2).
# D&P: do multi-pass processing of the data, build results base on each pass of the data: 
# First, pass, identify max profit selling at point i, second pass, identify max profit buying at point j. third pass, identify the max profit such that i < j

  def maxProfit_III(self, prices):
    min = prices[0]
    max_so_far = 0
    S = [0] # Store the max profit so far
    for i in prices[1:]:
      if min > i:
        min = i
      if i - min > max_so_far:
        max_so_far = i - min
      S.append(max_so_far)
    print S
    
    max = 0
    max_so_far = 0
    for j in range(len(prices)-1,0,-1):
      if max < prices[j]:
        max = prices[j]
      if max - prices[j] + S[j-1] > max_so_far:
        max_so_far = max - prices[j] + S[j-1]

    return max_so_far
        
      
if __name__ == "__main__":
  A= [1,2,3,4,2,3,8,4,3,10]
  s = Solution()
  print s.maxProfit_III(A)
  

# For the case of three transactions: first O(n^2) to identify all possible 2 transaction's max. # Then O(n) to compute the third case, total time == O(n^2)
# So essentially the DP part is that the x transaction profit is build upon profit from x-1 transactions. 
