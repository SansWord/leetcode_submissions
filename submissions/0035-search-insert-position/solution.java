class Solution {
    public int searchInsert(int[] nums, int target) {
        return search(nums, target, 0, nums.length-1);
    }
    
    private int search(int[] nums, int target, int left, int right) {
        
        if(left>right) {
            return left;
        }
        int currentIdx = left + (right-left)/2;
        int current = nums[currentIdx];
        if(target==current) {
            return currentIdx;
        }
        if(target < current) {
            return search(nums, target, left, currentIdx-1);
        } else {
            return search(nums, target, currentIdx+1, right);
        }
    }
}
