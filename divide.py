#! /usr/bin/python

'''
Divide Two Integers 

Divide two integers without using multiplication, division and mod operator.

https://oj.leetcode.com/problems/divide-two-integers/
'''

class Solution:
    # @return an integer
    def divide_1(self, dividend, divisor):
        result = 0
        isNegative = False
        if divisor == 0: return 0

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            isNegative = True

        divisor = abs(divisor)
        dividend = abs(dividend)

        while dividend >= divisor:
            dividend -= divisor
            result += 1
        if isNegative:
            return 0-result
        else: return result

    def divide(self, dividend, divisor):
        result = 0
        shift_count = 0
        div = divisor

        while dividend >= divisor:
            div = div << 1
            shift_count += 1

            if div > dividend:
                dividend -= div >> 1
                div = divisor
                result += 2**(shift_count-1)
                shift_count = 0

        return result
        
if __name__ == "__main__":
    s = Solution()
    print s.divide(23017917340132413,3)


