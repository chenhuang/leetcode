#! /usr/bin/python

'''
Remove Duplicates from Sorted Array 

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].

https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
'''

'''
Remove Duplicates from Sorted List I 

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/
'''

'''
Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

'''

'''
Remove Duplicates from Sorted Array II 

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].

https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
'''

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def removeDuplicates(self,A):
    len_A = len(A)
    if len_A <= 1: return len_A
    i = 0; j = 1
    while j < len_A:
      if A[i] != A[j]:
        i+=1
        if i < j: A[i] = A[j]
      j+=1
    return i+1

  def removeDuplicates_II(self,A):
    len_A = len(A)
    if len_A <= 1: return len_A
    i = 0; j = 1
    while j < len_A:
      if A[i] != A[j]:
        if A[i] == A[i+1]:i+=1
        i+=1
        if i < j: A[i] = A[j]
      j+=1
    return i+1

  def removeDuplicates_list(self,head):
    if head == None or head.next == None:
      return head
    unique = head
    detector = head.next

    while detector != None:
      if unique.val != detector.val:
        unique.next = detector
        unique = unique.next
      detector = detector.next
    unique.next = None
    return head

  def removeDuplicates_list_II(self, head):
    # Corner case:
    if head == None or head.next == None:
      return head
    # Inital three pointers:
    current = head
    prev = ListNode(-1)
    prev.next = current
    prev_head = prev
    detector = current.next

    while detector != None:
      if current.val == detector.val:
        while current.val == detector.val:
          detector = detector.next
        prev.next = detector # Jump over this node
    #    print '- '+str(prev.val), str(detector.val)
      else:
        prev = current
      current = detector
      detector = detector.next
    
    head = prev_head.next
    return head


if __name__ == "__main__":
  s = Solution()
  list_node_values = [1,1,2,2,3,3,4,5]
  l = ListNode(list_node_values[0])
  head = l
  for i in range(1,len(list_node_values)):
    l.next = ListNode(list_node_values[i])
    l = l.next

  l = head
  while l != None:
  #  print l.val
    l = l.next


  l = s.removeDuplicates_list_II(head)
  while l != None:
  #  print l.val
    l = l.next
  #print s.removeDuplicates([1,1,2])
  #print s.removeDuplicates_II([1,1,1,2,2,3])
