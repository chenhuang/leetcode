'''
Single Number

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

'''
Single Number II 

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

https://oj.leetcode.com/problems/single-number-ii/
'''

class Solution:
# @param A, a list of integer
# @return an integer
# Observations:
# 1. Sort, then search for element that does not appear with neighor: O(nlogn),
# 2. Hash function, O(n)
# 3. without extra memory == in-place replacement of A:
# 4. What can be used? index of the array: 
# 5. j = A[i] % n, swap [i,j]

  def singleNumber(self, A):
    sum = 0
    for i in A:
      sum = i^sum
    
    return sum

  def ten2binary(self,i):
    binary = []

    while i > 0:
      binary.insert(0,i%2)
      i = i / 2

    return binary
      

  def singleNumber_II(self, A):
    sum = [0 for i in range(32)]

    for i in A:
      binary = self.ten2binary(i)
      len_b = len(binary)

      for j in range(32-len_b):
        binary.insert(0,0)
      
      for k in range(32):
        sum[k] += binary[k]
      
    for k in range(32):
      sum[k] = str(sum[k]%3)
    result = ''.join(sum)
    return int(result,2)
      


if __name__ == "__main__":
  s = Solution()
  print s.singleNumber_II([1,2,1,2,1,2,4,4,4,10])


    
