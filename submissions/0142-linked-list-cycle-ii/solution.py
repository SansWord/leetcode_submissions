# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = head.next
        if not slow:
            return None
        fast = slow.next

        if not fast:
            return None
        
        while slow and fast and slow != fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return None
        if not slow or not fast:
            return None
        
        # slow == fast and cycle exists
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
        
