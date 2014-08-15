'''
Median of Two Sorted Arrays

There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

https://oj.leetcode.com/problems/median-of-two-sorted-arrays/
'''


class Solution:
# @return a float
# My take, use a similar heuristics as the optimal solution:
# Key observation: for an element A[i], find its order in B: o_b, if i+o_b == median then good, if i+o_b > median_order, means the median should be in the left half of A[i] or left half of B[o_b], if < then the other way around. 
# Compare with the optimal solution:
# 1. Should check with the element in B[median_order-i], reduce the problem into a binary problem as in n-sum problems.
# 2. Coding: redundent code to determine if the element is in A or B, should use: findSorderSorted(A,...,B,) and findOrderSorted(B,...,A,...),  
  def findMedianSortedArrays(self, A, B):
    return self.findOrderSorted(A,-1,len(A),B,-1,len(B),(len(A)+len(B)-2)/2)

  def findOrderSorted(self, A, i1,j1,B,i2,j2,o):
    k = (i1+j1)/2
    if k > i1 and k < j1:
      o_b = self.findOrderOne(B,A[k])
      if k+o_b == o:
        return A[k]
      elif  k+o_b > o:
        return self.findOrderSorted(A,i1,k,B,i2,o_b,o)
      elif k+o_b < o:
        return self.findOrderSorted(A,k,j1,B,o_b,j2,o)
    else:
      k = (i2+j2)/2 
      o_a = self.findOrderOne(A,B[k])
      if k+o_a == o:
        return B[k]
      elif  k+o_a > o:
        return self.findOrderSorted(A,i1,o_a,B,i2,k,o)
      elif k+o_a < o:
        return self.findOrderSorted(A,o_a,j1,B,k,j2,o)
      #self.findOrderSorted(B,i2,j2,A,0,len(A),o)
    
  def findOrderOne(self, A, k):
    i = 0; j = len(A)

    while i < j:
      m = (i+j)/2

      if A[m] == k:
        return m
      elif A[m] > k:
        j = m
      elif A[m] < k:
        i = m+1
    return i
  
  def findMedianSortedArrays_1(self, A, B):
    return self.findMedianSorted(A, B, 0, len(A)-1,(len(A)+len(B))/2)

# This is the MIT Version:
'''
http://www2.myoops.org/course_material/mit/NR/rdonlyres/Electrical-Engineering-and-Computer-Science/6-046JFall-2005/30C68118-E436-4FE3-8C79-6BAFBB07D935/0/ps9sol.pdf

The algorithm itself is easy to understand, however, the implementation is extremely confusing... So I stop at this point. 
'''
  def findMedianSorted(self,A,B,left,right,order):
    if left > right:
      return self.findMedianSorted(B,A,0,len(B)-1,order)

    m = (left+right)/2
    n = order-m-1

    # Recursion ends here
    if A[m] > B[n+1] and n < len(B) - 1:
      return self.findMedianSorted(A,B,left,m-1,order)
    elif A[m] < B[n] and n >= 0:
      return self.findMedianSorted(A,B,m+1,right,order)
    else:
      if order%2 == 1: return A[m]
      elif m > 0: return (A[m]+max(B[n],A[m-1]))/2
      else: return (A[m]+B[n])/2

'''
The third version: start with A_mid and B_mid, if A_mid+B_mid > median_order, then median in left half of max(A_mid,B_mid), exclude right half of max(A_mid,B_mid). 
If A_mid + B_mid < median_order, then median in right half of min(A_mid, B_mid), exclude left half of min(A_mid, B_mid). 
If A_mid + B_mid == median_order, then return (A_mid + B_mid)/2
'''
    
if __name__ == "__main__":
  s = Solution()
  #print s.findOrderOne([3,5,5,5,10,19],1)
  #print s.findMedianSortedArrays([1,3,5,7,9,16], [2,4,6,8,10,11,12,13,14,15])
  print s.findMedianSortedArrays_1([1,3], [2,4,6,8])
  #print s.findMedianSortedArrays([1], [1])
