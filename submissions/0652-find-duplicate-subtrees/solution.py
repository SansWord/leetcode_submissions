# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.sub_trees = defaultdict(list)
        self.res = []
        self.find(root)
        return self.res
    
    def find(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "x"
        
        left_tree = self.find(root.left)
        right_tree = self.find(root.right)

        s = f"{root.val},{left_tree},{right_tree}"

        if len(self.sub_trees[s]) == 1:
            self.res.append(root)
        self.sub_trees[s].append(root)

        return str(root.val) + "," + left_tree + "," + right_tree

