public class dfs {
    // Iterative with a stack
    public void dfs_iter(TreeNode root) {
        if (root is null) {
            return root;
        }
        Stack<Integer> stack = new Stack<Integer>();
        ArrayList<Integer> result = new ArrayList<Integer>();
        stack.push(root);

        while (!stack.empty()) {
            TreeNode node = stack.peek();
            stack.pop();
            result.add(node);
            stack.push(node.left);
            stack.push(node.right);
        }

        return result;
    }

    
    // Recursion.
    public void dfs_rec(TreeNode root) {
    }

    // Divide and conquer
    public ArrayList<TreeNode> dfs_dc(TreeNode root) {
        ArrayList<TreeNode> result = new ArrayList<TreeNode>();
        if (root == null) {
           return result; 
        }
        left = dfs_dc(root.left);
        right = dfs_dc(root.right);
        result.add(root);
        result.addAll(left);
        result.addAll(right);

        return result;
    }
}
