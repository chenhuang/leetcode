/*
 *Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1􏰀2􏰀3􏰀4, you should return the list as 2􏰀1􏰀4􏰀3.
Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
 *
 * */
public class swap_nodes_in_pairs {
    public ListNode swapPairs(ListNode head) {
        ListNode dummyOdd = new ListNode();
        ListNode dummyEven = new ListNode();
        ListNode cur = head;
        ListNode oddPointer = dummyOdd;
        ListNode evenPointer = dummyEven;
        int isOdd = true;

        while (cur.next) {
            if (isOdd) {
                oddPointer.next = cur;
                oddPointer = oddPointer.next;
            } else {
                evenPointer.next = cur;
                evenPointer = evenPointer.next;
            }

            isOdd = isOdd ^ true;
            cur = cur.next;
        }

        ListNode dummy = ListNode();
        cur = dummy;
        boolean selectEven = true;

        while (dummyOdd && dummyEven) {
            if (selectEven) {
                cur.next = dummyEven;
                dummyEven = dummyEven.next;
            } else {
                cur.next = dummyOdd;
                dummyOdd = dummyOdd.next;
            }

            cur = cur.next;
            selectEven ^= true;
        }

        if (dummyOdd) cur.next = dummyOdd;
        if (dummyEven) cur.next = dummyEven;

        return dummy.next;
    }

    public ListNode swapPairs(ListNode head) {
        ListNode dummyHead = ListNode();
        ListNode tmp;
        ListNode cur = head;
        ListNode dummyCur = dummy;
        boolean isTmp = true;
        
        while (cur) {
            if (isTmp) {
                tmp = cur;
            } else {
                dummyCur.next = cur;
                dummyCur = dummyCur.next;
                dummyCur.next = tmp;
                dummyCur = dummyCur.next;
            }
            cur = cur.next;
            isTmp ^= true;
        }

        if (isTmp) dummyCur.next = tmp;

        return dummyHead.next;
    }
}
