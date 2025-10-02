# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        list1_head = list1
        list2_head = list2
        merged_head_holder = ListNode()
        curr = merged_head_holder

        while list1_head != None and list2_head != None:
            if list1_head.val < list2_head.val:
                curr.next = list1_head
                curr = list1_head
                list1_head = list1_head.next
                curr.next = None
            else:
                curr.next = list2_head
                curr = list2_head
                list2_head = list2_head.next
                curr.next = None
        
        if list1_head != None:
            curr.next = list1_head

        if list2_head != None:
            curr.next = list2_head

        return merged_head_holder.next
