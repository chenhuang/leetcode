public class binary_tree_max_path_sum {
    private int maxSum
    public int maxPathSum(TreeNode root) {
        maxSum = Integer.MIN_VALUE;
        findMax(root);
        return maxSum;
    }

    // This actually finds max branchafter TreeNode p
    // pretty good idea compared with my idea of storing branch value of nodes, takes more space, this only uses constant space. 
    private int findMax(TreeNode p) {
        // leaf node returns 0
        if (p ==null) return 0;
        
        // return left tree largest branch
        int left = findMax(p.left);
        
        // return right tree largest branch
        int right = findMax(p.right);

        // compare max tree sum with the current max.
        maxSum = Math.max(p.val + left + right, maxSum);
        
        // compute branch max.
        int ret = p.val + Math.max(left, right);
        return ret > 0 ? ret : 0;
    }
}
