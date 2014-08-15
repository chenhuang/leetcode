#! /usr/bin/python
# -*- coding: utf-8 -*-

'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
# Recursion works in-place, but keepng recursion takes extra space so it's not a in-place algorithm.
    def reorderList(self, head):
        if head == None or head.next == None:
            return
        else:
            tail = head.next
            pre_tail = head
            if tail.next == None:
                return
            else:
                while tail.next:
                    pre_tail = tail
                    tail = tail.next
                tail.next = head.next
                head.next = tail
                pre_tail.next = None
                self.reorderList(head.next.next)
       
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

Solution().reorderList(head)

if 1:
  while head:
    print head.val
    head = head.next
