#! /usr/bin/env python

'''
Binary Tree Inorder Traversal 

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

https://oj.leetcode.com/problems/binary-tree-inorder-traversal/
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root == None: return None

        visit_stack = []
        visit_stack.append(root)

        in_order_list = []

        while len(visit_stack) > 0:
            node = visit_stack.pop()

            # leaf node, put into list
            if node.left == None and node.right == None:
                in_order_list.append(node)

            # check if the node is the next to visit
            # case 1, left child has been visited
            # case 2, right child has been visited
            if len(in_order_list) > 0:
                if node.left == in_order_list[-1]:
                    in_order_list.append(node)
                    continue
            if len(visit_stack) > 0:
                if node.right == visit_stack[-1]:
                    in_order_list.append(node)
                    continue

            # New node
            if node.right != None:
                visit_stack.append(node.right)
                visit_stack.append(node)

                if node.left:
                    visit_stack.append(node.left)
                
                    
        return in_order_list

    def inorderTraversal_1(self, root):
        if root == None: return []

        # to put into visit list
        visit_stack = []

        in_order_list = []

        # node to explore
        node = root

        while len(visit_stack) > 0 or node != None:
            if node == None:
                node = visit_stack.pop()  
                in_order_list.append(node.val)
                if node.right:  
                    node = node.right
                else:
                    node = None
            else:
                if node.left:
                    visit_stack.append(node)
                    node=node.left
                else:
                    in_order_list.append(node.val)
                    if node.right:
                        node = node.right
                    else:      
                        node = None

        return in_order_list

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)

    print s.inorderTraversal_1(root)

        

             
        
        
