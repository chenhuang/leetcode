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
    def reverseBetween1(self, head, m, n):
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

    def reverseBetween(self, head, m, n):
        dummy = ListNode(0, head)
        pre = dummy
        cur = head
        
        for i in range(m-1):
            pre = cur
            cur = cur.next
        
        next_ = cur.next
        for i in range(n - m):
            tmp = next_.next
            next_.next = cur
            cur = next_
            next_ = tmp
        
        pre.next.next = next_
        pre.next = cur
        
        return dummy.next

    def printList(self, head):
        while head is not None:
            print head.val
            head = head.next
     
if __name__ == "__main__":
    s = Solution()
    
    head = s.reverseBetween(ListNode(3,ListNode(5,ListNode(6, None))),1,2) 
    
    if 0:
        while head != None:
            print head.val
            head = head.next

