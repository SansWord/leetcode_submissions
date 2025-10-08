# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = self.walk(root)
        return result[0]
    
    # returns diameter and height
    def walk(self, root: Optional[TreeNode]) -> tuple[int, int]:

        if not root:
            return -1, -1
        
        leftDiameter, leftHeight = self.walk(root.left)
        rightDiameter, rightHeight = self.walk(root.right)

        diameter = leftHeight + rightHeight + 2
        height = max(leftHeight, rightHeight) + 1

        return max(leftDiameter, rightDiameter, diameter), height
        
