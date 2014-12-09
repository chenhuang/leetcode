public class add_two_numbers {
    public ListNode addTwoNumbers(ListNode n1, ListNode n2) {
        boolean add_one = false;
        ListNode result = new ListNode();
        ListNode cur = result.next;

        while (n1 != null && n2 != null) {
            int sum = n1.val + n2.val;
            if (add_one) sum += 1;
            cur = new ListNode();

            if (sum > 9) {
                add_one = true;
                cur.val = sum - 10;
            } else {
                add_one = false;
                cur.val = sum;
            }
            cur = cur.next();
        }

        if (n1 != null) cur = n1;
        if (n2 != null) cur = n2;

        while (cur != null) {
            if (add_one) cur.val += 1;
            if (cur.val < 10) {
                add_one = false;
                cur.next = n1.next;
                return result;
            } else {
                add_one = true;
                cur = cur.next;
            }
        }
        return result.next;
    }

    public ListNode addTwoNumberII(ListNode n1, ListNode n2) {
    // First identify matching position between n1 and n2
    // Recursivly compute 
    }
}
