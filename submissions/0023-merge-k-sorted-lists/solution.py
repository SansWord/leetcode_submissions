# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, id(l), l))
        
        head_holder = ListNode()
        curr = head_holder

        while len(heap) != 0:
            val, nodeId, minNode = heapq.heappop(heap)
            curr.next = minNode
            if minNode.next:
                nextNode = minNode.next
                heapq.heappush(heap, (nextNode.val, id(nextNode), nextNode))
                minNode.next = None
            curr = minNode

        return head_holder.next
        
