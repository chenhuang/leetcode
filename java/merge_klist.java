public class Solution {

    private Comparator<ListNode> ListNodeComparator = new Comparator<ListNode>() {
        private int compare(ListNode left, ListNode right) {
            if (left == null) {
                return 1;
            } else if (right == null) {
                return -1;
            }

            return left.val - right.val;
        }
    };
    

}
