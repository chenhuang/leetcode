#! /usr/bin/env python


# Definition for singly-linked list.
class ListNode:
    def __init__(self,x,y):
        self.val = x
        self.next = y

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if head == None or head.next == None: return head
        if m == n: return head
        
        newhead = ListNode(0, None)
        newhead.next = head
        pre = newhead
        for i in range(m-1):
            pre = pre.next
        start = pre.next
        
        end = newhead
        for i in range(n):
            end = end.next
            
        while start != end:
            tmp1 = end.next
            end.next = start
            tmp2 = start.next
            start.next = tmp1
            start = tmp2
        pre.next = end
            
        return newhead.next 
     
if __name__ == "__main__":
    s = Solution()
    head = s.reverseBetween(ListNode(3,ListNode(5,None)),1,2) 
    
    while head != None:
        print head.val
        head = head.next

