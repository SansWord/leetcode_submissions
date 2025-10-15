# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def walk(node: Optional[ListNode], head: Optional[ListNode]) -> tuple[bool, Optional[ListNode]]:
            if not node.next:
                return node.val == head.val, head.next
            
            res, currNode = walk(node.next, head)
            if not res:
                return False, None
            else:
                return node.val == currNode.val, currNode.next


        return walk(head, head)[0]
        
