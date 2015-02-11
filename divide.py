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

    def divide_2(self, divident, divisor):
        result = 0
        while divident > divisor:
            shift_count = 0    
            while divisor << shift_count < divident:
                shift_count += 1
            shift_count -= 1
            result += 1 << shift_count
            divident -= divisor << shift_count

        if divident * 2 > divisor:
            result += 1

        return result

    def divide_3(self, divident, divisor):
        left = divident/divisor
        right = divident%divisor
        right_output = ''
        right_mapping = {}  # 1/3 -> 1:3
        while right != 0 and right not in right_mapping.keys():
            left_ = right*10/divisor
            right_ = right*10%divisor
            right_mapping[right] = left_ 
            right_output += str(left_)
            right = right_

        if right_output != '':
            if right == 0:
                return str(left)+'.'+right_output
            else:
                result = str(left)+'.'
                for i in range(len(right_output)):
                    if int(right_output[i]) != right_mapping[right]:
                        result += str(right_output[i])
                    else:
                        result += '('+right_output[i:]+')'
                        break
                return result
        else:
            return str(left)
        
if __name__ == "__main__":
    s = Solution()
    print s.divide(23017917340132413,3)
    print s.divide_2(23017917340132413,3)
    print s.divide_3(1,17)


