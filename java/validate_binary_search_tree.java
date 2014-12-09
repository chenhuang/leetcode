public class validate_binary_search_tree {
/*
 * A valid binary search tree means the left children of a node is always less than the node, and the right children of a node is always larger than the node. 
 *
 * if do it recursively, that means a node should be larger than the largest node from it's left tree and less that the smallest element from its right tree, or, the children on the left tree should be less than the root, children on the right tree should be larger than the root.
 *
 * */
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, null, null);
    }

    private boolean isValidBST(TreeNode root, Integer low, Integer high) {
        if (root == null) {
            return true;
        }


        if (isValidBST(root.left, low, root.val) && isValidBST(root.right, root.val, high)) 
            if (root.val > low || low == null)  
                if (root.val < high || high == null)
                    return true;

        return false;
    }
}
