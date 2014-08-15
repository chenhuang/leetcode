#! /usr/bin/env python

'''
Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

https://oj.leetcode.com/problems/balanced-binary-tree/
'''

# Observations:
# 1. Tree problems can be solved in recursion in general
# 2. Subtrees to every node: requires to compute depth for each sub-tree then compare the results
# 3. D&C: a. identify tree branch depth. b. compare branch depth differences. 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root == None: return True

        self.isBalancedFlag = True
        self.isBalancedCheck(root)
        return self.isBalancedFlag


    def isBalancedCheck(self, roots):
        if root == None: return 0
        left_depth = self.isBalancedCheck(root.left) + 1
        right_depth = self.isBalancedCheck(root.right) + 1
    
        if abs(left_depth - right_depth) > 1:
            self.isBalancedFlag = False

        return max(left_depth, right_depth)
            
        
