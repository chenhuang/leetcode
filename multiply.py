#! /usr/bin/env python

'''
Multiply Strings 

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.

https://oj.leetcode.com/problems/multiply-strings/
'''

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    # D&C as introducted in stanford algorithm class
    # num1: len=m, num2: len=n
    # (A+B) * (C+D)
    # = AC*10**(m+n)/2 + AD*10**m/2 + BC*10**n/2 + BD
    def multiply(self, num1, num2):
        if len(num1) < 3 and len(num2) < 3:
            return int(num1)*int(num2)

        m,n = len(num1), len(num2)
        AC = self.multiply(num1[:m/2],num2[:n/2])
        AC *=10**((m+n)/2)
        AD = self.multiply(num1[:m/2],num2[n/2:])
        AD *=10**(m/2)
        BC = self.multiply(num1[m/2:],num2[:n/2])
        BC *=10**(n/2)
        BD = self.multiply(num1[m/2:],num2[n/2:])

        return AC+AD+BC+BD

if __name__ == "__main__":
    s = Solution()
    print s.multiply('1234','5678')
    
