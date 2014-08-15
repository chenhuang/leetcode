#! /usr/bin/python

'''
[LeetCode] Combination Sum, Solution

Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    # Looks like a DFS problem, use recursion should be fine.
    def combinationSum(self, candidates, target):
        self.output = []
        self.combinationSumRec(candidates, target, [], 0)

        return self.output

    def combinationSumRec(self, candidates, target, records, start):
        if target == 0:
            if records not in self.output:
                self.output.append(records)
        elif target > 0:
            for i in range(start, len(candidates)):
                self.combinationSumRec(candidates, target-candidates[i], records+[candidates[i]], i)

if __name__ == "__main__":
    s = Solution()
    print s.combinationSum([2,3,6,7], 7)

