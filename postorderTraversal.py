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

    # Instead of pushing and poping nodes, an alternative approach is to trevase along with one current variable, such as: current = current.left
    # Tips of tree traversal or the use of stacks:
    # 1. add more than one node at a time.
    #   e.g. DFS/BFS
    # 2. keep nodes in the stack to be those that are about to put into output list.
    #   e.g. in order, operators
    # 3. keep a prev node.

    def postorderTraversal_1(self, root):
        res, stack, current, prev = [], [], root, None
    
        while stack or current:
            # Not yet reached the end, record the node and explore its left tree
            if current:
                stack.append(current)
                current = current.left
            else:
            # If all left branches are explored, get the parent first
                parent = stack[-1]
            # check if the right leave is empty, or if the right leave has been visited:
                if parent.right in (None, prev):
                    prev = stack.pop()
                    res.append(prev.val)
                else:
                    current = parent.right
        return res

    def post_2(self, root):
        p = root
        stack = []
        output = []

        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                if p.right is None or (len(stack) > 0 and stack[-1].right == p):
                    output.append(p)

'''
                    p = stack.pop()
                    output.append(p)

                    if len(stack) > 0:
                        p = stack.pop()
    # problematic, need to use 
'''
                else:
                    stack.append(p)
                    p = p.right

        return output
                



