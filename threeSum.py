#! /usr/bin/python

'''
3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

https://oj.leetcode.com/problems/3sum/

3Sum Closest 

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num = sorted(num)
        index = {}
    
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                key = 0-num[i]-num[j]
                if key not in index.keys():
                    index[key] = [[num[i],num[j]]]
                else:
                    index[key].append([num[i],num[j]])

        solutions = []
        for i in range(len(num)):
            if num[i] in index.keys():
                tuples = index[num[i]]
                for t in tuples:
                    if num[i] > max(t):
                        solution = t+[num[i]]
                        if solution not in solutions:
                            solutions.append(solution)

        return solutions

    def threeSumClosest(self, num, target):
        num = sorted(num)
        min_dis = abs(target-num[0]-num[1]-num[2])
        min_sum = num[0]+num[1]+num[2]

        for i in range(len(num)):
            target_num = target-num[i]
            j,k = i+1, len(num)-1
            while j < k:
                if num[j]+num[k]>target_num:
                    dis = abs(target_num-num[j]-num[k])
                    if dis < min_dis:
                        min_dis = dis
                        min_sum = num[i]+num[j]+num[k]
                        print num[i],num[j],num[k]
                    k -= 1
                elif num[j]+num[k]==target_num:
                    return target
                else:
                    dis = abs(target_num-num[j]-num[k])
                    if dis < min_dis:
                        min_dis = dis
                        min_sum = num[i]+num[j]+num[k]
                        print num[i],num[j],num[k]
                    j+=1

        return min_sum

    

if __name__ == "__main__":
    s = Solution()
    print s.threeSum([-1,0,1,2,-1,-4])
    print s.threeSumClosest([-3,-2,-5,3,-4], -1)

