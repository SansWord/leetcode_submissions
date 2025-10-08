# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.walk(root, result)
        return result

    def walk(self, root: Optional[TreeNode], result: List[int]) -> None:
        if not root:
            return
        
        result.append(root.val)
        self.walk(root.left, result)
        self.walk(root.right, result)
        
