#! /usr/bin/envo python

'''
Binary Tree Zigzag Level Order Traversal 

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        queue = []
        order_list = []
        prev_level = -1
        if root == None: return []

        queue.insert(0,(root,0))

        while len(queue) > 0:
            (node, level) = queue.pop()

            if level > prev_level:
                order_list.append([])
                order_list[-1].append(node.val)
                prev_level = level
            else:
                if level%2 == 0:
                    order_list[-1].append(node.val)
                else:
                    order_list[-1].insert(0,node.val)

            if node.left: queue.insert(0,(node.left,level+1))
            if node.right: queue.insert(0,(node.right,level+1))

        return order_list
            


