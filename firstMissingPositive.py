#! /usr/bin/python

'''

First Missing Positive

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

https://oj.leetcode.com/problems/first-missing-positive/

'''

class Solution:
# @param A, a list of integers
# @return an integer
  def firstMissingPositive(self, A):
    max = 0

    for i in A:
      if i > max:
        max = i

    if max == 0: return 1
    
    for i in A:
      if i < max and i > 0:
        max = i-1
    
    if max == 0: return 1
    else: return max
        

if __name__ == "__main__":
  s = Solution()
  print s.firstMissingPositive([1,2,0])
  print s.firstMissingPositive([3,4,-1,1])
        
