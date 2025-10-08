# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.modes = []
        self.pre = None
        self.counter = 0
        self.max_count = float("-inf")

        self.walk(root)
        return self.modes
    
    def walk(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        # in-order traversal would vist value sorted
        self.walk(root.left)
        
        if self.pre == root.val:
            self.counter += 1
        else:
            self.counter = 1

        if self.counter == self.max_count:
            self.modes.append(root.val)

        if self.counter > self.max_count:
            self.max_count = self.counter
            self.modes = [root.val]
        
        self.pre = root.val

        self.walk(root.right)
        
        return

        
