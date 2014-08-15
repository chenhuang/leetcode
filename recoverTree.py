#! /usr/bin/python
'''
Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
'''

# Observations: 
# 1. In-order traversal and then identify the two elements, then switch 
# 2. after the swap, one key observation is that each element will either be larger than it's next successor, or will be smaller than it's previous' precedetor. 

import os
import re
import sys

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        if root == None: return None
        self.prev = None
        self.nodes = []
        self.inOrderTraversal(root)
    
        self.swap(self.nodes[0], self.nodes[1])

    def swap(self, node1, node2):
        tmp  = node1.val
        node1.val = node2.val
        node2.val = tmp

    def inOrderTraversal(self,node):
        if node.left != None:
            self.inOrderTraversal(node.left)

        if self.prev == None:
            self.prev = node
        else:
            if self.prev.val > node.val:
                if len(self.nodes) == 0:
                    self.nodes.append(self.prev)
                else:
                    self.nodes.append(node)
            self.prev = node

        if node.right != None:
            self.inOrderTraversal(node.right)
        
