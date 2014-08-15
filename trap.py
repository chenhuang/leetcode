#! /usr/bin/python

import os
import re
import sys

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap_1(self, A):
        left_height = []
        right_height = []
        total_length = len(A)
        
        left_height.append(0)
        right_height.append(0)

        water_count = 0
        for i in range(1,total_length):
            left_height.append(max(left_height[i-1],A[i-1]))
        for i in range(total_length-2, -1, -1):
            right_height.insert(0,max(right_height[0],A[i+1]))
            water = min(left_height[i],right_height[0])-A[i]
            if water > 0:water_count += water
        return water_count

    def trap(self, A):
        if len(A) == 0: return 0
        i = 0;j = len(A)-1
        sum = 0
        left_hi = A[i]
        right_hi = A[j]

        while i < j:
            if left_hi < A[i]:
                left_hi = A[i]
            if right_hi < A[j]:
                right_hi = A[j]

            if A[i] >= A[j]: 
                sum += right_hi - A[j]
                j -= 1
            if A[i] < A[j]:
                sum += left_hi - A[i]
                i += 1
        return sum

if __name__ == "__main__":
    s = Solution()
    print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])

'''
The naive approach:
1. compute the volume for each column. 
2. for each column, identify the left high point and the right high point.
3. accumulate the volume as the min(left_hi, right_hi)
4. rain at each column is determined by the lowest boundary

Optimization, based on observations: 
    if left_hi and right_hi is fixed, then all water inside is easy to compute

    i = 0, j = n, sum = 0
    left_hi = hi[i], right_hi = hi[j]

    while i < j:
        if left_hi < hi[i]:
            left_hi = hi[i]
        if right_hi < hi[j]:
            right_hi = hi[j]

        if hi[i] >= hi[j]: 
            sum += right_hi - hi[j]
            j -= 1
        if hi[i] < hi[j]:
            sum += left-hi - hi[i]
            i += 1

left_hi = 2  
right_hi = 2
hi = 2
hj = 1
sum = 0,0,0,1,1,2,

'''


