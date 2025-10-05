# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result = []
        self.findAndCollect(root, target, k, result, False, 0)
        return result

    def findAndCollect(self, root: TreeNode, target: TreeNode, k: int, result:List[int], found: bool, level) -> tuple[bool, int]:
        if root == None:
            return (found, k)

        print(" " * level + "visit:", root.val, found, k)

        if found:
            if k == 0:
                result.append(root.val)
                print(" " * level + "found and collect,", root.val)
                return True, k + 1
            else:
                self.findAndCollect(root.left, target, k-1, result, True, level + 1)
                self.findAndCollect(root.right, target, k-1, result, True, level + 1)
                print(" " * level + "found and collect children,", root.val, k)
                return True, k + 1
        else:
            if root.val == target.val:
                # visiting the target node, for the only time.
                # k should be k - 1 for parent and children
                found = True
                if k == 0:
                    result.append(root.val)
                else:
                    self.findAndCollect(root.left, target, k-1, result, True, level + 1)
                    self.findAndCollect(root.right, target, k-1, result, True, level + 1)

                print(" " * level + "found and collect parent,", root.val, k)
                return True, k - 1 # trace back
            else:
                print(" " * level + "not found yet, looking for both children, starts from left", root.val)
                leftResult = self.findAndCollect(root.left, target, k, result, False, level + 1)
                
                if leftResult[0]:
                    print(" " * level + "found in left, collect in right", root.val)
                    # collect self and found from right
                    k = leftResult[1]
                    if k == 0:
                        print(" " * level + "collecting ", root.val, " while back tracing")
                        result.append(root.val)
                    else:
                        self.findAndCollect(root.right, target, k-1, result, True, level + 1)
                    return True, k-1
                else:
                    print(" " * level + "not found in left, looking in right", root.val)
                    rightResult = self.findAndCollect(root.right, target, k, result, False, level + 1)
                    if rightResult[0]:
                        print(" " * level + "found in right, collect in left", root.val)
                        k = rightResult[1]
                        # collect self and found from left
                        if k == 0:
                            result.append(root.val)
                        else:
                            self.findAndCollect(root.left, target, k-1, result, True, level + 1)
                        return True, k-1
                    else:
                        print(" " * level + "not found", root.val, k)
                        print(" " * level + "children not found", root.val, k)
                        return False, k # k does not matter here since we both not found.
        
