# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.walk(root)[0]
        
    def walk(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        if not root:
            return True, 0
        
        leftBalanced, leftHeight = self.walk(root.left)
        if not leftBalanced:
            return False, -1

        rightBalanced, rightHeight = self.walk(root.right)
        if not rightBalanced:
            return False, -1
        
        if abs(leftHeight - rightHeight) >= 2:
            return False, -1
        
        return True, max(leftHeight, rightHeight) + 1

        
