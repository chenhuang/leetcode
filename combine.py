#! /usr/bin/python

'''
Combinations 

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

https://oj.leetcode.com/problems/combinations/
'''

# Choose k out of n:
class Solution:
    # @return a list of lists of integers
    def combine_1(self, n, k):
        if k == 0: return []
        queue = []
        for i in range(1,n+1):
            queue.insert(0,[i])
    
        for i in range(k-1):
            next = []
            while len(queue) > 0:
                num_list = queue.pop()
                for j in range(num_list[-1]+1, n+1):
                    next.insert(0,num_list+[j])
            queue.extend(next)

        return queue

    def combine(self, n, k):
        return self.combine_rec(1,n,[],k)

    def combine_rec(self, start, end, current_comb,k):
        result = []
        if k == 0:
            result.append(current_comb)
        for i in range(start,end+1):
            result.extend(self.combine_rec(i+1,end,current_comb+[i],k-1))

        return result
        


if __name__ == "__main__":
    s = Solution()
    print s.combine(4,3)
    #print s.combine_1(4,2)
        
