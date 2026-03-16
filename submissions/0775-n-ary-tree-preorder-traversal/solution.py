"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def travel(root, result):
            if not root:
                return result

            result.append(root.val)
            for child in root.children:
                travel(child, result)

            return result
        
        return travel(root, [])

        
