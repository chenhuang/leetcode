#! /usr/bin/env python
'''
Maximum Subarray

Given an array of integers, find a contiguous subarray which has the largest sum.

Note
The subarray should contain at least one number

Example
For example, given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

Maximum Subarray II

Fair Maximum Subarray II

18% Accepted
Given an array of integers, find two non-overlapping subarrays which have the largest sum.

The number in each subarray should be contiguous.

Return the largest sum.

Note
The subarray should contain at least one number

Example
For given [1, 3, -1, 2, -1, 2], the two subarrays are [1, 3] and [2, -1, -2] or [1, 3, -1, 2] and [2], they both have the largest sum 7.
'''

import os
import re
import sys

class solution:
    def max_subarray(self, nums):
        # Naive solution: O(n^2): iterate through all possible sub arraies. 
        # Better: many subproblems: sum[i][j] = sum[i][j-1]+num[j]
        # sum[0][n]: max sum from 0 to n = max(sum[0][n-1]+num[n-1], sum[0][n-1])
        # pre-processing: a[i] = sum(num[0] to num[i])
        # then the problem would become: find max(a[j]-a[i]): stock market price problem. 

    def max_subarray_ii(self, nums):
        # Based on solution of max_subarray, preprocessing nums such that:
        # a[i] = sum(sum[0] to sum[i])
        # b[i]: max (a[i]-a[0])
        # c[i]: max (a[n]-a[i])

    def max_subarray_iii(self, nums):
        # DP:
        # A[n][k]: max sum from nums[0] to nums[i]
        # A[n][k] = max(A[i][k-1], max_subarray(i,n))
