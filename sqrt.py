#! /usr/bin/python

'''
Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.

https://oj.leetcode.com/problems/sqrtx/
'''

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        shift_count = 0
        y = x
        
        while 2 ** shift_count < y:
            y = y >> 1
            shift_count += 1

        for i in range(2**(shift_count-1),2**shift_count):
            if i * i == x:
                return i
        return None

if __name__ == "__main__":
    s = Solution()
    print s.sqrt(65025)


