# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.isMirrored(root.left, root.right)
        

    def isMirrored(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            return not q
        
        if not q:
            return False

        if p.val != q.val:
            return False
        
        return self.isMirrored(p.left, q.right) and self.isMirrored(p.right, q.left)
        
        
