# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        return self.makeTree(nums, 0, len(nums))

    def makeTree(self, nums: List[int], lo: int, hi: int) -> Optional[TreeNode]:
        if lo >= hi:
            return None
        
        mid = (lo+hi) // 2
        return TreeNode(nums[mid], self.makeTree(nums, lo, mid), self.makeTree(nums, mid+1, hi))
        
