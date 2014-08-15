#! /usr/bin/python

'''
Pow(x,n)

Implement pow(x,n)

https://oj.leetcode.com/problems/powx-n/
'''

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow_rec(self, x, n):
        if n == 0:
            return 1.0    
        if n == 1:
            return float(x)

        a = self.pow_rec(x,n/2)
        if n%2 == 1:
            return a * a * x
        else:
            return a * a

    def pow(self, x, n):
        isNegative = False
        result = 0 
        if n < 0:
            isNegative = True
            n = 0-n

        result = self.pow_rec(x,n)

        if isNegative:
            return 1/result
        else:
            return result

if __name__ == "__main__":
    s = Solution()
    print s.pow(4.70975,-6)
