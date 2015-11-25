/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if(l1 == null) {
            return l2;
        }
        
        ListNode result = l1;
        ListNode l1Last = null;
        int carry = 0;
        while(l1 != null && l2 != null) {
            int sum = l1.val + l2.val + carry;
            l1.val = sum % 10;
            carry = sum / 10;
            l1Last = l1;
            l1 = l1.next;
            l2 = l2.next;
        }
        
        // some of l1, l2 are null;
        if(l1 == null) {
            l1Last.next = l2;
        }
        
        while(carry != 0 && l1Last.next != null) {
            int sum = l1Last.next.val + carry;
            l1Last.next.val = sum % 10;
            carry = sum / 10;
            l1Last = l1Last.next;
        }
        
        if(carry!=0) {
            l1Last.next = new ListNode(carry);
        }
        
        return result;    
    }
    
}
