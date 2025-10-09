# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        return self.walk(root)[0]
    
    # returns tilt_sum, sum
    def walk(self, root: Optional[TreeNode]) -> tuple[int, int]:
        if not root:
            return 0, 0
        
        leftTiltSum, leftSum = self.walk(root.left)
        rightTiltSum, rightSum = self.walk(root.right)

        tilt = abs(leftSum - rightSum)
        tiltSum = leftTiltSum + rightTiltSum + tilt
        treeSum = leftSum + rightSum + root.val

        return tiltSum, treeSum

        
