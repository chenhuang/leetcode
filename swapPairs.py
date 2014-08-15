#! /usr/bin/env python

'''
Swap Nodes in Pairs 

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

https://oj.leetcode.com/problems/swap-nodes-in-pairs/
'''

'''
Reverse Nodes in k-Group 

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

https://oj.leetcode.com/problems/reverse-nodes-in-k-group/

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    # Observations: 
    # 1. Keep a prev pointer, 
    # 2. Swap two pointers.
    # 3. Move pointers by 2, corner cases: a. 
    def swapPairs(self, head):
        if head == None or head.next == None: 
            return head
        i = head; j = head.next; prev = ListNode(0); 
        prev.next = i
        head = head.next

        while True:
            prev.next = j
            i.next = j.next
            j.next = i
            prev = i

            i = i.next
            if i == None:
                return head
            j = i.next
            if j == None:
                return head

    # Observation:
    # 1. keep prev, and next
    # 2. reverse within group: use stack? reverse_stack 
    # 
    def reverseKGroup(self, head, k):
        if head == None or head.next == None:
            return head

        i = head
        j = head
        for m in range(k-1):
            j = j.next
            if j == None:
                return head

        head = j
        pre = i
        i = self.reverseByij(i,j)
        j = i

        m = 0
        while j != None:
            j = j.next
            m += 1

            if m == k-1 and j != None:
                pre.next = j
                pre = i
                i = self.reverseByij(i,j)
                j = i
                m = 0

        return head        

    def reverseByij(self,i,j):
        jnext = j.next
        while i != j:
            tmp = j.next
            j.next = i
            i = i.next
            j.next.next = tmp
        return jnext

            
            
