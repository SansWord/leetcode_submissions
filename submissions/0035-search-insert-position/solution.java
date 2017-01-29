public class Solution {
    public int searchInsert(int[] nums, int target) {
        return binarySearch(nums, target, 0, nums.length - 1);
    }

    private int binarySearch(int[] nums, int target, int start, int end) {
        if (start > end) {
            return start;
        } else {
            int startNum = nums[start];
            int endNum = nums[end];
            if (target <= startNum) {
                return start;
            }

            if (endNum == target) {
                return end;
            }
            if (endNum < target) {
                return end + 1;
            }

            int pivot = (start + end) / 2;
            int current = nums[pivot];
            if (target == current) {
                return pivot;
            } else if (target < current) {
                return binarySearch(nums, target, start + 1, pivot - 1);
            } else { //if (target > current)
                return binarySearch(nums, target, pivot + 1, end - 1);
            }
        }
    }
}
