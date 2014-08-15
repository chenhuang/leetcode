#! /usr/bin/env python

'''
Binary Tree Postorder Traversal 

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

https://oj.leetcode.com/problems/binary-tree-postorder-traversal/
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        order_list = []
        if root is None: return []

        stack = []
        stack.append((root,0))

        while len(stack) > 0:
            (node,seen) = stack.pop()
            if seen == 0:
                stack.append((node,1))
                if node.right:
                    stack.append((node.right,0))
                if node.left:
                    stack.append((node.left,0))

            if seen == 1:
                order_list.append(node.val)

        return order_list

                
                
    
