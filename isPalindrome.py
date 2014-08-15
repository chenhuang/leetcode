#! /usr/bin/python

'''
Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

https://oj.leetcode.com/problems/palindrome-number/
'''

import re

class Solution:
    # @return a boolean
    # Here no extra space means constant space, does not mean no space at all...
    # Need to clearify such questions in the future.
    def isPalindrome(self, x):
        if x < 0: return False
        div = 1
        while x/div >= 10:
            div *= 10

        while x > 0 and div > 1:
            right = x%10
            left = (x/div)%10
            #print left, right, x, div
            if right != left:
                return False
            x /= 10
            div /= 100

        return True

    def isPalindrome_1(self, x):
        x = re.sub('[^A-Z|a-z|0-9]','',x)
        if x == reversed(x):
            return True
        else return False
        
        

if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome(1200021)
        
