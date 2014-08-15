#! /usr/bin/env python

'''
Leetcode: 3Sum

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    http://www.programcreek.com/2013/02/leetcode-3sum-closest-java/
'''

def three_sum_closest(s, target):
	s = sorted(s)
	min_distance = s[0]+s[1]+s[2]
	output = ()

	for i in range(len(s)):
		target = 0 - s[i]
		j = i + 1
		k = len(s) - 1
		while j < k:
			sum_two = s[j] + s[k]
			if abs(target-sum_two) < min_distance:
				min_distance = sum_two
				output = (s[i],s[j],s[k])
				
			if sum_two > target:
				k -= 1
			elif sum_two < target:
				j += 1
			else:
				min_distance = 0
				output = (s[i],s[j],s[k])
				return output
				j += 1
				k -= 1
	return output

if __name__ == '__main__':
    print three_sum_closest([-1, 0, 1, 2, -1, -4],0)
    #for p in k_sum([1, 0, -1, 0, -2, 2, 3, 5, -3], 4, 0): print p
    #print two_sum([2, 7, 11, 15, 3], 13)

