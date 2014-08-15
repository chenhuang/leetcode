#! /usr/bin/env python

'''
Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

https://oj.leetcode.com/problems/longest-consecutive-sequence/
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    # Space for time, also multiple passes? 
    # Two pass: 
    # 1. record all elements in an array
    # 2. expand each element

    def longestConsecutive(self, num):
        num_set = set()
        for i in num:
            num_set.add(i)
        
        max_seq_len = 0
    
        for i in num:
            seq_len = 0
            # expand left:
            j = i
            while j in num_set:
                num_set.remove(j)
                seq_len += 1
                j -= 1

            j = i+1
            while j in num_set:
                num_set.remove(j)
                seq_len += 1 
                j += 1

            max_seq_len = max(max_seq_len,seq_len)

        return max_seq_len


if __name__ == "__main__":
    s = Solution()
    print s.longestConsecutive([100,4,200,1,3,2])
