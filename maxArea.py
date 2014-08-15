#! /usr/bin/env python

'''
Container With Most Water 

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

https://oj.leetcode.com/problems/container-with-most-water/
'''

# Observations:

class Solution:
    # @return an integer
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        max_area = (j-i)*min(height[i],height[j])

        while i < j:
            if height[i] < height[j]:
                i+=1
            else:
                j-=1

            if max_area < (j-i)*min(height[i],height[j]):
                max_area = (j-i)*min(height[i],height[j])
        
        return max_area
