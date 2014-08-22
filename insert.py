#! /usr/bin/env python

'''
Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

https://oj.leetcode.com/problems/insert-interval/
'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert_1(self, intervals, newInterval):
        stack = []
        for i in intervals:
            if i.start > newInterval.end:
                stack.append(newInterval)
                newInterval = i
            elif (newInterval.start >= i.start and newInterval.start <= i.end) or (i.start >= newInterval.start and i.start <= newInterval.end):
                newInterval.start = min(newInterval.start, i.start)
                newInterval.end = max(newInterval.end, i.end)
            else:
                stack.append(i)
                
        stack.append(newInterval)

        return stack

    def insert(self, intervals, newInterval):
        stack = []
        for i in intervals:
            if i[0] > newInterval[1]:
                stack.append(newInterval)
                newInterval = i
            elif (newInterval[0] > i[0] and newInterval[0] < i[1]) or (i[0] > newInterval[0] and i[0]< newInterval[1]):
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])
            else:
                stack.append(i)
                
        stack.append(newInterval)

        return stack

if __name__ == "__main__":
    s = Solution()

    print s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,9])
    print s.insert([[1,3],[6,9]],[2,5])
