"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def travel(root, result):
            if not root:
                return result

            
            for child in root.children:
                travel(child, result)

            result.append(root.val)

            return result
        
        return travel(root, [])
