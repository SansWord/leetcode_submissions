# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.walk(head, None)
    
    def walk(self, node: Optional[ListNode], pre: Optional[ListNode]) -> Optional[ListNode]:
        if not node:
            return None

        if not pre or pre.val != node.val:
            self.walk(node.next, node)
            return node
        else:
            # found duplicate node, remove this node from list
            nextNode = node.next
            node.next = None

            cleanedSubList = self.walk(nextNode, pre)
            pre.next = cleanedSubList
            return cleanedSubList



            
    
        
