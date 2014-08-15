'''
Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

https://oj.leetcode.com/problems/path-sum/
'''

'''
Path Sum II 

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
https://oj.leetcode.com/problems/path-sum-ii/
'''

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    # DFS
    def hasPathSum(self, root, sum):
        stack = []
        if root != None:
            stack.append((root,root.val))

        while len(stack) != 0:
            (node,val) = stack.pop()
            if node.left == None and node.right == None and val == sum:
                return True

            if node.left != None:
                stack.append((node.left, val+node.left.val))
            if node.right != None:
                stack.append((node.right,val+node.right.val))

        return False
            
        
    def pathSum(self, root, sum):
        stack = []
        if root != None:
            stack.append((root,root.val,None))

        paths = []

        while len(stack) != 0:
            (node,val,prev_node) = stack.pop()
            if node.left == None and node.right == None and val == sum:
                paths.append([])
                paths[-1].insert(0,node.val)
                while prev_node != None:
                    paths[-1].insert(0,prev_node[0].val)
                    prev_node = prev_node[2]

            if node.left != None:
                stack.append((node.left, val+node.left.val,(node,val,prev_node)))
            if node.right != None:
                stack.append((node.right,val+node.right.val,(node,val,prev_node)))

        return paths
