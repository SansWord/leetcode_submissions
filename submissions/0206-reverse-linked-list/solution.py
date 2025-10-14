# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.walk(head)[0]

    def walk(self, head: Optional[ListNode]) -> tuple[Optional[ListNode], Optional[ListNode]]:
        if not head:
            return None, None

        if not head.next:
            return head, head
        
        nextNode = head.next
        head.next = None

        nextHead, nextLast = self.walk(nextNode)
        nextLast.next = head
        return nextHead, head


        
