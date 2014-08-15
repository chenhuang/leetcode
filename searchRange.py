#! /usr/bin/python

class Solution:
# @param A, a list of integers
# @param target, an integer to be searched
# @return a list of length 2, [index1, index2]
  def searchRange(self, A, target):
    l = self.searchBound(A,target,True)
    if l != -1: u = self.searchBound(A,target,False)
    else: return (-1,-1)
    return (l,u)
        
  def searchBound(self,A,target,is_lower):
    l = 0; u = len(A)-1
    while l <= u:
      k = (l+u)/2
      if A[k] < target:
        l = k + 1
      elif A[k] > target:
        u = k - 1
      elif A[k] == target:
        if is_lower:
          if k == 0: return k
          if A[k-1] < target: return k
          else: u = k - 1
        else:
          if k == len(A)-1:return k
          if A[k+1] > target: return k
          else: l = k + 1

    return -1

if __name__ == "__main__":
  s = Solution()
  print s.searchRange([],10)
