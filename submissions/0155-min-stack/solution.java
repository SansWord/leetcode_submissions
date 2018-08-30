class MinStack {
    
    private LinkNode numStack;
    private LinkNode minStack;

    /** initialize your data structure here. */
    public MinStack() {
        
    }
    
    public void push(int x) {
        if(numStack == null) {
            numStack = LinkNode.of(x);
            minStack = LinkNode.of(x);
        } else {
            numStack = push(x, numStack);
            if(x <= minStack.val) {
                minStack = push(x, minStack);
            }
        }
    }
    
    private LinkNode push(int val, LinkNode head) {
        LinkNode newHead = LinkNode.of(val);
        newHead.next = head;
        return newHead;
    }
    
    
    public void pop() {
        LinkNode toPop = numStack;
        numStack = toPop.next;
        toPop.next = null;
        if(toPop.val == minStack.val) {
            toPop = minStack;
            minStack = toPop.next;
            toPop.next = null;
        }
    }
    
    public int top() {
        return numStack.val;
    }
    
    public int getMin() {
        return minStack.val;
    }
    
    private static class LinkNode {
        int val;
        LinkNode next;
        
        LinkNode(int input) {
            this.val = input;
        }
        public static LinkNode of(int input) {
            return new LinkNode(input);
        }
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
