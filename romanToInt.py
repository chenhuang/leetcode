#! /usr/bin/env python

'''
Roman to Integer 

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

https://oj.leetcode.com/problems/roman-to-integer/
'''

class Solution:
    # @return an integer
    def romanToInt(self, s):
        rtoi = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        sum_total = 0
        sum_part = 0 
        i = 0 

        while i < len(s)-1: 
            if rtoi[s[i]] >= rtoi[s[i+1]]:
                sum_total += rtoi[s[i]]-sum_part
                sum_part = 0
            else:
                sum_part += rtoi[s[i]]
            i+=1
        sum_total += rtoi[s[i]]-sum_part
        sum_part = 0

        return sum_total

    def intToRoman(self, num):
        itor = {
            1:'I',
            5:'V',
            10:'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M'
        }

        output = []
        while num > 0:
            while num >= 1000:
                num -= 1000
                output.append('M')
            while num >= 900:
                num -= 900
                output.append('CM')
            while num >= 500:
                num -= 500
                output.append('D')
            while num >= 400:
                num -= 400
                output.append('CD')
            while num >= 100:
                num -= 100
                output.append('C')
            while num >= 90:
                num -= 90
                output.append('XC')
            while num >= 50:
                num -= 50
                output.append('L')
            while num >= 40:
                num -= 40
                output.append('XL')
            while num >= 10:   
                num -= 10
                output.append('X')
            while num >= 9:
                num -= 9
                output.append('IX')
            while num >= 5: 
                num -= 5
                output.append('V')
            if num == 4:
                num -= 4
                output.append('IV')
            if num >= 3:
                num -= 3
                output.append('III')
            if num >= 2:
                num -= 2
                output.append('II')
            if num >= 1:
                num -= 1
                output.append('I')

        return ''.join(output)
                


if __name__ == "__main__":
    s = Solution()
    print s.romanToInt('DCXXI')
    print s.intToRoman(2014)
                
