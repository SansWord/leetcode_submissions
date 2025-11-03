# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numsFilter = set(nums)

        def walk(node):
            if not node:
                return node

            if node.val in numsFilter:
                return walk(node.next)

            node.next = walk(node.next)
            return node

        return walk(head)
    
        
        
