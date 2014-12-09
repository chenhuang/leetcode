public class binary_tree_upside_down {

    public TreeNode UpsideDownBinaryTree(TreeNode root) {
        return dfsBottomUp(root, null);
    }

    public TreeNode dfsBottomUp(TreeNode p, TreeNode parent) {
        if (p == null) return parent;
        TreeNode root = dfsBottomUp(p.left, p);
        p.left = (parent == null) ? parent : parent.right;
        p.right = parent;

        return root;
    }
}
