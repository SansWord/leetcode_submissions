# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        p1 = head
        p2 = head

        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
            if not p2:
                return False
            p2 = p2.next

            if p1 == p2:
                return True
            
        
