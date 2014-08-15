#! /usr/bin/python
'''
Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

https://oj.leetcode.com/problems/merge-k-sorted-lists/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            i = self.mergeKLists(lists[:len(lists)/2])
            j = self.mergeKLists(lists[len(lists)/2:])
            return self.merge2Lists(i,j)

    # Merge two lists
    def merge2Lists(self, i, j):
        if i == None:
            return j
        if j == None:
            return i
            
        if i.val < j.val:
            head=i
            i = i.next
        else:
            head=j
            j = j.next
        
        k = head
        while i != None and j != None:
            if i.val > j.val:
                k.next = j
                k = k.next
                j = j.next
            else:
                k.next = i
                k = k.next
                i = i.next

        while i != None:
            k.next = i
            k = k.next
            i = i.next
            
        while j != None:
            k.next = j
            k = k.next
            j = j.next
            
        return head 
    
