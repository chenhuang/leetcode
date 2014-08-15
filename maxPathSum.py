#! /usr/bin/env python

'''
Binary Tree Maximum Path Sum 

Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 
# Observations: 
# 1. for each node, compute the max left and max right
# 2. select the max (left+right)
# 3. Traverse the tree with post-order traversal

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.max_path_sum = 0
        self.node_weights = {}
        self.maxPathSumRec(root) 
        return self.max_path_sum

    def maxPathSumRec(self, root):

        if root is None: return None
        if root.left: self.maxPathSumRec(root.left)
        if root.right: self.maxPathSumRec(root.right)

        if root.left is None and root.right is None:
            self.node_weights[root] = (0,0)
        else:
            if root.left is None:    
                self.node_weights[root] = (0,max(self.node_weights[root.right])+root.right.val)
            elif root.right is None:
                self.node_weights[root] = (max(self.node_weights[root.left])+root.left.val,0)
            else:
                self.node_weights[root] = (max(self.node_weights[root.left])+root.left.val,max(self.node_weights[root.right])+root.right.val)

            if self.node_weights[root][0] + self.node_weights[root][1] + root.val > self.max_path_sum:
                self.max_path_sum = self.node_weights[root][0] + self.node_weights[root][1] + root.val 

    def maxPathSum(self,root):
        if root == None: return 0
        self.max = root.val
        
        self.findMax(root)
        return self.max

    def findMax(self,node):
        if node is None:
            return 0
        
        left = max(self.findMax(node.left),0)
        right = max(self.findMax(node.right),0)

        self.max = max(node.val+left+right,self.max)

        return node.val+max(left,right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    s = Solution()
    print s.maxPathSum(root)


