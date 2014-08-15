#! /usr/bin/env python

'''
Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

https://oj.leetcode.com/problems/decode-ways/
'''

class Solution:
    # @param s, a string
    # @return an integer
    # DFS/BFS 
    def numDecodings(self, s):
        coding = {}
        for i in range(1,27):
            coding[i] = 'C'+str(i)

        queue = []
        queue.insert(0,(s,''))
        count = 0
        while len(queue) > 0:
            (left,right) = queue.pop()
            if len(left) > 1:
                if int(left[0:2]) in coding.keys():
                    queue.insert(0,(left[2:],coding[int(left[0:2])]+right))
            if len(left) > 0:
                if int(left[0]) in coding.keys():
                    queue.insert(0,(left[1:],coding[int(left[0])]+right))
            if len(left) == 0:
                count += 1

        return count

if __name__ == "__main__":
    s = Solution()
    print s.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
        
            
        
