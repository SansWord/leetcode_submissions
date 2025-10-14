# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode], firstNode = None) -> Optional[ListNode]:

        if not head:
            return None

        if not firstNode:
            if not head.next:
                return head

            else:
                return self.swapPairs(head.next, head)
        else:
            nextNode = head.next
            head.next = firstNode
            firstNode.next = self.swapPairs(nextNode, None)
            return head

        

        
