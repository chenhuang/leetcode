#! /usr/bin/envo python

'''
Validate Binary Search Tree 

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

https://oj.leetcode.com/problems/validate-binary-search-tree/
'''

import os
import sys
import re

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Observations:
# 1. Tree traverse with checking rules included. 
# 2. Can be either recursive or iterative. 
# 3. Go with DFS and make sure all subtrees have values with less. 
# 4. Right nodes of the left hand side are less than parent nodes. Left nodes of the right hand side are more than parent nodes. 
# 5. Since parent nodes of the left hand side are decreasing in value, need to make sure that the right child is less than that of the smallest value of the left tree. 
# 6. Since parent nodes of the right hand side are increasing in value, need to make sure that the left child of each node is large thant the smallest value of the right tree. 
# 7. Left tree: right child less than parent's all parents. Right tree: left child larger than parent's all parents.  
# 8. left tree's parent's parents have increaing value, so keep the smallest parent's parents' value should be sufficient. 
# 9. Right tree's parent's parents have decreasing value, the same. 
# 10. 

class Solution:
    # @param root, a tree node
    # @return a boolean
    # This is the incorrect solution: 
    def isValidBST(self, root): 
        if not root.left and not root.right:
            return True
        
        left_valid = right_valid = False
        
        if root.left:
            print root.left.value, '<=', root.value
            if root.left.value <= root.value:
                left_valid = valid_BST(root.left)
        
        if root.right:
            print root.value, '<=', root.right.value
            if root.right.value >= root.value:
                right_valid = valid_BST(root.right)
        
        return left_valid and right_valid

    # In-order traverse, and identify if it's an increasing sequence
    def isValidBST(self, root):
        if root == None: return True

        # to put into visit list
        visit_stack = []

        in_order_list = []

        # node to explore
        node = root

        while len(visit_stack) > 0 or node != None:
            if node == None:
                node = visit_stack.pop()  
                in_order_list.append(node.val)
                if node.right:  
                    node = node.right
                else:
                    node = None
            else:
                if node.left:
                    visit_stack.append(node)
                    node=node.left
                else:
                    in_order_list.append(node.val)
                    if node.right:
                        node = node.right
                    else:      
                        node = None

        for i in range(len(in_order_list)-1):
            if in_order_list[i] >= in_order_list[i+1]:
                return False
        return True

    # validate by recursion, based on observations
    def isValidBST(self, root):
        return self.verifyBST(root,-2147483647,2147483647)
        
    def verifyBST(self, node, MIN, MAX):
        if node == None: return True
        if node.val <= MIN or node.val >= MAX:
            return False
        return self.verifyBST(node.left, MIN, node.val) and self.verifyBST(node.right,node.val,MAX)
        

