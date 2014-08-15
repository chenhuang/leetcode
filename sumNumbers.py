#! /usr/bin/env python

'''
Sum Root to Leaf Numbers 

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Observations:
# 1. DFS, record path
# 2. at leaf node, concatenate path into single number
# 3. sum all numbers

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root == None: return 0
        path = []
        return self.sumNumbersRec((root,path))

    def sumNumbersRec(self, root):
        (node,path) = root

        if node == None: return 0
        path.append(str(node.val))
        if node.left is None and node.right is None:
            return int(''.join(path))

        return self.sumNumbersRec((node.left,list(path))) + self.sumNumbersRec((node.right,list(path)))

if __name__ == "__main__":
    s = Solution()
    a=TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)

    print s.sumNumbers(a)
