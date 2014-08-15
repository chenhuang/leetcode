#! /usr/bin/env python

'''
Linked List Cycle 

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

https://oj.leetcode.com/problems/linked-list-cycle/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Observations: 
# 1. Two pointers are a very common strategy to use in cycle
# 2. Two pointers, one fast one slow, if they catch up then it's a cycle
# 3. 

class Solution:
# @param head, a ListNode
# @return a boolean
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        slow = head
        fast = head

        while True:
            fast = fast.next

            if fast == None: 
                return False
            fast = fast.next
            if fast == None:
                return False

            slow = slow.next

            if fast == slow:
                return True

        return False
        
