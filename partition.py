#! /usr/bin/env python

'''
Partition List 

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

https://oj.leetcode.com/problems/partition-list/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
# @param head, a ListNode
# @param x, an integer
# @return a ListNode
    def partition(self, head, x):
        s = None
        l = None
        shead = None
        lhead = None
        i = head
        while i != None:
            if i.val >= x:
                if lhead == None:
                    lhead = i
                    l = i
                else:
                    l.next = i
                    l = l.next

            if i.val < x:
                if shead == None:
                    shead = i
                    s = i
                else:
                    s.next = i
                    s = s.next
            tmp = i #Detail
            i = i.next
            tmp.next = None #Detail
        if shead != None:
            if lhead != None:
                s.next = lhead
            return shead
        else:
            return lhead

if __name__ == "__main__":
    l = ListNode(2)
    l.next = ListNode(1)

    s = Solution()
    head = s.partition(l,2)
    while head != None:
        print head.val
        head = head.next
