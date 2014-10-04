public class lowest_common_ancestor {
    // Divide and conquer
    // Search left tree, then right tree, if the node is found, return the node.
    public TreeNode LCA(TreeNode n1, TreeNode n2, TreeNode root) {
        if (root == null || root == n1 || root == n2) {
            return root;
        }

        left_ancestor = LCA(n1,n2,root.left);
        right_ancestor = LCA(n1,n2,root.right);

        if (left != null and right != null) {
            return root;
        }

        if (left != null) {
            return left;
        }

        if (right != null) {
            return right;
        }
    }
}
