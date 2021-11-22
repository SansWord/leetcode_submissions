class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int mid;
        int currentVal;
        
        while (left <= right) {
            mid = left + (right-left) / 2;
            currentVal = nums[mid];
            if(currentVal==target) {
                return mid;
            }
            if(target < currentVal) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return -1;
    }
}
