public class Solution {
    public int search(int[] nums, int target) {
        int turnPoint = -1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i-1] > nums[i]) {
                turnPoint = i;
                break;
            }
        }

        if (turnPoint == -1) {
            return binarySearch(nums, target, 0, nums.length - 1);
        } else {
            if (target < nums[0]) {
                return binarySearch(nums, target, turnPoint, nums.length - 1);
            } else {
                return binarySearch(nums, target, 0, turnPoint - 1);
            }
        }
    }

    private int binarySearch(int[] nums, int target, int start, int end) {
        if (start > end || nums[start] > target || nums[end] < target) {
            return -1;
        } else {
            int pivot = (start + end) / 2;
            int current = nums[pivot];
            if (current == target) {
                return pivot;
            } else {
                if (current < target) {
                    return binarySearch(nums, target, pivot + 1, end);
                } else {
                    return binarySearch(nums, target, start, pivot - 1);
                }
            }
        }
    }
}
