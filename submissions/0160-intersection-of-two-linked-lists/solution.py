# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        currA = headA
        currB = headB

        lenA = 0
        lenB = 0

        while currA:
            lenA += 1
            currA = currA.next

        while currB:
            lenB += 1
            currB = currB.next
        
        if lenA < lenB:
            big = headB
            small = headA
            diff = lenB - lenA
        else:
            big = headA
            small = headB
            diff = lenA - lenB

        for i in range(diff):
            big = big.next
        
        while big:
            if big == small:
                return big
            
            big = big.next
            small = small.next

        
        
        return None
        
