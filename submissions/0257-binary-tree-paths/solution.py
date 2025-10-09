# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)

        if not leftPaths and not rightPaths:
            return [f"{root.val}"]

        return [f"{root.val}->{path}" for path in leftPaths] + [f"{root.val}->{path}" for path in rightPaths]

    

        
