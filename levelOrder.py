#! /usr/bin/envo python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        queue = []
        order_list = []
        prev_level = -1
        if root == None: return []

        queue.insert(0,(root,0))

        while len(queue) > 0:
            (node, level) = queue.pop()

            if level > prev_level:
                order_list.append([])
                prev_level = level
            order_list[-1].append(node.val)

            if node.left: queue.insert(0,(node.left,level+1))
            if node.right: queue.insert(0,(node.right,level+1))

        return order_list

