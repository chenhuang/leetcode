#! /usr/bin/python

'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  # @param head, a ListNode
  # @return a list node
  # Detect cycle
  def detectCycle(self, head):
      slow = head
      fast = head 
      if slow == None:return None
      if slow.next == None:return None

      while True:
          if fast == None:return None
          if fast.next == None:return None
          fast = fast.next.next
          slow = slow.next
          
          if fast == slow:
              slow_1 = head
              while slow_1 != slow:
                  slow_1 = slow_1.next
                  slow = slow.next
              return slow

  # Has cycle
  def hasCycle(self, head):
      slow = head
      fast = head 

      if slow == None:
          return False
      if slow.next == None:
          return False
  
      while True:
          if fast == None:
              return False
          if fast.next == None:
              return False

          fast = fast.next.next
          slow = slow.next

          if fast == slow:
              return True
      

