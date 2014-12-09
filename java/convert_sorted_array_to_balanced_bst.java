public class convert_sorted_array_to_balanced_bst {
    public TreeNode array2BST(int[] nums) {
        return array2BST(nums, 0, nums.length);
    }

    private TreeNode array2BST(int[] nums, int start, int end) {
        if (start > end) return null;

        int mid = start + (end-start)/2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = convert_sorted_array_to_balanced_bst(nums,start, mid-1);
        root.right = convert_sorted_array_to_balanced_bst(nums,mid+1, end);
        return root;
    }

    public TreeNode list2BST(ListNode head) {
        int length = 0;
        ListNode cur = head;
        while (cur != null) {
           cur = cur.next; 
           length++;
        }

        return list2BST(head,length);

    }

    public TreeNode list2BST(ListNode head, int length) {
        if (length < 1) {
            return null;
        }

        ListNode cur = head;
        int mid = length/2;
        for (int i = 0; i < mid; i++) {
            cur = cur.next;
        }

        TreeNode root = new TreeNode(cur.val);
        root.left = list2BST(head, mid-1);
        root.right = list2BST(root.next, length - mid);
    }

}
