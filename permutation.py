#! /usr/bin/env python

def permutation(ilist,i,output):
    if i < len(ilist)-1:
        a = ilist[i]

        for j in range(i,len(ilist)):
            tmp = ilist[j]
            ilist[j] = a
            ilist[i] = tmp
            new_list = list(ilist)
            permutation(new_list,i+1,output)
            ilist[i] = a
            ilist[j] = tmp
    else:
        print ilist

#NOTE: Wrong code does not work
def permutation_rec_1(prefix,permus):
    permutations = []
    if len(prefix) == 1:
        permutations.append(prefix[0])
    else:
        for i in range(len(prefix)):
            for j in permutation_rec(prefix[0:i]+prefix[i+1:],permus):
                permutations.append(prefix[i]+j)
    return permutations

# Input: string s and t, output: list of strings
# The idea is to divide, and then merge, essentially a D&C scheme
def permutation_rec(s,t):
    output = []
    if len(s) == 0:
        output.append(t)
    else:
        for i in range(len(s)):
            output.extend(permutation_rec(s[:i]+s[i+1:],t+s[i]))
    return output

# The idea is to insert a number into different positions of current arraies.
# The idea is a simulation of insertion into different position approach
def permutation_iter(nums):
    solutions = [[]]
    for num in nums:
        next = []
        for solution in solutions:
            for i in range(len(solution) + 1):
                next.append(solution[:i] + [num] + solution[i:])
        solutions = next

    return solutions

# Uniuqe combinations for the numbers, numbers might be duplicated. 
def permutations_II(nums):
    nums = sorted(nums)

    return permu_rec(nums,[])

def permu_rec(nums, prefix):
    result = []
    if len(nums) == 0:
        result.append(prefix)
    for i in range(len(nums)):
        if i-1>=0 and nums[i] == nums[i-1]:
            continue
        result.extend(permu_rec(nums[:i]+nums[i+1:],prefix+[nums[i]]))

    return result




if __name__ == "__main__":
    #test_list = [1,2,3]
    #output = []
    #permutation(test_list,0,output)
    #print permutation_rec("abc","")
    #print permutation_iter(['a','b','c'])
    nums = [1,1,2]
    print permutations_II(nums)
