#! /usr/bin/python

'''
Permutations II 

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

https://oj.leetcode.com/problems/permutations-ii/
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        self.output = []
        self.permuteUniqueRec(num,0)
    
        return self.output
        
    def permuteUniqueRec(self, num, start):
        if start == len(num):
            #if num not in self.output:
            self.output.append(num)
        else:
            for i in range(start, len(num)):
                a=num[start]
                b=num[i]
                num[start] = b
                num[i] = a

                if i > start and a == b:
                    continue 
                self.permuteUniqueRec(list(num), start+1)
    
                num[start] = a
                num[i] = b

    def permuteUnique(self, nums):
        solutions = [[]]
        for num in nums:
            next = []
            for solution in solutions:
                for i in range(len(solution) + 1):
                    candidate = solution[:i] + [num] + solution[i:]
                    if candidate not in next:
                        next.append(candidate)
            solutions = next
        return solutions


if __name__ == "__main__":
    s = Solution()
    print s.permuteUnique([1,1,2])
            
