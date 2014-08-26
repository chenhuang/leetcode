#! /usr/bin/env python

import sys

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
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup_1(self, head, k):
        if head is None or k == 1: return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        i = 0

        while head is not None:
            i += 1
            if i%k == 0:
                pre = self.reverseRange(pre, head.next)
                head = pre.next
            else:
                head = head.next

        return dummy.next


    # Reverse the linked list from head to tail, return tail as the head. 
    def reverseRange(self, start, tail):
            last = start.next
            cur = last.next

            while cur is not None:
                last.next = cur.next
                cur.next = start.next
                start.next = cur
                cur = last.next

            return last

    def reverseLinkedList(self, head):
        prev = None
        current = head  

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev

    def reverseKGroup(self, head, k):
        current, next, prev = head, None, None

        count = 0
        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.reverseKGroup(next, k)

        return prev
            

        
if __name__ == "__main__":
    s = Solution()

    current = ListNode(0)
    head = current
    for i in range(1,10):
        node = ListNode(i)
        current.next = node
        current = current.next

    current = head
    while current is not None:
        print current.val
        current = current.next
    
    tail = head
    while tail.val != 5:
        tail = tail.next

    current = s.reverseKGroup(head, 3)
    #current = tail
    #s.reverseRange(head, tail)
    print 
    while current is not None:
        print current.val
        current = current.next



