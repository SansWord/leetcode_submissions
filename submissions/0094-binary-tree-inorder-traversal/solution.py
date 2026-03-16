# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        while root:
            stack.append(root)
            root = root.left
        
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
            while curr:
                stack.append(curr)
                curr = curr.left

        return res

        
