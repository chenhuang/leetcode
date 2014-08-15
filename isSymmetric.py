#! /usr/bin/envo python

'''
Symmetric Tree 

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Observations:
# 1. Symmetric tree means left hand == right hand
# 2. One approach is to traverse the tree in BFS and detecet duplicated patterns. 
# 3. D&C or 

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None: return True
        return self.detectSymmetric(root.left, root.right)
        
    def detectSymmetric(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None or left.val != right.val:
            return False

        return self.detectSymmetric(left.right, right.left) and self.detectSymmetric(left.left,right.right)

