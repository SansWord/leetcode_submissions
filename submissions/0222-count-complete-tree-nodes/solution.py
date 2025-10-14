# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode], leftH=-1, rightH=-1) -> int:
        if not root:
            return 0
        
        if leftH == -1:
            leftH = self.leftHeight(root)
        if rightH == -1:
            rightH = self.rightHeight(root)

        if leftH == rightH:
            return 2**leftH - 1
        
        elif leftH == 2:
            return 2
        else:
            return (1 + self.countNodes(root.left, leftH-1, -1) 
                + self.countNodes(root.right, -1, rightH-1))
        
    def leftHeight(self, root: Optional[TreeNode]) -> int:
        result = 0
        while root:
            root = root.left
            result += 1
        return result
    
    def rightHeight(self, root: Optional[TreeNode]) -> int:
        result = 0
        while root:
            root = root.right
            result += 1
        return result

