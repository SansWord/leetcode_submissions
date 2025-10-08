# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        minimum = root.val

        curr = root

        while curr:
            curr, val = self.pop(curr)
            if val != minimum:
                return val
        
        return -1

        
        
    def pop(self, root: Optional[TreeNode]) -> tuple[TreeNode, int]:
        if not root:
            return None, -1

        rootVal = root.val

        if not root.left and not root.right:
            return None, rootVal

        leftVal = float("inf") if not root.left else root.left.val
        rightVal = float("inf") if not root.right else root.right.val

        if leftVal <= rightVal:
            root.val = leftVal
            root.left = self.pop(root.left)[0]
        else:
            root.val = rightVal
            root.right = self.pop(root.right)[0]
        
        return root, rootVal
