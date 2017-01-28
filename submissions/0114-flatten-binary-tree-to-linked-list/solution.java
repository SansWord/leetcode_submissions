/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        } else {
            flatten(root.left);
            flatten(root.right);
            root.right = merge(root.left, root.right);
            root.left = null;
        }
    }
    
    private TreeNode merge(TreeNode flattenLeft, TreeNode flattenRight) {
        if (flattenLeft == null) {
            return flattenRight;    
        } else {
            if (flattenRight != null) {
                TreeNode current = flattenLeft;
                while(current.right != null) {
                    current = current.right;
                }
                current.right = flattenRight;
            }
            return flattenLeft;
        }
    }
}
