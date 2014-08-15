#! /usr/bin/envo python

'''
Maximum Depth of Binary Tree 

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Observations:
# DFS...keep the max

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None: return 0
        stack = []
        stack.append((root,1))
        max_level = 0

        while len(stack) > 0:
            (node,level) = stack.pop()
            if level > max_level: max_level = level
            if node.left: stack.append((node.left,level+1))
            if node.right: stack.append((node.right,level+1))

        return max_level

            

