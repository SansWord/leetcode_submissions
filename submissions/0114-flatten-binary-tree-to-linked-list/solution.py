# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        self.flattenAndReturnLastNode(root)

    def flattenAndReturnLastNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None
        if not root.left and not root.right:
            return root

        leftLast = self.flattenAndReturnLastNode(root.left)
        rightLast = self.flattenAndReturnLastNode(root.right)

        if not leftLast:
            return rightLast
        
        if not rightLast:
            root.right = root.left
            root.left = None
            return leftLast

        if leftLast and rightLast:
            leftLast.right = root.right
            root.right = root.left
            root.left = None
            return rightLast
        
