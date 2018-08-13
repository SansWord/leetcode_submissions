/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {     
        // dummy node for holding partitioned result
        ListNode h1 = new ListNode(-1);
        ListNode tail1 = h1;
        ListNode h2 = new ListNode(-1);
        ListNode tail2 = h2;
        
        ListNode current = head;
        
        while (current != null) {
            if(current.val < x) {
                tail1.next = current;
                tail1 = current;
            } else {
                tail2.next = current;
                tail2 = current;
            }
            ListNode tmp = current;
            current = current.next;
            tmp.next = null;
        }
        
        tail1.next = h2.next;
    
        return h1.next;
    }
}
