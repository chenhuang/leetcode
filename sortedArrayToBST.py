#! /usr/bin/envo python

'''

Convert Sorted Array to Binary Search Tree 

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

----

Convert Sorted List to Binary Search Tree 

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

'''

# Observations:
# 1. Divide and conquer

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) == 0: return None
        if len(num) == 1: return TreeNode(num[0])
        node = TreeNode(num[len(num)/2])

        node.left = self.sortedArrayToBST(num[0:len(num)/2])
        node.right = self.sortedArrayToBST(num[len(num)/2+1:])
        return node

    # Observations: the obvious solution is to first convert the list into an array, and then apply the above algorithm. 
    # The clever solution is not obvious to understand: in order traversal, needs deep understanding of recursion. 
    # http://www.geeksforgeeks.org/sorted-linked-list-to-balanced-bst/
    # The tricky method is so tricky that I give up on the solution. Here I adopt an easy to understand solution:
    # 1. use slow and fast pointer to find the middle point of a linked list.
    # 2. recursively build left children, and build root and build right children. 
    # 3. 
    def sortedListToBST(self, head):
        if head == None: return None
        if head.next == None: return TreeNode(head.val)
        # Identify mid pointer in a linked list
        mid = self.findMidPoint(head)

        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return root

    def findMidPoint(self, head):
        if head == None or head.next == None: return head
        prev_mid = None

        mid = head
        end = head 

        while end != None:
            end = end.next
            if end != None: 
                end = end.next
                prev = mid
                mid = mid.next

        if prev != None:
            prev.next = None

        return mid
    
        

