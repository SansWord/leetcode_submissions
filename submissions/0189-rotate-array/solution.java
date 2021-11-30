class Solution {
    public void rotate(int[] nums, int k) {
        int length = nums.length;
        int tmp;
        int switchCount = 0;
        int delta = 1;
        while(switchCount<length) {
            int start = length-delta;
            tmp = nums[start];
            int current = start;
            // iterate over a full circle
            do {                
                int next = ((current - k) % length + length) % length;
                nums[current] = nums[next];
                switchCount++;
                current = next;
            } while (current != start);
            // re-assign the last assignment with tmp value (the last assignment should use the first value)
            nums[(current+k)%length] = tmp;
            // complete a full cycle, move on to the next cycle
            delta++;
        }
    }
}
