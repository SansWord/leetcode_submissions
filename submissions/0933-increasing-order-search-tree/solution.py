# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.walk(root)[0]
    
    def walk(self, root: Optional[TreeNode]) -> tuple[Optional[TreeNode], Optional[TreeNode]]:

        if not root:
            return None, None

        if not root.left and not root.right:
            return root, root
        

        if not root.left:
            root.right, last = self.walk(root.right)
            return root, last
        
        else:
            leftHead, leftLast = self.walk(root.left)
            root.left = None
            leftLast.right = root

            if not root.right:
                return leftHead, root
            else: # both exists
                root.right, rightLast = self.walk(root.right)
                return leftHead, rightLast



        
