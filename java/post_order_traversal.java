/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class post_order_traversal {
    // use recursion 
    public List<Integer> postorderTraversalRec(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<Integer>();

        if (root == null) {
            return result;
        } else {
            ArrayList<Integer> left = postorderTraversalRec(root.left);
            ArrayList<Integer> right = postorderTraversalRec(root.right); 
            result.addAll(left);
            result.addAll(right);
            result.add(root.val);
        }

        return result;
    }

    // use iteration
    // need to use a stack
    public List<Integer> postorderTraversalIter(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode prev = null;
        TreeNode curr = root;

        if (root == null) {
            return result
        }

        stack.push(root);
        while (!stack.empty()) {
            curr = stack.peek();
            if (prev == null || prev.left == curr || prev.right == curr) {
                if (curr.left != null) {
                    stack.push(curr.left);
                } else if (curr.right != null) {
                    stack.push(curr.right);
                }       
            } else if (curr.left == prev) {
                if (curr.right != null) {
                    stack.push(curr.right);
                }
            } else {
                result.add(curr.val);
                stack.pop();    
            }
            prev = curr;
        }
        return result;
    }
}
