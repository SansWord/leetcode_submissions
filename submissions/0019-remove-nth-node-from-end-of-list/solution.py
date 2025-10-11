# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return self.walk(head, n)[0]

    def walk(self, head, n) -> tuple[Optional[ListNode], int]:
        if not head:
            return None, n

        restHead, k = self.walk(head.next,n)
        if k > 1:
            return head, k - 1
        
        if k == 1:
            # remove given node
            head.next = None
            return restHead, 0

        if k == 0:
            head.next = restHead
            return head, -1
        
        return head, -1

        
