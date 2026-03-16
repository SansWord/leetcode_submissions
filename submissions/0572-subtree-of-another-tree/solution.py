# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
        def getPreOrder(root) -> str:
            if not root:
                return ""
            return str(root.val) + getPreOrder(root.left) + getPreOrder(root.right)
        
        def getInOrder(root) -> str:
            if not root:
                return ""
            return getInOrder(root.left) + str(root.val) +  getInOrder(root.right)
        
        def getCount(root) -> int:
            if not root:
                return 0
            else:
                return getCount(root.left) + getCount(root.right) + 1
        
        def getTreeHash(root) -> str:
            return (getPreOrder(root), getInOrder(root))

        subRootHash = getTreeHash(subRoot)
        subRootCount = getCount(subRoot)

        EMPTY_HASH = ("", "")

        # found, node count, (pre_order, in_order)
        def find(root) -> tuple[bool, int, tuple[str, str]]:
            if not root:
                return False, 0, EMPTY_HASH
            
            left_found, left_count, left_hash = find(root.left)
            
            if left_found:
                return True, -1, EMPTY_HASH
            
            right_found, right_count, right_hash = find(root.right)
            
            if right_found:
                return True, -1, EMPTY_HASH

            curr_count = left_count + right_count + 1
            if curr_count > subRootCount:
                return False, curr_count, EMPTY_HASH

            # (pre-order, in-order)
            curr_hash = (str(root.val) + left_hash[0] + right_hash[0], left_hash[1] + str(root.val) + right_hash[1])
            if curr_hash == subRootHash:
                return True, curr_count, EMPTY_HASH
            else:
                return False, curr_count, curr_hash
        
        return find(root)[0]

                


        
