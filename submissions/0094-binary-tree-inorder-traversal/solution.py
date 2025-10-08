# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        self.walk(root, result)
        return result

    def walk(self, node: Optional[TreeNode], result) -> None:
        if not node:
            return
        self.walk(node.left, result)
        result.append(node.val)
        self.walk(node.right, result)

        
