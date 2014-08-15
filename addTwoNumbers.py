#! /usr/bin/python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
# @return a ListNode
  def addTwoNumbers(self, l1, l2):
    i = 0
    result = []
    larger_than_10 = 0
    while i < len(l1) or i < len(l2):
      if i >= len(l1):
        sum = l2[i]+larger_than_10
      elif i >= len(l2):
        sum = l1[i]+larger_than_10
      else:
        sum = l1[i]+l2[i]+larger_than_10

      if sum >= 10:
        sum = sum - 10
        larger_than_10 = 1
      else:
        larger_than_10 = 0

      result.append(sum)
      i += 1
    return result

if __name__ == "__main__":
  s = Solution()
  print s.addTwoNumbers([2,4,3],[5,6,4])
      
