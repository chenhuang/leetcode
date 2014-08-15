#! /usr/bin/env python

'''
Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        node_index = {}
        for i in range(len(inorder)):
            node_index[inorder[i]] = i

        return self.buildTreeRecur(node_index, preorder, inorder, 0, len(preorder)-1, 0)
            
        
    def buildTreeRecur(self, node_index, preorder, inorder, in_start, in_end, pre_start):
        if in_start > in_end:
            return None

        # identify root
        current = TreeNode(preorder[pre_start])

        i = node_index[preorder[pre_start]]
        current.left = self.buildTreeRecur(node_index, preorder,inorder,in_start,i-1,pre_start+1)
        current.right = self.buildTreeRecur(node_index, preorder,inorder,i+1,in_end,pre_start+1-(in_start-i))

        return current

    def buildTree(self, inorder, postorder):
        node_index = {}
        for i in range(len(inorder)):
            node_index[inorder[i]] = i

        return self.buildTreeInPostOrder(node_index, inorder, postorder, 0, len(postorder)-1, len(postorder)-1)

    def buildTreeInPostOrder(self, node_index, inorder, postorder, in_start, in_end, post_end):
        if in_start > in_end:
            return None
        
        current = TreeNode(postorder[post_end])
        i = node_index[postorder[post_end]]
        current.left = self.buildTreeInPostOrder(node_index, inorder, postorder, in_start, i-1, post_end - (in_end - i) - 1)
        current.right = self.buildTreeInPostOrder(node_index, inorder, postorder, i+1, in_end, post_end-1)

        return current  
