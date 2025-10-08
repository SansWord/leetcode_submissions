# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.curr = 0
        return self.findKthElm(root)
        
    def findKthElm(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        leftResult = self.findKthElm(root.left)
        if leftResult != -1:
            return leftResult
        
        self.curr += 1
        if self.curr == self.k:
            return root.val
        
        return self.findKthElm(root.right)



