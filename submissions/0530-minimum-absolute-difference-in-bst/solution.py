# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        # keep min_diff, prev while in-order traversal
        def find(root, min_diff, prev) -> tuple[int, int]:
            
            if root.left:
                left_diff, left_prev = find(root.left, min_diff, prev)
            else:
                left_diff, left_prev = min_diff, prev
            
            if left_prev != None:
                curr_diff = root.val - left_prev
                curr_min = min(left_diff, curr_diff) if left_diff != None else curr_diff
            else:
                # there's no previous element, meaning there's no current minimum difference
                curr_min = None
            
            if root.right:
                return find(root.right, curr_min, root.val)
            else:
                # reaches the end of this tree, there's no following elements
                return curr_min, root.val
            

        return find(root, None, None)[0]
        
