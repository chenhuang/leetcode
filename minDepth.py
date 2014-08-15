#! /usr/bin/env python

'''
Minimum Depth of Binary Tree 

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Observations:
# 1. BFS, seems obvious. 

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None: return 0
        queue = []
        queue.insert(0,(root,1))

        while len(queue) > 0:
            node,level = queue.pop()
            if node.left is None and node.right is None: 
                return level
            else:
                if node.left is not None:
                    queue.insert(0,(node.left,level+1))
                if node.right is not None:
                    queue.insert(0,(node.right,level+1))

            
            
            
        
