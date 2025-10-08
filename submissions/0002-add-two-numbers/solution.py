# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result_holder = ListNode()
        result_curr = result_holder

        carry = 0

        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = val // 10
            val = val % 10
            l1.val = val

            result_curr.next = l1
            result_curr = l1
            l1 = l1.next
            l2 = l2.next

        remain = None
        if l1:
            remain = l1

        if l2:
            remain = l2

        while remain:
            result_curr.next = remain
            if carry == 0:
                break
            val = remain.val + carry
            carry = val // 10
            val = val % 10
            remain.val = val
            result_curr = remain
            remain = remain.next
        
        if carry == 1:
            node = ListNode(1)
            result_curr.next = node


        return result_holder.next

        
