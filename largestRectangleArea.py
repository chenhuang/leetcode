#! /usr/bin/env python
'''
Largest Rectangle in Histogram 

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.

https://oj.leetcode.com/problems/largest-rectangle-in-histogram/
'''

# Observations:
# 1. Looks like a DP problem:
# 2. Sub problem: [start, length], value is not total space but min length in the span
# 3. construction of a problem from subproblems: [s,l] = min([s,l-1],[s+l-1,1])

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea_2(self, height):
        min_heights = []
        height_len = len(height)
        max_space = 0

        for i in range(height_len):
            min_height = height[i]
            for j in range(i, height_len):
                min_height = min(height[j],min_height)
                max_space = max(max_space,min_height*(j-i+1))

        return max_space

    def largestRectangleArea_1(self, height):
        min_heights = []
        height_len = len(height)
        max_space = 0
        for i in range(height_len):
            min_heights.append([0 for j in range(height_len-i)])
            min_heights[i][0] = height[i]

        for i in range(height_len):
            for j in range(1,height_len-i):
                min_heights[i][j]=min(min_heights[i][j-1],min_heights[i+j][0])
                current_space = min_heights[i][j] * (j+1)
                if max_space < current_space:
                    max_space = current_space

        return max_space



    def largestRectangleArea_3(self, height):
        S = {}
        # left --> right
        stack = []
        for i in xrange(len(height)):
            while stack:
                if height[i] < height[stack[-1]]:
                    start_i = stack.pop()
                    S[start_i] = height[start_i] * (i-1-start_i)
                else:
                    break
            stack.append(i)

        while stack:
            start_i = stack.pop()
            S[start_i] = height[start_i] * (len(height)-1-start_i)
        
        # left --> right
        stack = []
        for i in reversed(xrange(len(height))):
            while stack:
                if height[i] < height[stack[-1]]:
                    start_i = stack.pop()
                    S[start_i] += height[start_i] * (start_i-i-1)
                else:
                    break
            stack.append(i)
        while stack:
            start_i = stack.pop()
            S[start_i] += height[start_i] * start_i
        print S
        return max(S.values())

    def largestRectangleArea(self, height):
        # The "increasing" stack stores the index of heights
        increasing, area, i = [], 0, 0
        while i <= len(height):
            # when height[i] is larger than previous height, add the height into stack
            if len(increasing) == 0 or (i < len(height) and height[i] > height[increasing[-1]]):
                increasing.append(i)
                i += 1
            # when height[i] is smaller than previous height, identify the largetst area. i is current position, increasing[-1] is current stack head, why?  
            else:
                last = increasing.pop()
                if len(increasing) == 0:
                    area = max(area, height[last] * i)
                else:
                    area = max(area, height[last] * (i - increasing[-1] - 1))
        return area
              

        
if __name__ == "__main__":
    s = Solution()
    print s.largestRectangleArea([2,1,5,6,2,3])
