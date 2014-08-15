'''
Binary Tree Preorder Traversal 

    Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

https://oj.leetcode.com/problems/binary-tree-preorder-traversal/
'''

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        order_list = []

        if root is None: return None
        stack = []

        stack.append(root)

        while len(stack) > 0:
            node = stack.pop()
            order_list.append(node)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return order_list
        

