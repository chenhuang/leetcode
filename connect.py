'''
Populating Next Right Pointers in Each Node

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    # Obs: looks like a BFS

    def connect(self, root):
        queue = [(root,1)]
        
        while len(queue) > 0:
            (node,lvl) = queue.pop(0)
            if node != None:
                if node.left:
                    queue.append((node.left,lvl+1))
                if node.right:
                    queue.append((node.right,lvl+1))
                if len(queue) > 0 and lvl == queue[0][1]:
                    node.next = queue[0][0]
    
    def connect_II(self, root):
        if not root:
            return 

        # Child's right
        p = root.next
        while p != None:
            if p.left:
                p = p.left  
                break
            elif p.right:
                p = p.right
                break
            else:
                p = p.next
            
        if root.left and root.right:
            root.left.next = root.right
        elif root.right:
            root.right.next = p
        elif root.left:
            root.left.next = p
                
        self.connect_II(root.left)
        self.connect_II(root.right)

    def connect_1(self, root):
        head = None # head of the next level
        prev = None # leading node on the next level
        cur = root  # current node of current level

        while cur is not None:
            while cur is not None: # Iteration the current level
                if cur.left is not None: # Left child
                    if prev is not None:
                        prev.next = cur.left
                    else:
                        head = cur.left
                    prev = cur.left

                if cur.right is not None:
                    if prev is not None:
                        prev.next = cur.right
                    else:
                        head = cur.right
                    prev = cur.right

                cur = cur.next # Move to next node

            # Move to next level
            cur = head
            head = None
            prev = None
        

