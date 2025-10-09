# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        self.xNode = None
        self.head = head

        self.walk(head, None, x)

        return self.head
    
    def walk(self, curr: Optional[ListNode], pre: Optional[ListNode] , x: int) -> None:
        if not curr:
            return
        
        if not self.xNode:
            if curr.val >= x:
                self.preX = pre
                self.xNode = curr

            self.walk(curr.next, curr, x)
        else:
            if curr.val >= x:
                self.walk(curr.next, curr, x)
                
            else:
                nextNode = curr.next

                if not self.preX:
                    self.preX = curr
                    self.head = curr
                else:
                    self.preX.next = curr

                self.preX = curr
                curr.next = self.xNode
                    
                
                pre.next = nextNode
                
                
                self.walk(nextNode, pre, x)
        
        
