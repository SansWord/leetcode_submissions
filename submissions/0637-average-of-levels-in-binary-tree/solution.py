# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        queue = []
        queue.append(root)
        while len(queue) != 0:
            levelLen = len(queue)
            sum = 0
            for i in range(levelLen):
                n = queue.pop(0)
                sum += n.val
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            result.append(sum/levelLen)
        return result
