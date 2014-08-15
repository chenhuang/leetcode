#! /usr/bin/env python

'''
Leetcode: 3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ? b ? c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},
    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
http://leetcode.com/2010/04/finding-all-unique-triplets-that-sums.html
'''

def three_sum(s):
	s = sorted(s)
	output = set()
	for i in range(len(s)):
		target = 0 - s[i]
		j = i + 1
		k = len(s) - 1
		while j < k:
			sum_two = s[j] + s[k]
			if sum_two > target:
				k -= 1
			elif sum_two < target:
				j += 1
			else:
				output.add((s[i],s[j],s[k]))
				j += 1
				k -= 1
	return output

if __name__ == '__main__':
    print three_sum([-1, 0, 1, 2, -1, -4])
    #for p in k_sum([1, 0, -1, 0, -2, 2, 3, 5, -3], 4, 0): print p
    #print two_sum([2, 7, 11, 15, 3], 13)

