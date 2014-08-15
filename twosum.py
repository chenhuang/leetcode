
'''
Two Sum 

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

https://oj.leetcode.com/problems/two-sum/
'''


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        target_num = {}
        for i in range(len(num)):
            if num[i] in target_num.keys():
                return (target_num[num[i]]+1,i+1)
            else:
                target_num[target-num[i]] = i
            


    def twoSum_1(num, target):
      num_pos = {}
      for i in range(len(num)):
        if target-num[i] in num_pos.keys():
          return (num_pos[target-num[i]]+1, i+1)
        num_pos[num[i]] = i

s = Solution()
print s.twoSum([3,2,4],6)

