# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


        # returns head and tail of given list and if the list is being flipped
        def walk(node: Optional[ListNode], step:int, start: Optional[ListNode]) -> tuple[Optional[ListNode], Optional[ListNode], bool]:
            if not node:
                return None, None, False
            if not node.next:
                if step == k:
                    revHead, revTail = reverse(start)
                    return revHead, revTail, True
                else:
                    return node, node, False

            if step < k:
                restHead, restTail, flipped = walk(node.next, step+1, start)

                # if the list is being flipped, means the given node is a part of flipping.
                # hence return the result directly (current node is in it)
                if flipped:
                    return restHead, restTail, flipped
                
                # if not, means we're in the remainder list, should return the current node.
                else:
                    return node, restTail, False

            # reach kTh step, reverse list from start to now. and restart another round
            if step == k:
                nextNode = node.next
                node.next = None
                revHead, revTail = reverse(start)
                restHead, restTail, flipped = walk(nextNode, 1, nextNode)
                revTail.next = restHead
                return revHead, restTail, True

        # returns head and tail of given list
        def reverse(head: Optional[ListNode]) -> tuple[Optional[ListNode], Optional[ListNode]]:
            if not head:
                return None, None
            
            if not head.next:
                return head, head
            
            nextHead, nextTail = reverse(head.next)
            nextTail.next = head
            head.next = None
            return nextHead, head

        return walk(head, 1, head)[0]
        
