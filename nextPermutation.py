#! /usr/bin/env python

'''
Next Permutation 

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

https://oj.leetcode.com/problems/next-permutation/
'''

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        # Identify the cross line between increaing and decreasing sequence
        num_str = str(num)
        len_num = len(num_str)
        if len_num < 2: return num
        i,j=0,len_num-1
        while num_str[i]<num_str[i+1]:
            i+=1
        while num_str[j]>num_str[j-1]:
            j-=1

        # Swap 
        
        

    def swap(self,num,i,j):
        num_str = str(num)
        lo = min(i,j)
        hi = max(i,j)
        num_str = ''.join(num_str[:lo])+num_str[hi]+''.join(num_str[lo+1:hi])+num_str[lo]+''.join(num_str[hi+1:])

        return num_str
    
if __name__ == "__main__":
    s = Solution()

