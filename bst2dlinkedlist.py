#! /usr/bin/python

class Solution:
    def __init__(self):
        pass
        self.dummy = ListNode()
        self.cur = None
        
    def bst2ll(self, node):
        if node is None:
            return 

        self.bst2ll(node.left)
        if self.cur is None:
            self.cur = node
            self.dummy.next = self.cur
        else:
            self.cur.next = node
            node.pre = self.cur
            self.cur = self.cur.next
        self.bst2ll(node.right)
            
