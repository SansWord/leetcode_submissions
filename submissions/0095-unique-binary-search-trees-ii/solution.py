# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        result = []
        trees_without_vals = self.generateTreeStructures(n)
        for tree in trees_without_vals:
            tree_with_num, _ = self.copyTree(tree, 1)
            result.append(tree_with_num)
        
        return result

    def copyTree(self, root: TreeNode, startNum: int) -> tuple[TreeNode, int]:
        if not root:
            return None, startNum
        
        leftTree, nextNum = self.copyTree(root.left, startNum)
        newRoot = TreeNode(val=nextNum)
        newRoot.left = leftTree
        rightTree, nextNum = self.copyTree(root.right, nextNum + 1)
        newRoot.right = rightTree


        return newRoot, nextNum
        


    
    @cache
    def generateTreeStructures(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return [None]
        if n == 1:
            return [TreeNode(val=1)]

        result = []
        for i in range(n):
            leftNum = i
            rightNum = n - 1 - i
            leftTrees = self.generateTreeStructures(leftNum)
            rightTrees = self.generateTreeStructures(rightNum)

            for leftTree in leftTrees:
                for rightTree in rightTrees:
                    root = TreeNode(val=1)
                    root.left = leftTree
                    root.right = rightTree

                    result.append(root)

        return result

        
