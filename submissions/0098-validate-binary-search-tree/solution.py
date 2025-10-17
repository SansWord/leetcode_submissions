# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root)[0]
    
    def validate(self, node: Optional[TreeNode]) -> tuple[bool, int, int]:
        if not node:
            return True, float("-inf"), float("inf")
        
        if not node.left and not node.right:
            return True, node.val, node.val        
    
        if not node.right:
            isValid, leftMin, leftMax = self.validate(node.left)
            if not isValid:
                return False, None, None
            if leftMax >= node.val:
                return False, None, None
            return True, leftMin, node.val
        
        if not node.left:
            isValid, rightMin, rightMax = self.validate(node.right)
            if not isValid:
                return False, None, None
            if node.val >= rightMin:
                return False, None, None
            return True, node.val, rightMax
        
        isValid, leftMin, leftMax = self.validate(node.left)
        if not isValid:
            return False, None, None
        if leftMax >= node.val:
            return False, None, None

        isValid, rightMin, rightMax = self.validate(node.right)
        if not isValid:
            return False, None, None
        if node.val >= rightMin:
            return False, None, None
        
        return True, leftMin, rightMax
        
