#! /usr/bin/env python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# This is a verg elegant solution that helps to understand recursion, it's a double recursion with nested loops. 


class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.generateTreeRange(1,n)
    
    # generate trees from i to j
    def generateTreeRange(self, i, j):
        # stop creteria
        if i > j: return [None]
        if i == j: return [TreeNode(i)]
        
        heads = []
        for k in range(i,j+1):
            for m in self.generateTreeRange(i,k-1):
                for n in self.generateTreeRange(k+1,j):
                    head = TreeNode(k)
                    head.left = m
                    head.right = n
                    heads.append(head)
        return heads

    def generateTrees_Rec(self,i,j):
        nodes = []

        if i > j:
            nodes.append(None)
        if i == j:
            nodes.append(TreeNode(i))
        else:
            for k in range(i,j+1):
                for l in self.generateTrees_Rec(i,k-1):
                    for j in self.generateTrees_Rec(k+1,j):
                        head = TreeNode(k)
                        k.left = l
                        k.right = j
                        nodes.append(k)

        return nodes

